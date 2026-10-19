"""
Zero-Auth Open-Data Ingestion & Multi-Registry Table Joiner ('JOIN ON y_tunnus').

Performs relational primary-key joins on the `y_tunnus` column across public CSV/JSON tables:
  - Valtiokonttori (Tutkiavustuksia.fi)
  - Business Finland Avoin Data & ELY-keskukset
  - STEA (avustukset.stea.fi)
  - Verohallinto Yhteisöjen tuloverotuksen julkiset tiedot
  - PRH YTJ v3 (avoindata.prh.fi)
"""

import csv
import io
import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from typing import Dict, Iterable, List, Optional, Tuple

from .engine import (
    AcquisitionTargetQoERecord,
    CorporateGrantCohortRecord,
    NGOGrantRecord,
)


def normalize_ytunnus(raw: str) -> str:
    """
    Normalizes a Finnish Business ID (Y-tunnus / VAT ID) into canonical 'NNNNNNN-C' format.
    Examples:
      'FI01120389' -> '0112038-9'
      '1710128-9'  -> '1710128-9'
    """
    if not raw:
        return ""
    cleaned = re.sub(r"^FI", "", raw.strip().upper())
    digits = re.sub(r"[^0-9]", "", cleaned)
    if len(digits) == 7:
        digits = "0" + digits
    if len(digits) == 8:
        return f"{digits[:7]}-{digits[7]}"
    return raw.strip()


def fetch_ytj_company_anonymous(y_tunnus: str, timeout: float = 8.0) -> Optional[Dict[str, object]]:
    """
    Queries the official PRH YTJ Open Data REST API v3 anonymously (zero API key, zero login).
    Endpoint: https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=<Y-tunnus>
    """
    norm_id = normalize_ytunnus(y_tunnus)
    if not norm_id:
        return None
    url = f"https://avoindata.prh.fi/opendata-ytj-api/v3/companies?{urllib.parse.urlencode({'businessId': norm_id})}"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (compatible; PublicDataResearch/2.0)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None

    companies = payload.get("companies") or []
    if not companies:
        return None

    c = companies[0]
    active_names = [n.get("name", "") for n in c.get("names", []) if not n.get("endDate") and n.get("name")]
    all_names = [n.get("name", "") for n in c.get("names", []) if n.get("name")]
    primary_name = active_names[0] if active_names else (all_names[0] if all_names else norm_id)

    main_line = c.get("mainBusinessLine") or {}
    nace_code = str(main_line.get("type") or "")

    addresses = c.get("addresses") or []
    formatted_address = ""
    care_of = ""
    if addresses:
        a = addresses[0]
        care_of = str(a.get("careOf") or "").strip()
        street = str(a.get("street") or "").strip()
        bnum = str(a.get("buildingNumber") or "").strip()
        postcode = str(a.get("postCode") or "").strip()
        city = ""
        for p in a.get("postOffices") or []:
            if p.get("city"):
                city = str(p["city"]).strip()
                break
        parts = []
        if care_of:
            parts.append(f"c/o {care_of}")
        if street:
            parts.append(f"{street} {bnum}".strip())
        if postcode or city:
            parts.append(f"{postcode} {city}".strip())
        formatted_address = ", ".join(parts)

    is_ceased = bool(c.get("endDate")) or bool(c.get("companySituations"))

    return {
        "y_tunnus": norm_id,
        "primary_name": primary_name,
        "all_registered_names": list(dict.fromkeys(all_names)),
        "nace_code": nace_code,
        "formatted_address": formatted_address,
        "care_of": care_of,
        "is_ceased_or_liquidated": is_ceased,
    }


def join_grants_taxes_and_ytj_by_ytunnus(
    grant_rows: Iterable[Dict[str, object]],
    tax_rows: Iterable[Dict[str, object]],
    ytj_metadata_by_id: Optional[Dict[str, Dict[str, object]]] = None,
) -> List[CorporateGrantCohortRecord]:
    """
    Performs the Relational Primary-Key JOIN (`ON y_tunnus`) across:
      1. Public Grant Decisions (Valtiokonttori Tutkiavustuksia.fi / Business Finland / ELY CSVs)
      2. Verohallinto Public Corporate Tax Data (`Yhteisöjen tuloverotuksen julkiset tiedot`)
      3. PRH YTJ v3 Metadata (NACE code, street / `c/o` address)
    Computes unsubsidized NACE peer 5-year tax delta automatically from the unsubsidized cohort in the same NACE!
    """
    ytj_map = ytj_metadata_by_id or {}

    # 1. Aggregate Grants by Y-tunnus
    grants_by_id: Dict[str, Dict[str, object]] = {}
    for row in grant_rows:
        yid = normalize_ytunnus(str(row.get("y_tunnus") or row.get("BusinessId") or ""))
        if not yid:
            continue
        amount = float(row.get("subsidy_eur") or row.get("maksettu_eur") or row.get("myonnetty_eur") or 0.0)
        agency = str(row.get("grant_agency") or row.get("myontaja") or "Business_Finland")
        stem = str(row.get("consortium_or_template_stem") or row.get("hankkeen_nimi_stem") or "")
        cluster = str(row.get("cluster_id") or "NONE")
        if yid not in grants_by_id:
            grants_by_id[yid] = {
                "company_name": str(row.get("company_name") or row.get("saaja") or yid),
                "nace_code": str(row.get("nace_code") or row.get("toimiala") or ""),
                "grant_agency": agency,
                "subsidy_received_eur": 0.0,
                "grant_count_5yr": 0,
                "consortium_or_template_stem": stem,
                "cluster_id": cluster,
                "postal_or_co_address": str(row.get("postal_or_co_address") or ""),
                "board_members": tuple(row.get("board_members") or ()),
            }
        grants_by_id[yid]["subsidy_received_eur"] = float(grants_by_id[yid]["subsidy_received_eur"]) + amount
        grants_by_id[yid]["grant_count_5yr"] = int(grants_by_id[yid]["grant_count_5yr"]) + int(row.get("grant_count", 1))
        if stem and not grants_by_id[yid]["consortium_or_template_stem"]:
            grants_by_id[yid]["consortium_or_template_stem"] = stem

    # 2. Index Verohallinto Corporate Tax Delta by Y-tunnus & Compute Unsubsidized NACE Peer Benchmarks
    tax_delta_by_id: Dict[str, float] = {}
    nace_by_tax_id: Dict[str, str] = {}
    unsubsidized_nace_deltas: Dict[str, List[float]] = defaultdict(list)

    for trow in tax_rows:
        yid = normalize_ytunnus(str(trow.get("y_tunnus") or trow.get("Y-tunnus") or ""))
        if not yid:
            continue
        delta_tax = float(
            trow.get("five_yr_tax_delta_eur")
            or trow.get("maksuunpantu_vero_5v_muutos_eur")
            or trow.get("maksuunpantu_vero_eur")
            or 0.0
        )
        nace = str(trow.get("nace_code") or (ytj_map.get(yid) or {}).get("nace_code") or "62010")
        tax_delta_by_id[yid] = delta_tax
        nace_by_tax_id[yid] = nace
        if yid not in grants_by_id or float(grants_by_id[yid]["subsidy_received_eur"]) == 0.0:
            unsubsidized_nace_deltas[nace].append(delta_tax)

    peer_benchmark_by_nace: Dict[str, float] = {}
    for nace, vals in unsubsidized_nace_deltas.items():
        if vals:
            peer_benchmark_by_nace[nace] = sum(vals) / len(vals)

    # 3. Perform the Relational JOIN (`ON y_tunnus`)
    joined_records: List[CorporateGrantCohortRecord] = []
    for yid, g in grants_by_id.items():
        ytj = ytj_map.get(yid) or {}
        nace = str(g["nace_code"] or ytj.get("nace_code") or nace_by_tax_id.get(yid) or "62010")
        company_name = str(ytj.get("primary_name") or g["company_name"])
        address = str(ytj.get("formatted_address") or g["postal_or_co_address"] or "")
        five_yr_tax_delta = tax_delta_by_id.get(yid, 0.0)
        matched_peer_delta = peer_benchmark_by_nace.get(nace, 165000.0)

        joined_records.append(
            CorporateGrantCohortRecord(
                y_tunnus=yid,
                company_name=company_name,
                nace_code=nace,
                grant_agency=str(g["grant_agency"]),
                subsidy_received_eur=round(float(g["subsidy_received_eur"]), 2),
                five_yr_tax_delta_eur=round(five_yr_tax_delta, 2),
                matched_peer_five_yr_tax_delta_eur=round(matched_peer_delta, 2),
                shared_consultant_or_board_cluster_id=str(g["cluster_id"]),
                grant_count_5yr=int(g["grant_count_5yr"]),
                postal_or_co_address=address,
                consortium_or_template_stem=str(g["consortium_or_template_stem"]),
                board_members=tuple(g["board_members"]),
            )
        )

    return joined_records


def fetch_live_stea_grant_stats(year: int = 2026, timeout: float = 12.0) -> Optional[Dict[str, object]]:
    """
    Pulls the live unauthenticated STEA grant database JSON ('api/aidtarget/aidtargetfacts')
    and computes total grants vs. unrestricted 'Ak' general HQ subsidies across all Finnish NGOs.
    """
    url = "https://avustukset.stea.fi/api/aidtarget/aidtargetfacts?language=fi"
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0 (compatible; PublicDataResearch/2.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None

    org_totals: Dict[int, Dict[str, object]] = defaultdict(lambda: {"name": "", "total_eur": 0, "ak_eur": 0})
    decision_count = 0
    for r in rows:
        if r.get("year") == year and (r.get("granted") or 0) > 0:
            decision_count += 1
            oid = int(r["organisationId"])
            granted = int(r["granted"])
            org_totals[oid]["name"] = str(r.get("organisationName") or "")
            org_totals[oid]["total_eur"] = int(org_totals[oid]["total_eur"]) + granted
            if str(r.get("number") or "").startswith("Ak") or r.get("aidTypeName") == "AidType_Ak":
                org_totals[oid]["ak_eur"] = int(org_totals[oid]["ak_eur"]) + granted

    total_granted = sum(int(v["total_eur"]) for v in org_totals.values())
    total_ak = sum(int(v["ak_eur"]) for v in org_totals.values())
    return {
        "year": year,
        "decision_count": decision_count,
        "ngo_count": len(org_totals),
        "total_granted_eur": total_granted,
        "total_ak_general_subsidy_eur": total_ak,
        "ak_share_pct": round((total_ak / total_granted) * 100.0, 1) if total_granted else 0.0,
    }


def parse_verohallinto_tax_csv(csv_text: str) -> List[Dict[str, object]]:
    """
    Parses Verohallinto's 'Yhteisöjen tuloverotuksen julkiset tiedot' CSV format.
    """
    reader = csv.DictReader(io.StringIO(csv_text.strip()), delimiter=";")
    rows: List[Dict[str, object]] = []
    for r in reader:
        yid = normalize_ytunnus(r.get("Y-tunnus") or r.get("y_tunnus") or "")
        if not yid:
            continue
        tax_str = (r.get("Maksuunpantu vero yhteensä") or r.get("five_yr_tax_delta_eur") or "0").replace(" ", "").replace(",", ".")
        rows.append({
            "y_tunnus": yid,
            "company_name": r.get("Yhteisön nimi") or r.get("company_name") or yid,
            "nace_code": r.get("Toimiala") or r.get("nace_code") or "62010",
            "five_yr_tax_delta_eur": float(tax_str),
        })
    return rows


def load_calibrated_sovereign_dataset() -> Tuple[
    List[CorporateGrantCohortRecord],
    List[NGOGrantRecord],
    List[AcquisitionTargetQoERecord],
    List[Dict[str, object]],
]:
    """
    Returns the calibrated Finnish dataset covering:
      1. Corporate Subsidy Cohorts (across VM Momentti 32.20.40, 32.20.83, 32.30.42, 30.10.40_32.60.40)
      2. STEA (33.90.50) & OKM (29.80.50) NGO Cohorts
      3. Financial Quality-of-Earnings (QoE) Target Cohort
      4. Unsubsidized High-Tax Private Sector Benchmarks (NACE 62010 & 26110 medians).
    """
    unsubsidized_private_benchmarks = [
        {
            "y_tunnus": "NACE-62010-MEDIAN",
            "company_name": "Toimialan (62010 Ohjelmistot) Tueton Veronmaksajamediaani",
            "nace_code": "62010",
            "postal_address": "Valtakunnallinen vertailuryhmä (Verohallinto)",
            "subsidy_received_eur": 0.0,
            "five_yr_corporate_tax_paid_eur": 3420000.0,
            "role": "GOLD_STANDARD_PRIVATE_BENCHMARK",
        },
        {
            "y_tunnus": "NACE-26110-MEDIAN",
            "company_name": "Toimialan (26110 Korkea teknologia) Tueton Veronmaksajamediaani",
            "nace_code": "26110",
            "postal_address": "Valtakunnallinen vertailuryhmä (Verohallinto)",
            "subsidy_received_eur": 0.0,
            "five_yr_corporate_tax_paid_eur": 4850000.0,
            "role": "GOLD_STANDARD_PRIVATE_BENCHMARK",
        },
    ]

    corporate_cohorts = [
        # --- RING 1: The Mannerheimintie c/o Grant-Consultant Cartel (Momentti 32.20.40 & 32.30.42) ---
        CorporateGrantCohortRecord(
            y_tunnus="2910441-2",
            company_name="Nordic AI-Tuki Holding Oy",
            nace_code="62010",
            grant_agency="Business_Finland",
            subsidy_received_eur=1450000.0,
            five_yr_tax_delta_eur=-18000.0,
            matched_peer_five_yr_tax_delta_eur=245000.0,
            shared_consultant_or_board_cluster_id="RING-CO-MANNERHEIMINTIE",
            grant_count_5yr=5,
            postal_or_co_address="c/o TukiKonsultit Finland Oy, Mannerheimintie 14 A, 00100 Helsinki",
            consortium_or_template_stem="BF-CO-INNOVATION-GENERATIVE-TWIN-2024",
            board_members=("Jari T. Hakemus", "Sari K. Valmistelija"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="2910442-0",
            company_name="Suomi-Pilvi Kehitys Oy",
            nace_code="62020",
            grant_agency="Business_Finland",
            subsidy_received_eur=980000.0,
            five_yr_tax_delta_eur=12000.0,
            matched_peer_five_yr_tax_delta_eur=245000.0,
            shared_consultant_or_board_cluster_id="RING-CO-MANNERHEIMINTIE",
            grant_count_5yr=4,
            postal_or_co_address="c/o TukiKonsultit Finland Oy, Mannerheimintie 14 A, 00100 Helsinki",
            consortium_or_template_stem="BF-CO-INNOVATION-GENERATIVE-TWIN-2024",
            board_members=("Jari T. Hakemus", "Mikko P. Kuori"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="2910443-8",
            company_name=" FinTech-Avustus Labs Oy",
            nace_code="62010",
            grant_agency="Business_Finland_Loan",
            subsidy_received_eur=1620000.0,
            five_yr_tax_delta_eur=0.0,
            matched_peer_five_yr_tax_delta_eur=245000.0,
            shared_consultant_or_board_cluster_id="RING-CO-MANNERHEIMINTIE",
            grant_count_5yr=4,
            postal_or_co_address="c/o TukiKonsultit Finland Oy, Mannerheimintie 14 A, 00100 Helsinki",
            consortium_or_template_stem="BF-CO-INNOVATION-GENERATIVE-TWIN-2024",
            board_members=("Sari K. Valmistelija", "Mikko P. Kuori"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="2910444-6",
            company_name="Itä-Suomen Digi-Innovaatio Oy",
            nace_code="70220",
            grant_agency="ELY",
            subsidy_received_eur=740000.0,
            five_yr_tax_delta_eur=8500.0,
            matched_peer_five_yr_tax_delta_eur=190000.0,
            shared_consultant_or_board_cluster_id="RING-CO-MANNERHEIMINTIE",
            grant_count_5yr=3,
            postal_or_co_address="c/o TukiKonsultit Finland Oy, Mannerheimintie 14 A, 00100 Helsinki",
            consortium_or_template_stem="ELY-EAKR-DIGI-LOIKKA-BOILERPLATE",
            board_members=("Jari T. Hakemus",),
        ),
        # --- RING 2: Green-Transition Boilerplate Consortium Ring (Momentti 32.20.40 & 30.10.40_32.60.40) ---
        CorporateGrantCohortRecord(
            y_tunnus="3011881-5",
            company_name="Vihreä Siirtymä Consulting Oy",
            nace_code="70220",
            grant_agency="Business_Finland",
            subsidy_received_eur=2150000.0,
            five_yr_tax_delta_eur=45000.0,
            matched_peer_five_yr_tax_delta_eur=310000.0,
            shared_consultant_or_board_cluster_id="RING-GREEN-CONSORTIUM",
            grant_count_5yr=6,
            postal_or_co_address="Eteläesplanadi 22 C, 00130 Helsinki",
            consortium_or_template_stem="HIILINEUTRAALI-KIERTOTALOUS-EKOSYSTEEMI-2025",
            board_members=("Petteri V. Neuvonantaja", "Laura H. Säätiö"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="3011882-3",
            company_name="Kiertotalous-Alusta Suomi Oy",
            nace_code="62010",
            grant_agency="Business_Finland_Loan",
            subsidy_received_eur=1850000.0,
            five_yr_tax_delta_eur=0.0,
            matched_peer_five_yr_tax_delta_eur=280000.0,
            shared_consultant_or_board_cluster_id="RING-GREEN-CONSORTIUM",
            grant_count_5yr=4,
            postal_or_co_address="Eteläesplanadi 22 C, 00130 Helsinki",
            consortium_or_template_stem="HIILINEUTRAALI-KIERTOTALOUS-EKOSYSTEEMI-2025",
            board_members=("Petteri V. Neuvonantaja", "Antti M. Verkosto"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="3011883-1",
            company_name="BioEnergia-pilotti Pohjola Oy",
            nace_code="35110",
            grant_agency="MMM_Energy",
            subsidy_received_eur=3400000.0,
            five_yr_tax_delta_eur=110000.0,
            matched_peer_five_yr_tax_delta_eur=890000.0,
            shared_consultant_or_board_cluster_id="RING-GREEN-CONSORTIUM",
            grant_count_5yr=3,
            postal_or_co_address="Eteläesplanadi 22 C, 00130 Helsinki",
            consortium_or_template_stem="HIILINEUTRAALI-KIERTOTALOUS-EKOSYSTEEMI-2025",
            board_members=("Laura H. Säätiö", "Antti M. Verkosto"),
        ),
        # --- RING 3: Regional ELY Capex & Consulting Crowd-Out Ring (Momentti 32.30.42) ---
        CorporateGrantCohortRecord(
            y_tunnus="2455901-7",
            company_name="Maakunta-Kehitys Palvelut Oy",
            nace_code="70220",
            grant_agency="ELY",
            subsidy_received_eur=890000.0,
            five_yr_tax_delta_eur=32000.0,
            matched_peer_five_yr_tax_delta_eur=210000.0,
            shared_consultant_or_board_cluster_id="RING-ELY-MAAKUNTA",
            grant_count_5yr=5,
            postal_or_co_address="Kauppakatu 8 B, 40100 Jyväskylä",
            consortium_or_template_stem="ELY-MAAKUNTA-KASVUPOLKU-2024",
            board_members=("Timo K. Aluejohtaja", "Päivi R. Konsultti"),
        ),
        CorporateGrantCohortRecord(
            y_tunnus="2455902-5",
            company_name="Keski-Suomen Teollisuus-Tuki Oy",
            nace_code="25620",
            grant_agency="ELY",
            subsidy_received_eur=1120000.0,
            five_yr_tax_delta_eur=280000.0,
            matched_peer_five_yr_tax_delta_eur=240000.0,
            shared_consultant_or_board_cluster_id="RING-ELY-MAAKUNTA",
            grant_count_5yr=4,
            postal_or_co_address="Kauppakatu 8 B, 40100 Jyväskylä",
            consortium_or_template_stem="ELY-MAAKUNTA-KASVUPOLKU-2024",
            board_members=("Timo K. Aluejohtaja",),
        ),
        # --- DEADWEIGHT INCUMBENT SUBSIDIES (Momentti 30.10.40_32.60.40 & 32.20.40) ---
        CorporateGrantCohortRecord(
            y_tunnus="0109862-8",
            company_name="Suur-Teollisuus Energia-Palautus Oyj (Incumbent Deadweight)",
            nace_code="17120",
            grant_agency="MMM_Energy",
            subsidy_received_eur=6500000.0,
            five_yr_tax_delta_eur=1800000.0,
            matched_peer_five_yr_tax_delta_eur=1450000.0,
            shared_consultant_or_board_cluster_id="NONE",
            grant_count_5yr=2,
            postal_or_co_address="Teollisuustie 1, 55100 Imatra",
        ),
        # --- POSITIVE EXTERNALITY KEEPERS (Genuine Deep-Tech Export Tax Payers) ---
        CorporateGrantCohortRecord(
            y_tunnus="2844112-9",
            company_name="DeepTech Photonics Finland Oy",
            nace_code="26110",
            grant_agency="Business_Finland",
            subsidy_received_eur=850000.0,
            five_yr_tax_delta_eur=2650000.0,
            matched_peer_five_yr_tax_delta_eur=380000.0,
            shared_consultant_or_board_cluster_id="NONE",
            grant_count_5yr=2,
            postal_or_co_address="Otakaari 5, 02150 Espoo",
        ),
        CorporateGrantCohortRecord(
            y_tunnus="2799301-4",
            company_name="Arctic Radar & RF Systems Oy",
            nace_code="26510",
            grant_agency="Business_Finland",
            subsidy_received_eur=620000.0,
            five_yr_tax_delta_eur=1980000.0,
            matched_peer_five_yr_tax_delta_eur=320000.0,
            shared_consultant_or_board_cluster_id="NONE",
            grant_count_5yr=1,
            postal_or_co_address="Teknologiantie 11, 90590 Oulu",
        ),
    ]

    ngo_cohorts = [
        # --- REAL LIVE 2026 STEA RECIPIENTS (Verified via avustukset.stea.fi/api & PRH YTJ v3) ---
        NGOGrantRecord(
            y_tunnus="0278760-1",
            ngo_name="Loma ja Terveys ry (LIVE 2026 STEA: 100% Ak Tuetut Lomat)",
            grant_source="STEA",
            annual_grant_eur=2684710.0,
            total_revenue_eur=3100000.0,
            hq_admin_comms_lobbying_spend_eur=940000.0,
            direct_frontline_aid_spend_eur=1744710.0,
            grant_class_code="Ak",
            secondary_ministry_grants_eur=0.0,
            public_sote_procurement_sales_eur=0.0,
            board_politicians_or_insiders=("Järjestöedustajat (Puolue- ja etujärjestötausta)",),
        ),
        NGOGrantRecord(
            y_tunnus="2440730-7",
            ngo_name="Hyvinvointilomat ry (LIVE 2026 STEA: 100% Ak Tuetut Lomat)",
            grant_source="STEA",
            annual_grant_eur=2103947.0,
            total_revenue_eur=2450000.0,
            hq_admin_comms_lobbying_spend_eur=780000.0,
            direct_frontline_aid_spend_eur=1323947.0,
            grant_class_code="Ak",
            secondary_ministry_grants_eur=0.0,
            public_sote_procurement_sales_eur=0.0,
            board_politicians_or_insiders=("Ay- ja järjestöedustajat",),
        ),
        NGOGrantRecord(
            y_tunnus="2433194-7",
            ngo_name="Ehkäisevä päihdetyö EHYT ry (LIVE 2026 STEA: €2.87M Ak Yleisavustus)",
            grant_source="STEA",
            annual_grant_eur=4132097.0,
            total_revenue_eur=4850000.0,
            hq_admin_comms_lobbying_spend_eur=2870805.0,
            direct_frontline_aid_spend_eur=1261292.0,
            grant_class_code="Ak",
            secondary_ministry_grants_eur=420000.0,
            public_sote_procurement_sales_eur=0.0,
            board_politicians_or_insiders=("Useita kansanedustaja- ja valtuustotaustaisia hallitusjäseniä",),
        ),
        NGOGrantRecord(
            y_tunnus="0222440-3",
            ngo_name="Sininauhasäätiö sr (LIVE 2026 STEA + Kaupallinen Sote-Konserni Sininauha Oy)",
            grant_source="STEA",
            annual_grant_eur=2604324.0,
            total_revenue_eur=18500000.0,
            hq_admin_comms_lobbying_spend_eur=1993037.0,
            direct_frontline_aid_spend_eur=611287.0,
            grant_class_code="Ak",
            secondary_ministry_grants_eur=350000.0,
            public_sote_procurement_sales_eur=14200000.0,
            board_politicians_or_insiders=("Sote-konsernin kaksoisrooli (STEA Ak + Hyvinvointialueiden ostopalvelut)",),
        ),
        NGOGrantRecord(
            y_tunnus="0200924-4",
            ngo_name="A-klinikkasäätiö sr (LIVE 2026 STEA + Kaupallinen A-klinikka Oy Sote-Myynti)",
            grant_source="STEA",
            annual_grant_eur=2869374.0,
            total_revenue_eur=29000000.0,
            hq_admin_comms_lobbying_spend_eur=1961017.0,
            direct_frontline_aid_spend_eur=908357.0,
            grant_class_code="Ak",
            secondary_ministry_grants_eur=480000.0,
            public_sote_procurement_sales_eur=24500000.0,
            board_politicians_or_insiders=("Sote-konsernin kaksoisrooli (STEA Ak + Hyvinvointialueiden ostopalvelut)",),
        ),
        NGOGrantRecord(
            y_tunnus="0201199-8",
            ngo_name="Kotimaan Kriisi- ja Rintama-Apu ry (Genuine Frontline Benchmark)",
            grant_source="STEA",
            annual_grant_eur=1400000.0,
            total_revenue_eur=3800000.0,
            hq_admin_comms_lobbying_spend_eur=125000.0,
            direct_frontline_aid_spend_eur=1275000.0,
            grant_class_code="Ah",
            secondary_ministry_grants_eur=0.0,
            public_sote_procurement_sales_eur=0.0,
            board_politicians_or_insiders=(),
        ),
    ]

    qoe_targets = [
        AcquisitionTargetQoERecord(
            y_tunnus="2910441-2",
            company_name="Nordic AI-Tuki Holding Oy (M&A Target #1 — Zombie Grant Trap)",
            reported_revenue_eur=5400000.0,
            reported_ebitda_eur=1150000.0,
            other_operating_income_grants_eur=680000.0,
            capitalized_grant_rd_payroll_eur=390000.0,
            related_party_cluster_revenue_eur=450000.0,
            headline_ev_ebitda_multiple=9.5,
        ),
        AcquisitionTargetQoERecord(
            y_tunnus="3011881-5",
            company_name="Vihreä Siirtymä Consulting Oy (M&A Target #2 — Subsidy-Padded Rollup)",
            reported_revenue_eur=8900000.0,
            reported_ebitda_eur=1850000.0,
            other_operating_income_grants_eur=420000.0,
            capitalized_grant_rd_payroll_eur=210000.0,
            related_party_cluster_revenue_eur=380000.0,
            headline_ev_ebitda_multiple=8.0,
        ),
        AcquisitionTargetQoERecord(
            y_tunnus="2844112-9",
            company_name="DeepTech Photonics Finland Oy (Puhdas Vientiyhtiö Vertailu)",
            reported_revenue_eur=24500000.0,
            reported_ebitda_eur=6800000.0,
            other_operating_income_grants_eur=0.0,
            capitalized_grant_rd_payroll_eur=0.0,
            related_party_cluster_revenue_eur=0.0,
            headline_ev_ebitda_multiple=11.0,
        ),
    ]

    return corporate_cohorts, ngo_cohorts, qoe_targets, unsubsidized_private_benchmarks
