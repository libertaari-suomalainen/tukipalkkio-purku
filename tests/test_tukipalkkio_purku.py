import os
import tempfile
import unittest
import zipfile

from tukipalkkio_purku.cli import run_full_build
from tukipalkkio_purku.engine import (
    AcquisitionTargetQoERecord,
    CorporateGrantCohortRecord,
    NGOGrantRecord,
    compute_subsidy_causal_roi,
    compute_subsidy_qoe_ebitda_strip,
    detect_entity_grant_rings,
    score_ngo_grant_efficiency,
    summarize_vm_momentti_guillotine,
)
from tukipalkkio_purku.ingest import (
    join_grants_taxes_and_ytj_by_ytunnus,
    load_calibrated_sovereign_dataset,
    normalize_ytunnus,
    parse_verohallinto_tax_csv,
    validate_ytunnus_checksum,
)


class TestTukipalkkioPurkuEngine(unittest.TestCase):
    def test_corporate_subsidy_did_roi(self) -> None:
        sample = [
            CorporateGrantCohortRecord(
                "1111111-1",
                "Zombie Consulting Oy",
                "62020",
                "Business_Finland",
                500000.0,
                20000.0,
                180000.0,
                "RING-01",
            ),
            CorporateGrantCohortRecord(
                "2222222-2",
                "DeepTech Photonics Oy",
                "26110",
                "Business_Finland",
                400000.0,
                950000.0,
                200000.0,
                "NONE",
            ),
        ]
        res = compute_subsidy_causal_roi(sample)
        self.assertEqual(res[0]["classification"], "BLACKLIST_ZOMBIE")
        self.assertEqual(res[0]["recommended_cut_eur"], 500000.0)
        self.assertEqual(res[0]["vm_momentti"], "32.20.40")
        self.assertEqual(res[1]["classification"], "POSITIVE_EXTERNALITY_KEEP")
        self.assertEqual(res[1]["recommended_cut_eur"], 0.0)

    def test_entity_ring_detector_zero_cost_signals(self) -> None:
        cohort = [
            CorporateGrantCohortRecord(
                "1000001-1",
                "Tukihaku Alpha Oy",
                "62010",
                "Business_Finland",
                350000.0,
                0.0,
                140000.0,
                postal_or_co_address="c/o TukiKonsultit Oy, Mannerheimintie 12 B, 00100 Helsinki",
                consortium_or_template_stem="AI-GREEN-TRANSITION-BOILERPLATE-2025",
            ),
            CorporateGrantCohortRecord(
                "1000002-2",
                "Tukihaku Beta Oy",
                "62020",
                "ELY",
                280000.0,
                15000.0,
                120000.0,
                postal_or_co_address="c/o TukiKonsultit Oy, Mannerheimintie 12 B, 00100 Helsinki",
            ),
            CorporateGrantCohortRecord(
                "1000003-3",
                "Tukihaku Gamma Oy",
                "70220",
                "Business_Finland",
                420000.0,
                5000.0,
                160000.0,
                consortium_or_template_stem="AI-GREEN-TRANSITION-BOILERPLATE-2025",
            ),
        ]
        rings = detect_entity_grant_rings(cohort, min_cluster_entities=2, min_cluster_subsidy_eur=500000.0)
        self.assertEqual(len(rings), 1)
        self.assertEqual(rings[0]["entity_count"], 3)
        self.assertEqual(rings[0]["total_subsidy_eur"], 1050000.0)
        self.assertEqual(rings[0]["estimated_20pct_consultant_cut_eur"], 210000.0)
        self.assertTrue(rings[0]["flagged_zombie_ring"])

    def test_ngo_grant_efficiency_and_double_dip(self) -> None:
        ngos = [
            NGOGrantRecord(
                "3333333-3",
                "Byrokratia-Liitto ry",
                "STEA",
                2500000.0,
                2600000.0,
                1450000.0,
                1050000.0,
                grant_class_code="Ak",
                secondary_ministry_grants_eur=300000.0,
                board_politicians_or_insiders=("Kansanedustaja X",),
            ),
        ]
        scored = score_ngo_grant_efficiency(ngos)
        self.assertTrue(scored[0]["flagged_for_defunding"])
        self.assertTrue(scored[0]["is_multi_source_double_dipper"])
        self.assertEqual(scored[0]["recoverable_cut_eur"], 1750000.0)
        self.assertEqual(scored[0]["vm_momentti"], "33.90.50")

    def test_subsidy_qoe_ebitda_stripper(self) -> None:
        targets = [
            AcquisitionTargetQoERecord(
                y_tunnus="9999999-9",
                company_name="Grant-Propped SaaS Oy",
                reported_revenue_eur=6000000.0,
                reported_ebitda_eur=1200000.0,
                other_operating_income_grants_eur=550000.0,
                capitalized_grant_rd_payroll_eur=350000.0,
                related_party_cluster_revenue_eur=400000.0,
                headline_ev_ebitda_multiple=10.0,
            )
        ]
        qoe = compute_subsidy_qoe_ebitda_strip(targets)
        self.assertEqual(qoe[0]["qoe_verdict"], "CRITICAL_GRANT_ZOMBIE_DO_NOT_BUY")
        self.assertEqual(qoe[0]["true_subsidy_stripped_core_ebitda_eur"], 160000.0)
        self.assertEqual(qoe[0]["ev_overpayment_trap_at_headline_multiple_eur"], 10400000.0)

    def test_vm_momentti_summary(self) -> None:
        corp = compute_subsidy_causal_roi([
            CorporateGrantCohortRecord("1111111-1", "Zombie Oy", "62020", "Business_Finland", 500000.0, 0.0, 150000.0),
        ])
        ngo = score_ngo_grant_efficiency([
            NGOGrantRecord("3333333-3", "Byrokratia ry", "STEA", 2000000.0, 2100000.0, 1200000.0, 800000.0),
        ])
        summary = summarize_vm_momentti_guillotine(corp, ngo)
        self.assertEqual(summary["32.20.40"], 500000.0)
        self.assertEqual(summary["33.90.50"], 1200000.0)

    def test_relational_join_on_ytunnus_and_csv_parser(self) -> None:
        self.assertEqual(normalize_ytunnus("FI01120389"), "0112038-9")
        self.assertEqual(normalize_ytunnus("1710128-9"), "1710128-9")

        csv_text = (
            "Y-tunnus;Yhteisön nimi;Toimiala;Maksuunpantu vero yhteensä\n"
            "1710128-9;Tueton Ohjelmistoverrokki Oy;61100;950000,00\n"
            "2910441-2;Nordic AI-Tuki Holding Oy;61100;0,00\n"
        )
        tax_rows = parse_verohallinto_tax_csv(csv_text)
        grant_rows = [
            {
                "y_tunnus": "FI29104412",
                "company_name": "Nordic AI-Tuki Holding Oy",
                "nace_code": "61100",
                "grant_agency": "Business_Finland",
                "subsidy_eur": 750000.0,
                "grant_count": 4,
            }
        ]
        joined = join_grants_taxes_and_ytj_by_ytunnus(grant_rows, tax_rows)
        self.assertEqual(len(joined), 1)
        self.assertEqual(joined[0].y_tunnus, "2910441-2")
        self.assertEqual(joined[0].matched_peer_five_yr_tax_delta_eur, 950000.0)

    def test_full_end_to_end_artifact_compilation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            artifacts = run_full_build(tmpdir, live_ytj_enrich=False)
            self.assertTrue(os.path.exists(artifacts["xlsx"]))
            self.assertTrue(os.path.exists(artifacts["html"]))
            self.assertTrue(os.path.exists(artifacts["dossier"]))
            with zipfile.ZipFile(artifacts["xlsx"], "r") as zf:
                names = zf.namelist()
                self.assertIn("xl/worksheets/sheet1.xml", names)
                self.assertIn("xl/worksheets/sheet5.xml", names)
            with open(artifacts["html"], "r", encoding="utf-8") as f:
                html_text = f.read()
            self.assertNotIn("Konkurssiin 2024", html_text)
            self.assertIn("1 288 virallista avustuspäätöstä", html_text)

    def test_peer_review_ytunnus_checksums_and_classifications(self) -> None:
        corps, ngos, qoes, benchmarks = load_calibrated_sovereign_dataset()
        self.assertEqual(len(corps) + len(benchmarks), 47)
        for c in corps:
            self.assertTrue(validate_ytunnus_checksum(c.y_tunnus), f"Invalid corporate Y-tunnus: {c.y_tunnus}")
        for n in ngos:
            self.assertTrue(validate_ytunnus_checksum(n.y_tunnus), f"Invalid NGO Y-tunnus: {n.y_tunnus}")
        for b in benchmarks:
            self.assertTrue(validate_ytunnus_checksum(str(b["y_tunnus"])), f"Invalid benchmark Y-tunnus: {b['y_tunnus']}")

        evals = {x["y_tunnus"]: x for x in compute_subsidy_causal_roi(corps)}
        self.assertEqual(evals["2766860-9"]["classification"], "BLACKLIST_ZOMBIE")  # Infinited Fiber (€0 tax)
        self.assertEqual(evals["2712152-3"]["classification"], "BLACKLIST_ZOMBIE")  # Woodio (€0 tax)
        self.assertEqual(evals["1041090-0"]["classification"], "DEADWEIGHT_CROWD_OUT")  # UPM-Kymmene
        self.assertEqual(evals["1852302-9"]["classification"], "DEADWEIGHT_CROWD_OUT")  # Neste
        self.assertEqual(evals["0112038-9"]["classification"], "POSITIVE_EXTERNALITY_KEEP")  # Nokia

        ngo_evals = score_ngo_grant_efficiency(ngos)
        for ne in ngo_evals:
            self.assertLessEqual(float(ne["recoverable_cut_eur"]), float(ne["annual_grant_eur"]))


if __name__ == "__main__":
    unittest.main()
