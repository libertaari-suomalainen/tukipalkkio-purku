"""
End-to-End Build CLI for `tukipalkkio-purku` ("Veronmaksajan Tuomioistuin").
Runs all 4 algorithmic engines and compiles `dist/index.html`, `dist/Veronmaksajan_Tuomioistuin_2026.html`,
`dist/VM_Tukipalkkio_Leikkuri_2027.xlsx`, and `dist/Media_ja_VM_Dossierit_2026.md`.
"""

import argparse
import os
import shutil
import zipfile
from typing import Dict, List

from .engine import (
    compute_subsidy_causal_roi,
    compute_subsidy_qoe_ebitda_strip,
    detect_entity_grant_rings,
    score_ngo_grant_efficiency,
    summarize_vm_momentti_guillotine,
)
from .excel_compiler import compile_vm_kehysriihi_xlsx
from .ingest import fetch_ytj_company_anonymous, load_calibrated_sovereign_dataset
from .web_compiler import compile_media_and_vm_dossiers, compile_tuomioistuin_html


def verify_reproducible_artifacts(output_dir: str) -> List[str]:
    """
    Verifies that all compiled `.xlsx` workbooks use deterministic ZIP headers and zero author metadata.
    """
    violations: List[str] = []
    for fname in os.listdir(output_dir):
        fpath = os.path.join(output_dir, fname)
        if not os.path.isfile(fpath):
            continue
        if fname.endswith(".xlsx"):
            with zipfile.ZipFile(fpath, "r") as zf:
                for zinfo in zf.infolist():
                    member = zinfo.filename
                    if "docprops" in member.lower():
                        violations.append(f"{fname}: contains author metadata file '{member}'")
                    if zinfo.date_time != (2026, 1, 1, 12, 0, 0):
                        violations.append(f"{fname} ({member}): non-deterministic ZIP timestamp {zinfo.date_time}")
                    if zinfo.create_system != 0 or zinfo.external_attr not in (0, 0x80):
                        violations.append(
                            f"{fname} ({member}): non-neutral OS header create_system={zinfo.create_system} external_attr={zinfo.external_attr}"
                        )
    return violations


def run_full_build(output_dir: str, live_ytj_enrich: bool = True) -> Dict[str, str]:
    corporate_cohorts, ngo_cohorts, qoe_targets, benchmarks = load_calibrated_sovereign_dataset()

    if live_ytj_enrich:
        for b in benchmarks:
            if not str(b["y_tunnus"]).startswith("NACE-"):
                live_meta = fetch_ytj_company_anonymous(str(b["y_tunnus"]), timeout=5.0)
                if live_meta and live_meta.get("primary_name"):
                    b["company_name"] = str(live_meta["primary_name"])

    corporate_evals = compute_subsidy_causal_roi(corporate_cohorts)
    rings = detect_entity_grant_rings(corporate_cohorts, min_cluster_entities=2, min_cluster_subsidy_eur=500000.0)
    ngo_evals = score_ngo_grant_efficiency(ngo_cohorts)
    qoe_reports = compute_subsidy_qoe_ebitda_strip(qoe_targets)
    momentti_summary = summarize_vm_momentti_guillotine(corporate_evals, ngo_evals)

    os.makedirs(output_dir, exist_ok=True)
    xlsx_path = compile_vm_kehysriihi_xlsx(
        os.path.join(output_dir, "VM_Tukipalkkio_Leikkuri_2027.xlsx"),
        corporate_evals=corporate_evals,
        rings=rings,
        ngo_evals=ngo_evals,
        qoe_reports=qoe_reports,
        benchmarks=benchmarks,
    )
    html_path = compile_tuomioistuin_html(
        os.path.join(output_dir, "Veronmaksajan_Tuomioistuin_2026.html"),
        corporate_evals=corporate_evals,
        rings=rings,
        ngo_evals=ngo_evals,
        qoe_reports=qoe_reports,
        benchmarks=benchmarks,
        momentti_summary=momentti_summary,
    )
    index_html_path = os.path.join(output_dir, "index.html")
    shutil.copyfile(html_path, index_html_path)

    dossier_path = compile_media_and_vm_dossiers(
        os.path.join(output_dir, "Media_ja_VM_Dossierit_2026.md"),
        corporate_evals=corporate_evals,
        rings=rings,
        ngo_evals=ngo_evals,
        qoe_reports=qoe_reports,
        momentti_summary=momentti_summary,
    )

    violations = verify_reproducible_artifacts(output_dir)
    if violations:
        raise RuntimeError("Reproducible Artifact Check Failed:\n  - " + "\n  - ".join(violations))

    return {
        "xlsx": xlsx_path,
        "html": html_path,
        "pages_index": index_html_path,
        "dossier": dossier_path,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Tukipalkkio-Purku Build CLI")
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "dist"),
        help="Output directory for compiled Excel, HTML, and Markdown deliverables",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Skip live PRH YTJ Open Data API v3 enrichment",
    )
    args = parser.parse_args()
    artifacts = run_full_build(args.output_dir, live_ytj_enrich=not args.offline)
    for k, v in artifacts.items():
        print(f"[OK] Compiled {k.upper()}: dist/{os.path.basename(v)}")


if __name__ == "__main__":
    main()
