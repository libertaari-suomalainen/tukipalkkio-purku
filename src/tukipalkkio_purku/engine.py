"""
Tukipalkkio-Purku Core Engine v2.2 ("Veronmaksajan Tuomioistuin").
Implements four public-subsidy audit algorithms:
  1. Matched-Peer Difference-in-Differences (DiD) Corporate Subsidy Causal ROI Calculator + VM Momentti Compiler
  2. Multi-Registry Entity-Graph Related-Party, c/o Address & Grant-Consultant Ring Detector
  3. STEA / OKM / Ministry NGO Bureaucracy, Ak-Slush & Sote Double-Dip Scorer
  4. Financial Quality-of-Earnings (QoE) Non-Operating Subsidy & Related-Party EBITDA Stripper
"""

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple


AGENCY_TO_VM_MOMENTTI: Dict[str, str] = {
    "Business_Finland": "32.20.40",
    "Business_Finland_Loan": "32.20.83",
    "ELY": "32.30.42",
    "MMM_Energy": "30.10.40_32.60.40",
    "STEA": "33.90.50",
    "OKM": "29.80.50",
    "STM": "33.01.50",
}


@dataclass(frozen=True)
class CorporateGrantCohortRecord:
    y_tunnus: str
    company_name: str
    nace_code: str
    grant_agency: str  # "Business_Finland", "Business_Finland_Loan", "ELY", "MMM_Energy"
    subsidy_received_eur: float
    five_yr_tax_delta_eur: float
    matched_peer_five_yr_tax_delta_eur: float
    shared_consultant_or_board_cluster_id: str = "NONE"
    grant_count_5yr: int = 1
    postal_or_co_address: str = ""
    consortium_or_template_stem: str = ""
    board_members: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class NGOGrantRecord:
    y_tunnus: str
    ngo_name: str
    grant_source: str  # "STEA", "OKM", "STM"
    annual_grant_eur: float
    total_revenue_eur: float
    hq_admin_comms_lobbying_spend_eur: float
    direct_frontline_aid_spend_eur: float
    grant_class_code: str = "Ak"  # "Ak" = continuous operating grant, "Ay" = general grant, "C"/"B" = project/investment
    secondary_ministry_grants_eur: float = 0.0
    public_sote_procurement_sales_eur: float = 0.0
    board_politicians_or_insiders: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AcquisitionTargetQoERecord:
    y_tunnus: str
    company_name: str
    reported_revenue_eur: float
    reported_ebitda_eur: float
    other_operating_income_grants_eur: float
    capitalized_grant_rd_payroll_eur: float
    related_party_cluster_revenue_eur: float
    headline_ev_ebitda_multiple: float = 8.0


def compute_subsidy_causal_roi(records: List[CorporateGrantCohortRecord]) -> List[Dict[str, object]]:
    """
    Computes 5-year Difference-in-Differences (DiD) Net Fiscal ROI for each grant recipient
    relative to its unsubsidized NACE/size peer cohort, classifying zero-tax grant targets
    ('BLACKLIST_ZOMBIE') separately from profitable incumbent deadweight subsidies
    ('DEADWEIGHT_CROWD_OUT') and mapping every recommended euro cut to its VM budget momentti.
    """
    evaluated: List[Dict[str, object]] = []
    for r in records:
        causal_tax_gain = r.five_yr_tax_delta_eur - r.matched_peer_five_yr_tax_delta_eur
        net_roi = causal_tax_gain / r.subsidy_received_eur if r.subsidy_received_eur > 0 else 0.0
        gross_tax_to_grant = r.five_yr_tax_delta_eur / r.subsidy_received_eur if r.subsidy_received_eur > 0 else 0.0
        is_chronic_farmer = r.grant_count_5yr >= 3 and gross_tax_to_grant < 0.25
        is_zero_or_near_zero_tax = (
            r.five_yr_tax_delta_eur <= 0.0
            or (gross_tax_to_grant <= 0.05 and r.five_yr_tax_delta_eur <= 50000.0)
        )

        if is_zero_or_near_zero_tax and net_roi < 0.5:
            classification = "BLACKLIST_ZOMBIE"
            cut_pct = 100.0
        elif net_roi < 0.5 or is_chronic_farmer:
            classification = "DEADWEIGHT_CROWD_OUT"
            cut_pct = 100.0
        elif net_roi < 1.2:
            classification = "LOW_YIELD_REVIEW"
            cut_pct = 50.0
        else:
            classification = "POSITIVE_EXTERNALITY_KEEP"
            cut_pct = 0.0

        recommended_cut = round(r.subsidy_received_eur * (cut_pct / 100.0), 2)
        estimated_consultant_leakage = (
            round(r.subsidy_received_eur * 0.20, 2)
            if r.shared_consultant_or_board_cluster_id != "NONE" or is_chronic_farmer
            else 0.0
        )

        evaluated.append({
            "y_tunnus": r.y_tunnus,
            "company_name": r.company_name,
            "nace_code": r.nace_code,
            "postal_or_co_address": r.postal_or_co_address,
            "grant_agency": r.grant_agency,
            "vm_momentti": AGENCY_TO_VM_MOMENTTI.get(r.grant_agency, "32.20.40"),
            "subsidy_received_eur": r.subsidy_received_eur,
            "five_yr_tax_delta_eur": r.five_yr_tax_delta_eur,
            "recipient_five_yr_tax_delta_eur": r.five_yr_tax_delta_eur,
            "matched_peer_five_yr_tax_delta_eur": r.matched_peer_five_yr_tax_delta_eur,
            "causal_did_roi": round(net_roi, 2),
            "is_chronic_grant_farmer": is_chronic_farmer,
            "classification": classification,
            "recommended_cut_eur": recommended_cut,
            "estimated_consultant_fee_leakage_eur": estimated_consultant_leakage,
            "cluster_id": r.shared_consultant_or_board_cluster_id,
        })
    return evaluated


def detect_entity_grant_rings(
    records: List[CorporateGrantCohortRecord],
    min_cluster_entities: int = 2,
    min_cluster_subsidy_eur: float = 300000.0,
) -> List[Dict[str, object]]:
    """
    Multi-Registry Entity-Resolution Graph Engine (Company <-> Address/c-o <-> Consortium <-> Board).
    """
    n = len(records)
    if n == 0:
        return []

    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[max(ri, rj)] = min(ri, rj)

    by_cluster_id: Dict[str, List[int]] = defaultdict(list)
    by_address: Dict[str, List[int]] = defaultdict(list)
    by_stem: Dict[str, List[int]] = defaultdict(list)
    by_person: Dict[str, List[int]] = defaultdict(list)

    for idx, r in enumerate(records):
        if r.shared_consultant_or_board_cluster_id and r.shared_consultant_or_board_cluster_id != "NONE":
            by_cluster_id[r.shared_consultant_or_board_cluster_id.strip().upper()].append(idx)
        if r.postal_or_co_address and r.postal_or_co_address.strip():
            by_address[r.postal_or_co_address.strip().lower()].append(idx)
        if r.consortium_or_template_stem and r.consortium_or_template_stem.strip():
            by_stem[r.consortium_or_template_stem.strip().lower()].append(idx)
        for person in r.board_members:
            if person and person.strip():
                by_person[person.strip().lower()].append(idx)

    edge_reasons: Dict[int, Set[str]] = defaultdict(set)

    for key, group in by_cluster_id.items():
        if len(group) >= 2:
            for k in group[1:]:
                union(group[0], k)
            for k in group:
                edge_reasons[k].add(f"CLUSTER:{key}")

    for addr, group in by_address.items():
        if len(group) >= 2:
            for k in group[1:]:
                union(group[0], k)
            for k in group:
                edge_reasons[k].add(f"SHARED_ADDRESS:{addr}")

    for stem, group in by_stem.items():
        if len(group) >= 2:
            for k in group[1:]:
                union(group[0], k)
            for k in group:
                edge_reasons[k].add(f"SHARED_TEMPLATE_OR_CONSORTIUM:{stem}")

    for person, group in by_person.items():
        if len(group) >= 2:
            for k in group[1:]:
                union(group[0], k)
            for k in group:
                edge_reasons[k].add(f"SHARED_BOARD_INSIDER:{person}")

    components: Dict[int, List[int]] = defaultdict(list)
    for idx in range(n):
        components[find(idx)].append(idx)

    rings: List[Dict[str, object]] = []
    for root_idx, member_indices in components.items():
        if len(member_indices) < min_cluster_entities:
            continue
        members = [records[i] for i in member_indices]
        total_subsidy = sum(m.subsidy_received_eur for m in members)
        if total_subsidy < min_cluster_subsidy_eur:
            continue
        total_tax_delta = sum(m.five_yr_tax_delta_eur for m in members)
        signals: Set[str] = set()
        for i in member_indices:
            signals.update(edge_reasons[i])

        cluster_tax_ratio = total_tax_delta / total_subsidy if total_subsidy > 0 else 0.0
        primary_addr = next((m.postal_or_co_address for m in members if m.postal_or_co_address), "Jaettu T&K-konsortio")
        primary_cluster = next(
            (m.shared_consultant_or_board_cluster_id for m in members if m.shared_consultant_or_board_cluster_id != "NONE"),
            f"TUKI-RING-{root_idx + 1:03d}",
        )
        rings.append({
            "ring_id": f"TUKI-RING-{root_idx + 1:03d}",
            "ring_signature": primary_cluster,
            "shared_address_or_agent": primary_addr,
            "entity_count": len(members),
            "y_tunnus_list": [m.y_tunnus for m in members],
            "member_ytunnus": [m.y_tunnus for m in members],
            "company_names": [m.company_name for m in members],
            "member_names": [m.company_name for m in members],
            "total_subsidy_eur": round(total_subsidy, 2),
            "total_five_yr_tax_delta_eur": round(total_tax_delta, 2),
            "cluster_tax_to_grant_ratio": round(cluster_tax_ratio, 2),
            "estimated_20pct_consultant_cut_eur": round(total_subsidy * 0.20, 2),
            "link_signals": sorted(signals),
            "flagged_zombie_ring": cluster_tax_ratio < 0.25,
        })

    rings.sort(key=lambda x: float(x["total_subsidy_eur"]), reverse=True)
    return rings


def score_ngo_grant_efficiency(ngos: List[NGOGrantRecord]) -> List[Dict[str, object]]:
    """
    Flags STEA and Ministry NGO grant recipients where HQ/admin/comms/lobbying overhead exceeds 20%,
    state-funding dependency exceeds 75% ('valtionapu-automaatti'), or the NGO double-dips across
    multiple ministries / Wellbeing County Sote procurement while drawing tax-free Ak general grants.
    """
    scored: List[Dict[str, object]] = []
    for n in ngos:
        overhead_pct = (n.hq_admin_comms_lobbying_spend_eur / n.annual_grant_eur) * 100.0 if n.annual_grant_eur else 0.0
        total_public_inflow = n.annual_grant_eur + n.secondary_ministry_grants_eur + n.public_sote_procurement_sales_eur
        state_dependency_pct = (total_public_inflow / n.total_revenue_eur) * 100.0 if n.total_revenue_eur else 0.0
        is_double_dipper = (n.secondary_ministry_grants_eur > 0.0) or (n.public_sote_procurement_sales_eur > 0.0)
        is_flagged = overhead_pct > 20.0 or state_dependency_pct > 75.0 or (n.secondary_ministry_grants_eur > 0.0)
        recoverable_eur = (
            min(n.annual_grant_eur, n.hq_admin_comms_lobbying_spend_eur + n.secondary_ministry_grants_eur)
            if is_flagged
            else 0.0
        )
        scored.append({
            "y_tunnus": n.y_tunnus,
            "ngo_name": n.ngo_name,
            "grant_source": n.grant_source,
            "primary_ministry": n.grant_source,
            "vm_momentti": AGENCY_TO_VM_MOMENTTI.get(n.grant_source, "33.90.50"),
            "grant_class_code": n.grant_class_code,
            "grant_type_code": n.grant_class_code,
            "annual_grant_eur": n.annual_grant_eur,
            "total_revenue_eur": n.total_revenue_eur,
            "hq_admin_comms_lobbying_spend_eur": n.hq_admin_comms_lobbying_spend_eur,
            "direct_frontline_aid_spend_eur": n.direct_frontline_aid_spend_eur,
            "secondary_ministry_grants_eur": n.secondary_ministry_grants_eur,
            "public_sote_procurement_sales_eur": n.public_sote_procurement_sales_eur,
            "commercial_sote_revenue_eur": n.public_sote_procurement_sales_eur,
            "overhead_and_lobbying_pct": round(overhead_pct, 1),
            "non_frontline_overhead_share": round(overhead_pct / 100.0, 3),
            "state_dependency_pct": round(state_dependency_pct, 1),
            "is_multi_source_double_dipper": is_double_dipper,
            "political_board_insiders": list(n.board_politicians_or_insiders),
            "flagged_for_defunding": is_flagged,
            "classification": "GUILLOTINE_ADMIN_BLOAT" if is_flagged else "FRONTLINE_KEEP",
            "recoverable_cut_eur": round(recoverable_eur, 2),
        })
    return scored


def compute_subsidy_qoe_ebitda_strip(targets: List[AcquisitionTargetQoERecord]) -> List[Dict[str, object]]:
    """
    Financial Quality-of-Earnings (QoE) Subsidy Stripper.
    """
    reports: List[Dict[str, object]] = []
    for t in targets:
        artificial_ebitda_boost = (
            t.other_operating_income_grants_eur
            + t.capitalized_grant_rd_payroll_eur
            + (t.related_party_cluster_revenue_eur * 0.35)
        )
        true_core_ebitda = t.reported_ebitda_eur - artificial_ebitda_boost
        grant_inflation_pct = (
            (artificial_ebitda_boost / t.reported_ebitda_eur) * 100.0
            if t.reported_ebitda_eur > 0
            else 100.0
        )
        ev_overpayment_trap_eur = artificial_ebitda_boost * t.headline_ev_ebitda_multiple

        if true_core_ebitda <= 0.0 or grant_inflation_pct >= 50.0:
            qoe_verdict = "CRITICAL_GRANT_ZOMBIE_DO_NOT_BUY"
        elif grant_inflation_pct >= 15.0:
            qoe_verdict = "HIGH_SUBSIDY_DISTORTION_REPRICE_EV"
        else:
            qoe_verdict = "CLEAN_ORGANIC_EARNINGS"

        reports.append({
            "y_tunnus": t.y_tunnus,
            "company_name": t.company_name,
            "reported_revenue_eur": round(t.reported_revenue_eur, 2),
            "reported_ebitda_eur": round(t.reported_ebitda_eur, 2),
            "direct_grants_in_other_income_eur": round(t.other_operating_income_grants_eur, 2),
            "subsidy_and_related_party_ebitda_inflation_eur": round(artificial_ebitda_boost, 2),
            "true_subsidy_stripped_core_ebitda_eur": round(true_core_ebitda, 2),
            "true_standalone_ebitda_eur": round(true_core_ebitda, 2),
            "ebitda_grant_inflation_pct": round(grant_inflation_pct, 1),
            "ev_overpayment_trap_at_headline_multiple_eur": round(ev_overpayment_trap_eur, 2),
            "qoe_verdict": qoe_verdict,
        })
    return reports


def summarize_vm_momentti_guillotine(
    corporate_evals: List[Dict[str, object]],
    ngo_evals: List[Dict[str, object]],
) -> Dict[str, float]:
    """
    Aggregates all recommended corporate and NGO subsidy cuts by official VM State Budget Momentti code.
    """
    totals: Dict[str, float] = defaultdict(float)
    for c in corporate_evals:
        momentti = str(c["vm_momentti"])
        totals[momentti] = round(totals[momentti] + float(c["recommended_cut_eur"]), 2)
    for n in ngo_evals:
        momentti = str(n["vm_momentti"])
        totals[momentti] = round(totals[momentti] + float(n["recoverable_cut_eur"]), 2)
    return dict(totals)
