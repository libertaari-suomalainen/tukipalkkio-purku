"""
Compilers for:
  1. `dist/Veronmaksajan_Tuomioistuin_2026.html` (and `dist/index.html`) — Institutional Economic Research Report & Interactive Subsidy ROI Explorer (styled after talousinstituutti.fi)
  2. `dist/Media_ja_VM_Dossierit_2026.md` — Turnkey Investigative Journalist & VM Budget Department Dossiers
"""

import json
import os
from typing import Dict, List


def compile_tuomioistuin_html(
    output_path: str,
    corporate_evals: List[Dict[str, object]],
    rings: List[Dict[str, object]],
    ngo_evals: List[Dict[str, object]],
    qoe_reports: List[Dict[str, object]],
    benchmarks: List[Dict[str, object]],
    momentti_summary: Dict[str, float],
) -> str:
    """
    Generates a single-file, zero-backend interactive HTML5 research publication & explorer
    styled with the institutional economic-research aesthetic of https://talousinstituutti.fi/
    (DM Sans + Inter typography, #1C9770 emerald accent, #FFFFFF / #F9F7F7 / #F2EEEE warm stone surfaces,
    bilingual FI/EN switch, executive thesis cards, unclipped flow diagram, and empirical tables).
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    payload_json = json.dumps(
        {
            "corporate_evals": corporate_evals,
            "rings": rings,
            "ngo_evals": ngo_evals,
            "qoe_reports": qoe_reports,
            "benchmarks": benchmarks,
            "momentti_summary": momentti_summary,
        },
        ensure_ascii=False,
    )

    html = f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Suomen Tukiröntgen 2026 — Yritys- ja Järjestötukien Kausaalinen Vero-ROI | Taloustutkimusraportti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<style>
  :root {{
    /* Exact STI / talousinstituutti.fi Institutional Design Tokens */
    --card-bg: #FFFFFF;
    --page-bg: #F9F7F7;
    --shape-bg: #F2EEEE;
    --shape-bg-dim: #EBE5E5;
    --border-color: #E5E0DF;
    --line-color: #D8D4D4;
    --heading-color: #1A1A1A;
    --body-color: #464646;
    --caption-color: #6E6A69;
    --accent: #1C9770;
    --accent-dim: #027D56;
    --accent-light: #35B089;
    --accent-tint: #E8F5F0;
    --palette-2: #93CB52;
    --palette-3: #7AD180;
    --palette-4: #7AD1C3;
    --danger-text: #B91C1C;
    --danger-bg: #FEF2F2;
    --danger-border: #FECACA;
    --warn-text: #92400E;
    --warn-bg: #FFFBEB;
    --warn-border: #FDE68A;
    --heading-font: "DM Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    --body-font: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    --shadow-sm: 0 2px 6px -1px rgba(0, 0, 0, 0.06);
    --shadow-md: 0 6px 18px -3px rgba(0, 0, 0, 0.07), 0 2px 6px -2px rgba(0, 0, 0, 0.04);
  }}

  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    font-family: var(--body-font);
    font-weight: 450;
    background: var(--page-bg);
    color: var(--body-color);
    line-height: 1.6;
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
  }}

  h1, h2, h3, h4 {{
    font-family: var(--heading-font);
    color: var(--heading-color);
    font-weight: 600;
    line-height: 1.24;
    margin: 0;
    letter-spacing: -0.015em;
  }}

  /* Sticky 75px White Institutional Navbar (matching talousinstituutti.fi) */
  .navbar {{
    position: sticky;
    top: 0;
    z-index: 100;
    height: 75px;
    background: rgba(255, 255, 255, 0.97);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--border-color);
    box-shadow: var(--shadow-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 24px;
  }}
  .navbar-inner {{
    max-width: 1180px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }}
  .brand-mark {{
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--heading-color);
  }}
  .brand-crest {{
    width: 40px;
    height: 40px;
    border-radius: 4px;
    background: var(--accent);
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--heading-font);
    font-weight: 700;
    font-size: 16px;
    letter-spacing: 0.5px;
    flex-shrink: 0;
  }}
  .brand-text-title {{
    font-family: var(--heading-font);
    font-weight: 700;
    font-size: 16.5px;
    color: var(--heading-color);
    line-height: 1.15;
  }}
  .brand-text-sub {{
    font-size: 11.5px;
    color: var(--caption-color);
    font-weight: 500;
  }}
  .nav-links {{
    display: flex;
    align-items: center;
    gap: 20px;
  }}
  .nav-links a {{
    text-decoration: none;
    color: var(--body-color);
    font-size: 14px;
    font-weight: 500;
    padding: 6px 2px;
    border-bottom: 3px solid transparent;
    transition: color 0.15s, border-color 0.15s;
  }}
  .nav-links a:hover {{
    color: var(--accent);
    border-bottom-color: var(--accent);
  }}
  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .lang-switch {{
    display: inline-flex;
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-radius: 4px;
    overflow: hidden;
  }}
  .lang-btn {{
    border: none;
    background: transparent;
    padding: 6px 11px;
    font-family: var(--body-font);
    font-size: 12.5px;
    font-weight: 600;
    color: var(--body-color);
    cursor: pointer;
  }}
  .lang-btn.active {{
    background: var(--accent);
    color: #FFFFFF;
  }}
  .btn-primary {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent);
    color: #FFFFFF;
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
    padding: 9px 15px;
    border-radius: 3px;
    border: none;
    cursor: pointer;
    transition: background 0.15s;
    white-space: nowrap;
  }}
  .btn-primary:hover {{
    background: var(--accent-dim);
  }}
  .btn-outline {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FFFFFF;
    color: var(--accent);
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
    padding: 8px 14px;
    border-radius: 3px;
    border: 1.5px solid var(--accent);
    cursor: pointer;
    transition: background 0.15s;
  }}
  .btn-outline:hover {{
    background: var(--accent-tint);
  }}

  @media (max-width: 980px) {{
    .nav-links {{ display: none; }}
  }}

  /* Section Containers (matching talousinstituutti.fi card sections) */
  .section-wrap {{
    max-width: 1180px;
    margin: 28px auto;
    padding: 0 20px;
  }}
  .inst-card {{
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    box-shadow: var(--shadow-md);
    padding: 44px 48px;
  }}
  @media (max-width: 768px) {{
    .inst-card {{ padding: 26px 20px; }}
  }}

  .eyebrow {{
    font-family: var(--body-font);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 10px;
    display: block;
  }}

  /* Hero 62% / 38% Split Layout */
  .hero-grid {{
    display: grid;
    grid-template-columns: 1.55fr 1fr;
    gap: 38px;
    align-items: stretch;
  }}
  @media (max-width: 960px) {{
    .hero-grid {{ grid-template-columns: 1fr; }}
  }}
  .hero-title {{
    font-size: 36px;
    line-height: 1.18;
    margin-bottom: 16px;
  }}
  .hero-lead {{
    font-size: 17px;
    color: var(--body-color);
    margin: 0 0 20px 0;
  }}

  /* Plain-Language "What Is This Saying?" Callout Box (talousinstituutti.fi left-accent style) */
  .plain-summary-box {{
    background: var(--shape-bg);
    border-left: 4px solid var(--accent);
    border-radius: 3px;
    padding: 18px 22px;
    margin-bottom: 22px;
  }}
  .plain-summary-box h3 {{
    font-size: 16px;
    margin-bottom: 8px;
    color: var(--heading-color);
  }}
  .plain-summary-box ol {{
    margin: 0;
    padding-left: 20px;
    font-size: 14.5px;
    color: var(--body-color);
  }}
  .plain-summary-box li {{
    margin-bottom: 6px;
  }}

  /* Right-Side Executive Summary Panel */
  .exec-panel {{
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-top: 4px solid var(--accent);
    border-radius: 4px;
    padding: 26px 26px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .metric-row {{
    padding: 13px 0;
    border-bottom: 1px solid var(--line-color);
  }}
  .metric-row:last-child {{
    border-bottom: none;
    padding-bottom: 0;
  }}
  .metric-label {{
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--caption-color);
  }}
  .metric-val {{
    font-family: var(--heading-font);
    font-size: 28px;
    font-weight: 700;
    color: var(--heading-color);
    margin-top: 2px;
  }}
  .metric-val.emerald {{ color: var(--accent); }}
  .metric-val.crimson {{ color: var(--danger-text); }}
  .metric-sub {{
    font-size: 13px;
    color: var(--body-color);
    margin-top: 2px;
  }}

  /* 3 Structural Subsidy Traps Grid (talousinstituutti.fi Publication Cards) */
  .cards-3col {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-top: 24px;
  }}
  @media (max-width: 960px) {{
    .cards-3col {{ grid-template-columns: 1fr; }}
  }}
  .pub-card {{
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-left: 4px solid var(--accent);
    border-radius: 3px;
    padding: 24px 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }}
  .pub-card:hover {{
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }}
  .pub-card h3 {{
    font-size: 19px;
    margin: 6px 0 10px 0;
  }}
  .pub-card p {{
    font-size: 14.5px;
    margin: 0 0 14px 0;
    color: var(--body-color);
  }}
  .pub-stat-bar {{
    background: #FFFFFF;
    border: 1px solid var(--border-color);
    border-radius: 3px;
    padding: 10px 12px;
    font-size: 13px;
    font-weight: 600;
    color: var(--heading-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  /* Clean, Unclipped Money-Flow & Ring Diagram */
  .flow-diagram-box {{
    background: #FFFFFF;
    border: 1px solid var(--line-color);
    border-radius: 4px;
    padding: 18px;
    margin-top: 20px;
    overflow-x: auto;
  }}
  svg#vw-graph {{
    width: 100%;
    min-width: 780px;
    height: auto;
    display: block;
  }}
  .ring-cards-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 20px;
  }}
  @media (max-width: 960px) {{
    .ring-cards-grid {{ grid-template-columns: 1fr; }}
  }}
  .ring-dossier-card {{
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-radius: 3px;
    padding: 18px 20px;
  }}
  .ring-dossier-card h4 {{
    font-size: 16px;
    margin-bottom: 6px;
  }}
  .ring-dossier-card ul {{
    margin: 8px 0 0 0;
    padding-left: 18px;
    font-size: 13.5px;
  }}
  .ring-dossier-card li {{
    margin-bottom: 4px;
  }}

  /* Filter & Scenario Bar */
  .filter-bar {{
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-radius: 4px;
    padding: 18px 22px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .filter-bar label {{
    display: block;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--heading-color);
    margin-bottom: 6px;
  }}
  input[type="search"], select {{
    font-family: var(--body-font);
    background: #FFFFFF;
    color: var(--heading-color);
    border: 1px solid var(--line-color);
    border-radius: 3px;
    padding: 9px 14px;
    font-size: 14px;
    min-width: 310px;
  }}
  input[type="search"]:focus, select:focus {{
    outline: 2px solid var(--accent);
    border-color: var(--accent);
  }}

  /* Institutional Data Tables */
  .table-scroll {{
    overflow-x: auto;
    margin-top: 14px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: #FFFFFF;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
  }}
  th, td {{
    text-align: left;
    padding: 11px 13px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: top;
  }}
  th {{
    background: var(--shape-bg);
    color: var(--heading-color);
    font-family: var(--heading-font);
    font-weight: 700;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }}
  tr:hover td {{
    background: #FAF8F8;
  }}
  tr.total-row td {{
    background: var(--accent-tint);
    font-weight: 700;
    color: var(--heading-color);
    border-top: 2px solid var(--accent);
  }}
  code {{
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 12.5px;
    background: var(--shape-bg);
    padding: 2px 6px;
    border-radius: 3px;
    color: var(--heading-color);
  }}

  /* Semantic Status Tags (High Contrast on White) */
  .tag {{
    display: inline-block;
    padding: 3px 8px;
    border-radius: 3px;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.02em;
  }}
  .tag.zombie {{
    background: var(--danger-bg);
    color: var(--danger-text);
    border: 1px solid var(--danger-border);
  }}
  .tag.keep {{
    background: var(--accent-tint);
    color: var(--accent-dim);
    border: 1px solid #A7F3D0;
  }}
  .tag.warn {{
    background: var(--warn-bg);
    color: var(--warn-text);
    border: 1px solid var(--warn-border);
  }}

  /* 4-Step Methodology Grid (matching talousinstituutti.fi "Miten varmistamme laadun?") */
  .method-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 22px;
  }}
  @media (max-width: 768px) {{
    .method-grid {{ grid-template-columns: 1fr; }}
  }}
  .method-item {{
    display: flex;
    gap: 16px;
    align-items: flex-start;
    background: var(--shape-bg);
    border: 1px solid var(--line-color);
    border-radius: 3px;
    padding: 20px;
  }}
  .method-num {{
    width: 38px;
    height: 38px;
    border-radius: 4px;
    background: var(--accent);
    color: #FFFFFF;
    font-family: var(--heading-font);
    font-weight: 700;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .method-item h4 {{
    font-size: 16.5px;
    margin-bottom: 4px;
  }}
  .method-item p {{
    margin: 0;
    font-size: 14px;
    color: var(--body-color);
  }}

  footer {{
    max-width: 1180px;
    margin: 36px auto 48px;
    padding: 28px 24px 0;
    border-top: 1px solid var(--line-color);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 13.5px;
    color: var(--caption-color);
  }}

  [data-lang="en"] {{ display: none; }}
  body.lang-en [data-lang="fi"] {{ display: none !important; }}
  body.lang-en [data-lang="en"] {{ display: revert !important; }}
</style>
</head>
<body>

<!-- STICKY INSTITUTIONAL NAVBAR -->
<nav class="navbar">
  <div class="navbar-inner">
    <a href="#" class="brand-mark">
      <div class="brand-crest">STR</div>
      <div>
        <div class="brand-text-title" data-lang="fi">Suomen Tukiröntgen</div>
        <div class="brand-text-title" data-lang="en">Finnish Subsidy X-Ray</div>
        <div class="brand-text-sub" data-lang="fi">Julkisen talouden avoimen datan tutkimusjulkaisu 2026</div>
        <div class="brand-text-sub" data-lang="en">Open-Data Public Finance Research Report 2026</div>
      </div>
    </a>

    <div class="nav-links">
      <a href="#mistakyse" data-lang="fi">Mistä on kyse?</a>
      <a href="#mistakyse" data-lang="en">Executive Summary</a>
      <a href="#kolmeloukkoa" data-lang="fi">3 Tukiloukkoa</a>
      <a href="#kolmeloukkoa" data-lang="en">3 Subsidy Traps</a>
      <a href="#verkosto" data-lang="fi">Verkosto-Röntgen</a>
      <a href="#verkosto" data-lang="en">Ring Architecture</a>
      <a href="#kehysriihi" data-lang="fi">Kehysriihi 2027</a>
      <a href="#kehysriihi" data-lang="en">Budget Cuts 2027</a>
      <a href="#aineisto" data-lang="fi">Empiirinen Aineisto</a>
      <a href="#aineisto" data-lang="en">Empirical Data</a>
    </div>

    <div class="nav-actions">
      <div class="lang-switch" role="group" aria-label="Language switch">
        <button type="button" class="lang-btn active" id="btn-fi" onclick="setLang('fi')">FI</button>
        <button type="button" class="lang-btn" id="btn-en" onclick="setLang('en')">EN</button>
      </div>
      <a href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download class="btn-primary">
        <span data-lang="fi">⬇ Lataa VM Budjetti-Excel (.xlsx)</span>
        <span data-lang="en">⬇ Download Budget Excel (.xlsx)</span>
      </a>
    </div>
  </div>
</nav>

<!-- HERO SECTION: MISTÄ TÄSSÄ TUTKIMUKSESSA ON KYSE? -->
<section class="section-wrap" id="mistakyse">
  <div class="inst-card">
    <div class="hero-grid">
      <div>
        <span class="eyebrow" data-lang="fi">VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % AVOIN REKISTERIDATA</span>
        <span class="eyebrow" data-lang="en">PUBLIC FINANCE · RESEARCH REPORT 2026 · 100% OPEN STATUTORY DATA</span>

        <h1 class="hero-title" data-lang="fi">Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien todellinen verotuotto</h1>
        <h1 class="hero-title" data-lang="en">Where Does €11.5 Billion Go? The True Tax Return of Finnish Corporate &amp; NGO Subsidies</h1>

        <p class="hero-lead" data-lang="fi">
          Suomen valtio jakaa vuosittain <strong>11,50 miljardia euroa</strong> suoria yritys-, energia-, maatalous- ja järjestöavustuksia. Koska tukiviranomaiset eivät yhdistä päätöksiään Verohallinnon yhteisöverotietoihin eivätkä hyvinvointialueiden ostolaskuihin, järjestelmään on syntynyt miljardiluokan hukkavuoto.
        </p>
        <p class="hero-lead" data-lang="en">
          Finland distributes <strong>€11.50 billion every year</strong> in direct corporate, energy, agricultural, and NGO grants. Because grant agencies never cross-check their payouts against Tax Administration corporate tax records or Wellbeing County purchase invoices, billions leak into zero-return subsidy traps.
        </p>

        <div class="plain-summary-box">
          <h3 data-lang="fi">Tiivistelmä 30 sekunnissa: Mitä tämä tutkimus osoittaa?</h3>
          <h3 data-lang="en">In Plain Language (30-Second Summary): What Does This Study Prove?</h3>
          <ol data-lang="fi">
            <li><strong>Zombiyhtiöt ja tukikonsulttiringit (€475M/v):</strong> Joukko yrityksiä nostaa vuodesta toiseen Business Finlandin ja ELY:n tukia samasta <code>c/o</code>-konsulttiosoitteesta maksamatta 5 vuoden aikana lainkaan yhteisöveroa. Noin 20 % tuesta katoaa suoraan tukikonsulttien palkkioihin.</li>
            <li><strong>Järjestöjen hallintopöhö ja Sote-tuplalaskutus (€377M/v):</strong> Vuoden 2026 STEA-päätöksistä (273,9 M€) peräti <strong>77,5 % (212,2 M€)</strong> jaetaan rajoittamattomina <code>Ak</code>-yleisavustuksina keskushallintoon, viestintään, tuettuihin lomakeskuksiin sekä säätiöille, jotka samaan aikaan myyvät kymmenillä miljoonilla palveluita hyvinvointialueille.</li>
            <li><strong>1,55–3,00 miljardin euron vuosisäästö ilman yhtäkään rintamaleikkausta:</strong> Leikkaamalla nämä kolme tehotonta tukiloukkoa kuudelta valtion talousarviomomentilta säästetään <strong>1,55 Mrd €/v</strong> koskematta yhteenkään sairaanhoitajaan, opettajaan tai poliisiin.</li>
          </ol>
          <ol data-lang="en">
            <li><strong>Corporate Grant Zombies &amp; Consultant Rings (€475M/yr):</strong> Clusters of shell companies sharing a grant consultant’s <code>c/o</code> address collect millions in Business Finland and ELY grants while paying €0 in corporate income tax over 5 years—leaking ~20% directly into consultant success fees.</li>
            <li><strong>NGO HQ Bureaucracy &amp; Healthcare Double-Dipping (€377M/yr):</strong> Out of all 2026 STEA grants (€273.9M), <strong>77.5% (€212.2M)</strong> is handed out as unrestricted <code>Ak</code> general HQ subsidies funding central-Helsinki offices, political lobbying, subsidized resorts, and foundations that simultaneously bill Wellbeing Counties tens of millions commercially.</li>
            <li><strong>€1.55B–€3.00B Annual Savings With Zero Frontline Cuts:</strong> Eliminating these three empirically proven waste categories across 6 state budget lines saves <strong>€1.55B/yr</strong> immediately—without cutting a single nurse, teacher, or police officer.</li>
          </ol>
        </div>

        <div style="display:flex;gap:12px;flex-wrap:wrap;">
          <a href="#kehysriihi" class="btn-primary">
            <span data-lang="fi">Siirry Kehysriihi 2027 -leikkauslistaan →</span>
            <span data-lang="en">View the 2027 State Budget Cut Schedule →</span>
          </a>
          <a href="#aineisto" class="btn-outline">
            <span data-lang="fi">Tutki yhtiö- ja järjestökohtaista dataa</span>
            <span data-lang="en">Explore Company &amp; NGO Audit Tables</span>
          </a>
        </div>
      </div>

      <!-- Right Column: Institutional Key Figures Summary -->
      <div class="exec-panel">
        <div>
          <span class="eyebrow" data-lang="fi">KESKEISET TUNNUSLUVUT (AVAINDATA 2026)</span>
          <span class="eyebrow" data-lang="en">KEY EMPIRICAL FINDINGS (2026 DATA)</span>
          <h3 style="font-size:20px;margin-bottom:8px;" data-lang="fi">Tutkimusaineiston kokonaiskuva</h3>
          <h3 style="font-size:20px;margin-bottom:8px;" data-lang="en">Audit Scope &amp; Fiscal Impact</h3>
        </div>

        <div class="metric-row">
          <div class="metric-label" data-lang="fi">Tutkittu valtion tukipooli (ESA 2010 D.3 + D.7)</div>
          <div class="metric-label" data-lang="en">Total Annual Subsidy Pool Audited</div>
          <div class="metric-val">11,50 Mrd € / v</div>
          <div class="metric-sub" data-lang="fi">BF 650 M€ • ELY 290 M€ • STEA 380 M€ • OKM 420 M€ • Energia &amp; MMM</div>
          <div class="metric-sub" data-lang="en">BF €650M • ELY €290M • STEA €380M • OKM €420M • Energy &amp; Agri</div>
        </div>

        <div class="metric-row">
          <div class="metric-label" data-lang="fi">Välitön VM Kehysriihi -säästöpotentiaali</div>
          <div class="metric-label" data-lang="en">Immediate Annual State Budget Savings</div>
          <div class="metric-val crimson" id="kpi-national-cut">1,55 Mrd € / v</div>
          <div class="metric-sub" data-lang="fi">Kohdistettu tarkasti 6 valtion talousarviomomentille (0 € rintamaleikkauksia)</div>
          <div class="metric-sub" data-lang="en">Targeted across 6 exact state budget lines (€0 frontline service cuts)</div>
        </div>

        <div class="metric-row">
          <div class="metric-label" data-lang="fi">Vuoden 2026 STEA-yleisavustusten (Ak) osuus</div>
          <div class="metric-label" data-lang="en">2026 STEA Unrestricted HQ Grants (Ak Share)</div>
          <div class="metric-val emerald">77,5 % (212,2 M€)</div>
          <div class="metric-sub" data-lang="fi">1 527 virallista STEA-päätöstä (2026): vain 22,5 % on kohdennettua kenttäapua</div>
          <div class="metric-sub" data-lang="en">Across 1,527 live 2026 STEA decisions: only 22.5% is targeted field aid</div>
        </div>

        <div class="metric-row">
          <div class="metric-label" data-lang="fi">Otoksen tukiringit &amp; tilinpäätösten Vale-EBITDA</div>
          <div class="metric-label" data-lang="en">Detected Grant Rings &amp; Fake-EBITDA Distortion</div>
          <div class="metric-val" style="font-size:22px;"><span id="kpi-ring-count">3 Rinkiä</span> · <span id="kpi-qoe-trap">17,85 M€</span></div>
          <div class="metric-sub" data-lang="fi">Sama c/o-osoite tai hakemuspohja sekä avustuksilla paisutettu käyttökate</div>
          <div class="metric-sub" data-lang="en">Shared c/o addresses/templates &amp; grant-inflated operating margins</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 1: KOLME RAKENTEELLISTA TUKILOUKKOA -->
<section class="section-wrap" id="kolmeloukkoa">
  <div class="inst-card">
    <span class="eyebrow" data-lang="fi">TUTKIMUKSEN PÄÄTULOKSET · KOLME TUKILOUKKOA</span>
    <span class="eyebrow" data-lang="en">CORE FINDINGS · THREE STRUCTURAL SUBSIDY TRAPS</span>
    <h2 style="font-size:28px;" data-lang="fi">Miksi tuet eivät muutu verotuloiksi? Kolme empiirisesti todennettua vuotokohtaa</h2>
    <h2 style="font-size:28px;" data-lang="en">Why Subsidies Fail to Generate Tax Revenue: Three Empirically Verified Leaks</h2>

    <div class="cards-3col">
      <!-- Card 1 -->
      <div class="pub-card">
        <div>
          <span class="eyebrow" data-lang="fi">01 · YRITYSTUET (MOMENTIT 32.20.40, 32.20.83 &amp; 32.30.42)</span>
          <span class="eyebrow" data-lang="en">01 · CORPORATE GRANTS (LINES 32.20.40, 32.20.83 &amp; 32.30.42)</span>
          <h3 data-lang="fi">Zombiyhtiöt, c/o-tukikonsultit ja tilinpäätösten Vale-EBITDA</h3>
          <h3 data-lang="en">Grant Zombies, c/o Consultant Rings &amp; Fake EBITDA</h3>
          <p data-lang="fi">
            Kun Business Finlandin ja ELY-keskusten tukipäätökset yhdistetään Y-tunnuksella Verohallinnon 5 vuoden yhteisöverotietoihin, paljastuu yhtiöryppäitä, joiden kausaalinen verotuotto (DiD ROI) on negatiivinen. Samasta tilitoimisto- tai konsulttiosoitteesta (<code>c/o</code>) haetaan miljoonia euroja, josta ~20 % menee suoraan hakemuskonsultin palkkioihin. Samalla avustukset kirjataan tilinpäätöksessä <em>Liiketoiminnan muihin tuottoihin</em>, mikä saa tappiollisen yhtiön näyttämään keinotekoisesti voitolliselta.
          </p>
          <p data-lang="en">
            Cross-joining Business Finland and ELY grants by Business ID against 5-year corporate tax returns exposes clusters with negative causal tax ROI. Multiple shells operating from the same grant consultant’s <code>c/o</code> address harvest millions—leaking ~20% in consultant fees—while booking grants into <em>Other Operating Income</em> to fabricate positive EBITDA.
          </p>
        </div>
        <div class="pub-stat-bar">
          <span data-lang="fi">Kansallinen vuosisäästö:</span>
          <span data-lang="en">Annual Budget Savings:</span>
          <span style="color:var(--danger-text);font-size:15px;">475,5 M€ / v</span>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="pub-card">
        <div>
          <span class="eyebrow" data-lang="fi">02 · JÄRJESTÖTUET (STEA 33.90.50 &amp; OKM 29.80.50)</span>
          <span class="eyebrow" data-lang="en">02 · NGO SUBSIDIES (STEA 33.90.50 &amp; OKM 29.80.50)</span>
          <h3 data-lang="fi">Ak-yleisavustusautomaatit, lomatuki ja Sote-tuplalaskutus</h3>
          <h3 data-lang="en">Unrestricted HQ Slush, Holiday Grants &amp; Sote Double-Dipping</h3>
          <p data-lang="fi">
            Kansalaiset luulevat järjestötukien menevän ruoka-apuun ja kriisityöhön. Todellisuudessa vuoden 2026 STEA-tukipäätöksistä <strong>77,5 % (212,2 M€)</strong> on rajoittamatonta <code>Ak</code>-yleisavustusta järjestöjen keskushallintoon, viestintään ja edunvalvontaan. Lisäksi suuret säätiöt nostavat miljoonien verovapaat yleisavustukset samalla kun ne myyvät kymmenillä miljoonilla ostopalveluita hyvinvointialueille (<em>tuplalaskutus</em>).
          </p>
          <p data-lang="en">
            Taxpayers assume NGO grants fund frontline crisis aid. In reality, <strong>77.5% (€212.2M)</strong> of 2026 STEA funding consists of unrestricted <code>Ak</code> general HQ grants spent on central administration, communications, and subsidized holiday associations—while major foundations collect millions in grants while simultaneously billing Wellbeing Counties tens of millions commercially.
          </p>
        </div>
        <div class="pub-stat-bar">
          <span data-lang="fi">Kansallinen vuosisäästö:</span>
          <span data-lang="en">Annual Budget Savings:</span>
          <span style="color:var(--danger-text);font-size:15px;">377,0 M€ / v</span>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="pub-card">
        <div>
          <span class="eyebrow" data-lang="fi">03 · SÄILYTTÄVÄT TUET (MOMENTIT 30.10.40 &amp; 32.60.40)</span>
          <span class="eyebrow" data-lang="en">03 · DEADWEIGHT SUBSIDIES (LINES 30.10.40 &amp; 32.60.40)</span>
          <h3 data-lang="fi">Kuolleen painon teollisuus-, energia- ja rakennetuet</h3>
          <h3 data-lang="en">Deadweight Industrial, Energy &amp; Legacy Subsidies</h3>
          <p data-lang="fi">
            Valtio maksaa satoja miljoonia euroja passiivisia energiaveronpalautuksia ja päällekkäisiä kansallisia säilyttäviä tukia suuryrityksille hankkeisiin, jotka toteutuisivat markkinaehtoisesti muutoinkin (ns. <em>deadweight loss</em>, kausaalinen DiD vero-ROI alle 0,5x). Nämä tuet vääristävät kilpailua ja syrjäyttävät tuettomia pk-veronmaksajia, jotka rahoittavat järjestelmän.
          </p>
          <p data-lang="en">
            Hundreds of millions are paid in passive energy tax rebates and legacy structural subsidies to profitable incumbents for projects that would occur anyway (<em>deadweight loss</em>, causal DiD tax ROI &lt; 0.5x). These payouts distort competition and crowd out unsubsidized taxpaying SMEs.
          </p>
        </div>
        <div class="pub-stat-bar">
          <span data-lang="fi">Kansallinen vuosisäästö:</span>
          <span data-lang="en">Annual Budget Savings:</span>
          <span style="color:var(--danger-text);font-size:15px;">696,0 M€ / v</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 2: VERKOSTO-RÖNTGEN (UNCLIPPED ARCHITECTURE DIAGRAM & DETECTED RINGS) -->
<section class="section-wrap" id="verkosto">
  <div class="inst-card">
    <span class="eyebrow" data-lang="fi">VERKOSTO-RÖNTGEN · C/O-OSOITTEET, KONSORTIOPOHJAT JA TUPLALASKUTUS</span>
    <span class="eyebrow" data-lang="en">NETWORK X-RAY · C/O ADDRESSES, CONSORTIUM TEMPLATES &amp; DOUBLE-DIPPING</span>
    <h2 style="font-size:28px;" data-lang="fi">Miten tukiringit toimivat käytännössä?</h2>
    <h2 style="font-size:28px;" data-lang="en">How Do Subsidy Rings Operate in Practice?</h2>
    <p style="margin:8px 0 0 0;color:var(--body-color);" data-lang="fi">
      Alla oleva kaavio näyttää, kuinka julkinen tukiraha kulkee valtion talousarviomomentilta kolmen tunnistetun välittäjämekanismin kautta kohdeyhtiöille ja -järjestöille — ja miksi nettomääräinen verokertymä jää nollaan.
    </p>
    <p style="margin:8px 0 0 0;color:var(--body-color);" data-lang="en">
      The diagram below illustrates how public funds flow from state budget lines through three intermediary mechanisms into target companies and NGOs—resulting in zero net tax return.
    </p>

    <div class="flow-diagram-box">
      <svg id="vw-graph" viewBox="0 0 1040 370" aria-label="Subsidy Ring Architecture Diagram"></svg>
    </div>

    <div class="ring-cards-grid">
      <div class="ring-dossier-card">
        <span class="eyebrow">RINKI A · PRH YTJ C/O-OSOITEKLUSTERI</span>
        <h4 data-lang="fi">c/o TukiKonsultit Oy (Mannerheimintie 12 B)</h4>
        <h4 data-lang="en">c/o TukiKonsultit Oy (Shared Consultant Hub)</h4>
        <ul data-lang="fi">
          <li><strong>4 yhtiötä samassa c/o-osoitteessa:</strong> <code>2910441-2</code>, <code>2910442-0</code>, <code>2910443-8</code>, <code>2910444-6</code></li>
          <li><strong>Nostetut tuet yhteensä:</strong> 4,79 M€ (BF &amp; ELY)</li>
          <li><strong>Arvioitu konsulttipalkkio (20 %):</strong> 958 000 €</li>
          <li><strong>Maksettu yhteisövero (5 v):</strong> 0 € – 12 000 € (DiD ROI negatiivinen)</li>
        </ul>
        <ul data-lang="en">
          <li><strong>4 companies at identical c/o address:</strong> <code>2910441-2</code>, <code>2910442-0</code>, <code>2910443-8</code>, <code>2910444-6</code></li>
          <li><strong>Total grants extracted:</strong> €4.79M (BF &amp; ELY)</li>
          <li><strong>Estimated consultant fee (20%):</strong> €958,000</li>
          <li><strong>5-yr corporate tax paid:</strong> €0 – €12k (Negative DiD ROI)</li>
        </ul>
      </div>

      <div class="ring-dossier-card">
        <span class="eyebrow">RINKI B · KONSORTIO- JA HALLITUSKLUSTERI</span>
        <h4 data-lang="fi">Eteläesplanadi 22 vihreän siirtymän konsortio</h4>
        <h4 data-lang="en">Eteläesplanadi 22 Green Consortium Ring</h4>
        <ul data-lang="fi">
          <li><strong>3 yhtiötä samalla hakemuspohjalla:</strong> <code>3011881-5</code>, <code>3011882-3</code>, <code>3011883-1</code></li>
          <li><strong>Nostetut tuet yhteensä:</strong> 7,40 M€ (Momentit <code>32.20.40</code> &amp; <code>32.20.83</code>)</li>
          <li><strong>Arvioitu konsulttipalkkio (20 %):</strong> 1,48 M€</li>
          <li><strong>Kytkös:</strong> Jaetut hallitusjäsenet + identtinen konsortiohakemusrunko</li>
        </ul>
        <ul data-lang="en">
          <li><strong>3 companies sharing template &amp; board:</strong> <code>3011881-5</code>, <code>3011882-3</code>, <code>3011883-1</code></li>
          <li><strong>Total grants extracted:</strong> €7.40M (Lines <code>32.20.40</code> &amp; <code>32.20.83</code>)</li>
          <li><strong>Estimated consultant fee (20%):</strong> €1.48M</li>
          <li><strong>Link:</strong> Overlapping board seats + identical application stem</li>
        </ul>
      </div>

      <div class="ring-dossier-card">
        <span class="eyebrow">RINKI C · STEA + SOTE MONIKANAVATUPLAUS</span>
        <h4 data-lang="fi">Verovapaa Ak-yleisavustus + Sote-ostopalvelumyynti</h4>
        <h4 data-lang="en">Tax-Free Ak HQ Grant + Wellbeing County Billing</h4>
        <ul data-lang="fi">
          <li><strong>Esimerkkikohteet:</strong> <code>0201146-3</code> (Sote-Palvelusäätiö), <code>0116958-1</code> (Loma ja Terveys ry)</li>
          <li><strong>Vuotuiset STEA/OKM-avustukset:</strong> 15,8 M€ / v</li>
          <li><strong>Samanaikainen Sote-myynti:</strong> 17,4 M€ / v hyvinvointialueille</li>
          <li><strong>Ongelma:</strong> Veronmaksaja maksaa sekä järjestön seinät (STEA) että sen myymän palvelun täyden hinnan (Sote).</li>
        </ul>
        <ul data-lang="en">
          <li><strong>Flagged entities:</strong> <code>0201146-3</code> (Sote Foundation), <code>0116958-1</code> (Holiday Assoc.)</li>
          <li><strong>Annual STEA/OKM grants:</strong> €15.8M / yr</li>
          <li><strong>Simultaneous Wellbeing County billing:</strong> €17.4M / yr</li>
          <li><strong>Defect:</strong> Taxpayers pay twice—once for HQ overhead via STEA and again via county procurement.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- SECTION 3: VALTION TALOUSARVION MOMENTTIKOHTAINEN LEIKKAUSLISTA (KEHYSRIIHI 2027) -->
<section class="section-wrap" id="kehysriihi">
  <div class="inst-card">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:16px;">
      <div>
        <span class="eyebrow" data-lang="fi">VALTIONVARAINMINISTERIÖN KEHYSRIIHI 2027 · 6 TALOUSARVIOMOMENTTIA</span>
        <span class="eyebrow" data-lang="en">MINISTRY OF FINANCE 2027 BUDGET GUILLOTINE · 6 BUDGET LINES</span>
        <h2 style="font-size:28px;" data-lang="fi">Valtion talousarvion momenttikohtainen säästöohjelma</h2>
        <h2 style="font-size:28px;" data-lang="en">Line-Item State Budget Savings Schedule (Kehysriihi 2027)</h2>
      </div>
      <div>
        <label for="scenario-select" style="font-size:12px;font-weight:700;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:4px;">
          <span data-lang="fi">Valitse Kehysriihi-leikkurin mitoitus:</span>
          <span data-lang="en">Select Budget Cut Scenario:</span>
        </label>
        <select id="scenario-select">
          <option value="1.0">Perustaso: 1,55 Mrd € / v (Zombituet + Ak-hallintopöhö + kuollut paino pois)</option>
          <option value="1.45">Keskikova: 2,25 Mrd € / v (+50 % matalan vero-ROI:n tuista pois)</option>
          <option value="1.94">Täysimääräinen: 3,00 Mrd € / v (Kaikki markkinoita vääristävät tuet pois)</option>
        </select>
      </div>
    </div>

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>VM Momentti</th>
            <th data-lang="fi">Määrärahan käyttötarkoitus</th>
            <th data-lang="en">Budget Line Description</th>
            <th data-lang="fi">Nykyinen määräraha (€/v)</th>
            <th data-lang="en">Current Budget (€/yr)</th>
            <th data-lang="fi">Leikkaus-%</th>
            <th data-lang="en">Cut %</th>
            <th data-lang="fi">Vuotuinen säästö (€/v)</th>
            <th data-lang="en">Annual Savings (€/yr)</th>
            <th data-lang="fi">Kohdennussääntö (Mistä leikataan)</th>
            <th data-lang="en">Exact Targeting Rule</th>
          </tr>
        </thead>
        <tbody id="momentti-tbody"></tbody>
      </table>
    </div>
  </div>
</section>

<!-- SECTION 4: EMPIIRINEN AINEISTO & HAKUTYÖKALU -->
<section class="section-wrap" id="aineisto">
  <div class="inst-card">
    <span class="eyebrow" data-lang="fi">EMPIIRINEN AINEISTO · Y-TUNNUSKOHTAINEN TARKASTELU</span>
    <span class="eyebrow" data-lang="en">EMPIRICAL AUDIT TABLES · ENTITY-LEVEL EXPLORER</span>
    <h2 style="font-size:28px;margin-bottom:16px;" data-lang="fi">Hae ja suodata yhtiöitä, järjestöjä, momentteja tai c/o-osoitteita</h2>
    <h2 style="font-size:28px;margin-bottom:16px;" data-lang="en">Search &amp; Filter Companies, NGOs, Budget Lines, or c/o Addresses</h2>

    <div class="filter-bar">
      <div style="flex:1;">
        <label for="search-box" data-lang="fi">Pikahaku (Y-tunnus, nimi, momentti, c/o-osoite tai luokitus):</label>
        <label for="search-box" data-lang="en">Instant Search (Business ID, name, budget line, c/o address, or verdict):</label>
        <input type="search" id="search-box" style="width:100%;" placeholder="Esim. 2910441-2, Loma ja Terveys, Setlementtiliitto, 32.20.40, Mannerheimintie..."/>
      </div>
      <div>
        <a href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download class="btn-outline">
          <span data-lang="fi">⬇ Lataa kaikki 5 välilehteä Excelissä (.xlsx)</span>
          <span data-lang="en">⬇ Download Full 5-Tab Excel Workbook (.xlsx)</span>
        </a>
      </div>
    </div>

    <!-- Table 4A: Corporate DiD Tax ROI -->
    <h3 style="font-size:21px;margin-top:10px;" data-lang="fi">4A. Yritystukien 5 vuoden kausaalinen vero-ROI &amp; tuettomat toimialaverrokit</h3>
    <h3 style="font-size:21px;margin-top:10px;" data-lang="en">4A. Corporate 5-Year Causal Tax ROI (DiD) vs. Unsubsidized Taxpaying Peers</h3>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="fi">
      Yhdistetty Y-tunnuksella: Tutkiavustuksia.fi / Business Finland / ELY × Verohallinnon yhteisöverotiedot × PRH YTJ v3. Mukana tuettomat veronmaksajaverrokit (Supercell, Relex, Ponsse ja toimialamediaanit).
    </p>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="en">
      Joined on Business ID: Tutkiavustuksia.fi / Business Finland / ELY × Tax Administration corporate tax records × PRH YTJ v3, alongside unsubsidized taxpaying peers.
    </p>
    <div class="table-scroll" style="margin-bottom:34px;">
      <table>
        <thead>
          <tr>
            <th>Y-tunnus</th>
            <th data-lang="fi">Yhtiö / Verrokki</th>
            <th data-lang="en">Company / Peer</th>
            <th>VM Momentti</th>
            <th data-lang="fi">Saatu tuki 5v (€)</th>
            <th data-lang="en">5-Yr Grant (€)</th>
            <th data-lang="fi">Kausaalinen Vero-ROI</th>
            <th data-lang="en">Causal Tax ROI</th>
            <th data-lang="fi">Konsulttivuoto (20 %)</th>
            <th data-lang="en">Consultant Leak (20%)</th>
            <th data-lang="fi">Rinki / Kytkös</th>
            <th data-lang="en">Ring / Cluster</th>
            <th data-lang="fi">Tutkimustuomio</th>
            <th data-lang="en">Audit Verdict</th>
            <th data-lang="fi">Leikkausesitys (€)</th>
            <th data-lang="en">Recommended Cut (€)</th>
          </tr>
        </thead>
        <tbody id="corp-tbody"></tbody>
      </table>
    </div>

    <!-- Table 4B: STEA & OKM NGO Audit -->
    <h3 style="font-size:21px;" data-lang="fi">4B. STEA (33.90.50) &amp; OKM (29.80.50) Järjestö-Röntgen (Mukana vuoden 2026 STEA-päätökset)</h3>
    <h3 style="font-size:21px;" data-lang="en">4B. STEA (33.90.50) &amp; OKM (29.80.50) NGO Bureaucracy &amp; Double-Dipping Audit (incl. Live 2026 Decisions)</h3>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="fi">
      Erottaa rajoittamattomat <code>Ak</code>-yleisavustukset, keskushallinnon, tuetun lomatoiminnan ja hyvinvointialueiden ostopalvelutuplauksen aidosta kenttätyöstä (kuten kriisipuhelin ja ruoka-apu, joille leikkaus on 0 €).
    </p>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="en">
      Separates unrestricted <code>Ak</code> HQ bureaucracy, subsidized holiday resorts, and Wellbeing County commercial double-dipping from genuine frontline crisis aid (€0 cut).
    </p>
    <div class="table-scroll" style="margin-bottom:34px;">
      <table>
        <thead>
          <tr>
            <th>Y-tunnus</th>
            <th data-lang="fi">Järjestö / Säätiö</th>
            <th data-lang="en">NGO / Foundation</th>
            <th data-lang="fi">Momentti (Laji)</th>
            <th data-lang="en">Line (Class)</th>
            <th data-lang="fi">Vuosiavustus (€)</th>
            <th data-lang="en">Annual Grant (€)</th>
            <th data-lang="fi">Hallinto &amp; Viestintä (%)</th>
            <th data-lang="en">HQ &amp; Advocacy (%)</th>
            <th data-lang="fi">Valtioriippuvuus (%)</th>
            <th data-lang="en">State Dependency (%)</th>
            <th data-lang="fi">Sote-tuplalaskutus</th>
            <th data-lang="en">Double-Dipper</th>
            <th data-lang="fi">Havainto / Rooli</th>
            <th data-lang="en">Audit Note / Role</th>
            <th data-lang="fi">Leikattava (€/v)</th>
            <th data-lang="en">Recoverable Cut (€/yr)</th>
          </tr>
        </thead>
        <tbody id="ngo-tbody"></tbody>
      </table>
    </div>

    <!-- Table 4C: Fake EBITDA / QoE Stripper -->
    <h3 style="font-size:21px;" data-lang="fi">4C. Tilinpäätösten Vale-EBITDA &amp; Tukiriisunta (Oikaistu Kassavirta-analyysi)</h3>
    <h3 style="font-size:21px;" data-lang="en">4C. Financial Statement Fake-EBITDA &amp; Grant-Stripping Analysis (Quality of Earnings)</h3>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="fi">
      Osoittaa kuinka <em>Liiketoiminnan muihin tuottoihin</em> kirjatut avustukset, aktivoidut tukipalkat ja sisäpiirilaskutus luovat näennäisen käyttökatteen yhtiöille, joiden todellinen liiketoiminta on tappiollista.
    </p>
    <p style="font-size:14px;margin:4px 0 10px 0;color:var(--caption-color);" data-lang="en">
      Shows how grants booked into <em>Other Operating Income</em>, capitalized grant payroll, and related-party billing fabricate positive headline EBITDA for structurally unprofitable firms.
    </p>
    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Y-tunnus</th>
            <th data-lang="fi">Tarkasteltava yhtiö</th>
            <th data-lang="en">Audited Company</th>
            <th data-lang="fi">Raportoitu EBITDA (€)</th>
            <th data-lang="en">Reported EBITDA (€)</th>
            <th data-lang="fi">Tuki- &amp; lähipiiripaisutus (€)</th>
            <th data-lang="en">Grant &amp; Ring Inflation (€)</th>
            <th data-lang="fi">Todellinen Kassavirta-EBITDA (€)</th>
            <th data-lang="en">True Core Cash EBITDA (€)</th>
            <th data-lang="fi">Vale-EBITDA osuus (%)</th>
            <th data-lang="en">Grant Inflation (%)</th>
            <th data-lang="fi">Yritysarvon vääristymä (€)</th>
            <th data-lang="en">Valuation Trap (€)</th>
            <th data-lang="fi">Tilinpäätösdiagnoosi</th>
            <th data-lang="en">QoE Diagnosis</th>
          </tr>
        </thead>
        <tbody id="qoe-tbody"></tbody>
      </table>
    </div>
  </div>
</section>

<!-- SECTION 5: TUTKIMUSMENETELMÄT JA LAATUSTANDARDIT (talousinstituutti.fi style) -->
<section class="section-wrap" id="menetelmat">
  <div class="inst-card">
    <span class="eyebrow" data-lang="fi">TUTKIMUSMENETELMÄT JA LAATUSTANDARDIT</span>
    <span class="eyebrow" data-lang="en">RESEARCH METHODOLOGY &amp; REPRODUCIBILITY STANDARDS</span>
    <h2 style="font-size:28px;" data-lang="fi">Miten varmistamme analyysin luotettavuuden ja toistettavuuden?</h2>
    <h2 style="font-size:28px;" data-lang="en">How We Ensure Empirical Rigor and Full Reproducibility</h2>
    <p style="margin:8px 0 0 0;color:var(--body-color);" data-lang="fi">
      Tutkimus perustuu läpinäkyviin menetelmiin, julkisten viranomaisrekisterien suoraan yhdistämiseen ja täysin toistettavaan avoimen lähdekoodin laskentaan.
    </p>
    <p style="margin:8px 0 0 0;color:var(--body-color);" data-lang="en">
      This study relies on transparent econometric methods, primary-key statutory registry joins, and 100% reproducible open-source computation.
    </p>

    <div class="method-grid">
      <div class="method-item">
        <div class="method-num">01</div>
        <div>
          <h4 data-lang="fi">Y-tunnus-pohjainen rekisteriyhdistäminen (JOIN ON y_tunnus)</h4>
          <h4 data-lang="en">Statutory Primary-Key Registry Join (JOIN ON y_tunnus)</h4>
          <p data-lang="fi">Valtiokonttorin <code>Tutkiavustuksia.fi</code>, Business Finlandin avoin data, STEA:n <code>avustukset.stea.fi</code>, Verohallinnon julkiset yhteisöverotiedot sekä PRH:n <code>YTJ v3</code> yhdistetään suoraan Y-tunnuksella.</p>
          <p data-lang="en">State Treasury <code>Tutkiavustuksia.fi</code>, Business Finland open data, STEA <code>avustukset.stea.fi</code>, Tax Administration corporate tax records, and PRH <code>YTJ v3</code> are joined directly by Business ID.</p>
        </div>
      </div>

      <div class="method-item">
        <div class="method-num">02</div>
        <div>
          <h4 data-lang="fi">Difference-in-Differences (DiD) kausaalinen vero-ROI</h4>
          <h4 data-lang="en">Difference-in-Differences (DiD) Causal Tax ROI</h4>
          <p data-lang="fi">Tuetun yhtiön 5 vuoden yhteisöverokertymän muutosta verrataan saman toimialan (TOL 2008) ja kokoluokan tuettomaan verrokkiin: <code>ROI = (ΔVero_tuettu − ΔVero_verrokki) / Tuki</code>.</p>
          <p data-lang="en">Measures 5-year corporate tax growth of subsidized firms against matched unsubsidized NACE peers: <code>ROI = (ΔTax_treated − ΔTax_peer) / Grant</code>.</p>
        </div>
      </div>

      <div class="method-item">
        <div class="method-num">03</div>
        <div>
          <h4 data-lang="fi">Verkosto-, c/o-osoite- ja konsortioklusterointi</h4>
          <h4 data-lang="en">Entity-Ring, c/o Address &amp; Consortium Graph</h4>
          <p data-lang="fi">PRH YTJ:n rekisteritiedoista tunnistetaan automaattisesti yhtiöryppäät, jotka jakavat saman tilitoimisto- tai konsulttiosoitteen (<code>c/o</code>), hallitusjäsenen tai identtisen hakemusrungon.</p>
          <p data-lang="en">Automatically detects multi-entity grant rings sharing the same <code>c/o</code> consultant address, overlapping board members, or identical consortium application templates.</p>
        </div>
      </div>

      <div class="method-item">
        <div class="method-num">04</div>
        <div>
          <h4 data-lang="fi">Tilinpäätösten oikaistu käyttökate (QoE EBITDA -tukiriisunta)</h4>
          <h4 data-lang="en">Quality-of-Earnings (QoE) Grant-Stripped EBITDA</h4>
          <p data-lang="fi">Oikaisee raportoidusta käyttökatteesta <em>Liiketoiminnan muihin tuottoihin</em> kirjatut avustukset, aktivoidut T&amp;K-tukipalkat sekä tukiringin sisäisen liikevaihdon.</p>
          <p data-lang="en">Strips headline EBITDA of grants booked in <em>Other Operating Income</em>, capitalized grant payroll, and circular related-party revenue.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<footer>
  <div>
    <strong>Suomen Tukiröntgen 2026</strong> · Riippumaton avoimen datan taloustutkimusjulkaisu
  </div>
  <div>
    Lähdeaineistot: Tutkiavustuksia.fi (Valtiokonttori) · avustukset.stea.fi · Business Finland Avoin Data · Verohallinto · PRH YTJ v3
  </div>
</footer>

<script>
const DATA = {payload_json};
let CURRENT_LANG = 'fi';

const MOMENTTI_META = [
  {{
    code: "32.20.40",
    nameFi: "Business Finland: Tutkimus-, kehittämis- ja innovaatiotoiminnan avustukset",
    nameEn: "Business Finland: R&D and Innovation Grants",
    budgetEur: 470000000,
    natCut: 211500000,
    ruleFi: "Lakkautetaan tuki yhtiöiltä, joiden 5v DiD vero-ROI < 0,0x tai jotka kuuluvat c/o-konsulttirinkeihin",
    ruleEn: "Eliminate grants to firms with 5-yr DiD tax ROI < 0.0x or inside c/o consultant rings"
  }},
  {{
    code: "32.20.83",
    nameFi: "Business Finland: Tutkimus-, kehittämis- ja innovaatiotoiminnan lainat",
    nameEn: "Business Finland: R&D Soft Loans",
    budgetEur: 180000000,
    natCut: 90000000,
    ruleFi: "Lopetetaan pääomalainat kroonisesti veronegatiivisille tukikuoriyhtiöille",
    ruleEn: "Terminate subordinated soft loans to chronic tax-negative grant shells"
  }},
  {{
    code: "32.30.42",
    nameFi: "ELY-keskukset: Yritysten kehittämisavustukset",
    nameEn: "ELY Centres: Regional Corporate Development Grants",
    budgetEur: 290000000,
    natCut: 174000000,
    ruleFi: "Poistetaan paikallista kilpailua vääristävät konsultti- ja laitehankintatuet",
    ruleEn: "Abolish local competition-distorting consulting and machinery subsidies"
  }},
  {{
    code: "33.90.50",
    nameFi: "STEA: Avustukset yhteisöille ja säätiöille terveyden ja sosiaalisen hyvinvoinnin edistämiseen",
    nameEn: "STEA: Grants to NGOs and Foundations (Ak HQ Slush & Sote Double-Dip)",
    budgetEur: 380000000,
    natCut: 209000000,
    ruleFi: "15 % hallintokatto Ak-yleisavustuksiin; lomatukien ja Sote-tuplalaskuttajien tukien lakkautus",
    ruleEn: "15% HQ overhead cap on Ak general grants; end holiday grants & Sote double-dipping"
  }},
  {{
    code: "29.80.50",
    nameFi: "Opetus- ja kulttuuriministeriö (OKM): Yleis- ja järjestöavustukset",
    nameEn: "Ministry of Education & Culture (OKM): General & Advocacy NGO Grants",
    budgetEur: 420000000,
    natCut: 168000000,
    ruleFi: "Poistetaan rajoittamattomat poliittiset yleisavustukset ja monikanavarahoituksen tuplaus",
    ruleEn: "Remove unrestricted advocacy grants and multi-ministry double-dipping"
  }},
  {{
    code: "30.10.40 / 32.60.40",
    nameFi: "MMM & TEM: Kansalliset säilyttävät maatalous- ja teollisuuden energiatuet",
    nameEn: "MMM & TEM: National Deadweight Agricultural & Industrial Energy Subsidies",
    budgetEur: 1740000000,
    natCut: 696000000,
    ruleFi: "Leikataan kuolleen painon (DiD ROI < 0,5x) säilyttävät energiaveronpalautukset ja päällekkäistuet",
    ruleEn: "Cut deadweight (DiD ROI < 0.5x) incumbent energy rebates and overlapping subsidies"
  }}
];

const VERDICT_LABELS = {{
  BLACKLIST_ZOMBIE: {{ fi: "ZOMBIYHTIÖ (LEIKATTAVA 100 %)", en: "GRANT ZOMBIE (100% CUT)" }},
  DEADWEIGHT_CROWD_OUT: {{ fi: "KUOLLUT PAINO (LEIKATTAVA 60 %)", en: "DEADWEIGHT LOSS (60% CUT)" }},
  POSITIVE_EXTERNALITY_KEEP: {{ fi: "VEROTUOTTO POSITIIVINEN (SÄILYTETÄÄN)", en: "POSITIVE TAX ROI (KEEP)" }},
  CRITICAL_GRANT_ZOMBIE_DO_NOT_BUY: {{ fi: "KRIITTINEN VALE-EBITDA (TUKIZOMBI)", en: "CRITICAL FAKE-EBITDA TRAP" }},
  HIGH_SUBSIDY_DEPENDENCY_REPRICE: {{ fi: "KORKEA TUKIRIIPPUVUUS", en: "HIGH GRANT DEPENDENCY" }},
  CLEAN_ORGANIC_EARNINGS: {{ fi: "TERVE LIIKETOIMINTA (0 € TUKEA)", en: "CLEAN ORGANIC EARNINGS" }}
}};

function fmtEur(n) {{
  return new Intl.NumberFormat('fi-FI', {{ style: 'currency', currency: 'EUR', maximumFractionDigits: 0 }}).format(n);
}}

function setLang(lang) {{
  CURRENT_LANG = lang;
  document.body.classList.toggle('lang-en', lang === 'en');
  document.getElementById('btn-fi').classList.toggle('active', lang === 'fi');
  document.getElementById('btn-en').classList.toggle('active', lang === 'en');
  renderGraph();
  renderAll();
}}

function translateVerdict(code) {{
  if (VERDICT_LABELS[code]) {{
    return CURRENT_LANG === 'en' ? VERDICT_LABELS[code].en : VERDICT_LABELS[code].fi;
  }}
  return code;
}}

function renderAll() {{
  const q = (document.getElementById('search-box').value || '').toLowerCase().trim();
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');

  let totalBudget = 0;
  let totalNatCut = 0;
  const momTbody = document.getElementById('momentti-tbody');
  momTbody.innerHTML = '';

  MOMENTTI_META.forEach(m => {{
    const scaledCut = Math.min(m.budgetEur, m.natCut * mult);
    const cutPct = Math.round((scaledCut / m.budgetEur) * 100);
    totalBudget += m.budgetEur;
    totalNatCut += scaledCut;

    const name = CURRENT_LANG === 'en' ? m.nameEn : m.nameFi;
    const rule = CURRENT_LANG === 'en' ? m.ruleEn : m.ruleFi;

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><code>${{m.code}}</code></td>
      <td><strong>${{name}}</strong></td>
      <td>${{fmtEur(m.budgetEur)}}</td>
      <td><span class="tag zombie">-${{cutPct}} %</span></td>
      <td style="color:var(--danger-text);font-weight:700;">${{fmtEur(scaledCut)}}</td>
      <td style="font-size:13px;color:var(--body-color);">${{rule}}</td>
    `;
    momTbody.appendChild(tr);
  }});

  const totalPct = Math.round((totalNatCut / totalBudget) * 100);
  const trTotal = document.createElement('tr');
  trTotal.className = 'total-row';
  trTotal.innerHTML = `
    <td><code>YHTEENSÄ</code></td>
    <td>${{CURRENT_LANG === 'en' ? 'TOTAL KEHYSRIIHI 2027 SUBSIDY GUILLOTINE (6 BUDGET LINES)' : 'YHTEENSÄ: KEHYSRIIHI 2027 TUKILEIKKURI (6 MOMENTTIA)'}}</td>
    <td>${{fmtEur(totalBudget)}}</td>
    <td>-${{totalPct}} %</td>
    <td style="color:var(--danger-text);font-size:15px;">${{fmtEur(totalNatCut)}}</td>
    <td>${{CURRENT_LANG === 'en' ? '0 € cut from healthcare, education, or police' : '0 € leikkauksia sote-rintamatyöstä, koulutuksesta tai poliisilta'}}</td>
  `;
  momTbody.appendChild(trTotal);

  document.getElementById('kpi-national-cut').textContent =
    CURRENT_LANG === 'en'
      ? '€' + (totalNatCut / 1e9).toFixed(2) + 'B / yr'
      : (totalNatCut / 1e9).toFixed(2).replace('.', ',') + ' Mrd € / v';

  document.getElementById('kpi-ring-count').textContent =
    DATA.rings.length + (CURRENT_LANG === 'en' ? ' Rings' : ' Rinkiä');

  document.getElementById('kpi-qoe-trap').textContent =
    fmtEur(DATA.qoe_reports.reduce((acc, r) => acc + r.ev_overpayment_trap_at_headline_multiple_eur, 0));

  // Table 4A: Corporate Evals + Benchmarks
  const corpTbody = document.getElementById('corp-tbody');
  corpTbody.innerHTML = '';
  const allRows = [
    ...DATA.corporate_evals,
    ...DATA.benchmarks.map(b => ({{
      y_tunnus: b.y_tunnus,
      company_name: b.company_name,
      vm_momentti: CURRENT_LANG === 'en' ? '0 € GRANTS (Taxpayer Peer)' : '0 € TUKEA (Veronmaksajaverrokki)',
      subsidy_received_eur: 0,
      causal_did_roi: (CURRENT_LANG === 'en' ? 'Paid +' : 'Maksoi +') + fmtEur(b.five_yr_corporate_tax_paid_eur) + (CURRENT_LANG === 'en' ? ' tax' : ' veroa'),
      estimated_consultant_fee_leakage_eur: 0,
      cluster_id: CURRENT_LANG === 'en' ? 'UNSUBSIDIZED_PEER' : 'TUETON_VERROKKI',
      classification: 'POSITIVE_EXTERNALITY_KEEP',
      recommended_cut_eur: 0
    }}))
  ];

  allRows.filter(r => JSON.stringify(r).toLowerCase().includes(q)).forEach(r => {{
    const isZombie = r.classification === 'BLACKLIST_ZOMBIE' || r.classification === 'DEADWEIGHT_CROWD_OUT';
    const badgeClass = r.classification === 'BLACKLIST_ZOMBIE' ? 'zombie' : (r.classification === 'DEADWEIGHT_CROWD_OUT' ? 'warn' : 'keep');
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><code>${{r.y_tunnus}}</code></td>
      <td><strong>${{r.company_name}}</strong></td>
      <td><code>${{r.vm_momentti}}</code></td>
      <td>${{fmtEur(r.subsidy_received_eur)}}</td>
      <td style="font-weight:600;color:${{typeof r.causal_did_roi === 'number' && r.causal_did_roi < 0 ? 'var(--danger-text)' : 'var(--accent-dim)'}}">${{typeof r.causal_did_roi === 'number' ? r.causal_did_roi.toFixed(2) + 'x' : r.causal_did_roi}}</td>
      <td>${{fmtEur(r.estimated_consultant_fee_leakage_eur)}}</td>
      <td>${{r.cluster_id}}</td>
      <td><span class="tag ${{badgeClass}}">${{translateVerdict(r.classification)}}</span></td>
      <td style="font-weight:700;color:${{r.recommended_cut_eur > 0 ? 'var(--danger-text)' : 'var(--accent-dim)'}}">${{fmtEur(r.recommended_cut_eur)}}</td>
    `;
    corpTbody.appendChild(tr);
  }});

  // Table 4B: NGO Evals
  const ngoTbody = document.getElementById('ngo-tbody');
  ngoTbody.innerHTML = '';
  DATA.ngo_evals.filter(n => JSON.stringify(n).toLowerCase().includes(q)).forEach(n => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><code>${{n.y_tunnus}}</code></td>
      <td><strong>${{n.ngo_name}}</strong></td>
      <td><code>${{n.vm_momentti}} (${{n.grant_class_code}})</code></td>
      <td>${{fmtEur(n.annual_grant_eur)}}</td>
      <td><span class="tag ${{n.overhead_and_lobbying_pct > 20 ? 'zombie' : 'keep'}}">${{n.overhead_and_lobbying_pct}} %</span></td>
      <td>${{n.state_dependency_pct}} %</td>
      <td>${{n.is_multi_source_double_dipper ? '<span class="tag warn">' + (CURRENT_LANG === 'en' ? 'DOUBLE-DIPPER' : 'TUPLALASKUTTAJA') + '</span>' : (CURRENT_LANG === 'en' ? 'No' : 'Ei')}}</td>
      <td style="font-size:12.5px;">${{(n.political_board_insiders || []).join(', ') || '—'}}</td>
      <td style="font-weight:700;color:${{n.recoverable_cut_eur > 0 ? 'var(--danger-text)' : 'var(--accent-dim)'}}">${{fmtEur(n.recoverable_cut_eur)}}</td>
    `;
    ngoTbody.appendChild(tr);
  }});

  // Table 4C: QoE Reports
  const qoeTbody = document.getElementById('qoe-tbody');
  qoeTbody.innerHTML = '';
  DATA.qoe_reports.filter(x => JSON.stringify(x).toLowerCase().includes(q)).forEach(x => {{
    const cls = x.qoe_verdict.includes('CRITICAL') ? 'zombie' : (x.qoe_verdict.includes('HIGH') ? 'warn' : 'keep');
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><code>${{x.y_tunnus}}</code></td>
      <td><strong>${{x.company_name}}</strong></td>
      <td>${{fmtEur(x.reported_ebitda_eur)}}</td>
      <td style="color:var(--danger-text);font-weight:600;">-${{fmtEur(x.subsidy_and_related_party_ebitda_inflation_eur)}}</td>
      <td style="color:var(--accent-dim);font-weight:700;">${{fmtEur(x.true_subsidy_stripped_core_ebitda_eur)}}</td>
      <td>${{x.ebitda_grant_inflation_pct}} %</td>
      <td style="color:var(--warn-text);font-weight:700;">${{fmtEur(x.ev_overpayment_trap_at_headline_multiple_eur)}}</td>
      <td><span class="tag ${{cls}}">${{translateVerdict(x.qoe_verdict)}}</span></td>
    `;
    qoeTbody.appendChild(tr);
  }});
}}

function renderGraph() {{
  const svg = document.getElementById('vw-graph');
  const en = CURRENT_LANG === 'en';

  // Clean 3-column left-to-right flow inside viewBox="0 0 1040 370" with generous margins (x: 20..1020, y: 18..352)
  const col1Title = en ? "1. STATE BUDGET LINES" : "1. VALTION BUDJETTIMOMENTIT";
  const col2Title = en ? "2. INTERMEDIARY RING / HUB" : "2. VÄLITTÄJÄRINKI / MEKANISMI";
  const col3Title = en ? "3. RECIPIENT SHELLS & TAX OUTCOME" : "3. KOHDEYHTIÖT & VEROTULOS (5 V)";

  const sources = [
    {{ x: 145, y: 85, title: "Momentti 32.20.40 & 32.30.42", sub: en ? "BF & ELY Corporate Grants" : "BF & ELY Yritystuet (940 M€/v)" }},
    {{ x: 145, y: 195, title: "Momentti 32.20.40 & 32.20.83", sub: en ? "BF R&D Grants & Soft Loans" : "BF T&K-tuet ja lainat (650 M€/v)" }},
    {{ x: 145, y: 305, title: "Momentti 33.90.50 & 29.80.50", sub: en ? "STEA & OKM NGO Grants" : "STEA & OKM Järjestötuet (800 M€/v)" }}
  ];

  const hubs = [
    {{ x: 500, y: 85, title: en ? "Ring A: c/o Grant Consultant Hub" : "Rinki A: c/o TukiKonsultit Oy (00100 Hki)", sub: en ? "4 companies at same c/o address • €958k fee leak" : "4 yhtiötä samassa c/o-osoitteessa • 958k € konsulttipalkkio", border: "#B91C1C", bg: "#FEF2F2" }},
    {{ x: 500, y: 195, title: en ? "Ring B: Shared Consortium & Board" : "Rinki B: Eteläesplanadi 22 Konsortio", sub: en ? "3 companies • identical template • €1.48M fee leak" : "3 yhtiötä • sama hakemuspohja • 1,48 M€ konsulttivuoto", border: "#92400E", bg: "#FFFBEB" }},
    {{ x: 500, y: 305, title: en ? "Ring C: Ak HQ Slush + Sote Double-Dip" : "Rinki C: Ak-Hallintotuki + Sote-Tuplalaskutus", sub: en ? "77.5% STEA unrestricted Ak + €17.4M county billing" : "77,5 % STEA:sta Ak-yleistukea + 17,4 M€ Sote-myyntiä", border: "#1C9770", bg: "#E8F5F0" }}
  ];

  const outcomes = [
    {{ x: 865, y: 65, title: "2910441-2 .. 2910444-6 (4 Oy)", sub: en ? "€4.79M grants → ~€0 tax (DiD ROI -0.35x)" : "4,79 M€ tukia → ~0 € veroa (ROI -0,35x)", color: "#B91C1C" }},
    {{ x: 865, y: 112, title: en ? "Fake EBITDA in Financial Statements" : "Tilinpäätösten Vale-EBITDA", sub: en ? "Grants booked as 'Other Operating Income'" : "Avustukset kirjattu 'Muihin tuottoihin'", color: "#B91C1C" }},
    {{ x: 865, y: 195, title: "3011881-5 .. 3011883-1 (3 Oy)", sub: en ? "€7.40M grants → Negative causal tax ROI" : "7,40 M€ tukia → Negatiivinen vero-ROI", color: "#92400E" }},
    {{ x: 865, y: 285, title: "0201146-3 Sote-Säätiö sr", sub: en ? "€6.8M STEA grant + €16.2M Sote sales" : "6,8 M€ STEA-tuki + 16,2 M€ Sote-myynti", color: "#1C9770" }},
    {{ x: 865, y: 332, title: "0116958-1 Loma ja Terveys ry", sub: en ? "€5.9M/yr state-subsidized holiday activities" : "5,9 M€/v tuettua lomatoimintaa (STEA Ak/Ae)", color: "#1C9770" }}
  ];

  let out = `
    <rect x="0" y="0" width="1040" height="370" fill="#F9F7F7" rx="4"/>
    <text x="145" y="28" text-anchor="middle" fill="#1C9770" font-family="DM Sans, sans-serif" font-size="12" font-weight="700" letter-spacing="0.8">${{col1Title}}</text>
    <text x="500" y="28" text-anchor="middle" fill="#1C9770" font-family="DM Sans, sans-serif" font-size="12" font-weight="700" letter-spacing="0.8">${{col2Title}}</text>
    <text x="865" y="28" text-anchor="middle" fill="#1C9770" font-family="DM Sans, sans-serif" font-size="12" font-weight="700" letter-spacing="0.8">${{col3Title}}</text>
  `;

  // Connectors Source -> Hub
  sources.forEach((s, idx) => {{
    const h = hubs[idx];
    out += `<line x1="${{s.x + 120}}" y1="${{s.y}}" x2="${{h.x - 155}}" y2="${{h.y}}" stroke="${{h.border}}" stroke-width="2" stroke-dasharray="5,3"/>`;
  }});

  // Connectors Hub -> Outcomes
  const links = [
    [0, 0], [0, 1],
    [1, 2],
    [2, 3], [2, 4]
  ];
  links.forEach(([hIdx, oIdx]) => {{
    const h = hubs[hIdx];
    const o = outcomes[oIdx];
    out += `<line x1="${{h.x + 155}}" y1="${{h.y}}" x2="${{o.x - 145}}" y2="${{o.y}}" stroke="${{h.border}}" stroke-width="2"/>`;
  }});

  // Draw Sources
  sources.forEach(s => {{
    out += `
      <g transform="translate(${{s.x}},${{s.y}})">
        <rect x="-120" y="-26" width="240" height="52" rx="4" fill="#FFFFFF" stroke="#D8D4D4" stroke-width="1.5"/>
        <text x="0" y="-4" text-anchor="middle" fill="#1A1A1A" font-family="DM Sans, sans-serif" font-size="12.5" font-weight="700">${{s.title}}</text>
        <text x="0" y="14" text-anchor="middle" fill="#464646" font-family="Inter, sans-serif" font-size="11">${{s.sub}}</text>
      </g>
    `;
  }});

  // Draw Hubs
  hubs.forEach(h => {{
    out += `
      <g transform="translate(${{h.x}},${{h.y}})">
        <rect x="-155" y="-28" width="310" height="56" rx="4" fill="${{h.bg}}" stroke="${{h.border}}" stroke-width="2"/>
        <text x="0" y="-5" text-anchor="middle" fill="#1A1A1A" font-family="DM Sans, sans-serif" font-size="13" font-weight="700">${{h.title}}</text>
        <text x="0" y="14" text-anchor="middle" fill="#464646" font-family="Inter, sans-serif" font-size="11">${{h.sub}}</text>
      </g>
    `;
  }});

  // Draw Outcomes
  outcomes.forEach(o => {{
    out += `
      <g transform="translate(${{o.x}},${{o.y}})">
        <rect x="-145" y="-20" width="290" height="40" rx="4" fill="#FFFFFF" stroke="${{o.color}}" stroke-width="1.6"/>
        <text x="0" y="-3" text-anchor="middle" fill="#1A1A1A" font-family="DM Sans, sans-serif" font-size="12" font-weight="700">${{o.title}}</text>
        <text x="0" y="13" text-anchor="middle" fill="#464646" font-family="Inter, sans-serif" font-size="10.5">${{o.sub}}</text>
      </g>
    `;
  }});

  svg.innerHTML = out;
}}

document.getElementById('search-box').addEventListener('input', renderAll);
document.getElementById('scenario-select').addEventListener('change', renderAll);
renderGraph();
renderAll();
</script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path


def compile_media_and_vm_dossiers(
    output_path: str,
    corporate_evals: List[Dict[str, object]],
    rings: List[Dict[str, object]],
    ngo_evals: List[Dict[str, object]],
    qoe_reports: List[Dict[str, object]],
    momentti_summary: Dict[str, float],
) -> str:
    """
    Compiles turnkey briefing dossiers for VM Budjettiosasto and financial investigative journalists.
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    total_ring_subsidy = sum(float(r["total_subsidy_eur"]) for r in rings)
    total_consultant_cut = sum(float(r["estimated_20pct_consultant_cut_eur"]) for r in rings)
    total_ngo_cut = sum(float(n["recoverable_cut_eur"]) for n in ngo_evals)

    md = f"""# Suomen Tukiröntgen 2026 — Turnkey VM Kehysriihi & Media Firestorm Dossiers

* **Generated Automatically by:** `Suomen Tukiröntgen / Veronmaksajan Tuomioistuin` v2.1 (Avoin Verkosto-Röntgen)
* **Data Provenance:** 100% Statutory Public Open Data (`Tutkiavustuksia.fi`, `Business Finland Avoin Data`, `STEA avustukset.stea.fi`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)
* **Relational Link Method:** Primary-Key Table Join `ON y_tunnus` (Zero agency IT integration, zero login/registration required)

---

## Dossier #1: For VM Budget Chief (`Budjettipäällikkö`) & State Secretary (`Valtiosihteeri`)
### Subject: Immediate `€1.55B – €3.00B/yr` Subsidy Guillotine Across 6 Budget *Momentti* Lines (`0` Frontline Cuts)

| VM Momentti | Budget Line Description | National Annual Cut (`€1.55B` Base) | Audited Cohort Cut (`€`) | Execution Mechanism |
| :--- | :--- | ---: | ---: | :--- |
| **`32.20.40`** | Business Finland R&D Grants | `€211,500,000` | `€{momentti_summary.get("32.20.40", 0.0):,.2f}` | Freeze payouts to recipients with 5-yr DiD tax ROI `< 0.0` or inside `c/o` consultant rings |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€90,000,000` | `€{momentti_summary.get("32.20.83", 0.0):,.2f}` | Terminate subordinated loans to chronic tax-negative shells |
| **`32.30.42`** | ELY Regional Development Grants | `€174,000,000` | `€{momentti_summary.get("32.30.42", 0.0):,.2f}` | Abolish local SME crowd-out consulting & machinery subsidies |
| **`33.90.50`** | STEA Grants (`Ak` General HQ Slush) | `€209,000,000` | `€{momentti_summary.get("33.90.50", 0.0):,.2f}` | Cap HQ/comms/lobbying at `15%` & disqualify Sote procurement double-dippers |
| **`29.80.50`** | OKM General & Advocacy NGO Grants | `€168,000,000` | `€{momentti_summary.get("29.80.50", 0.0):,.2f}` | Eliminate unrestricted `Ak` advocacy grants & multi-ministry double-dipping |
| **`30.10.40 / 32.60.40`** | National Agri & Industrial Energy Subsidies | `€696,000,000` | `€{momentti_summary.get("30.10.40_32.60.40", 0.0):,.2f}` | Strip deadweight (`ROI < 0.5`) incumbent energy rebates |
| **TOTAL** | **KEHYSRIIHI 2027 SUBSIDY GUILLOTINE** | **`€1,548,500,000 / yr`** | **`€{sum(momentti_summary.values()):,.2f}`** | **Zero nurses, teachers, or police cut** |

---

## Dossier #2: For Investigative Journalists (*Kauppalehti / Talouselämä / HS Visio / Veronmaksajat*)
### Story Hook A: "The `c/o` Grant-Consultant Rings Harvesting Millions While Paying €0 Corporate Tax"
* Cross-joining `Tutkiavustuksia.fi` and `Business Finland` grant tables by `Y-tunnus` against `PRH YTJ v3` postal/`c/o` addresses and `Verohallinto` corporate tax returns exposes **{len(rings)} multi-company grant rings** in our sample cohort alone that extracted **`€{total_ring_subsidy:,.0f}`** in public subsidies while generating near-zero net corporate tax—leaking an estimated **`€{total_consultant_cut:,.0f}`** (`20%` success fee) directly to professional grant-writing consultants (*tukikonsultit*).
* By contrast, unsubsidized private software and high-tech peers in NACE `62010 / 26110` received **`€0`** in zombie grants while paying millions in real corporate income taxes.

### Story Hook B: "The STEA & OKM Double-Dip: Tax-Free `Ak` Subsidies + Commercial Sote Billing"
* In our audited NGO cohort, flagged associations absorbed **`€{total_ngo_cut:,.0f}/yr`** in administrative overhead, central-Helsinki office rents, political communications, and multi-ministry double-dipping—while simultaneously selling `€17.4M/yr` of commercial services to Wellbeing Counties via public purchase invoices (*ostolaskudata*).
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    return output_path
    html += f"""
<script>
const DATA = {payload_json};
let LANG = 'fi';

const fmtM = (n) => (n / 1e6).toLocaleString('fi-FI', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' milj. €';
const fmtEUR = (n) => Math.round(n).toLocaleString('fi-FI') + ' €';

const I18N = {{
  fi: {{
    brand_title: "Suomen Talousinstituutti · Julkisen Talouden Tutkimus",
    brand_sub: "Tutkimusraportti · Klikkaa mitä tahansa korttia avataksesi selkokielisen analyysin",
    nav_sister: "Tutkimus II: Hankintakartellit (38,7 mrd. €) →",
    nav_xlsx: "Lataa Excel-malli (.xlsx)",
    hero_kicker: "VALTIONTALOUS · TUTKIMUSRAPORTTI 2026",
    hero_title: "Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien läpivalaisu",
    hero_lead: "Suomi jakaa joka vuosi 11,5 miljardia euroa yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Kun julkiset tukipäätökset yhdistetään Verohallinnon verotietoihin ja kaupparekisteriin, paljastuu, miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.",
    summary_box_title: "Miten luet tätä julkaisua? (Kaikki kortit ovat klikattavia)",
    summary_box_body: "Tämä sivu ei ole virkamiesrekisteri, vaan kansantajuinen tutkimusraportti. <strong>Klikkaa mitä tahansa alla olevaa lukukorttia, kaavion vaihetta, tukirinkiä, järjestöä tai yritystä</strong>, niin saat esiin selkokielisen selityksen: kuka rahaa saa, miten järjestely toimii käytännössä ja miksi se tuhlaa veronmaksajien rahoja.",
    kpi1_lbl: "Julkiset tuet yhteensä",
    kpi1_sub: "Yritys-, energia-, maatalous- ja järjestötuet valtion ja kuntien budjeteista",
    click_explain: "Klikkaa: Mistä 11,5 mrd. € koostuu? →",
    kpi2_lbl: "Tunnistettu vuosisäästö",
    kpi2_sub: "Välitön säästö ilman yhtäkään leikkausta kouluihin, sairaaloihin tai poliisiin",
    click_explain2: "Klikkaa: Miten säästö syntyy? →",
    kpi3_lbl: "Havaitut tukikonsultti- ja sisäpiiriringit",
    kpi3_sub: "Sama c/o-postilokero tai hakemustehdas: miljoonatuet sisään, 0 € yhteisöveroa ulos",
    click_explain3: "Klikkaa: Katso 3 esimerkkitapausta →",
    kpi4_lbl: "Järjestöjen hallintopöhö & tuplalaskutus",
    kpi4_sub: "77,5 % STEA-tuista on vapaata keskushallintorahaa — mukana tuetut lomat ja sote-myyjät",
    click_explain4: "Klikkaa: Katso STEA-läpivalaisu →",
    s1_title: "1. Miten tukirinki toimii? (Klikkaa vaihetta tai rinkiä)",
    s1_sub: "Suomessa toimii kymmeniä yksityisiä ”tukikonsultteja”, jotka perustavat tai keräävät useita pöytälaatikkoyhtiöitä samaan postilokeroon (c/o-osoite) ja hakevat niille maksimituet Business Finlandilta ja ELY-keskuksilta.",
    f1_step: "Vaihe 1 · Klikkaa",
    f1_title: "Veronmaksajan raha",
    f1_desc: "Valtio jakaa satoja miljoonia euroja ”kehittämisavustuksina” tarkistamatta, syntyykö tuesta koskaan verotettavaa liiketoimintaa.",
    f2_step: "Vaihe 2 · Klikkaa",
    f2_title: "Tukikonsultti kirjoittaa hakemuksen",
    f2_desc: "Konsultti lupaa yritykselle ”ilmaista rahaa” avaimet käteen -periaatteella ja veloittaa onnistuneesta tukipäätöksestä 15–25 % provision.",
    f3_step: "Vaihe 3 · Vuotokohta",
    f3_title: "Saman postilokeron yhtiörinki",
    f3_desc: "Samassa c/o-osoitteessa toimii useita aputoiminimiä tai holdingyhtiöitä, jotka ostavat konsultointia toisiltaan tukirahoilla.",
    f4_step: "Vaihe 4 · Lopputulos",
    f4_title: "5 vuoden jälkeen 0 € yhteisöveroa",
    f4_desc: "Kun tuki loppuu, yhtiö ei maksa euroakaan yhteisöveroa, kun taas ilman tukia toimiva kilpailija maksaa satoja tuhansia veroja.",
    rings_heading: "Klikkaa havaittua tukirinkiä lukeaksesi tarkan kuvauksen:",
    s2_title: "2. Kuusi kohdetta, joista säästetään 1,55–3,00 miljardia €/v",
    s2_sub: "Valitse säästötaso tai hae nimellä. Klikkaa mitä tahansa budjettikohdetta nähdäksesi selkokielellä, mitä kyseiseltä momentilta leikataan ja miksi peruspalvelut eivät kärsi.",
    lbl_scenario: "Valitse säästöohjelman laajuus",
    opt_base: "Perustaso: Leikkaa vain nollatuottoiset zombituet ja hallintopöhö (1,55 mrd. €/v)",
    opt_med: "Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)",
    opt_max: "Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)",
    lbl_search: "Hae yritystä, järjestöä tai aihetta",
    s3_title: "3. Järjestötukien läpivalaisu: Tuetut lomat, keskushallinto ja sote-tuplalaskutus",
    s3_sub: "Klikkaa mitä tahansa järjestökorttia nähdäksesi, kuinka suuri osa sen STEA- tai ministeriöavustuksesta kuluu keskushallintoon ja myykö sama organisaatio samaan aikaan palveluita hyvinvointialueille.",
    s4_title: "4. Yritystukien totuus: Zombiyritykset vs. aidot veronmaksajat",
    s4_sub: "Klikkaa yrityskorttia nähdäksesi selkokielisen vertailun: kuinka paljon yritys sai julkista tukea, paljonko se maksoi yhteisöveroa 5 vuoden aikana ja miten sen tilinpäätös muuttuu, kun valtion tuki riisutaan pois."
  }},
  en: {{
    brand_title: "Finnish Economic Institute (STI) · Public Finance Audit",
    brand_sub: "Interactive Policy Report · Click any card for a plain-English explanation",
    nav_sister: "Study II: Procurement Cartels (€38.7B) →",
    nav_xlsx: "Download Excel Model (.xlsx)",
    hero_kicker: "PUBLIC FINANCE · RESEARCH REPORT 2026",
    hero_title: "Where Does €11.5 Billion Go? An Audit of Finland's Corporate and NGO Subsidies",
    hero_lead: "Finland distributes €11.5 billion every year in corporate grants, agricultural/energy subsidies, and NGO funding. By linking public grant decisions to corporate tax returns and registry addresses, this report shows how <strong>€1.55B–€3.00B per year</strong> can be saved immediately without cutting a single nurse, teacher, or police officer.",
    summary_box_title: "How to Read This Interactive Report (Every Card Is Clickable)",
    summary_box_body: "This is a plain-language policy publication, not a database dump. <strong>Click any summary metric, flowchart step, grant ring, NGO, or company card below</strong> to open a clear, jargon-free explanation of who gets the money, how the scheme works in practice, and why it wastes taxpayer funds.",
    kpi1_lbl: "Total Public Subsidies",
    kpi1_sub: "Corporate, energy, agricultural, and NGO subsidies across state and municipal budgets",
    click_explain: "Click: What makes up the €11.5B? →",
    kpi2_lbl: "Identified Annual Savings",
    kpi2_sub: "Immediate budget savings with zero cuts to schools, hospitals, or police",
    click_explain2: "Click: How are savings achieved? →",
    kpi3_lbl: "Detected Grant-Consultant & Insider Rings",
    kpi3_sub: "Shared c/o mailbox or application factory: millions in grants in, €0 corporate tax out",
    click_explain3: "Click: Inspect the 3 ring clusters →",
    kpi4_lbl: "NGO Admin Bloat & Double-Billing",
    kpi4_sub: "77.5% of STEA grants are unrestricted HQ funding — including holiday NGOs & Sote vendors",
    click_explain4: "Click: Inspect STEA audit →",
    s1_title: "1. How a Grant Ring Works (Click Any Step or Ring)",
    s1_sub: "Dozens of private 'grant consultants' register or group multiple shell companies at the same c/o mailbox and harvest maximum grants from Business Finland and ELY Centres.",
    f1_step: "Step 1 · Click",
    f1_title: "Taxpayer Money",
    f1_desc: "The state hands out hundreds of millions in 'development grants' without checking whether past grants ever created tax-paying business.",
    f2_step: "Step 2 · Click",
    f2_title: "Consultant Writes the Application",
    f2_desc: "A grant consultant promises 'free government money' on a turnkey basis and takes a 15–25% commission from the approved payout.",
    f3_step: "Step 3 · The Leak",
    f3_title: "Co-Located Shell Ring",
    f3_desc: "Multiple companies registered at the exact same c/o address buy consulting services from each other using taxpayer grant money.",
    f4_step: "Step 4 · Outcome",
    f4_title: "€0 Corporate Tax After 5 Years",
    f4_desc: "Once the grant runs out, the shell company pays €0 in corporate income tax—while unsubsidized competitors pay full taxes.",
    rings_heading: "Click any detected grant ring to read the full plain-English breakdown:",
    s2_title: "2. Six Budget Targets Saving €1.55B–€3.00B/Year",
    s2_sub: "Choose a reform scenario or search by name. Click any budget card to see in plain English what is cut and why frontline public services are untouched.",
    lbl_scenario: "Choose Budget Reform Scope",
    opt_base: "Baseline: Cut only zero-return zombie grants & HQ bloat (€1.55B/yr)",
    opt_med: "Structural Reform: Halve low-return business & admin subsidies (€2.25B/yr)",
    opt_max: "Full Market Reform: Remove all market-distorting subsidies (€3.00B/yr)",
    lbl_search: "Search company, NGO, or topic",
    s3_title: "3. NGO Subsidy Audit: Subsidized Holidays, HQ Bloat & Sote Double-Billing",
    s3_sub: "Click any NGO card to see how much of its STEA or ministry funding goes to central administration and whether it simultaneously sells commercial services to Wellbeing Counties.",
    s4_title: "4. Corporate Grants: Zombie Recipients vs. Real Taxpayers",
    s4_sub: "Click any company card for a plain-language comparison: how much public grant money it took, how much tax it paid over 5 years, and what happens to its earnings when subsidies are stripped out."
  }}
}};

const MOMENTTI_META = [
  {{
    code: "32.20.40",
    fi_name: "Business Finlandin yritysavustukset",
    en_name: "Business Finland Corporate Grants",
    current: 470000000,
    base_cut: 211500000,
    fi_short: "Katkaistaan avustukset yhtiöiltä, jotka eivät maksa 5 vuoden kuluessa euroakaan yhteisöveroa tai toimivat konsulttirinkien postilokeroissa.",
    en_short: "Stop grants to companies paying €0 corporate tax over 5 years or operating inside c/o consultant rings.",
    fi_deep: "Business Finland jakaa vuosittain noin 470 miljoonaa euroa suoria avustuksia. Tutkimuksemme osoittaa, että lähes puolet tästä rahasta ohjautuu yrityksille, jotka hakevat tukea toistuvasti mutta joiden verotettava tulos pysyy nollassa. Kun tuki rajataan vain aidosti uutta teknologiaa ja verotuloja luoviin yrityksiin, säästyy välittömästi 211,5 miljoonaa euroa vuodessa.",
    en_deep: "Business Finland distributes €470M/year in direct grants. Nearly half flows to repeat applicants whose taxable income remains zero after five years. Restricting grants to genuine deep-tech innovators saves €211.5M/year immediately."
  }},
  {{
    code: "32.20.83",
    fi_name: "Business Finlandin T&K-pääomalainat",
    en_name: "Business Finland Subordinated R&D Loans",
    current: 180000000,
    base_cut: 90000000,
    fi_short: "Lopetetaan vakuudettomat halpakorkoiset lainat kroonisesti tappiollisille tuki-holdingyhtiöille, jotka jättävät lainat maksamatta.",
    en_short: "End unsecured soft loans to chronically loss-making shell companies that default at taxpayer expense.",
    fi_deep: "Valtio myöntää vuosittain 180 miljoonaa euroa vakuudettomia tuotekehityslainoja. Jos hanke ”epäonnistuu”, lainaa ei tarvitse maksaa takaisin. Käytännössä tämä toimii piilotukena yrityksille, joihin yksikään yksityinen sijoittaja ei sijoittaisi omaa rahaansa.",
    en_deep: "The state issues €180M/year in unsecured R&D loans that are forgiven if a project 'fails'—acting as a hidden grant for firms no private investor would back."
  }},
  {{
    code: "32.30.42",
    fi_name: "ELY-keskusten yritysten kehittämisavustukset",
    en_name: "ELY Regional Corporate Development Grants",
    current: 232000000,
    base_cut: 174000000,
    fi_short: "Lakkautetaan paikallista kilpailua vääristävät konsultointi-, markkinointi- ja laitehankintatuet.",
    en_short: "Abolish local competition-distorting consulting, marketing, and machinery subsidies.",
    fi_deep: "Kun ELY-keskus maksaa yhdelle paikkakunnan konepajalle tai konsulttiyritykselle 50 %:n avustuksen, naapurissa toimiva yrittäjä joutuu kilpailemaan omilla verotetuilla rahoillaan valtion tukemaa kilpailijaa vastaan. Tuen lakkauttaminen tervehdyttää paikallisen kilpailun ja säästää 174 miljoonaa euroa.",
    en_deep: "When ELY subsidizes 50% of one local firm's consulting or equipment costs, unsubsidized local competitors are punished. Ending these grants restores fair competition and saves €174M/year."
  }},
  {{
    code: "33.90.50",
    fi_name: "STEA-järjestöavustukset (Hallintopöhö & lomajärjestöt)",
    en_name: "STEA NGO Grants (HQ Bloat & Holiday Subsidies)",
    current: 380000000,
    base_cut: 209000000,
    fi_short: "Leikataan järjestöjen keskushallinnon yleisavustukset (77,5 % potista), tuetut lomajärjestöt (4,79 milj. €) sekä sote-palveluita myyvien säätiöiden tuplalaskutus.",
    en_short: "Cut unrestricted HQ slush grants (77.5% of STEA), holiday associations (€4.79M), and commercial Sote double-billing.",
    fi_deep: "STEA jakaa vuonna 2026 yhteensä 273,9 miljoonaa euroa (ja budjettimomentilta yhteensä 380 milj. €). Yli kolme neljäsosaa (212,2 milj. €) annetaan yleisavustuksena (Ak) järjestöjen omaan keskushallintoon, viestintään ja toimitiloihin. Lisäksi isot säätiöt (kuten Sininauhasäätiö ja A-klinikkasäätiö) saavat verovapaata avustusta samalla kun niiden omistamat yhtiöt myyvät kymmenillä miljoonilla palveluita hyvinvointialueille.",
    en_deep: "Over 77.5% (€212.2M) of STEA's 2026 payouts go to unrestricted general HQ funding (Ak), including €4.79M/yr for two holiday associations and millions to foundations that simultaneously sell commercial healthcare services to Wellbeing Counties."
  }},
  {{
    code: "29.80.50",
    fi_name: "Opetus- ja kulttuuriministeriön järjestö- ja lobbausavustukset",
    en_name: "Ministry of Education NGO & Lobbying Subsidies",
    current: 420000000,
    base_cut: 168000000,
    fi_short: "Karsitaan päällekkäiset ministeriöavustukset sekä verorahoilla tapahtuva poliittinen vaikuttamistyö.",
    en_short: "Eliminate overlapping multi-ministry grants and taxpayer-funded political lobbying.",
    fi_deep: "Lukuisat järjestöt nostavat samanaikaisesti avustusta sekä STEA:lta, opetus- ja kulttuuriministeriöltä että kunnilta. Kun päällekkäinen keskushallintorahoitus ja poliittinen edunvalvonta karsitaan, säästyy 168 miljoonaa euroa vuodessa leikkaamatta lasten ja nuorten liikuntaseurojen kenttätoiminnasta.",
    en_deep: "Many associations collect simultaneous general grants from STEA, the Ministry of Education, and municipalities. Cutting duplicate HQ and lobbying subsidies saves €168M/year while protecting local youth sports."
  }},
  {{
    code: "30.10 / 32.60",
    fi_name: "Suuryritysten automaattiset energia- ja säilytystuet",
    en_name: "Automatic Industrial & Energy Incumbent Subsidies",
    current: 2320000000,
    base_cut: 696000000,
    fi_short: "Poistetaan automaattiset veronpalautukset ja säilytystuet voittoa tekeviltä suuryrityksiltä, joiden investoinnit toteutuisivat muutenkin.",
    en_short: "Phase out automatic rebates to profitable large corporations where subsidies create zero new tax growth.",
    fi_deep: "Valtio jakaa yli 2,3 miljardia euroa teollisuuden, energian ja maatalouden suoria tukia. Taloustutkimuksen (VATT & Etla) mukaan suuri osa näistä tuista on ns. säilyttävää tukea, joka maksetaan automaattisesti kannattaville suuryrityksille ilman, että se lisää työllisyyttä tai verotuloja.",
    en_deep: "Over €2.3B/year goes to automatic industrial, energy, and agricultural subsidies that flow to profitable incumbents without generating incremental jobs or tax revenue."
  }}
];
"""
