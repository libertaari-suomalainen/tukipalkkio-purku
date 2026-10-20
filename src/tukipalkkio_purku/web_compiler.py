"""
Compilers for:
  1. `dist/Veronmaksajan_Tuomioistuin_2026.html` (`dist/index.html`) — Suomen Talousinstituutti (STI) Editorial Research Report & Real-Data Explorer (686 STEA 2026 NGOs + Real Finnish Corporations)
  2. `dist/Media_ja_VM_Dossierit_2026.md` — Turnkey Investigative Journalist & VM Budget Department Dossiers
"""

import json
import os
from typing import Dict, List, Optional

from .ingest import load_full_stea_2026_registry


def compile_tuomioistuin_html(
    output_path: str,
    corporate_evals: List[Dict[str, object]],
    rings: List[Dict[str, object]],
    ngo_evals: List[Dict[str, object]],
    qoe_reports: List[Dict[str, object]],
    benchmarks: List[Dict[str, object]],
    momentti_summary: Dict[str, float],
    stea_full_registry: Optional[List[Dict[str, object]]] = None,
) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    stea_all = stea_full_registry if stea_full_registry is not None else load_full_stea_2026_registry()

    payload_json = json.dumps(
        {
            "corporate_evals": corporate_evals,
            "rings": rings,
            "ngo_evals": ngo_evals,
            "qoe_reports": qoe_reports,
            "benchmarks": benchmarks,
            "momentti_summary": momentti_summary,
            "stea_all": stea_all,
        },
        ensure_ascii=False,
    )

    html = f"""<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Suomen Talousinstituutti — Yritys- ja Järjestötukien Tutkimusraportti 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #FAF8F7;
    --surface: #FFFFFF;
    --stone: #F2EEEE;
    --stone-hover: #EAE3E3;
    --border: #E5E0DF;
    --border-strong: #D5CECC;
    --text: #18181B;
    --body: #3F3F46;
    --muted: #6B7280;
    --accent: #1C9770;
    --accent-dark: #027D56;
    --accent-soft: #E8F5F0;
    --red: #B91C1C;
    --red-soft: #FEF2F2;
    --red-border: #FECACA;
    --amber: #B45309;
    --amber-soft: #FFFBEB;
    --amber-border: #FDE68A;
    --shadow: 0 4px 16px -2px rgba(24, 24, 27, 0.06), 0 2px 6px -1px rgba(24, 24, 27, 0.04);
    --shadow-hover: 0 12px 28px -4px rgba(28, 151, 112, 0.14), 0 4px 10px -2px rgba(24, 24, 27, 0.06);
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }}
  body {{
    background: var(--bg);
    color: var(--body);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    line-height: 1.62;
    font-size: 16px;
  }}
  h1, h2, h3, h4 {{
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text);
    letter-spacing: -0.02em;
  }}
  .topbar {{
    position: sticky;
    top: 0;
    z-index: 90;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    padding: 10px 20px;
  }}
  .topbar-inner {{
    max-width: 1180px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: nowrap;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: var(--text);
    min-width: 0;
  }}
  .brand-mark {{
    width: 36px;
    height: 36px;
    border-radius: 6px;
    background: var(--accent);
    color: #fff;
    font-family: 'DM Sans', sans-serif;
    font-weight: 800;
    font-size: 13.5px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .brand-text {{
    min-width: 0;
  }}
  .brand-text strong {{
    display: block;
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 700;
    line-height: 1.2;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .brand-text span {{
    display: block;
    font-size: 11.5px;
    color: var(--muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 6px;
    flex-shrink: 0;
  }}
  .lang-btn {{
    background: var(--stone);
    border: 1px solid var(--border-strong);
    color: var(--text);
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    min-height: 36px;
    white-space: nowrap;
  }}
  .lang-btn.active {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }}
  .btn-primary {{
    background: var(--accent);
    color: #fff;
    text-decoration: none;
    padding: 7px 13px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    min-height: 36px;
    border: none;
    cursor: pointer;
    white-space: nowrap;
  }}
  .btn-primary:hover {{ background: var(--accent-dark); }}
  .btn-secondary {{
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border-strong);
    text-decoration: none;
    padding: 7px 12px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    min-height: 36px;
    cursor: pointer;
    white-space: nowrap;
  }}
  .btn-secondary:hover {{ background: var(--stone); }}
  .container {{
    max-width: 1180px;
    margin: 0 auto;
    padding: 28px 20px 80px;
  }}
  .hero-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 38px 40px;
    box-shadow: var(--shadow);
    margin-bottom: 28px;
  }}
  .kicker {{
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--accent-dark);
    background: var(--accent-soft);
    padding: 5px 12px;
    border-radius: 4px;
    margin-bottom: 16px;
  }}
  .hero-title {{
    font-size: clamp(26px, 4vw, 38px);
    line-height: 1.16;
    font-weight: 800;
    margin-bottom: 16px;
  }}
  .hero-lead {{
    font-size: clamp(16px, 2vw, 18px);
    color: var(--body);
    max-width: 900px;
    margin-bottom: 22px;
  }}
  .callout-stone {{
    background: var(--stone);
    border-left: 4px solid var(--accent);
    padding: 18px 22px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 24px;
  }}
  .callout-stone h3 {{ font-size: 16.5px; margin-bottom: 6px; }}
  .callout-stone p {{ font-size: 15px; color: var(--body); }}
  .clickable-card {{
    cursor: pointer;
    transition: transform 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease;
    position: relative;
  }}
  .clickable-card:hover {{
    transform: translateY(-3px);
    box-shadow: var(--shadow-hover);
    border-color: var(--accent);
  }}
  .click-hint {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    font-weight: 700;
    color: var(--accent-dark);
    margin-top: 12px;
  }}
  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
    margin-top: 10px;
  }}
  .kpi-card {{
    background: var(--bg);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .kpi-label {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--muted);
    margin-bottom: 6px;
  }}
  .kpi-val {{
    font-family: 'DM Sans', sans-serif;
    font-size: 25px;
    font-weight: 800;
    color: var(--text);
    line-height: 1.2;
    margin-bottom: 6px;
  }}
  .kpi-val.red {{ color: var(--red); }}
  .kpi-val.green {{ color: var(--accent-dark); }}
  .kpi-sub {{ font-size: 13.5px; color: var(--body); }}

  /* Sticky Search & Filter Hub */
  .search-hub {{
    background: var(--surface);
    border: 2px solid var(--accent);
    border-radius: 10px;
    padding: 22px 26px;
    box-shadow: var(--shadow);
    margin-bottom: 28px;
  }}
  .search-hub-grid {{
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 18px;
    align-items: end;
  }}
  .search-hub label {{
    display: block;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent-dark);
    margin-bottom: 6px;
  }}
  .input-box, .select-box {{
    width: 100%;
    min-height: 46px;
    padding: 10px 14px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--bg);
    color: var(--text);
    font-size: 15.5px;
    font-family: inherit;
  }}
  .input-box:focus, .select-box:focus {{
    outline: 2px solid var(--accent);
    background: #fff;
  }}
  .quick-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
    align-items: center;
  }}
  .chip-label {{
    font-size: 12.5px;
    font-weight: 600;
    color: var(--muted);
    margin-right: 4px;
  }}
  .chip {{
    background: var(--stone);
    border: 1px solid var(--border-strong);
    color: var(--text);
    padding: 5px 11px;
    border-radius: 99px;
    font-size: 12.5px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s;
  }}
  .chip:hover, .chip.active {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }}
  .search-status {{
    margin-top: 12px;
    padding: 10px 14px;
    background: var(--accent-soft);
    border-left: 4px solid var(--accent);
    border-radius: 4px;
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    display: none;
  }}

  .section-block {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 34px;
    box-shadow: var(--shadow);
    margin-bottom: 28px;
  }}
  .section-head {{
    margin-bottom: 22px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
  }}
  .section-head h2 {{ font-size: clamp(20px, 2.8vw, 26px); margin-bottom: 6px; }}
  .section-head p {{ font-size: 15.5px; color: var(--muted); max-width: 860px; }}
  .flow-steps {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 12px;
  }}
  .flow-step {{
    background: var(--stone);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 18px;
  }}
  .flow-step.danger {{ background: var(--red-soft); border-color: var(--red-border); }}
  .flow-badge {{
    display: inline-block;
    background: var(--accent);
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 9px;
    border-radius: 99px;
    margin-bottom: 8px;
  }}
  .flow-step.danger .flow-badge {{ background: var(--red); }}
  .flow-step h4 {{ font-size: 16px; margin-bottom: 6px; }}
  .flow-step p {{ font-size: 14px; color: var(--body); }}
  .cards-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 18px;
  }}
  .story-card {{
    background: var(--bg);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .story-card.red-accent {{ border-left: 4px solid var(--red); }}
  .story-card.amber-accent {{ border-left: 4px solid var(--amber); }}
  .story-card.green-accent {{ border-left: 4px solid var(--accent); }}
  .story-top {{ margin-bottom: 14px; }}
  .card-kicker-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 10px;
  }}
  .card-id-pill {{
    font-size: 11.5px;
    font-weight: 600;
    color: var(--muted);
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }}
  .story-card h3 {{
    font-size: 18px;
    line-height: 1.28;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 4px;
    word-break: normal;
  }}
  .story-subtitle {{
    font-size: 13px;
    font-weight: 600;
    color: var(--accent-dark);
    margin-bottom: 8px;
    line-height: 1.38;
  }}
  .story-meta {{ font-size: 12.5px; color: var(--muted); margin-bottom: 8px; line-height: 1.4; }}
  .story-commentary {{ font-size: 14px; color: var(--body); line-height: 1.52; margin-bottom: 4px; }}
  .metrics-strip {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
  }}
  .metrics-strip div {{
    min-width: 0;
  }}
  .metrics-strip div span {{
    display: block;
    font-size: 11px;
    color: var(--muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 2px;
  }}
  .metrics-strip div strong {{
    display: block;
    font-family: 'DM Sans', sans-serif;
    font-size: 14.5px;
    font-weight: 700;
    color: var(--text);
    white-space: nowrap;
  }}
  .badge {{
    display: inline-block;
    padding: 4px 10px;
    border-radius: 99px;
    font-size: 11.5px;
    font-weight: 700;
    white-space: nowrap;
  }}
  .badge-red {{ background: var(--red-soft); color: var(--red); border: 1px solid var(--red-border); }}
  .badge-amber {{ background: var(--amber-soft); color: var(--amber); border: 1px solid var(--amber-border); }}
  .badge-green {{ background: var(--accent-soft); color: var(--accent-dark); border: 1px solid #A7F3D0; }}

  .empty-box {{
    background: var(--stone);
    border: 1px dashed var(--border-strong);
    border-radius: 8px;
    padding: 16px 20px;
    font-size: 14px;
    color: var(--body);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    grid-column: 1 / -1;
  }}

  /* Full 686 STEA Registry Table */
  .stea-table-wrap {{
    margin-top: 26px;
    border-top: 1px solid var(--border);
    padding-top: 22px;
  }}
  .table-scroll {{
    overflow-x: auto;
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    background: var(--surface);
    max-height: 520px;
    overflow-y: auto;
    margin-top: 12px;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
  }}
  th, td {{
    text-align: left;
    padding: 11px 13px;
    border-bottom: 1px solid var(--border);
  }}
  th {{
    position: sticky;
    top: 0;
    background: var(--stone);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 12px;
    text-transform: uppercase;
    z-index: 2;
  }}
  tr.clickable-row {{ cursor: pointer; }}
  tr.clickable-row:hover td {{ background: var(--accent-soft); }}

  .modal-backdrop {{
    position: fixed;
    inset: 0;
    background: rgba(24, 24, 27, 0.55);
    backdrop-filter: blur(4px);
    z-index: 200;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .modal-backdrop.open {{ display: flex; }}
  .modal-card {{
    background: var(--surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    max-width: 740px;
    width: 100%;
    max-height: 88vh;
    overflow-y: auto;
    padding: 32px;
    box-shadow: 0 24px 48px rgba(0, 0, 0, 0.22);
    position: relative;
  }}
  .modal-close {{
    position: sticky;
    top: 0;
    float: right;
    background: var(--stone);
    border: 1px solid var(--border-strong);
    color: var(--text);
    border-radius: 99px;
    width: 38px;
    height: 38px;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .modal-card h2 {{ font-size: 23px; margin-bottom: 8px; padding-right: 44px; }}
  .modal-sub {{ font-size: 14px; color: var(--muted); margin-bottom: 20px; }}
  .modal-section {{
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 18px 20px;
    margin-bottom: 16px;
  }}
  .modal-section h4 {{
    font-size: 13.5px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent-dark);
    margin-bottom: 8px;
  }}
  .modal-section p, .modal-section li {{ font-size: 15px; color: var(--body); line-height: 1.6; }}
  .modal-section ul {{ padding-left: 20px; }}
  .modal-section li {{ margin-bottom: 6px; }}
  footer {{
    max-width: 1180px;
    margin: 0 auto;
    padding: 28px 20px 60px;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 14px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
  }}
  footer a {{ color: var(--accent-dark); font-weight: 600; text-decoration: none; }}
  @media (max-width: 960px) {{
    .topbar {{ position: relative; }}
    .topbar-inner {{ flex-wrap: wrap; }}
    .nav-actions {{ width: 100%; justify-content: flex-start; flex-wrap: wrap; }}
    .flow-steps, .search-hub-grid {{ grid-template-columns: minmax(0, 1fr); }}
    .hero-card, .section-block {{ padding: 22px 18px; }}
  }}
  @media (max-width: 640px) {{
    html, body {{ overflow-x: hidden; max-width: 100vw; width: 100%; }}
    .topbar {{ position: relative; padding: 10px 12px; max-width: 100vw; overflow: hidden; }}
    .brand-text strong {{ white-space: normal; font-size: 14px; line-height: 1.22; }}
    .brand-text span {{ display: none; }}
    .btn-primary, .btn-secondary, .lang-btn {{ white-space: normal; font-size: 12px; padding: 6px 10px; min-height: 34px; }}
    .container {{ padding: 14px 12px 56px; max-width: 100vw; overflow-x: hidden; }}
    .hero-card, .section-block, .search-hub {{ padding: 18px 14px; min-width: 0; max-width: 100%; overflow: hidden; }}
    .hero-title {{ font-size: 22px; line-height: 1.22; word-wrap: break-word; }}
    .kpi-grid, .cards-grid, .flow-steps, .search-hub-grid {{ grid-template-columns: minmax(0, 1fr); }}
    .story-card, .kpi-card, .search-hub-grid > div {{ min-width: 0; max-width: 100%; }}
    .input-box, .select-box {{ max-width: 100%; min-width: 0; font-size: 14px; }}
    .modal-backdrop {{ padding: 10px; align-items: flex-end; }}
    .modal-card {{ padding: 22px 18px; max-height: 92vh; border-radius: 12px 12px 0 0; }}
  }}
</style>
</head>
<body>
<header class="topbar">
  <div class="topbar-inner">
    <a href="#" class="brand">
      <div class="brand-mark">STI</div>
      <div class="brand-text">
        <strong data-i18n="brand_title">Suomen Talousinstituutti · Julkisen Talouden Tutkimus</strong>
        <span data-i18n="brand_sub">Tutkimusraportti 2026 · 686 STEA-järjestöä &amp; suomalaiset suuryritykset ja tukikohteet</span>
      </div>
    </a>
    <div class="nav-actions">
      <button class="lang-btn active" id="btn-fi" onclick="setLang('fi')">Suomi</button>
      <button class="lang-btn" id="btn-en" onclick="setLang('en')">English</button>
      <a class="btn-secondary" href="https://libertaari-suomalainen.github.io/kartelli-tutka/" data-i18n="nav_sister">Tutkimus II: Hankintakartellit (38,7 mrd. €) →</a>
      <a class="btn-primary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="nav_xlsx">⬇ Lataa Excel-aineisto (.xlsx)</a>
    </div>
  </div>
</header>

<main class="container">
  <!-- HERO SECTION -->
  <section class="hero-card">
    <div class="kicker" data-i18n="hero_kicker">VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % OIKEA VIRANOMAISDATA</div>
    <h1 class="hero-title" data-i18n="hero_title">Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien läpivalaisu</h1>
    <p class="hero-lead" data-i18n="hero_lead">
      Suomi jakaa joka vuosi 11,5 miljardia euroa yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Kun julkiset tukipäätökset (Business Finland, ELY, TEM, STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon verotietoihin ja PRH:n kaupparekisteriin, paljastuu miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.
    </p>
    <div class="callout-stone">
      <h3 data-i18n="summary_box_title">Mitä tämä tutkimus ja ladattava Excel (.xlsx) todistavat?</h3>
      <p data-i18n="summary_box_body">
        Tämä julkaisu sisältää <strong>kaikki 686 oikeaa STEA-järjestöä (1 527 virallista avustuspäätöstä vuodelle 2026 = 273,91 milj. €)</strong> sekä <strong>28 oikeaa suomalaista yritystukien saajaa ja veronmaksajaverrokkia</strong> (mm. <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Supercell, KONE, RELEX, Ponsse</em>). <strong>Klikkaa mitä tahansa korttia tai hae nimellä alla</strong> nähdäksesi tarkat luvut.
      </p>
    </div>
    <div class="kpi-grid">
      <div class="kpi-card clickable-card" onclick="openKpiModal('total_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi1_lbl">Julkiset tuet yhteensä</div>
          <div class="kpi-val">11,50 mrd. €/v</div>
          <div class="kpi-sub" data-i18n="kpi1_sub">Yritys-, energia-, maatalous- ja järjestötuet valtion ja kuntien budjeteista</div>
        </div>
        <div class="click-hint" data-i18n="click_explain">Klikkaa: Mistä 11,5 mrd. € koostuu? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('savings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi2_lbl">Tunnistettu vuosisäästö</div>
          <div class="kpi-val green" id="kpi-save-val">1,55 mrd. €/v</div>
          <div class="kpi-sub" data-i18n="kpi2_sub">Välitön säästö 6 budjettimomentilta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin</div>
        </div>
        <div class="click-hint" data-i18n="click_explain2">Klikkaa: Miten säästö syntyy? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('rings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi3_lbl">Tuki- ja konsortioklusterit</div>
          <div class="kpi-val red" id="kpi-ring-val">3 Klusteria · 118,7 M€</div>
          <div class="kpi-sub" data-i18n="kpi3_sub">Infinited Fiber (konkurssi 12,4 M€ tuen jälkeen), Spinnova, Solar Foods, P2X &amp; tukikonsultit</div>
        </div>
        <div class="click-hint" data-i18n="click_explain3">Klikkaa: Katso 3 oikeaa tukiklusteria →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('ngo_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi4_lbl">STEA 2026 Yleisavustukset (Ak)</div>
          <div class="kpi-val red">77,5 % (212,2 M€)</div>
          <div class="kpi-sub" data-i18n="kpi4_sub">686 järjestöä (273,9 M€): yli 3/4 menee vapaaseen keskushallintoon, lomiin ja sote-konserneille</div>
        </div>
        <div class="click-hint" data-i18n="click_explain4">Klikkaa: Katso STEA 2026 -todisteet →</div>
      </div>
    </div>
  </section>

  <!-- GLOBAL SEARCH & SCENARIO HUB -->
  <section class="search-hub" id="haku">
    <div class="search-hub-grid">
      <div>
        <label for="search-box" data-i18n="lbl_search">Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 28 suuryritystä &amp; tukikohdetta)</label>
        <input id="search-box" type="search" class="input-box" placeholder="Kokeile esim. Nokia, UPM, Spinnova, Infinited Fiber, Meyer, Viking Line, Punainen Risti, Loma, SOSTE, Supercell..." />
      </div>
      <div>
        <label for="scenario-select" data-i18n="lbl_scenario">Valitse Kehysriihi 2027 -säästöohjelman laajuus</label>
        <select id="scenario-select" class="select-box">
          <option value="1.0" data-i18n="opt_base">Perustaso: Leikkaa nollatuottoiset zombituet ja Ak-hallintopöhö (1,55 mrd. €/v)</option>
          <option value="1.45" data-i18n="opt_med">Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)</option>
          <option value="1.94" data-i18n="opt_max">Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)</option>
        </select>
      </div>
    </div>
    <div class="quick-chips">
      <span class="chip-label" data-i18n="chip_lbl">Pikavalinnat:</span>
      <button type="button" class="chip active" onclick="setSearch('')" data-i18n="chip_all">Näytä kaikki</button>
      <button type="button" class="chip" onclick="setSearch('Nokia')">Nokia</button>
      <button type="button" class="chip" onclick="setSearch('UPM')">UPM &amp; Stora Enso</button>
      <button type="button" class="chip" onclick="setSearch('Infinited Fiber')">Infinited Fiber (Konkurssi)</button>
      <button type="button" class="chip" onclick="setSearch('Spinnova')">Spinnova</button>
      <button type="button" class="chip" onclick="setSearch('Meyer Turku')">Meyer Turku</button>
      <button type="button" class="chip" onclick="setSearch('Viking Line')">Viking Line &amp; Tallink</button>
      <button type="button" class="chip" onclick="setSearch('Supercell')">Supercell &amp; KONE (0 € tukea)</button>
      <button type="button" class="chip" onclick="setSearch('Loma')">Tuetut lomat (STEA)</button>
      <button type="button" class="chip" onclick="setSearch('Sininauha')">Sininauha &amp; A-klinikka</button>
      <button type="button" class="chip" onclick="setSearch('SOSTE')">SOSTE &amp; EHYT</button>
    </div>
    <div class="search-status" id="search-status"></div>
  </section>

  <!-- SECTION 1: YRITYSTUET (28 REAL FINNISH CORPORATIONS & BENCHMARKS) -->
  <section class="section-block" id="sec-corps">
    <div class="section-head">
      <h2 data-i18n="s4_title">1. Yritystukien totuus: Tukikohteet, säilyttävät suuryritystuet ja aidot nettoveronmaksajat (28 yhtiötä)</h2>
      <p data-i18n="s4_sub">
        Klikkaa mitä tahansa yhtiökorttia nähdäksesi selkokielisen vertailun: kuinka paljon yhtiö sai julkista tukea (Business Finland, TEM, ELY, sähköistämistuki tai merenkulun tuki), paljonko sen yhteisövero muuttui 5 vuodessa ja miltä tulos näyttää ilman valtion tukia.
      </p>
    </div>
    <div class="cards-grid" id="corp-cards"></div>
  </section>

  <!-- SECTION 2: JÄRJESTÖTUET (TOP AUDITED + ALL 686 REAL 2026 STEA ORGANIZATIONS) -->
  <section class="section-block" id="sec-ngos">
    <div class="section-head">
      <h2 data-i18n="s3_title">2. Järjestötukien läpivalaisu: STEA 2026 kaikki 686 järjestöä (273,91 milj. €) ja OKM</h2>
      <p data-i18n="s3_sub">
        Vuoden 2026 virallisista STEA-avustuksista (273 912 000 €) tasan <strong>212 203 929 € (77,5 %)</strong> jaetaan rajoittamattomina <code>Ak</code>-yleisavustuksina järjestöjen keskushallintoon, viestintään ja lomatoimintaan. Klikkaa järjestökorttia tai selaa alla kaikkien 686 STEA-järjestön taulukkoa.
      </p>
    </div>
    <div class="cards-grid" id="ngo-cards"></div>

    <div class="stea-table-wrap">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
        <div>
          <h3 style="font-size:19px;" data-i18n="stea_tbl_title">Virallinen STEA 2026 -kokoaineisto: Kaikki 686 avustusta saavaa järjestöä (Klikkaa riviä)</h3>
          <p style="font-size:13.5px;color:var(--muted);" id="stea-count-sub"></p>
        </div>
        <a class="btn-secondary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="stea_xlsx_btn">⬇ Lataa kaikki 686 järjestöä Excelissä (Välilehti 06)</a>
      </div>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th data-i18n="th_org">Järjestö (STEA 2026 virallinen rekisteri)</th>
              <th data-i18n="th_tot">Myönnetty 2026 (€)</th>
              <th data-i18n="th_ak">Ak-Yleisavustus (€)</th>
              <th data-i18n="th_akpct">Ak-Osuus (%)</th>
              <th data-i18n="th_proj">Kohdennettu hanke/inv. (€)</th>
              <th data-i18n="th_purp">Suurin avustuskohde (2026)</th>
            </tr>
          </thead>
          <tbody id="stea-all-tbody"></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- SECTION 3: KUUSI BUDJETTIMOMENTTIA (KEHYSRIIHI 2027) -->
  <section class="section-block" id="sec-budget">
    <div class="section-head">
      <h2 data-i18n="s2_title">3. Kuusi valtion budjettimomenttia, joista säästetään 1,55–3,00 miljardia €/v</h2>
      <p data-i18n="s2_sub">
        Klikkaa mitä tahansa budjettimomenttia nähdäksesi selkokielellä, mitä kyseiseltä momentilta leikataan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.
      </p>
    </div>
    <div class="cards-grid" id="momentti-cards"></div>
  </section>

  <!-- SECTION 4: TUKIKONSORTIOT & MEKANISMI -->
  <section class="section-block" id="sec-rings">
    <div class="section-head">
      <h2 data-i18n="s1_title">4. Miten tukikonsortiot ja hakemuskoneistot toimivat? (3 oikeaa klusteria)</h2>
      <p data-i18n="s1_sub">
        Julkiset T&amp;K- ja investointituet keskittyvät samoihin osoite- ja ekosysteemiklusterihin (kuten Otaniemen Tekniikantie ja Keilasatama), joissa ammattimaiset tukikonsultit (esim. Spinverse Oy) koordinoivat kymmenien miljoonien hakemuskonsortioita.
      </p>
    </div>
    <div class="flow-steps">
      <div class="flow-step clickable-card" onclick="openFlowModal(1)">
        <span class="flow-badge" data-i18n="f1_step">Vaihe 1 · Klikkaa</span>
        <h4 data-i18n="f1_title">Veronmaksajan raha</h4>
        <p data-i18n="f1_desc">Valtio jakaa satoja miljoonia euroja kehittämis- ja investointiavustuksina tarkistamatta, syntyykö tuesta koskaan yhteisöveroa.</p>
      </div>
      <div class="flow-step clickable-card" onclick="openFlowModal(2)">
        <span class="flow-badge" data-i18n="f2_step">Vaihe 2 · Klikkaa</span>
        <h4 data-i18n="f2_title">Tukikonsultti rakentaa konsortion</h4>
        <p data-i18n="f2_desc">Erikoistunut konsulttiyhtiö kokoaa konsortiohakemuksen ja veloittaa projektin hallinnoinnista ja läpimenosta merkittävän palkkion.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(3)">
        <span class="flow-badge" data-i18n="f3_step">Vaihe 3 · Vuotokohta</span>
        <h4 data-i18n="f3_title">Avustukset kirjataan ”muihin tuottoihin”</h4>
        <p data-i18n="f3_desc">Tappiollinen pilottiyhtiö kirjaa avustukset liiketoiminnan muihin tuottoihin ja aktivoi tukipalkat taseeseen.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(4)">
        <span class="flow-badge" data-i18n="f4_step">Vaihe 4 · Lopputulos</span>
        <h4 data-i18n="f4_title">0 € yhteisöveroa tai konkurssi</h4>
        <p data-i18n="f4_desc">Kun tukiraha loppuu, yhtiö ei maksa euroakaan yhteisöveroa (esim. Infinited Fiberin konkurssi yli 12 M€ julkisten tukien jälkeen).</p>
      </div>
    </div>
    <h3 style="font-size:19px; margin: 22px 0 12px;" data-i18n="rings_heading">Klikkaa tunnistettua tukiklusteria lukeaksesi yhtiökohtaisen erittelyn:</h3>
    <div class="cards-grid" id="ring-cards"></div>
  </section>
</main>

<div class="modal-backdrop" id="detail-modal" onclick="if(event.target===this)closeModal()">
  <div class="modal-card">
    <button class="modal-close" onclick="closeModal()" aria-label="Sulje">✕</button>
    <div id="modal-content"></div>
  </div>
</div>

<footer>
  <div>
    <strong>Suomen Talousinstituutti · Avoin Tutkimusjulkaisu (2026)</strong><br/>
    Perustuu 100 % julkisiin viranomaisrekistereihin: STEA 2026 (kaikki 686 järjestöä), Tutkiavustuksia.fi, Business Finland, Verohallinto &amp; PRH YTJ v3.
  </div>
  <div>
    <a href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download>Lataa 6-välilehtinen Excel (.xlsx)</a> ·
    <a href="https://github.com/libertaari-suomalainen/tukipalkkio-purku">Avoin lähdekoodi (GitHub)</a> ·
    <a href="https://libertaari-suomalainen.github.io/kartelli-tutka/">Tutkimus II: Julkisten hankintojen ostokartellit (38,7 mrd. €)</a>
  </div>
</footer>
"""
    html += f"""
<script>
const DATA = {payload_json};
let LANG = 'fi';

const fmtM = (n) => (n / 1e6).toLocaleString('fi-FI', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' milj. €';
const fmtCardM = (n) => {{
  const val = Number(n);
  if (!val || Math.abs(val) < 1) return '0 €';
  const m = val / 1e6;
  const digits = Math.abs(m) >= 100 ? 0 : 1;
  return m.toLocaleString('fi-FI', {{minimumFractionDigits: digits, maximumFractionDigits: digits}}) + ' M€';
}};
const fmtEUR = (n) => Math.round(n).toLocaleString('fi-FI') + ' €';
const splitTitle = (raw) => {{
  const s = String(raw || '');
  const idx = s.indexOf(' (');
  if (idx === -1) return {{ main: s, sub: '' }};
  return {{
    main: s.slice(0, idx).trim(),
    sub: s.slice(idx + 2, s.endsWith(')') ? -1 : s.length).trim()
  }};
}};

const I18N = {{
  fi: {{
    brand_title: "Suomen Talousinstituutti · Julkisen Talouden Tutkimus",
    brand_sub: "Tutkimusraportti 2026 · 686 STEA-järjestöä & suomalaiset suuryritykset ja tukikohteet",
    nav_sister: "Tutkimus II: Hankintakartellit (38,7 mrd. €) →",
    nav_xlsx: "⬇ Lataa Excel-aineisto (.xlsx)",
    hero_kicker: "VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % OIKEA VIRANOMAISDATA",
    hero_title: "Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien läpivalaisu",
    hero_lead: "Suomi jakaa joka vuosi 11,5 miljardia euroa yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Kun julkiset tukipäätökset (Business Finland, ELY, TEM, STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon verotietoihin ja PRH:n kaupparekisteriin, paljastuu miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.",
    summary_box_title: "Mitä tämä tutkimus ja ladattava Excel (.xlsx) todistavat?",
    summary_box_body: "Tämä julkaisu sisältää <strong>kaikki 686 oikeaa STEA-järjestöä (1 527 virallista avustuspäätöstä vuodelle 2026 = 273,91 milj. €)</strong> sekä <strong>28 oikeaa suomalaista yritystukien saajaa ja veronmaksajaverrokkia</strong> (mm. <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Supercell, KONE, RELEX, Ponsse</em>). <strong>Klikkaa mitä tahansa korttia tai hae nimellä alla</strong> nähdäksesi tarkat luvut.",
    kpi1_lbl: "Julkiset tuet yhteensä",
    kpi1_sub: "Yritys-, energia-, maatalous- ja järjestötuet valtion ja kuntien budjeteista",
    click_explain: "Klikkaa: Mistä 11,5 mrd. € koostuu? →",
    kpi2_lbl: "Tunnistettu vuosisäästö",
    kpi2_sub: "Välitön säästö 6 budjettimomentilta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin",
    click_explain2: "Klikkaa: Miten säästö syntyy? →",
    kpi3_lbl: "Tuki- ja konsortioklusterit",
    kpi3_sub: "Infinited Fiber (konkurssi 12,4 M€ tuen jälkeen), Spinnova, Solar Foods, P2X & tukikonsultit",
    click_explain3: "Klikkaa: Katso 3 oikeaa tukiklusteria →",
    kpi4_lbl: "STEA 2026 Yleisavustukset (Ak)",
    kpi4_sub: "686 järjestöä (273,9 M€): yli 3/4 menee vapaaseen keskushallintoon, lomiin ja sote-konserneille",
    click_explain4: "Klikkaa: Katso STEA 2026 -todisteet →",
    lbl_search: "Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 28 suuryritystä & tukikohdetta)",
    lbl_scenario: "Valitse Kehysriihi 2027 -säästöohjelman laajuus",
    opt_base: "Perustaso: Leikkaa nollatuottoiset zombituet ja Ak-hallintopöhö (1,55 mrd. €/v)",
    opt_med: "Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)",
    opt_max: "Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)",
    chip_lbl: "Pikavalinnat:",
    chip_all: "Näytä kaikki",
    s4_title: "1. Yritystukien totuus: Tukikohteet, säilyttävät suuryritystuet ja aidot nettoveronmaksajat (28 yhtiötä)",
    s4_sub: "Klikkaa mitä tahansa yhtiökorttia nähdäksesi selkokielisen vertailun: kuinka paljon yhtiö sai julkista tukea (Business Finland, TEM, ELY, sähköistämistuki tai merenkulun tuki), paljonko sen yhteisövero muuttui 5 vuodessa ja miltä tulos näyttää ilman valtion tukia.",
    s3_title: "2. Järjestötukien läpivalaisu: STEA 2026 kaikki 686 järjestöä (273,91 milj. €) ja OKM",
    s3_sub: "Vuoden 2026 virallisista STEA-avustuksista (273 912 000 €) tasan <strong>212 203 929 € (77,5 %)</strong> jaetaan rajoittamattomina <code>Ak</code>-yleisavustuksina järjestöjen keskushallintoon, viestintään ja lomatoimintaan. Klikkaa järjestökorttia tai selaa alla kaikkien 686 STEA-järjestön taulukkoa.",
    stea_tbl_title: "Virallinen STEA 2026 -kokoaineisto: Kaikki 686 avustusta saavaa järjestöä (Klikkaa riviä)",
    stea_xlsx_btn: "⬇ Lataa kaikki 686 järjestöä Excelissä (Välilehti 06)",
    th_org: "Järjestö (STEA 2026 virallinen rekisteri)",
    th_tot: "Myönnetty 2026 (€)",
    th_ak: "Ak-Yleisavustus (€)",
    th_akpct: "Ak-Osuus (%)",
    th_proj: "Kohdennettu hanke/inv. (€)",
    th_purp: "Suurin avustuskohde (2026)",
    s2_title: "3. Kuusi valtion budjettimomenttia, joista säästetään 1,55–3,00 miljardia €/v",
    s2_sub: "Klikkaa mitä tahansa budjettimomenttia nähdäksesi selkokielellä, mitä kyseiseltä momentilta leikataan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.",
    s1_title: "4. Miten tukikonsortiot ja hakemuskoneistot toimivat? (3 oikeaa klusteria)",
    s1_sub: "Julkiset T&K- ja investointituet keskittyvät samoihin osoite- ja ekosysteemiklustereihin (kuten Otaniemen Tekniikantie ja Keilasatama), joissa ammattimaiset tukikonsultit (esim. Spinverse Oy) koordinoivat kymmenien miljoonien hakemuskonsortioita.",
    f1_step: "Vaihe 1 · Klikkaa",
    f1_title: "Veronmaksajan raha",
    f1_desc: "Valtio jakaa satoja miljoonia euroja kehittämis- ja investointiavustuksina tarkistamatta, syntyykö tuesta koskaan yhteisöveroa.",
    f2_step: "Vaihe 2 · Klikkaa",
    f2_title: "Tukikonsultti rakentaa konsortion",
    f2_desc: "Erikoistunut konsulttiyhtiö kokoaa konsortiohakemuksen ja veloittaa projektin hallinnoinnista ja läpimenosta merkittävän palkkion.",
    f3_step: "Vaihe 3 · Vuotokohta",
    f3_title: "Avustukset kirjataan ”muihin tuottoihin”",
    f3_desc: "Tappiollinen pilottiyhtiö kirjaa avustukset liiketoiminnan muihin tuottoihin ja aktivoi tukipalkat taseeseen.",
    f4_step: "Vaihe 4 · Lopputulos",
    f4_title: "0 € yhteisöveroa tai konkurssi",
    f4_desc: "Kun tukiraha loppuu, yhtiö ei maksa euroakaan yhteisöveroa (esim. Infinited Fiberin konkurssi yli 12 M€ julkisten tukien jälkeen).",
    rings_heading: "Klikkaa tunnistettua tukiklusteria lukeaksesi yhtiökohtaisen erittelyn:"
  }},
  en: {{
    brand_title: "Finnish Economic Institute (STI) · Public Finance Audit",
    brand_sub: "2026 Empirical Report · All 686 STEA NGOs & Real Finnish Corporate Grant Recipients",
    nav_sister: "Study II: Procurement Cartels (€38.7B) →",
    nav_xlsx: "⬇ Download Full Excel Dataset (.xlsx)",
    hero_kicker: "PUBLIC FINANCE · RESEARCH REPORT 2026 · 100% REAL STATUTORY DATA",
    hero_title: "Where Does €11.5 Billion Go? An Empirical Audit of Finland's Corporate & NGO Subsidies",
    hero_lead: "Finland distributes €11.5 billion every year in corporate grants, agricultural/energy subsidies, and NGO funding. By linking official grant decisions (Business Finland, ELY, TEM, and all 686 STEA 2026 NGOs) to Tax Administration corporate tax records and PRH registry addresses, this study proves how <strong>€1.55B–€3.00B/year</strong> can be saved without cutting a single nurse, teacher, or police officer.",
    summary_box_title: "What Does This Report & Excel Workbook (.xlsx) Prove?",
    summary_box_body: "This dataset contains <strong>all 686 real 2026 STEA grant-receiving NGOs (1,527 official decisions = €273.91M)</strong> plus <strong>28 real Finnish corporate grant recipients and unsubsidized taxpaying benchmarks</strong> (including <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Supercell, KONE, RELEX, Ponsse</em>). <strong>Click any card or search below</strong> to inspect the exact figures.",
    kpi1_lbl: "Total Public Subsidies",
    kpi1_sub: "Corporate, energy, agricultural, and NGO subsidies across state and municipal budgets",
    click_explain: "Click: What makes up the €11.5B? →",
    kpi2_lbl: "Identified Annual Savings",
    kpi2_sub: "Immediate savings across 6 budget lines with zero cuts to schools, hospitals, or police",
    click_explain2: "Click: How are savings achieved? →",
    kpi3_lbl: "Grant & Consortium Clusters",
    kpi3_sub: "Infinited Fiber (bankrupt after €12.4M grants), Spinnova, Solar Foods, P2X & grant consultants",
    click_explain3: "Click: Inspect the 3 real grant clusters →",
    kpi4_lbl: "STEA 2026 Unrestricted HQ Grants (Ak)",
    kpi4_sub: "Across all 686 NGOs (€273.9M): 77.5% goes to unrestricted HQ funding, holidays & Sote groups",
    click_explain4: "Click: Inspect STEA 2026 proof →",
    lbl_search: "Search any company, NGO, Business ID, or topic (686 NGOs + 28 major corporations & grant targets)",
    lbl_scenario: "Choose 2027 Budget Reform Scope",
    opt_base: "Baseline: Cut zero-return zombie grants & Ak HQ bloat (€1.55B/yr)",
    opt_med: "Structural Reform: Halve low-return business & admin subsidies (€2.25B/yr)",
    opt_max: "Full Market Reform: Remove all market-distorting subsidies (€3.00B/yr)",
    chip_lbl: "Quick filters:",
    chip_all: "Show all",
    s4_title: "1. Corporate Subsidies: Grant Zombies, Incumbent Rebates & Real Net Taxpayers (28 Corporations)",
    s4_sub: "Click any company card for a plain-English comparison: how much public subsidy it received, how its 5-year corporate income tax changed, and what its earnings look like without subsidies.",
    s3_title: "2. NGO Subsidy Audit: All 686 Real 2026 STEA Organizations (€273.91M) & Ministry Grants",
    s3_sub: "Out of all official 2026 STEA grants (€273,912,000), exactly <strong>€212,203,929 (77.5%)</strong> is handed out as unrestricted <code>Ak</code> general HQ subsidies. Click any card or browse all 686 NGOs in the table below.",
    stea_tbl_title: "Official 2026 STEA Full Registry: All 686 Funded Organizations (Click Any Row)",
    stea_xlsx_btn: "⬇ Download All 686 NGOs in Excel (Tab 06)",
    th_org: "Organization (Official 2026 STEA Registry)",
    th_tot: "Granted 2026 (€)",
    th_ak: "Ak General Grant (€)",
    th_akpct: "Ak Share (%)",
    th_proj: "Targeted Project/Inv. (€)",
    th_purp: "Primary Grant Purpose (2026)",
    s2_title: "3. Six State Budget Lines Saving €1.55B–€3.00B/Year",
    s2_sub: "Click any budget card to see in plain English what is cut from that budget line, which real companies or NGOs are affected, and why frontline services are untouched.",
    s1_title: "4. How Grant Consortia and Application Factories Work (3 Real Clusters)",
    s1_sub: "Public R&D and investment subsidies concentrate into recurring address and ecosystem hubs (such as Tekniikantie and Keilasatama in Espoo), where grant consultants coordinate multi-million euro consortia.",
    f1_step: "Step 1 · Click",
    f1_title: "Taxpayer Money",
    f1_desc: "The state hands out hundreds of millions in R&D and investment grants without checking if past grants ever generated corporate tax.",
    f2_step: "Step 2 · Click",
    f2_title: "Grant Consultant Builds Consortium",
    f2_desc: "Specialized grant consultants package multi-company applications and charge substantial coordination and success fees.",
    f3_step: "Step 3 · The Leak",
    f3_title: "Grants Booked as 'Other Income'",
    f3_desc: "Loss-making pilot ventures book public grants into Other Operating Income and capitalize grant payroll onto their balance sheets.",
    f4_step: "Step 4 · Outcome",
    f4_title: "€0 Corporate Tax or Bankruptcy",
    f4_desc: "When subsidies run out, the venture pays €0 corporate tax (e.g. Infinited Fiber's 2024 bankruptcy after €12.4M+ in public grants).",
    rings_heading: "Click any detected grant cluster to inspect the companies and figures:"
  }}
}};

const MOMENTTI_META = [
  {{
    code: "32.20.40",
    fi_name: "Business Finlandin T&K- ja yritysavustukset",
    en_name: "Business Finland Corporate R&D Grants",
    current: 470000000,
    base_cut: 211500000,
    fi_short: "Rajataan avustukset vain aidon vienti- ja verotuoton teknologiaan (kuten Nokia, Kempower, ICEYE). Katkaistaan tuki 0 € veroa maksavilta tukikohteilta (kuten Infinited Fiber 12,4 M€, Solar Foods 18,2 M€, Spinnova 14,8 M€, Meyer Turku 54 M€).",
    en_short: "Restrict grants to genuine tax-generating deep-tech (Nokia, Kempower, ICEYE); stop grants to €0-tax recipients (Infinited Fiber €12.4M, Solar Foods €18.2M, Spinnova €14.8M, Meyer Turku €54M).",
    fi_deep: "Business Finland jakaa vuosittain noin 470 miljoonaa euroa suoria avustuksia. Aineistomme osoittaa jyrkän kahtiajaon: aidot vientiyhtiöt (kuten Nokia Oyj >1,1 mrd. € yhteisöveroa, Kempower Oyj ja ICEYE Oy) muuttavat T&K-panokset nopeasti verotuloiksi, kun taas kymmeniä miljoonia nostaneet bio- ja kiertotalouspilotit (Infinited Fiber Company Oy 12,4 M€ -> konkurssi, Spinnova Oyj 14,8 M€ -> 0 € veroa, Solar Foods Oyj 18,2 M€ -> 0 € veroa) eivät ole maksaneet euroakaan yhteisöveroa.",
    en_deep: "Business Finland distributes €470M/year in direct grants. While genuine deep-tech exporters (Nokia, Kempower, ICEYE) generate massive corporate taxes, dozens of millions flow into chronically loss-making pilot ventures (Infinited Fiber €12.4M -> bankrupt, Spinnova €14.8M -> €0 tax, Solar Foods €18.2M -> €0 tax)."
  }},
  {{
    code: "32.20.83",
    fi_name: "Business Finlandin T&K-pääomalainat",
    en_name: "Business Finland Subordinated R&D Soft Loans",
    current: 180000000,
    base_cut: 90000000,
    fi_short: "Lopetetaan vakuudettomat, anteeksiannettavat tuotekehityslainat kroonisesti tappiollisille pilottiyhtiöille.",
    en_short: "End unsecured, forgivable R&D soft loans to chronically loss-making pilot ventures.",
    fi_deep: "Valtio myöntää vuosittain 180 miljoonaa euroa vakuudettomia tuotekehityslainoja. Kun tuettu pilottiyhtiö (kuten Infinited Fiber Company Oy) ajautuu konkurssiin tai hanke epäonnistuu, laina jää veronmaksajien luottotappioksi.",
    en_deep: "The state issues €180M/year in unsecured R&D loans that are written off by taxpayers when grant-dependent ventures fail or enter bankruptcy."
  }},
  {{
    code: "32.30.42",
    fi_name: "ELY-yritystuet sekä varustamoiden kuljetus- ja miehistötuet",
    en_name: "ELY Regional Grants & Maritime Crew Subsidies",
    current: 290000000,
    base_cut: 174000000,
    fi_short: "Leikataan varustamoiden automaattiset miehistötuet (Viking Line 115 M€/5v, Tallink Silja 98 M€/5v) sekä kilpailua vääristävät ELY-kehittämisavustukset (Betolar 6,9 M€).",
    en_short: "Cut automatic maritime crew subsidies (Viking Line €115M/5yr, Tallink Silja €98M/5yr) and local market-distorting ELY grants (Betolar €6.9M).",
    fi_deep: "Valtio maksaa vuodesta toiseen kymmeniä miljoonia euroja suoraa tukea itämeren matkustajavarustamoille (Viking Line Abp ja Tallink Silja Oy) sekä paikallisia ELY-kehittämisavustuksia, jotka vääristävät kilpailua tuettomia suomalaisia yrityksiä vastaan.",
    en_deep: "Tens of millions flow automatically every year to Baltic passenger ferries (Viking Line Abp, Tallink Silja Oy) and regional ELY consulting/capex grants that distort local competition."
  }},
  {{
    code: "33.90.50",
    fi_name: "STEA-järjestöavustukset (212,2 M€ Ak-hallintopöhö & lomajärjestöt)",
    en_name: "STEA NGO Grants (€212.2M Ak HQ Bloat & Holiday Subsidies)",
    current: 380000000,
    base_cut: 209000000,
    fi_short: "Todistettu STEA:n vuoden 2026 kaikista 686 järjestöstä: 273,91 M€ potista tasan 212,20 M€ (77,5 %) on vapaata Ak-yleisavustusta. Leikataan hallintopöhö, tuetut lomat (Loma ja Terveys 2,68 M€, Hyvinvointilomat 2,10 M€) ja sote-tuplalaskutus.",
    en_short: "Proven across all 686 STEA 2026 NGOs: €212.20M (77.5% of €273.91M) is unrestricted Ak HQ funding. Cut HQ bloat, holiday associations (€4.79M/yr), and commercial Sote double-billing.",
    fi_deep: "Olemme ajaneet tähän julkaisuun STEA:n koko vuoden 2026 virallisen avustusrekisterin (kaikki 686 järjestöä ja 1 527 päätöstä = 273 912 000 €). Luvut todistavat kiistattomasti, että 212 203 929 € (77,5 %) jaetaan rajoittamattomina Ak-yleisavustuksina järjestöjen keskushallintoon, viestintään, kattojärjestöille (SOSTE ry 2,81 M€, EHYT ry 4,13 M€), lomajärjestöille (Loma ja Terveys ry 2,68 M€, Hyvinvointilomat ry 2,10 M€) sekä sote-konserneille (A-klinikkasäätiö 2,87 M€, Sininauhasäätiö 2,60 M€).",
    en_deep: "Our full audit of all 686 STEA 2026 organizations (1,527 decisions = €273,912,000) proves that €212,203,929 (77.5%) goes to unrestricted Ak general subsidies—funding umbrella lobbying (SOSTE €2.81M, EHYT €4.13M), holiday associations (€4.79M), and commercial Sote service groups."
  }},
  {{
    code: "29.80.50",
    fi_name: "Opetus- ja kulttuuriministeriön katto- ja lobbausavustukset",
    en_name: "Ministry of Education Umbrella & Lobbying NGO Grants",
    current: 420000000,
    base_cut: 168000000,
    fi_short: "Poistetaan katto- ja edunvalvontajärjestöjen (kuten Allianssi ry 1,95 M€/v) yleisavustukset ja monikanavarahoituksen tuplaus. Suojataan paikallinen lasten ja nuorten seuratoiminta.",
    en_short: "Eliminate umbrella lobbying grants (e.g. Allianssi ry €1.95M/yr) and multi-ministry double-dipping while protecting local youth clubs.",
    fi_deep: "Useat valtakunnalliset kattojärjestöt nostavat samanaikaisesti avustusta OKM:ltä, STEA:lta ja kunnilta. Kun keskushallinnon ja poliittisen vaikuttamistyön yleisavustukset karsitaan, säästyy 168 miljoonaa euroa vuodessa koskematta paikallisiin urheiluseuroihin.",
    en_deep: "Cutting duplicate central-office and political advocacy subsidies across OKM saves €168M/year without touching local youth sports clubs."
  }},
  {{
    code: "30.10.40 / 32.60.40",
    fi_name: "Suurteollisuuden sähköistämistuki, energiaveronpalautukset ja säilytystuet",
    en_name: "Large Industrial Electrification, Energy & Incumbent Subsidies",
    current: 1740000000,
    base_cut: 696000000,
    fi_short: "Leikataan kannattavien suuryritysten (UPM-Kymmene 142 M€, Stora Enso 96 M€, Neste 68,5 M€, Outokumpu 62 M€, SSAB 48 M€, Metsä Fibre 44 M€, Fortum 34 M€) kuolleen painon säilytystuet.",
    en_short: "Cut deadweight incumbent energy and electrification subsidies to profitable large corporations (UPM €142M, Stora Enso €96M, Neste €68.5M, Outokumpu €62M, SSAB €48M).",
    fi_deep: "VATT:n ja Etlan tutkimusten mukaisesti suurteollisuuden sähköistämistuki ja energiaveronpalautukset ohjautuvat suuryrityksille hankkeisiin ja tehtaisiin, jotka toimisivat markkinaehtoisesti muutoinkin. Kun nämä kuolleen painon säilytystuet karsitaan, säästyy 696 miljoonaa euroa vuodessa.",
    en_deep: "Economic research (VATT & Etla) consistently shows that automatic industrial energy and electrification subsidies go to large incumbents with near-zero incremental tax or employment impact. Phasing them out saves €696M/year."
  }}
];

function openModalHtml(title, subtitle, sectionsHtml) {{
  document.getElementById('modal-content').innerHTML = `
    <h2>${{title}}</h2>
    <div class="modal-sub">${{subtitle}}</div>
    ${{sectionsHtml}}
  `;
  document.getElementById('detail-modal').classList.add('open');
}}

function closeModal() {{
  document.getElementById('detail-modal').classList.remove('open');
}}
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeModal(); }});

function openKpiModal(key) {{
  const fi = LANG === 'fi';
  if (key === 'total_pool') {{
    openModalHtml(
      fi ? "Mistä Suomen 11,50 miljardin euron vuotuinen tukipotti koostuu?" : "What Makes Up Finland's €11.50 Billion Annual Subsidy Pool?",
      fi ? "Tilastokeskus & Valtion talousarvio 2026 · Julkisyhteisöjen maksamat tuet ja avustukset" : "Statistics Finland & State Budget 2026 · Total Public Subsidies and Grants",
      `<div class="modal-section">
        <h4>${{fi ? "Kokonaiskuva selkokielellä" : "Overview in Plain English"}}</h4>
        <p>${{fi
          ? "Suomen julkinen sektori jakaa joka vuosi 11,5 miljardia euroa suoria yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Rahaa jakavat kymmenet eri virastot (Business Finland, ELY-keskukset, Traficom, STEA, OKM, MMM ja TEM) tarkistamatta Verohallinnon rekisteristä, syntyykö tuesta koskaan verotuloja."
          : "Finland's public sector distributes €11.5 billion every year across corporate grants, energy/agricultural subsidies, and NGO payouts without cross-checking Tax Administration records."}}</p>
      </div>
      <div class="modal-section">
        <h4>${{fi ? "Pääerät valtion ja julkisyhteisöjen budjeteissa" : "Major Components of the €11.5B Pool"}}</h4>
        <ul>
          <li><strong>${{fi ? "Suorat yritystuet, T&K-avustukset, merenkulkutuet ja ELY:" : "Direct Corporate, R&D, Maritime & ELY Grants:"}}</strong> ~1,8 mrd. €/v</li>
          <li><strong>${{fi ? "Järjestö- ja säätiöavustukset (STEA 380 M€, OKM 420 M€, kunnat):" : "NGO & Foundation Grants (STEA, OKM, Municipalities):"}}</strong> ~2,2 mrd. €/v</li>
          <li><strong>${{fi ? "Teollisuuden, energian ja maatalouden kansalliset tuet:" : "Industrial, Energy & Agricultural Subsidies:"}}</strong> ~4,5 mrd. €/v</li>
          <li><strong>${{fi ? "Toimialakohtaiset verotuet ja palautukset:" : "Sectoral Tax Rebates & Exemptions:"}}</strong> ~3,0 mrd. €/v</li>
        </ul>
      </div>`
    );
  }} else if (key === 'savings_pool') {{
    openModalHtml(
      fi ? "Miten 1,55–3,00 miljardia euroa säästetään ilman leikkauksia peruspalveluihin?" : "How €1.55B–€3.00B Is Saved Without Touching Frontline Services",
      fi ? "Suomen Talousinstituutin kehysriihimalli 2027 (6 valtion budjettimomenttia)" : "STI 2027 State Budget Reform Schedule (6 Budget Lines)",
      `<div class="modal-section">
        <h4>${{fi ? "Tarkka säästöerittely (Perustaso 1,55 mrd. €/v)" : "Exact Savings Breakdown (Baseline €1.55B/yr)"}}</h4>
        <ul>
          <li><strong>Momentti 32.20.40 (Business Finland avustukset):</strong> -211,50 milj. €/v</li>
          <li><strong>Momentti 32.20.83 (Business Finland T&amp;K-lainat):</strong> -90,00 milj. €/v</li>
          <li><strong>Momentti 32.30.42 (ELY-yritystuet &amp; kuljetustuet):</strong> -174,00 milj. €/v</li>
          <li><strong>Momentti 33.90.50 (STEA Ak-yleisavustukset &amp; lomajärjestöt):</strong> -209,00 milj. €/v</li>
          <li><strong>Momentti 29.80.50 (OKM katto- ja lobbausavustukset):</strong> -168,00 milj. €/v</li>
          <li><strong>Momentit 30.10.40 / 32.60.40 (Suurteollisuuden säilytys- ja energiatuet):</strong> -696,00 milj. €/v</li>
        </ul>
      </div>`
    );
  }} else if (key === 'rings_pool') {{
    const listHtml = DATA.rings.map(r => `<li><strong>${{r.shared_address_or_agent}} (${{r.ring_signature}}):</strong> ${{r.entity_count}} ${{fi ? "yhtiötä" : "companies"}} (${{r.company_names.join(' · ')}}) — ${{fi ? "nostettu julkinen tuki" : "public grants"}} <strong>${{fmtM(r.total_subsidy_eur)}}</strong>, ${{fi ? "5v yhteisöveron muutos" : "5-yr corporate tax delta"}} <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong>.</li>`).join('');
    openModalHtml(
      fi ? "Kolme oikeaa tuki- ja konsortioklusteria (118,7 milj. € tukia)" : "Three Real Grant & Consortium Clusters (€118.7M in Grants)",
      fi ? "PRH YTJ -osoitteiden, Business Finland Veturi-konsortioiden ja verotietojen yhdistelmä" : "Cross-Join of PRH Registry Addresses, Consortium Programs & Tax Records",
      `<div class="modal-section">
        <h4>${{fi ? "Tunnistetut klusterit aineistossa" : "Audited Clusters in the Dataset"}}</h4>
        <ul>${{listHtml}}</ul>
      </div>`
    );
  }} else if (key === 'ngo_pool') {{
    openModalHtml(
      fi ? "Mitä STEA:n vuoden 2026 kaikki 686 järjestöä todistavat?" : "What All 686 Real 2026 STEA Organizations Prove",
      fi ? "Lähde: avustukset.stea.fi · 1 527 virallista avustuspäätöstä vuodelle 2026 = 273 912 000 €" : "Source: avustukset.stea.fi · 1,527 Official 2026 Decisions = €273,912,000",
      `<div class="modal-section">
        <h4>${{fi ? "Kiistaton rekisteritodiste (Lataa myös Excelin välilehti 06)" : "Hard Registry Proof (Also in Excel Tab 06)"}}</h4>
        <ul>
          <li><strong>${{fi ? "Kaikki STEA-avustukset 2026 yhteensä:" : "Total 2026 STEA Grants:"}}</strong> 273 912 000 € (686 järjestöä, 1 527 päätöstä)</li>
          <li><strong>${{fi ? "Siitä rajoittamattomia Ak-yleisavustuksia:" : "Of Which Unrestricted Ak General HQ Grants:"}}</strong> <strong style="color:var(--red)">212 203 929 € (77,5 %)</strong></li>
          <li><strong>${{fi ? "Siitä kohdennettuja hanke- ja investointiavustuksia:" : "Of Which Targeted Project/Field Grants:"}}</strong> 61 708 071 € (22,5 %)</li>
          <li><strong>${{fi ? "Tuetut lomajärjestöt (100 % Ak):" : "Taxpayer-Subsidized Holiday Associations (100% Ak):"}}</strong> Loma ja Terveys ry (2 684 710 €) + Hyvinvointilomat ry (2 103 947 €) = <strong>4 788 657 €/v</strong></li>
          <li><strong>${{fi ? "Suurimmat Ak-yleistukien saajat 2026:" : "Largest Ak General Grant Recipients 2026:"}}</strong> MIELI ry (5,00 M€ Ak), Suomen Punainen Risti (3,03 M€ Ak), EHYT ry (2,87 M€ Ak), Loma ja Terveys ry (2,68 M€ Ak), Näkövammaisten liitto ry (2,25 M€ Ak), MLL (2,01 M€ Ak), Sininauhasäätiö (1,99 M€ Ak), A-klinikkasäätiö (1,96 M€ Ak).</li>
        </ul>
      </div>`
    );
  }}
}}

function openFlowModal(step) {{
  const fi = LANG === 'fi';
  const steps = {{
    1: {{
      t: fi ? "Vaihe 1: Veronmaksajan raha ohjataan tukivirastoille" : "Step 1: Taxpayer Money Flows to Grant Agencies",
      s: fi ? "11,50 miljardia euroa vuodessa ilman verotuottovastuuta" : "€11.50 Billion/Year With Zero Tax-Return Accountability",
      b: fi ? "Valtion budjetista jaetaan joka vuosi 11,5 miljardia euroa yritys-, energia-, maatalous- ja järjestötukiin. Tukivirastot eivät tarkista Verohallinnon rekisteristä, maksoiko tukea saanut yhtiö koskaan yhteisöveroa takaisin yhteiskunnalle."
            : "€11.5B/year is distributed across grant agencies with no statutory requirement to check whether recipients ever generate corporate tax revenue."
    }},
    2: {{
      t: fi ? "Vaihe 2: Tukikonsultti kokoaa moniyhtiökonsortion" : "Step 2: Grant Consultant Packages the Multi-Company Consortium",
      s: fi ? "Esimerkkinä Business Finland Veturi-, RRF- ja EU-konsortiot" : "Business Finland Veturi, RRF & EU Grant Consortia",
      b: fi ? "Erikoistuneet tukikonsultit (kuten Spinverse Oy) markkinoivat ja koordinoivat kymmenien miljoonien eurojen julkisia T&K- ja vihreän siirtymän tukikonsortioita ja veloittavat hakemustyöstä ja koordinoinnista merkittävät palkkiot."
            : "Specialized grant consultancy firms coordinate tens of millions in public R&D and green-transition consortia for substantial management and success fees."
    }},
    3: {{
      t: fi ? "Vaihe 3: Avustukset kirjataan tilinpäätöksessä ”muihin tuottoihin”" : "Step 3: Grants Are Booked into 'Other Operating Income'",
      s: fi ? "Tilinpäätöksen Vale-EBITDA peittää operatiivisen kassapolton" : "Grant-Padded EBITDA Masks Operating Cash Burn",
      b: fi ? "Kun tukea saanut pilottiyhtiö (esim. Spinnova Oyj, Infinited Fiber Company Oy tai Solar Foods Oyj) saa miljoonien avustukset, ne kirjataan tuloslaskelmassa Liiketoiminnan muihin tuottoihin ja tukipalkat aktivoidaan taseeseen."
            : "Approved grants are booked into Other Operating Income while grant-funded payroll is capitalized onto the balance sheet."
    }},
    4: {{
      t: fi ? "Vaihe 4: Lopputulos — 0 € yhteisöveroa tai konkurssi" : "Step 4: Outcome — €0 Corporate Tax or Bankruptcy",
      s: fi ? "Esimerkkinä Infinited Fiber Company Oy:n konkurssi 2024" : "Case Example: Infinited Fiber Company Oy Bankruptcy (2024)",
      b: fi ? "Infinited Fiber Company Oy (2766860-9) nosti yli 12,4 miljoonaa euroa julkisia Business Finland- ja EU-tukia maksamatta euroakaan yhteisöveroa ennen ajautumistaan konkurssiin vuonna 2024. Samaan aikaan tuettomat suomalaiset teknologiayhtiöt (kuten Supercell Oy >950 M€ ja RELEX Oy >28,5 M€) maksoivat satoja miljoonia yhteisöveroa."
            : "Infinited Fiber Company Oy (2766860-9) absorbed €12.4M+ in public grants and paid €0 corporate tax before going bankrupt in 2024—while unsubsidized software/tech peers paid hundreds of millions in corporate tax."
    }}
  }};
  const item = steps[step];
  openModalHtml(item.t, item.s, `<div class="modal-section"><h4>${{fi ? "Analyysi" : "Analysis"}}</h4><p>${{item.b}}</p></div>`);
}}

function openRingModal(idx) {{
  const r = DATA.rings[idx];
  const fi = LANG === 'fi';
  const members = DATA.corporate_evals.filter(c => r.y_tunnus_list.includes(c.y_tunnus));
  const memberRows = members.map(m => `<li><strong>${{m.company_name}} (${{m.y_tunnus}}):</strong> ${{fi ? "Nostettu tuki" : "Grant received"}} <strong>${{fmtEUR(m.subsidy_received_eur)}}</strong> (${{m.grant_agency.replace('_',' ')}}) · ${{fi ? "5v yhteisöveron muutos:" : "5-yr corporate tax delta:"}} <strong>${{fmtEUR(m.five_yr_tax_delta_eur)}}</strong>.</li>`).join('');
  openModalHtml(
    `${{r.shared_address_or_agent}} (${{r.ring_signature}})`,
    fi ? `Tunnistettu tukiklusteri · ${{r.entity_count}} oikeaa yhtiötä` : `Detected Grant Cluster · ${{r.entity_count}} Real Companies`,
    `<div class="modal-section">
      <h4>${{fi ? "Klusterin kokonaiskuva" : "Cluster Summary"}}</h4>
      <p>${{fi
        ? `Nämä ${{r.entity_count}} yhtiötä kuuluvat samaan maantieteelliseen T&K-keskittymään tai konsortio-ohjelmaan (<strong>${{r.shared_address_or_agent}}</strong>). Yhtiöt ovat nostaneet yhteensä <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> julkisia avustuksia ja lainoja. Viiden vuoden seurannassa klusterin yhteenlaskettu yhteisöveron muutos oli <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong>.`
        : `These ${{r.entity_count}} companies belong to the same R&D address hub or consortium program (<strong>${{r.shared_address_or_agent}}</strong>), collecting <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> in public subsidies with <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong> in 5-year corporate tax change.`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Klusterin yhtiöt (PRH YTJ Y-tunnus)" : "Companies in This Cluster"}}</h4>
      <ul>${{memberRows}}</ul>
    </div>`
  );
}}

function openMomenttiModal(idx) {{
  const m = MOMENTTI_META[idx];
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');
  const save = Math.min(m.current, m.base_cut * mult);
  const fi = LANG === 'fi';
  openModalHtml(
    `${{fi ? m.fi_name : m.en_name}} (${{m.code}})`,
    fi ? `Nykyinen määräraha: ${{fmtM(m.current)}} · Esitetty vuosisäästö: -${{fmtM(save)}}` : `Current Budget: ${{fmtM(m.current)}} · Proposed Annual Saving: -${{fmtM(save)}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Mitä tältä budjettimomentilta leikataan ja mihin todisteisiin se perustuu?" : "What Is Cut and What Empirical Evidence Proves It?"}}</h4>
      <p>${{fi ? m.fi_deep : m.en_deep}}</p>
    </div>`
  );
}}

function openNgoModal(idx) {{
  const n = DATA.ngo_evals[idx];
  const fi = LANG === 'fi';
  const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
  openModalHtml(
    `${{n.ngo_name}} (Y-tunnus: ${{n.y_tunnus}})`,
    `${{n.grant_source}} (Momentti ${{n.vm_momentti}}) · ${{fi ? "Avustuslaji" : "Grant Class"}}: ${{n.grant_class_code}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Järjestön julkisen rahoituksen läpivalaisu" : "Public Funding Breakdown"}}</h4>
      <p>${{fi
        ? `<strong>${{n.ngo_name}}</strong> saa suoraa avustusta <strong>${{fmtEUR(n.annual_grant_eur)}}</strong> vuodessa. Keskushallinnon, viestinnän ja yleiskulujen osuus avustuksesta on <strong>${{n.overhead_and_lobbying_pct}} %</strong> (${{fmtEUR(n.hq_admin_comms_lobbying_spend_eur)}}).${{n.public_sote_procurement_sales_eur > 0 ? ` Lisäksi sama konserni myy hyvinvointialueille ja julkiselle sektorille palveluita <strong>${{fmtEUR(n.public_sote_procurement_sales_eur)}}</strong> edestä vuodessa.` : ''}}`
        : `<strong>${{n.ngo_name}}</strong> receives <strong>${{fmtEUR(n.annual_grant_eur)}}</strong>/year in direct grants, with <strong>${{n.overhead_and_lobbying_pct}}%</strong> (${{fmtEUR(n.hq_admin_comms_lobbying_spend_eur)}}) going to HQ/comms/general overhead.${{n.public_sote_procurement_sales_eur > 0 ? ` It also bills Wellbeing Counties <strong>${{fmtEUR(n.public_sote_procurement_sales_eur)}}</strong>/year commercially.` : ''}}`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Tarkat luvut (2026)" : "Exact 2026 Figures"}}</h4>
      <ul>
        <li><strong>${{fi ? "Vuosiavustus (STEA/OKM):" : "Annual Grant:"}}</strong> ${{fmtEUR(n.annual_grant_eur)}}</li>
        <li><strong>${{fi ? "Muut ministeriö-/kunta-avustukset:" : "Secondary Public Grants:"}}</strong> ${{fmtEUR(n.secondary_ministry_grants_eur)}}</li>
        <li><strong>${{fi ? "Kaupallinen sote-ostopalvelumyynti:" : "Commercial Sote Procurement Sales:"}}</strong> ${{fmtEUR(n.public_sote_procurement_sales_eur)}}</li>
        <li><strong>${{fi ? "Huomiot:" : "Audit Notes:"}}</strong> ${{(n.political_board_insiders || []).join(', ') || 'Kohdennettu kenttätyö'}}</li>
        <li><strong>${{fi ? "Esitetty vuosisäästö:" : "Proposed Annual Saving:"}}</strong> <strong style="color:${{isCut ? 'var(--red)' : 'var(--accent-dark)'}}">${{fmtEUR(n.recoverable_cut_eur)}}</strong></li>
      </ul>
    </div>`
  );
}}

function openSteaRawModal(orgId) {{
  const org = DATA.stea_all.find(x => x.org_id === orgId);
  if (!org) return;
  const fi = LANG === 'fi';
  const akPct = org.granted_2026_eur > 0 ? ((org.ak_general_2026_eur / org.granted_2026_eur) * 100).toFixed(1) : '0.0';
  const purpHtml = (org.top_purposes || []).map(p => `<li>${{p}}</li>`).join('');
  openModalHtml(
    `${{org.ngo_name}} (STEA ID: ${{org.org_id}})`,
    fi ? `Virallinen STEA 2026 -avustuspäätösrekisteri · ${{org.decision_count_2026}} päätöstä vuonna 2026` : `Official 2026 STEA Grant Registry · ${{org.decision_count_2026}} Decisions in 2026`,
    `<div class="modal-section">
      <h4>${{fi ? "Vuoden 2026 viralliset STEA-avustusluvut" : "Official 2026 STEA Grant Breakdown"}}</h4>
      <ul>
        <li><strong>${{fi ? "Haettu STEA-avustus 2026:" : "Requested 2026 Grant:"}}</strong> ${{fmtEUR(org.requested_2026_eur)}}</li>
        <li><strong>${{fi ? "Myönnetty STEA-avustus 2026 yhteensä:" : "Total Granted 2026:"}}</strong> <strong>${{fmtEUR(org.granted_2026_eur)}}</strong></li>
        <li><strong>${{fi ? "Siitä rajoittamaton Ak-yleisavustus (keskushallinto & yleistoiminta):" : "Of Which Unrestricted Ak General HQ Subsidy:"}}</strong> <strong style="color:var(--red)">${{fmtEUR(org.ak_general_2026_eur)}} (${{akPct}} %)</strong></li>
        <li><strong>${{fi ? "Siitä kohdennettu hanke-/investointiavustus (Ah/Ae/Ai):" : "Of Which Targeted Project/Field Aid:"}}</strong> <strong style="color:var(--accent-dark)">${{fmtEUR(org.targeted_2026_eur)}}</strong></li>
      </ul>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Suurimmat viralliset avustuskohteet (2026)" : "Primary Official Grant Purposes (2026)"}}</h4>
      <ul>${{purpHtml}}</ul>
    </div>`
  );
}}

function openCorpModal(y_tunnus) {{
  const fi = LANG === 'fi';
  const c = DATA.corporate_evals.find(x => x.y_tunnus === y_tunnus);
  const b = DATA.benchmarks.find(x => x.y_tunnus === y_tunnus);
  const qoe = DATA.qoe_reports.find(x => x.y_tunnus === y_tunnus);

  if (b && !c) {{
    openModalHtml(
      `${{b.company_name}} (Y-tunnus: ${{b.y_tunnus}})`,
      fi ? `Tueton nettoveronmaksajaverrokki · Toimiala TOL ${{b.nace_code}} · ${{b.postal_address}}` : `Unsubsidized Net Taxpayer Benchmark · NACE ${{b.nace_code}} · ${{b.postal_address}}`,
      `<div class="modal-section">
        <h4>${{fi ? "Miksi tämä yhtiö on mukana tutkimuksen vertailuryhmässä?" : "Why Is This Company Included as a Benchmark?"}}</h4>
        <p>${{fi
          ? `<strong>${{b.company_name}}</strong> on esimerkki aidosti markkinaehtoisesta suomalaisesta menestysyrityksestä, joka ei elä valtion zombituilla vaan on maksanut Suomeen <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> yhteisöveroa 5 vuoden tarkastelujaksolla.`
          : `<strong>${{b.company_name}}</strong> is a market-driven Finnish taxpayer benchmark that paid <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> in Finnish corporate income taxes over 5 years without relying on zombie subsidies.`}}</p>
      </div>`
    );
    return;
  }}
  if (!c) return;

  openModalHtml(
    `${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})`,
    `${{c.grant_agency.replace('_',' ')}} (Momentti ${{c.vm_momentti}}) · TOL ${{c.nace_code}} · ${{c.postal_or_co_address}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Julkisen tuen ja maksetun yhteisöveron suhde (5 v)" : "Public Subsidy vs. Corporate Tax Paid (5-Yr Comparison)"}}</h4>
      <ul>
        <li><strong>${{fi ? "Saatu julkinen yritystuki (5v):" : "Public Subsidy Received (5-Yr):"}}</strong> <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong></li>
        <li><strong>${{fi ? "Yhtiön yhteisöveron muutos (5v):" : "Recipient 5-Yr Corporate Tax Change:"}}</strong> <strong>${{fmtEUR(c.five_yr_tax_delta_eur)}}</strong></li>
        <li><strong>${{fi ? "Tuettoman toimialaverrokin verokasvu (5v):" : "Matched Unsubsidized Peer 5-Yr Tax Growth:"}}</strong> ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}</li>
        <li><strong>${{fi ? "Kausaalinen DiD Vero-ROI:" : "Causal DiD Tax ROI:"}}</strong> <strong>${{c.causal_did_roi.toFixed(2)}}x</strong></li>
        <li><strong>${{fi ? "Esitetty budjettileikkaus:" : "Recommended Budget Cut:"}}</strong> <strong style="color:${{c.recommended_cut_eur > 0 ? 'var(--red)' : 'var(--accent-dark)'}}">${{fmtEUR(c.recommended_cut_eur)}}</strong></li>
      </ul>
    </div>
    ${{qoe ? `<div class="modal-section">
      <h4>${{fi ? "Tilinpäätöksen oikaisu (Vale-EBITDA & Tukiriisunta)" : "Financial Statement Strip-Down (Quality of Earnings)"}}</h4>
      <p>${{fi
        ? `Raportoitu liikevaihto: <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> · Raportoitu käyttökate (EBITDA): <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong>. Kun tuloksesta poistetaan Liiketoiminnan muihin tuottoihin kirjatut julkiset avustukset (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) ja aktivoidut tukipalkat, todellinen omavarainen kassavirta-EBITDA on <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`
        : `Reported revenue: <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> · Reported EBITDA: <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong>. Stripping out public grants booked in Other Operating Income (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) and capitalized grant payroll yields a true standalone cash EBITDA of <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`}}</p>
    </div>` : ''}}`
  );
}}

function setSearch(val) {{
  const box = document.getElementById('search-box');
  box.value = val;
  document.querySelectorAll('.chip').forEach(btn => {{
    const txt = btn.textContent.trim().toLowerCase();
    btn.classList.toggle('active', (val === '' && (txt.includes('kaikki') || txt.includes('all'))) || (val !== '' && txt.includes(val.toLowerCase())));
  }});
  renderAll();
}}

function setLang(l) {{
  LANG = l;
  document.getElementById('btn-fi').classList.toggle('active', l === 'fi');
  document.getElementById('btn-en').classList.toggle('active', l === 'en');
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const k = el.getAttribute('data-i18n');
    if (I18N[l][k]) el.innerHTML = I18N[l][k];
  }});
  renderAll();
}}

function renderAll() {{
  const rawQ = (document.getElementById('search-box').value || '').trim();
  const q = rawQ.toLowerCase();
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');
  const fi = LANG === 'fi';

  // Update KPI total savings based on scenario
  const totalBaseSave = MOMENTTI_META.reduce((acc, m) => acc + Math.min(m.current, m.base_cut * mult), 0);
  document.getElementById('kpi-save-val').textContent = (totalBaseSave / 1e9).toLocaleString('fi-FI', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + (fi ? ' mrd. €/v' : 'B €/yr');

  // 1. Corporate Cards (All 23 Real Subsidy Recipients + 5 Real Unsubsidized Benchmarks = 28 Real Companies)
  const allCorps = [
    ...DATA.corporate_evals.map(c => ({{ ...c, isBenchmark: false }})),
    ...DATA.benchmarks.map(b => ({{
      y_tunnus: b.y_tunnus,
      company_name: b.company_name,
      nace_code: b.nace_code,
      postal_or_co_address: b.postal_address,
      grant_agency: fi ? 'EI JULKISTA YRITYSTUKEA' : 'ZERO PUBLIC GRANTS',
      vm_momentti: '0 €',
      subsidy_received_eur: 0,
      five_yr_tax_delta_eur: b.five_yr_corporate_tax_paid_eur,
      matched_peer_five_yr_tax_delta_eur: b.five_yr_corporate_tax_paid_eur,
      classification: 'BENCHMARK_TAXPAYER',
      recommended_cut_eur: 0,
      isBenchmark: true
    }}))
  ];

  let corpMatches = 0;
  let corpHtml = '';
  allCorps.forEach(c => {{
    const hay = `${{c.company_name}} ${{c.y_tunnus}} ${{c.grant_agency}} ${{c.postal_or_co_address}} ${{c.nace_code}} ${{c.vm_momentti}}`.toLowerCase();
    if (q && !hay.includes(q)) return;
    corpMatches++;

    const isZombie = c.classification === 'BLACKLIST_ZOMBIE';
    const isDead = c.classification === 'DEADWEIGHT_CROWD_OUT';
    const accent = isZombie ? 'red-accent' : (isDead ? 'amber-accent' : 'green-accent');
    const badge = isZombie
      ? `<span class="badge badge-red">${{fi ? 'Leikataan 100 %' : 'Cut 100%'}}</span>`
      : (isDead ? `<span class="badge badge-amber">${{fi ? 'Säilyttävä tuki' : 'Deadweight Subsidy'}}</span>`
                : `<span class="badge badge-green">${{c.isBenchmark ? (fi ? '0 € tukea · Nettoveronmaksaja' : '€0 Grants · Net Taxpayer') : (fi ? 'Vahva verotuotto' : 'High Tax Return')}}</span>`);

    const tParts = splitTitle(c.company_name);
    const subText = tParts.sub || (c.isBenchmark ? (fi ? 'Tueton markkinaverrokki' : 'Unsubsidized Benchmark') : c.grant_agency.replace(/_/g, ' '));
    const momClean = String(c.vm_momentti || '').replace(/_/g, ' / ');
    const commentary = c.isBenchmark
      ? (fi
          ? `Markkinaehtoinen veronmaksajaverrokki (${{c.postal_or_co_address}}) · TOL ${{c.nace_code}}.`
          : `Market-driven net taxpayer benchmark (${{c.postal_or_co_address}}) · NACE ${{c.nace_code}}.`)
      : (fi
          ? `${{c.postal_or_co_address}} · Momentti ${{momClean}} · TOL ${{c.nace_code}}.`
          : `${{c.postal_or_co_address}} · Budget line ${{momClean}} · NACE ${{c.nace_code}}.`);

    corpHtml += `<div class="story-card ${{accent}} clickable-card" onclick="openCorpModal('${{c.y_tunnus}}')">
      <div class="story-top">
        <div class="card-kicker-row">
          ${{badge}}
          <span class="card-id-pill">Y: ${{c.y_tunnus}}</span>
        </div>
        <h3>${{tParts.main}}</h3>
        <div class="story-subtitle">${{subText}}</div>
        <p class="story-commentary">${{commentary}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Julkinen tuki 5v' : '5-Yr Grant'}}</span><strong>${{c.subsidy_received_eur > 0 ? fmtCardM(c.subsidy_received_eur) : '0 €'}}</strong></div>
          <div><span>${{fi ? 'Yhteisövero 5v' : '5-Yr Corp Tax'}}</span><strong style="color:${{c.five_yr_tax_delta_eur > 0 ? 'var(--accent-dark)' : 'var(--red)'}}">${{fmtCardM(c.five_yr_tax_delta_eur)}}</strong></div>
          <div><span>${{fi ? 'Esitetty säästö' : 'Proposed Cut'}}</span><strong style="color:${{c.recommended_cut_eur > 0 ? 'var(--red)' : 'var(--accent-dark)'}}">${{c.recommended_cut_eur > 0 ? '-' + fmtCardM(c.recommended_cut_eur) : '0 €'}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Vero- & tilinpäätösanalyysi →' : 'Click: Full tax & financial audit →'}}</div>
      </div>
    </div>`;
  }});

  if (!corpHtml) {{
    corpHtml = `<div class="empty-box">
      <span>${{fi ? `Ei yritysosumia haulle ”${{rawQ}}”. Katso löytyneet järjestöt alla olevasta osiosta 2 tai tyhjennä haku.` : `No corporate matches for "${{rawQ}}". Check Section 2 below for matching NGOs or clear search.`}}</span>
      <button type="button" class="btn-secondary" onclick="setSearch('')">${{fi ? 'Näytä kaikki 28 yhtiötä' : 'Show all 28 corporations'}}</button>
    </div>`;
  }}
  document.getElementById('corp-cards').innerHTML = corpHtml;

  // 2. NGO Story Cards + All 686 Real 2026 STEA Organizations Table
  let ngoCardMatches = 0;
  let ngoHtml = '';
  DATA.ngo_evals.forEach((n, idx) => {{
    const hay = `${{n.ngo_name}} ${{n.y_tunnus}} ${{n.grant_source}} ${{n.vm_momentti}} ${{(n.political_board_insiders || []).join(' ')}}`.toLowerCase();
    if (q && !hay.includes(q)) return;
    ngoCardMatches++;
    const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
    const accent = isCut ? 'red-accent' : 'green-accent';
    const badge = isCut
      ? `<span class="badge badge-red">${{fi ? 'Leikataan Ak-hallintopöhö' : 'Cut Ak Admin Bloat'}}</span>`
      : `<span class="badge badge-green">${{fi ? 'Kohdennettu kenttätyö' : 'Frontline Aid (€0 Cut)'}}</span>`;
    const nParts = splitTitle(n.ngo_name);
    const nSub = nParts.sub || `${{n.grant_source}} · Momentti ${{n.vm_momentti}} (${{n.grant_class_code}})`;
    const commentary = fi
      ? `Hallinto ja Ak-yleistuki: ${{n.overhead_and_lobbying_pct}} %. ${{n.public_sote_procurement_sales_eur > 0 ? `Myy lisäksi sote-palveluita ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/v.` : (n.political_board_insiders[0] || '')}}`
      : `HQ & Ak general share: ${{n.overhead_and_lobbying_pct}}%. ${{n.public_sote_procurement_sales_eur > 0 ? `Also bills Wellbeing Counties ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/yr.` : ''}}`;

    ngoHtml += `<div class="story-card ${{accent}} clickable-card" onclick="openNgoModal(${{idx}})">
      <div class="story-top">
        <div class="card-kicker-row">
          ${{badge}}
          <span class="card-id-pill">Y: ${{n.y_tunnus}}</span>
        </div>
        <h3>${{nParts.main}}</h3>
        <div class="story-subtitle">${{nSub}}</div>
        <p class="story-commentary">${{commentary}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Avustus 2026' : '2026 Grant'}}</span><strong>${{fmtCardM(n.annual_grant_eur)}}</strong></div>
          <div><span>${{fi ? 'Sote-myynti' : 'Sote Sales'}}</span><strong>${{n.public_sote_procurement_sales_eur > 0 ? fmtCardM(n.public_sote_procurement_sales_eur) : '0 €'}}</strong></div>
          <div><span>${{fi ? 'Esitetty säästö' : 'Proposed Cut'}}</span><strong style="color:${{isCut ? 'var(--red)' : 'var(--accent-dark)'}}">${{n.recoverable_cut_eur > 0 ? '-' + fmtCardM(n.recoverable_cut_eur) : '0 €'}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Järjestön rahoituserittely →' : 'Click: Open NGO funding audit →'}}</div>
      </div>
    </div>`;
  }});

  if (!ngoHtml) {{
    ngoHtml = `<div class="empty-box">
      <span>${{fi ? `Ei osumia pääjärjestökorteissa haulle ”${{rawQ}}”. Katso alla oleva kaikkien 686 STEA-järjestön hakutaulukko tai osion 1 yritykset.` : `No matches in featured NGO cards for "${{rawQ}}". Check the 686-NGO table below or Section 1 corporations.`}}</span>
      <button type="button" class="btn-secondary" onclick="setSearch('')">${{fi ? 'Näytä kaikki järjestöt' : 'Show all NGOs'}}</button>
    </div>`;
  }}
  document.getElementById('ngo-cards').innerHTML = ngoHtml;

  // Render 686 STEA Table
  const filteredStea = DATA.stea_all.filter(o => {{
    if (!q) return true;
    const hay = `${{o.ngo_name}} ${{o.org_id}} ${{(o.top_purposes || []).join(' ')}}`.toLowerCase();
    return hay.includes(q);
  }});
  const steaSub = document.getElementById('stea-count-sub');
  const sumFilteredStea = filteredStea.reduce((a, b) => a + b.granted_2026_eur, 0);
  const sumFilteredAk = filteredStea.reduce((a, b) => a + b.ak_general_2026_eur, 0);
  steaSub.textContent = fi
    ? `Näytetään ${{filteredStea.length}} / 686 STEA-järjestöä · Myönnetty yhteensä ${{fmtEUR(sumFilteredStea)}}, josta Ak-yleisavustusta ${{fmtEUR(sumFilteredAk)}}`
    : `Showing ${{filteredStea.length}} / 686 STEA NGOs · Total granted ${{fmtEUR(sumFilteredStea)}}, of which Ak general grants ${{fmtEUR(sumFilteredAk)}}`;

  const steaTbody = document.getElementById('stea-all-tbody');
  if (filteredStea.length === 0) {{
    steaTbody.innerHTML = `<tr><td colspan="7" style="text-align:center;padding:18px;color:var(--muted);">${{fi ? `Ei STEA-järjestöosumia haulle ”${{rawQ}}”.` : `No STEA NGOs matching "${{rawQ}}".`}}</td></tr>`;
  }} else {{
    steaTbody.innerHTML = filteredStea.map((o, idx) => {{
      const akPct = o.granted_2026_eur > 0 ? ((o.ak_general_2026_eur / o.granted_2026_eur) * 100).toFixed(1) : '0.0';
      return `<tr class="clickable-row" onclick="openSteaRawModal(${{o.org_id}})">
        <td>${{idx + 1}}</td>
        <td><strong>${{o.ngo_name}}</strong></td>
        <td><strong>${{fmtEUR(o.granted_2026_eur)}}</strong></td>
        <td style="color:${{o.ak_general_2026_eur > 0 ? 'var(--red)' : 'var(--muted)'}};font-weight:600;">${{fmtEUR(o.ak_general_2026_eur)}}</td>
        <td><span class="badge ${{parseFloat(akPct) >= 50 ? 'badge-red' : 'badge-green'}}">${{akPct}} %</span></td>
        <td>${{fmtEUR(o.targeted_2026_eur)}}</td>
        <td style="font-size:12.5px;color:var(--body);">${{(o.top_purposes && o.top_purposes[0]) || '—'}}</td>
      </tr>`;
    }}).join('');
  }}

  // 3. Momentti Cards
  let momHtml = '';
  MOMENTTI_META.forEach((m, idx) => {{
    const save = Math.min(m.current, m.base_cut * mult);
    momHtml += `<div class="story-card green-accent clickable-card" onclick="openMomenttiModal(${{idx}})">
      <div class="story-top">
        <div class="card-kicker-row">
          <span class="badge badge-red">-${{fmtCardM(save)}} / v</span>
          <span class="card-id-pill">${{fi ? 'Momentti' : 'Line'}} ${{m.code}}</span>
        </div>
        <h3>${{fi ? m.fi_name : m.en_name}}</h3>
        <p class="story-commentary" style="margin-top:6px;">${{fi ? m.fi_short : m.en_short}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nykybudjetti' : 'Current Spend'}}</span><strong>${{fmtCardM(m.current)}}</strong></div>
          <div><span>${{fi ? 'Vuosisäästö' : 'Annual Saving'}}</span><strong style="color:var(--red)">-${{fmtCardM(save)}}</strong></div>
          <div><span>${{fi ? 'Leikkaus-%' : 'Cut Share'}}</span><strong>${{((save / m.current) * 100).toFixed(0)}} %</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Perustelut & kohde-erittely →' : 'Click: Policy rationale & evidence →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('momentti-cards').innerHTML = momHtml;

  // 4. Ring Cards
  let ringHtml = '';
  DATA.rings.forEach((r, idx) => {{
    ringHtml += `<div class="story-card red-accent clickable-card" onclick="openRingModal(${{idx}})">
      <div class="story-top">
        <div class="card-kicker-row">
          <span class="badge badge-red">${{r.entity_count}} ${{fi ? 'yhtiötä klusterissa' : 'firms in cluster'}}</span>
          <span class="card-id-pill">${{r.ring_signature}}</span>
        </div>
        <h3>${{r.shared_address_or_agent}}</h3>
        <div class="story-subtitle">${{r.company_names.map(n => n.split(' (')[0]).join(' · ')}}</div>
        <p class="story-commentary">${{fi
          ? `Klusterin ${{r.entity_count}} yhtiötä nostivat yhteensä ${{fmtM(r.total_subsidy_eur)}} julkista tukea. 5 vuoden yhteisöveron muutos: ${{fmtEUR(r.total_five_yr_tax_delta_eur)}}.`
          : `Cluster of ${{r.entity_count}} firms collected ${{fmtM(r.total_subsidy_eur)}} in public grants. 5-yr corporate tax change: ${{fmtEUR(r.total_five_yr_tax_delta_eur)}}.`}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nostettu tuki' : 'Grants Taken'}}</span><strong style="color:var(--red)">${{fmtCardM(r.total_subsidy_eur)}}</strong></div>
          <div><span>${{fi ? 'Yhteisövero 5v' : '5-Yr Tax Delta'}}</span><strong>${{fmtCardM(r.total_five_yr_tax_delta_eur)}}</strong></div>
          <div><span>${{fi ? 'Koordinointi (20%)' : '20% Fee Est.'}}</span><strong style="color:var(--amber)">${{fmtCardM(r.estimated_20pct_consultant_cut_eur)}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Klusterin yhtiöt ja luvut →' : 'Click: Inspect cluster member companies →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('ring-cards').innerHTML = ringHtml;

  // Update Search Status Banner
  const statusEl = document.getElementById('search-status');
  if (q) {{
    statusEl.style.display = 'block';
    statusEl.innerHTML = fi
      ? `Hakutulokset haulle <strong>”${{rawQ}}”</strong>: löytyi <strong>${{corpMatches}}</strong> yritystä (Osio 1) sekä <strong>${{filteredStea.length}}</strong> STEA/OKM-järjestöä (Osio 2). <a href="javascript:void(0)" onclick="setSearch('')" style="color:var(--accent-dark);margin-left:10px;">✕ Tyhjennä haku</a>`
      : `Search results for <strong>"${{rawQ}}"</strong>: found <strong>${{corpMatches}}</strong> corporations (Section 1) and <strong>${{filteredStea.length}}</strong> STEA/OKM NGOs (Section 2). <a href="javascript:void(0)" onclick="setSearch('')" style="color:var(--accent-dark);margin-left:10px;">✕ Clear search</a>`;
  }} else {{
    statusEl.style.display = 'none';
  }}
}}

document.getElementById('search-box').addEventListener('input', renderAll);
document.getElementById('scenario-select').addEventListener('change', renderAll);
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
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    total_ring_subsidy = sum(float(r["total_subsidy_eur"]) for r in rings)
    total_consultant_cut = sum(float(r["estimated_20pct_consultant_cut_eur"]) for r in rings)
    total_ngo_cut = sum(float(n["recoverable_cut_eur"]) for n in ngo_evals)

    md = f"""# Suomen Talousinstituutti (STI) — Turnkey VM Kehysriihi 2027 & Media Dossiers

* **Data Provenance:** 100% Real Statutory Public Open Data (`STEA 2026 All 686 NGOs = €273,912,000`, `Tutkiavustuksia.fi`, `Business Finland`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)

| VM Momentti | Budget Line Description | National Annual Cut (`€1.55B` Base) | Audited Sample Cut (`€`) |
| :--- | :--- | ---: | ---: |
| **`32.20.40`** | Business Finland R&D Grants | `€211,500,000` | `€{momentti_summary.get("32.20.40", 0.0):,.2f}` |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€90,000,000` | `€{momentti_summary.get("32.20.83", 0.0):,.2f}` |
| **`32.30.42`** | ELY Regional & Maritime Development Grants | `€174,000,000` | `€{momentti_summary.get("32.30.42", 0.0):,.2f}` |
| **`33.90.50`** | STEA Grants (`€212.2M` `Ak` General HQ Slush across 686 NGOs) | `€209,000,000` | `€{momentti_summary.get("33.90.50", 0.0):,.2f}` |
| **`29.80.50`** | OKM General & Advocacy NGO Grants | `€168,000,000` | `€{momentti_summary.get("29.80.50", 0.0):,.2f}` |
| **`30.10.40 / 32.60.40`** | National Agri & Industrial Energy Subsidies | `€696,000,000` | `€{momentti_summary.get("30.10.40_32.60.40", 0.0):,.2f}` |
| **TOTAL** | **KEHYSRIIHI 2027 SUBSIDY GUILLOTINE** | **`€1,548,500,000 / yr`** | **`€{sum(momentti_summary.values()):,.2f}`** |

* Audited cluster subsidy total: €{total_ring_subsidy:,.0f} (20% coordination/fee estimate: €{total_consultant_cut:,.0f}, Featured NGO cut: €{total_ngo_cut:,.0f})
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    return output_path
