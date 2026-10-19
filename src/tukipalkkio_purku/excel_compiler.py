"""
Zero-Dependency OpenXML (.xlsx) Compiler for `VM_Tukipalkkio_Leikkuri_2027.xlsx`.
Generates a multi-sheet, formula-enabled Excel 2007+ workbook using only Python's standard library (`zipfile` + `xml.sax.saxutils`).
"""

import os
import zipfile
from typing import Dict, List, Sequence, Union
from xml.sax.saxutils import escape

CellValue = Union[str, int, float]


def _col_letter(col_idx_1based: int) -> str:
    res = ""
    n = col_idx_1based
    while n > 0:
        n, rem = divmod(n - 1, 26)
        res = chr(65 + rem) + res
    return res


def _build_worksheet_xml(rows: Sequence[Sequence[CellValue]], col_widths: Sequence[int]) -> str:
    cols_xml_parts = []
    for idx, w in enumerate(col_widths, start=1):
        cols_xml_parts.append(f'<col min="{idx}" max="{idx}" width="{w}" customWidth="1"/>')
    cols_xml = f"<cols>{''.join(cols_xml_parts)}</cols>" if cols_xml_parts else ""

    sheet_rows_xml = []
    for r_idx, row in enumerate(rows, start=1):
        cells_xml = []
        is_header = r_idx == 1
        for c_idx, val in enumerate(row, start=1):
            ref = f"{_col_letter(c_idx)}{r_idx}"
            style = ' s="1"' if is_header else (' s="2"' if isinstance(val, (int, float)) and not isinstance(val, bool) else ' s="0"')
            if isinstance(val, str) and val.startswith("="):
                formula = escape(val[1:])
                cells_xml.append(f'<c r="{ref}" s="3"><f>{formula}</f></c>')
            elif isinstance(val, (int, float)) and not isinstance(val, bool):
                cells_xml.append(f'<c r="{ref}"{style}><v>{val}</v></c>')
            else:
                text = escape(str(val))
                cells_xml.append(f'<c r="{ref}" t="inlineStr"{style}><is><t>{text}</t></is></c>')
        sheet_rows_xml.append(f'<row r="{r_idx}">{"".join(cells_xml)}</row>')

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"{cols_xml}"
        f'<sheetData>{"".join(sheet_rows_xml)}</sheetData>'
        "</worksheet>"
    )


def compile_vm_kehysriihi_xlsx(
    output_path: str,
    corporate_evals: List[Dict[str, object]],
    rings: List[Dict[str, object]],
    ngo_evals: List[Dict[str, object]],
    qoe_reports: List[Dict[str, object]],
    benchmarks: List[Dict[str, object]],
) -> str:
    """
    Compiles the 5-tab `VM_Tukipalkkio_Leikkuri_2027.xlsx` workbook for VM Budjettiosasto & Kehysriihi.
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Sheet 1: VM Momentti Leikkuri (National Scale + Audited Sample Rollup)
    s1_rows: List[Sequence[CellValue]] = [
        [
            "VM Momentti",
            "Valtion talousarvion momentin nimi",
            "Valtakunnallinen määräraha (€/v)",
            "Leikkausprosentti (%)",
            "Valtakunnallinen Kehysriihi-säästö (€/v)",
            "Kohdeotos: Leikattava zombi-/järjestötuki (€)",
            "Toimenpide & Lakipykälä / Ohjauskeino",
        ],
        [
            "32.20.40",
            "Tutkimus-, kehittämis- ja innovaatiotoiminnan tukeminen (Business Finland avustukset)",
            470000000,
            45.0,
            211500000,
            sum(float(c["recommended_cut_eur"]) for c in corporate_evals if c["vm_momentti"] == "32.20.40"),
            "Lakkautetaan negatiivisen DiD-verovaikutuksen zombituet ja c/o-tukikonsulttiringit",
        ],
        [
            "32.20.83",
            "Laina tutkimus- ja kehittämistoimintaan (Business Finland T&K-lainat)",
            180000000,
            50.0,
            90000000,
            sum(float(c["recommended_cut_eur"]) for c in corporate_evals if c["vm_momentti"] == "32.20.83"),
            "Lopetetaan vakuudettomat pehmolainat kroonisesti verokielteisille hakijoille",
        ],
        [
            "32.30.42",
            "Alueellinen kuljetustuki ja yritysten kehittämisavustukset (ELY-keskukset)",
            290000000,
            60.0,
            174000000,
            sum(float(c["recommended_cut_eur"]) for c in corporate_evals if c["vm_momentti"] == "32.30.42"),
            "Lakkautetaan kilpailua vääristävät paikalliset ELY-konsultti- ja koneinvestointituet",
        ],
        [
            "33.90.50",
            "Avustukset yhteisöille ja säätiöille terveyden ja sos. hyvinvoinnin edistämiseen (STEA)",
            380000000,
            55.0,
            209000000,
            sum(float(n["recoverable_cut_eur"]) for n in ngo_evals if n["vm_momentti"] == "33.90.50"),
            "Leikataan 100 % Ak-yleisavustusten keskushallinto-, vuokra- ja lobbauskulut sekä sote-tuplalaskuttajat",
        ],
        [
            "29.80.50",
            "Opetus- ja kulttuuriministeriön yleis- ja järjestöavustukset (OKM / Taike / Nuoriso)",
            420000000,
            40.0,
            168000000,
            sum(float(n["recoverable_cut_eur"]) for n in ngo_evals if n["vm_momentti"] == "29.80.50"),
            "Poistetaan poliittisten ja viestintäjärjestöjen päällekkäiset yleisavustukset",
        ],
        [
            "30.10.40_32.60.40",
            "Kansalliset maa-, teollisuus- ja energiatuet (Kuollut paino & Suurteollisuuden palautukset)",
            1450000000,
            48.0,
            696000000,
            sum(float(c["recommended_cut_eur"]) for c in corporate_evals if c["vm_momentti"] == "30.10.40_32.60.40"),
            "Leikataan suuryritysten kuolleen painon (Deadweight ROI < 0.5) energiaveropalautukset ja tuet",
        ],
        [
            "YHTEENSÄ",
            "KAIKKI TUKIPALKKIO-PURKU MOMENTIT YHTEENSÄ (KEHYSRIIHI 2027)",
            "=SUM(C2:C7)",
            48.5,
            "=SUM(E2:E7)",
            "=SUM(F2:F7)",
            "Välitön toimeenpano valtion talousarvioesityksessä (0 € leikkaus rintamatyöhön)",
        ],
    ]

    # Sheet 2: Corporate Zombie Blacklist & Benchmark Comparison
    s2_rows: List[Sequence[CellValue]] = [
        [
            "Y-tunnus",
            "Yrityksen nimi",
            "Virasto / Rahoittaja",
            "VM Momentti",
            "Saatu yritystuki 5v (€)",
            "Kausaalinen DiD-vero-ROI",
            "Krooninen tukifarmaaja",
            "Luokitus",
            "Suositeltu leikkaus (€)",
            "Arvioitu tukikonsulttien palkkiovuoto (20 % €)",
            "Verkosto-Klusteri ID",
        ]
    ]
    for c in corporate_evals:
        s2_rows.append([
            str(c["y_tunnus"]),
            str(c["company_name"]),
            str(c["grant_agency"]),
            str(c["vm_momentti"]),
            float(c["subsidy_received_eur"]),
            float(c["causal_did_roi"]),
            "KYLLÄ" if c["is_chronic_grant_farmer"] else "EI",
            str(c["classification"]),
            float(c["recommended_cut_eur"]),
            float(c["estimated_consultant_fee_leakage_eur"]),
            str(c["cluster_id"]),
        ])
    for b in benchmarks:
        s2_rows.append([
            str(b["y_tunnus"]),
            str(b["company_name"]),
            "YKSITYINEN_VERONMAKSAJA_VERTAILU",
            "EI_TUKEA",
            0.0,
            99.9,
            "EI",
            str(b["role"]),
            0.0,
            0.0,
            "BENCHMARK-CLEAN",
        ])

    # Sheet 3: Consultant & Insider Rings
    s3_rows: List[Sequence[CellValue]] = [
        [
            "Rinki-ID",
            "Yhtiöiden lkm",
            "Y-tunnukset",
            "Yhtiöiden nimet",
            "Ringin nostamat tuet yht. (€)",
            "Ringin 5v veromuutos yht. (€)",
            "Vero / Tuki -suhdeluku",
            "Tukikonsulttien 20 % siivu (€)",
            "Kytkössignaalit (Osoite / c-o / Konsortio / Hallitus)",
            "Zombi-rinki (Leikkaus 100 %)",
        ]
    ]
    for r in rings:
        s3_rows.append([
            str(r["ring_id"]),
            int(r["entity_count"]),
            ", ".join(r["y_tunnus_list"]),
            " | ".join(r["company_names"]),
            float(r["total_subsidy_eur"]),
            float(r["total_five_yr_tax_delta_eur"]),
            float(r["cluster_tax_to_grant_ratio"]),
            float(r["estimated_20pct_consultant_cut_eur"]),
            " ; ".join(r["link_signals"]),
            "KYLLÄ" if r["flagged_zombie_ring"] else "EI",
        ])

    # Sheet 4: STEA & OKM NGO Bureaucracy & Double-Dip Guillotine
    s4_rows: List[Sequence[CellValue]] = [
        [
            "Y-tunnus",
            "Järjestön / Säätiön nimi",
            "Rahoittaja",
            "VM Momentti",
            "Avustuslaji",
            "Vuosiavustus (€)",
            "Hallinto-, vuokra- ja lobbauskulut (%)",
            "Julkisen rahoituksen riippuvuusaste (%)",
            "Monikanavainen tuplalaskuttaja (Sote + STEA/OKM)",
            "Poliittiset sidonnaisuudet hallituksessa",
            "Leikkauslistalla",
            "Leikattava byrokratia- ja tuplatuki (€/v)",
        ]
    ]
    for n in ngo_evals:
        s4_rows.append([
            str(n["y_tunnus"]),
            str(n["ngo_name"]),
            str(n["grant_source"]),
            str(n["vm_momentti"]),
            str(n["grant_class_code"]),
            float(n["annual_grant_eur"]),
            float(n["overhead_and_lobbying_pct"]),
            float(n["state_dependency_pct"]),
            "KYLLÄ" if n["is_multi_source_double_dipper"] else "EI",
            ", ".join(n["political_board_insiders"]) or "Ei ilmoitettuja poliitikkoja",
            "KYLLÄ" if n["flagged_for_defunding"] else "EI (Rintama-apu säilyy)",
            float(n["recoverable_cut_eur"]),
        ])

    # Sheet 5: Tilinpäätösten Vale-EBITDA & Tukiriisunta
    s5_rows: List[Sequence[CellValue]] = [
        [
            "Y-tunnus",
            "Tarkasteltava yhtiö",
            "Raportoitu käyttökate / EBITDA (€)",
            "Tukien ja lähipiirin keinotekoinen EBITDA-lisä (€)",
            "Oikaistu todellinen kassavirta-EBITDA (€)",
            "Keinotekoisen EBITDA:n osuus (%)",
            "Yritysarvon (EV) vääristymä (€)",
            "Tilinpäätösdiagnoosi",
        ]
    ]
    for q in qoe_reports:
        s5_rows.append([
            str(q["y_tunnus"]),
            str(q["company_name"]),
            float(q["reported_ebitda_eur"]),
            float(q["subsidy_and_related_party_ebitda_inflation_eur"]),
            float(q["true_subsidy_stripped_core_ebitda_eur"]),
            float(q["ebitda_grant_inflation_pct"]),
            float(q["ev_overpayment_trap_at_headline_multiple_eur"]),
            str(q["qoe_verdict"]),
        ])

    sheets = [
        ("01_VM_Momentti_Leikkuri", _build_worksheet_xml(s1_rows, [18, 56, 26, 20, 30, 30, 56])),
        ("02_Yritystuki_Zombie_Lista", _build_worksheet_xml(s2_rows, [14, 42, 22, 16, 22, 20, 18, 28, 22, 24, 26])),
        ("03_Tukikonsultti_Ringit", _build_worksheet_xml(s3_rows, [16, 14, 34, 52, 24, 24, 18, 24, 65, 22])),
        ("04_STEA_OKM_Jarjesto_Leikkuri", _build_worksheet_xml(s4_rows, [14, 48, 14, 16, 14, 20, 26, 26, 28, 42, 22, 28])),
        ("05_Tilinpaatos_Vale_EBITDA", _build_worksheet_xml(s5_rows, [14, 48, 24, 32, 28, 24, 30, 34])),
    ]

    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        + "".join(
            f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            for i in range(1, len(sheets) + 1)
        )
        + "</Types>"
    )

    root_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        "</Relationships>"
    )

    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        "<sheets>"
        + "".join(
            f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
            for i, (name, _) in enumerate(sheets, start=1)
        )
        + "</sheets></workbook>"
    )

    wb_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + "".join(
            f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
            for i in range(1, len(sheets) + 1)
        )
        + f'<Relationship Id="rId{len(sheets) + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        + "</Relationships>"
    )

    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<numFmts count="1"><numFmt numFmtId="164" formatCode="#,##0.00"/></numFmts>'
        '<fonts count="2">'
        '<font><sz val="10"/><name val="Calibri"/></font>'
        '<font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>'
        "</fonts>"
        '<fills count="3">'
        '<fill><patternFill patternType="none"/></fill>'
        '<fill><patternFill patternType="gray125"/></fill>'
        '<fill><patternFill patternType="solid"><fgColor rgb="FF1B2A4A"/></patternFill></fill>'
        "</fills>"
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="4">'
        '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>'
        '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
        '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
        "</cellXfs>"
        "</styleSheet>"
    )

    def _write_deterministic_zip_entry(zf: zipfile.ZipFile, arcname: str, data_str: str) -> None:
        """
        Writes a ZIP entry with deterministic headers for reproducible builds.
        """
        zinfo = zipfile.ZipInfo(filename=arcname, date_time=(2026, 1, 1, 12, 0, 0))
        zinfo.compress_type = zipfile.ZIP_DEFLATED
        zinfo.create_system = 0
        zinfo.external_attr = 0x80
        with zf.open(zinfo, "w") as entry:
            entry.write(data_str.encode("utf-8"))

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        _write_deterministic_zip_entry(zf, "[Content_Types].xml", content_types_xml)
        _write_deterministic_zip_entry(zf, "_rels/.rels", root_rels_xml)
        _write_deterministic_zip_entry(zf, "xl/workbook.xml", workbook_xml)
        _write_deterministic_zip_entry(zf, "xl/_rels/workbook.xml.rels", wb_rels_xml)
        _write_deterministic_zip_entry(zf, "xl/styles.xml", styles_xml)
        for i, (_, xml_str) in enumerate(sheets, start=1):
            _write_deterministic_zip_entry(zf, f"xl/worksheets/sheet{i}.xml", xml_str)

    return output_path
