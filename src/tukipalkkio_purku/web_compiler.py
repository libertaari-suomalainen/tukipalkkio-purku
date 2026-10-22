"""
Compilers for:
  1. `dist/Veronmaksajan_Tuomioistuin_2026.html` (`dist/index.html`) — Suomen Talousinstituutti (STI) Editorial Research Report & Real-Data Explorer (686 STEA 2026 NGOs + 47 Real Finnish Corporations)
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

  /* Sortable Full Registry Tables */
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
    max-height: 540px;
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
    user-select: none;
  }}
  th.sortable {{
    cursor: pointer;
    transition: background 0.14s;
  }}
  th.sortable:hover {{
    background: var(--stone-hover);
    color: var(--accent-dark);
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
    max-width: 780px;
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
  .modal-sub {{ font-size: 14px; color: var(--muted); margin-bottom: 16px; }}
  .modal-toolbar {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
  }}
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
  .legal-box {{
    background: #18181B;
    color: #F4F4F5;
    font-family: 'SFMono-Regular', Consolas, Menlo, monospace;
    font-size: 12.5px;
    line-height: 1.55;
    padding: 14px 16px;
    border-radius: 6px;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 260px;
    overflow-y: auto;
    margin: 10px 0 12px;
  }}
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
  @media print {{
    body * {{ visibility: hidden; }}
    #detail-modal, #detail-modal * {{ visibility: visible; }}
    #detail-modal {{ position: absolute; left: 0; top: 0; width: 100%; background: #fff; padding: 0; display: block !important; }}
    .modal-card {{ max-height: none; box-shadow: none; border: none; width: 100%; max-width: 100%; padding: 0; }}
    .modal-close, .modal-toolbar {{ display: none !important; }}
  }}
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
        <span data-i18n="brand_sub">Tutkimusraportti 2026 · 686 STEA-järjestöä (1 288 päätöstä) &amp; 47 suuryritystä ja tukikohdetta</span>
      </div>
    </a>
    <div class="nav-actions">
      <button class="lang-btn active" id="btn-fi" onclick="setLang('fi')">Suomi</button>
      <button class="lang-btn" id="btn-en" onclick="setLang('en')">English</button>
      <a class="btn-secondary" href="https://libertaari-suomalainen.github.io/kartelli-tutka/" data-i18n="nav_sister">Tutkimus II: Julkiset hankinnat (38,7 mrd. €) →</a>
      <a class="btn-primary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="nav_xlsx">⬇ Lataa Excel-aineisto (.xlsx)</a>
    </div>
  </div>
</header>

<main class="container">
  <!-- HERO SECTION -->
  <section class="hero-card">
    <div class="kicker" data-i18n="hero_kicker">VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % OIKEA VIRANOMAISDATA</div>
    <h1 class="hero-title" data-i18n="hero_title">Suomen yritys- ja järjestötukien vaikuttavuus- ja verovasteanalyysi (11,5 mrd. €/v)</h1>
    <p class="hero-lead" data-i18n="hero_lead">
      Suomen julkinen sektori kohdentaa vuosittain noin 11,5 miljardia euroa suoriin yritystukiin, energia- ja maataloustukiin, toimialakohtaisiin verotukiin sekä järjestöavustuksiin. Kun viralliset tukipäätökset (TEM Yritystukien tietopalvelu, Business Finland, ELY, Traficom sekä STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon julkisiin yhteisöverotietoihin ja PRH:n yritysrekisteriin, tunnistetaan <strong>1,55–3,00 miljardin euron vuotuinen sopeutuspotentiaali</strong> ilman leikkauksia kouluihin, sairaaloihin, poliisiin tai maanpuolustukseen.
    </p>
    <div class="callout-stone">
      <h3 data-i18n="summary_box_title">Mitä tämä tutkimus ja ladattava Excel (.xlsx) sisältävät?</h3>
      <p data-i18n="summary_box_body">
        Julkaisu sisältää <strong>kaikki 686 STEA-järjestöä (kaikki 1 288 virallista avustuspäätöstä 1 527 hakemuksesta vuodelle 2026 = 273,91 milj. €: 212,20 M€ kohdennettuja Ak-toiminta-avustuksia, 58,21 M€ Ay-yleisavustuksia ja 3,49 M€ C/B-hankeavustuksia)</strong> sekä <strong>47 suomalaista yritystukien saajaa ja nettoveronmaksajaverrokkia</strong> (mm. Veturi- ja T&amp;K-vientiyhtiöt <em>Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Patria, Kempower, RELEX</em>; teollisuus- ja varustamotuet <em>UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Finnlines, Tallink Silja, Finnair</em>; T&amp;K-/pilottivaiheen tukikohteet <em>Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio</em>; sekä tuettomat yhteisöveronmaksajat <em>OP Ryhmä, Supercell, Sampo, Kesko, Elisa, Nokian Renkaat, Puuilo, Harvia, Marimekko, Olvi</em>).
      </p>
    </div>
    <div class="kpi-grid">
      <div class="kpi-card clickable-card" onclick="openKpiModal('total_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi1_lbl">Julkiset tuet &amp; verotuet yhteensä</div>
          <div class="kpi-val">11,50 mrd. €/v</div>
          <div class="kpi-sub" data-i18n="kpi1_sub">Suorat yritys-, energia-, maatalous- ja järjestötuet (~7,5 mrd. €) sekä toimialaverotuet (~4,0 mrd. €)</div>
        </div>
        <div class="click-hint" data-i18n="click_explain">Klikkaa: Mistä 11,5 mrd. € koostuu? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('savings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi2_lbl">Tunnistettu sopeutuspotentiaali</div>
          <div class="kpi-val green" id="kpi-save-val">1,55 mrd. €/v</div>
          <div class="kpi-sub" data-i18n="kpi2_sub">Rakenteellinen säästö 6 tukikokonaisuudesta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin</div>
        </div>
        <div class="click-hint" data-i18n="click_explain2">Klikkaa: Miten säästö syntyy? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('rings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi3_lbl">T&amp;K-ekosysteemi- ja konsortioklusterit</div>
          <div class="kpi-val red" id="kpi-ring-val">3 Klusteria · 132,2 M€</div>
          <div class="kpi-sub" data-i18n="kpi3_sub">Otaniemen puhtaan siirtymän keskittymä, biokuitu-/kiertotalouskonsortiot ja Keilasataman Veturi-ekosysteemi</div>
        </div>
        <div class="click-hint" data-i18n="click_explain3">Klikkaa: Katso 3 T&amp;K-klusteria →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('ngo_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi4_lbl">STEA 2026 Jatkuvat Ak- ja Ay-avustukset</div>
          <div class="kpi-val red">98,7 % (270,4 M€)</div>
          <div class="kpi-sub" data-i18n="kpi4_sub">686 järjestöä (273,9 M€): 212,2 M€ (77,5 %) jatkuvaa Ak-toimintatukea + 58,2 M€ (21,3 %) Ay-yleisavustusta</div>
        </div>
        <div class="click-hint" data-i18n="click_explain4">Klikkaa: Katso STEA 2026 -erittely →</div>
      </div>
    </div>
  </section>

  <!-- GLOBAL SEARCH & SCENARIO HUB -->
  <section class="search-hub" id="haku">
    <div class="search-hub-grid">
      <div>
        <label for="search-box" data-i18n="lbl_search">Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 47 suuryritystä &amp; tukikohdetta)</label>
        <input id="search-box" type="search" class="input-box" placeholder="Kokeile esim. Nokia, KONE, Orion, UPM, Spinnova, Infinited Fiber, Meyer, Viking Line, Punainen Risti, Loma, SOSTE, Supercell, OP..." />
      </div>
      <div>
        <label for="scenario-select" data-i18n="lbl_scenario">Valitse Kehysriihi 2027 -tukiuudistuksen laajuus</label>
        <select id="scenario-select" class="select-box">
          <option value="1.0" data-i18n="opt_base">Perustaso: Karsitaan matalan lisäisyyden tuet, lomajärjestöt ja Ay-yleisavustuksia (1,55 mrd. €/v)</option>
          <option value="1.45" data-i18n="opt_med">Rakenneuudistus: Puolitetaan säilyttävät elinkeino- ja yleisavustukset (2,25 mrd. €/v)</option>
          <option value="1.94" data-i18n="opt_max">Laaja markkinauudistus: Poistetaan kilpailua vääristävät yritystuet (3,00 mrd. €/v)</option>
        </select>
      </div>
    </div>
    <div class="quick-chips">
      <span class="chip-label" data-i18n="chip_lbl">Pikavalinnat:</span>
      <button type="button" class="chip active" onclick="setSearch('')" data-i18n="chip_all">Näytä kaikki</button>
      <button type="button" class="chip" onclick="setSearch('Nokia | KONE | Orion | Konecranes | Vaisala | Ponsse')">Veturi- &amp; T&amp;K-veronmaksajat (Nokia, KONE, Orion)</button>
      <button type="button" class="chip" onclick="setSearch('UPM | Stora Enso | Metsä Fibre')">Metsäteollisuus (UPM 140 M€, Stora Enso 96 M€)</button>
      <button type="button" class="chip" onclick="setSearch('Infinited Fiber | Spinnova | Woodio | Sulapac | Solar Foods')">T&amp;K- ja pilottivaiheen yhtiöt (0 € yhteisöveroa)</button>
      <button type="button" class="chip" onclick="setSearch('Meyer Turku | Finnair')">Meyer Turku &amp; Finnair</button>
      <button type="button" class="chip" onclick="setSearch('Viking Line | Tallink | Finnlines')">Varustamotuet (31.20.43)</button>
      <button type="button" class="chip" onclick="setSearch('OP Osuuskunta | Supercell | Sampo | Kesko | Elisa')">Tuettomat nettoveronmaksajat (0 € tukea)</button>
      <button type="button" class="chip" onclick="setSearch('Loma')">Tuetut lomat (STEA)</button>
      <button type="button" class="chip" onclick="setSearch('Sininauha | A-klinikka')">Sininauha &amp; A-klinikka</button>
      <button type="button" class="chip" onclick="setSearch('SOSTE | EHYT | Allianssi')">SOSTE, EHYT &amp; Allianssi</button>
    </div>
    <div class="search-status" id="search-status"></div>
  </section>

  <!-- SECTION 1: YRITYSTUET (47 REAL FINNISH CORPORATIONS & BENCHMARKS) -->
  <section class="section-block" id="sec-corps">
    <div class="section-head">
      <h2 data-i18n="s4_title">1. Yritystukien totuus: Nollavero-tukikohteet, säilyttävät suuryritystuet ja aidot nettoveronmaksajat (47 yhtiötä)</h2>
      <p data-i18n="s4_sub">
        Klikkaa mitä tahansa yhtiökorttia tai alla olevan kokonaistaulukon riviä nähdäksesi selkokielisen vertailun: kuinka paljon yhtiö sai julkista tukea (Business Finland, TEM, ELY, sähköistämistuki tai merenkulun miehistötuki), paljonko sen yhteisövero oli 5 vuodessa ja miltä tulos näyttää ilman valtion tukia.
      </p>
    </div>
    <div class="cards-grid" id="corp-cards"></div>

    <div class="stea-table-wrap">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
        <div>
          <h3 style="font-size:19px;" data-i18n="corp_tbl_title">Yritysaineiston kokonaistaulukko: Kaikki 47 yhtiötä &amp; veronmaksajaverrokkia (Klikkaa otsikkoa lajitellaksesi tai riviä avataksesi)</h3>
          <p style="font-size:13.5px;color:var(--muted);" id="corp-count-sub"></p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button type="button" class="btn-secondary" onclick="exportFilteredCorpsCsv()" data-i18n="corp_csv_btn">⬇ Vie suodatettu yritysaineisto (.csv)</button>
          <a class="btn-primary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="corp_xlsx_btn">⬇ Lataa Excel (Välilehti 02)</a>
        </div>
      </div>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th class="sortable" onclick="sortCorpTable('company_name')"><span data-i18n="th_c_name">Yritys &amp; Y-tunnus</span> <span id="sort-corp-company_name"></span></th>
              <th class="sortable" onclick="sortCorpTable('nace_code')"><span data-i18n="th_c_tol">TOL</span> <span id="sort-corp-nace_code"></span></th>
              <th class="sortable" onclick="sortCorpTable('vm_momentti')"><span data-i18n="th_c_mom">Momentti</span> <span id="sort-corp-vm_momentti"></span></th>
              <th class="sortable" onclick="sortCorpTable('subsidy_received_eur')"><span data-i18n="th_c_sub">Julkinen tuki 5v (€)</span> <span id="sort-corp-subsidy_received_eur">▼</span></th>
              <th class="sortable" onclick="sortCorpTable('five_yr_tax_delta_eur')"><span data-i18n="th_c_tax">Yhteisövero 5v (€)</span> <span id="sort-corp-five_yr_tax_delta_eur"></span></th>
              <th class="sortable" onclick="sortCorpTable('causal_did_roi')"><span data-i18n="th_c_roi">Vero-ROI</span> <span id="sort-corp-causal_did_roi"></span></th>
              <th class="sortable" onclick="sortCorpTable('classification')"><span data-i18n="th_c_cls">Luokitus</span> <span id="sort-corp-classification"></span></th>
              <th class="sortable" onclick="sortCorpTable('recommended_cut_eur')"><span data-i18n="th_c_cut">Esitetty säästö (€)</span> <span id="sort-corp-recommended_cut_eur"></span></th>
            </tr>
          </thead>
          <tbody id="corp-all-tbody"></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- SECTION 2: JÄRJESTÖTUET (TOP AUDITED + ALL 686 REAL 2026 STEA ORGANIZATIONS) -->
  <section class="section-block" id="sec-ngos">
    <div class="section-head">
      <h2 data-i18n="s3_title">2. Järjestöavustusten rakenneanalyysi: STEA 2026 kaikki 686 järjestöä (273,91 milj. € / 1 288 päätöstä) ja OKM</h2>
      <p data-i18n="s3_sub">
        Vuoden 2026 virallisista STEA-avustuksista (273 912 000 € / 1 288 avustuspäätöstä 1 527 hakemuksesta) tasan <strong>212 203 929 € (77,5 %)</strong> on jatkuvia kohdennettuja <code>Ak</code>-toiminta-avustuksia (sisältäen sekä kriisi- ja auttamistyötä että ei-lakisääteistä lomatoimintaa), <strong>58 214 068 € (21,3 %)</strong> on järjestöjen perustoimintaan ja hallintoon myönnettäviä <code>Ay</code>-yleisavustuksia, ja <strong>3 494 003 € (1,3 %)</strong> on <code>C/B</code>-hanke- ja investointiavustuksia. Klikkaa mitä tahansa järjestökorttia tai riviä alla nähdäksesi järjestön kaikki vuoden 2026 avustuspäätökset.
      </p>
    </div>
    <div class="cards-grid" id="ngo-cards"></div>

    <div class="stea-table-wrap">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
        <div>
          <h3 style="font-size:19px;" data-i18n="stea_tbl_title">Virallinen STEA 2026 -kokoaineisto: Kaikki 686 avustusta saavaa järjestöä (Klikkaa otsikkoa lajitellaksesi tai riviä avataksesi)</h3>
          <p style="font-size:13.5px;color:var(--muted);" id="stea-count-sub"></p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button type="button" class="btn-secondary" onclick="exportFilteredSteaCsv()" data-i18n="stea_csv_btn">⬇ Vie suodatettu STEA-aineisto (.csv)</button>
          <a class="btn-primary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="stea_xlsx_btn">⬇ Lataa kaikki 686 järjestöä Excelissä (Välilehti 06)</a>
        </div>
      </div>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th class="sortable" onclick="sortSteaTable('ngo_name')"><span data-i18n="th_org">Järjestö (STEA 2026 virallinen rekisteri)</span> <span id="sort-stea-ngo_name"></span></th>
              <th class="sortable" onclick="sortSteaTable('granted_2026_eur')"><span data-i18n="th_tot">Myönnetty 2026 (€)</span> <span id="sort-stea-granted_2026_eur">▼</span></th>
              <th class="sortable" onclick="sortSteaTable('ak_general_2026_eur')"><span data-i18n="th_ak">Ak-toiminta-avustus (€)</span> <span id="sort-stea-ak_general_2026_eur"></span></th>
              <th class="sortable" onclick="sortSteaTable('ak_pct')"><span data-i18n="th_akpct">Ak-Osuus (%)</span> <span id="sort-stea-ak_pct"></span></th>
              <th class="sortable" onclick="sortSteaTable('targeted_2026_eur')"><span data-i18n="th_proj">Muut lajit Ay/C/B (€)</span> <span id="sort-stea-targeted_2026_eur"></span></th>
              <th class="sortable" onclick="sortSteaTable('decision_count_2026')"><span data-i18n="th_purp">Päätökset &amp; suurin avustuskohde (2026)</span> <span id="sort-stea-decision_count_2026"></span></th>
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
      <h2 data-i18n="s2_title">3. Kuusi valtion budjettikokonaisuutta, joista tunnistetaan 1,55–3,00 miljardin €/v sopeutuspotentiaali</h2>
      <p data-i18n="s2_sub">
        Klikkaa mitä tahansa budjettikorttia nähdäksesi selkokielellä, mitä kyseisiltä momenteilta karsitaan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.
      </p>
    </div>
    <div class="cards-grid" id="momentti-cards"></div>
  </section>

  <!-- SECTION 4: TUKIKONSORTIOT & MEKANISMI -->
  <section class="section-block" id="sec-rings">
    <div class="section-head">
      <h2 data-i18n="s1_title">4. Julkisten T&amp;K-tukien keskittyminen ekosysteemi- ja konsortioklustereihin (3 klusteria · 132,2 M€)</h2>
      <p data-i18n="s1_sub">
        Julkiset T&amp;K- ja puhtaan siirtymän investointituet keskittyvät maantieteellisiin ja temaattisiin innovaatioklustereihin (kuten Otaniemen Tekniikantie, biokuitu-/kiertotalouskonsortiot ja Keilasataman Veturi-ekosysteemi). Alla verrataan klusterien saamia tukia niiden 5 vuoden yhteisöverokertymään.
      </p>
    </div>
    <div class="flow-steps">
      <div class="flow-step clickable-card" onclick="openFlowModal(1)">
        <span class="flow-badge" data-i18n="f1_step">Vaihe 1 · Klikkaa</span>
        <h4 data-i18n="f1_title">Tukivaltuuksien kohdentuminen</h4>
        <p data-i18n="f1_desc">Valtio myöntää satoja miljoonia euroja kehittämis- ja investointiavustuksia ilman sitovaa jälkikäteistä verovasteseurantaa.</p>
      </div>
      <div class="flow-step clickable-card" onclick="openFlowModal(2)">
        <span class="flow-badge" data-i18n="f2_step">Vaihe 2 · Klikkaa</span>
        <h4 data-i18n="f2_title">Konsortio- ja ekosysteemirakenne</h4>
        <p data-i18n="f2_desc">Veturi-, RRF- ja EU-ohjelmissa tuki kanavoidaan laajoihin yritys- ja tutkimuskonsortioihin sekä ekosysteemihankkeisiin.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(3)">
        <span class="flow-badge" data-i18n="f3_step">Vaihe 3 · Tilinpäätös</span>
        <h4 data-i18n="f3_title">Avustusten kirjaus (KPL / IAS 20)</h4>
        <p data-i18n="f3_desc">Kehitysvaiheen yhtiö kirjaa avustukset kirjanpitolain mukaisesti liiketoiminnan muihin tuottoihin tai aktivoi kehittämismenoja.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(4)">
        <span class="flow-badge" data-i18n="f4_step">Vaihe 4 · Verovaste</span>
        <h4 data-i18n="f4_title">Kaupallistamisriski &amp; 0 € yhteisövero</h4>
        <p data-i18n="f4_desc">Mikäli pilottivaiheen teknologia ei skaalaudu kaupallisesti (esim. Infinited Fiber tai Woodio), yhteisöverovaste jää 0 euroon.</p>
      </div>
    </div>
    <h3 style="font-size:19px; margin: 22px 0 12px;" data-i18n="rings_heading">Klikkaa tunnistettua T&amp;K-klusteria lukeaksesi yhtiökohtaisen erittelyn:</h3>
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
    Perustuu 100 % julkisiin viranomaisrekistereihin: STEA 2026 (kaikki 686 järjestöä / 1 288 avustuspäätöstä), TEM Yritystukien tietopalvelu, Tutkiavustuksia.fi, Business Finland, Verohallinto &amp; PRH YTJ v3.
  </div>
  <div>
    <a href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download>Lataa 6-välilehtinen Excel (.xlsx)</a> ·
    <a href="https://github.com/libertaari-suomalainen/tukipalkkio-purku">Avoin lähdekoodi (GitHub)</a> ·
    <a href="https://libertaari-suomalainen.github.io/kartelli-tutka/">Tutkimus II: Julkiset hankinnat &amp; sidosyksiköt (38,7 mrd. €)</a>
  </div>
</footer>
"""
    html += f"""
<script>
const DATA = {payload_json};
let LANG = 'fi';
let CORP_SORT = {{ col: 'subsidy_received_eur', asc: false }};
let STEA_SORT = {{ col: 'granted_2026_eur', asc: false }};
let LAST_FILTERED_CORPS = [];
let LAST_FILTERED_STEA = [];

const fmtM = (n) => (n / 1e6).toLocaleString('fi-FI', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' milj. €';
const fmtCardM = (n) => {{
  const val = Number(n);
  if (!val || Math.abs(val) < 1) return '0 €';
  const m = val / 1e6;
  const digits = Math.abs(m) >= 100 ? 0 : 1;
  return m.toLocaleString('fi-FI', {{minimumFractionDigits: digits, maximumFractionDigits: digits}}) + ' M€';
}};
const fmtEUR = (n) => Math.round(n).toLocaleString('fi-FI') + ' €';
const escHtml = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const splitTitle = (raw) => {{
  const s = String(raw || '');
  const idx = s.indexOf(' (');
  if (idx === -1) return {{ main: s, sub: '' }};
  return {{
    main: s.slice(0, idx).trim(),
    sub: s.slice(idx + 2, s.endsWith(')') ? -1 : s.length).trim()
  }};
}};
const fmtCorpMomentti = (c) => {{
  if (!c || c.isBenchmark) return '0 €';
  if (c.nace_code === '50101' || c.nace_code === '50201') return '31.20.43';
  if (c.nace_code === '51100') return '31.20.20 / 32.30.42';
  const raw = String(c.vm_momentti || '').replace(/_/g, ' / ');
  if (raw === '30.10.40 / 32.60.40') return '32.20.43 / 32.60.40';
  return raw;
}};

const I18N = {{
  fi: {{
    brand_title: "Suomen Talousinstituutti · Julkisen Talouden Tutkimus",
    brand_sub: "Tutkimusraportti 2026 · 686 STEA-järjestöä (1 288 päätöstä) & 47 suuryritystä ja tukikohdetta",
    nav_sister: "Tutkimus II: Julkiset hankinnat (38,7 mrd. €) →",
    nav_xlsx: "⬇ Lataa Excel-aineisto (.xlsx)",
    hero_kicker: "VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % OIKEA VIRANOMAISDATA",
    hero_title: "Suomen yritys- ja järjestötukien vaikuttavuus- ja verovasteanalyysi (11,5 mrd. €/v)",
    hero_lead: "Suomen julkinen sektori kohdentaa vuosittain noin 11,5 miljardia euroa suoriin yritystukiin, energia- ja maataloustukiin, toimialakohtaisiin verotukiin sekä järjestöavustuksiin. Kun viralliset tukipäätökset (TEM Yritystukien tietopalvelu, Business Finland, ELY, Traficom sekä STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon julkisiin yhteisöverotietoihin ja PRH:n yritysrekisteriin, tunnistetaan <strong>1,55–3,00 miljardin euron vuotuinen sopeutuspotentiaali</strong> ilman leikkauksia kouluihin, sairaaloihin, poliisiin tai maanpuolustukseen.",
    summary_box_title: "Mitä tämä tutkimus ja ladattava Excel (.xlsx) sisältävät?",
    summary_box_body: "Julkaisu sisältää <strong>kaikki 686 STEA-järjestöä (kaikki 1 288 virallista avustuspäätöstä 1 527 hakemuksesta vuodelle 2026 = 273,91 milj. €: 212,20 M€ kohdennettuja Ak-toiminta-avustuksia, 58,21 M€ Ay-yleisavustuksia ja 3,49 M€ C/B-hankeavustuksia)</strong> sekä <strong>47 suomalaista yritystukien saajaa ja nettoveronmaksajaverrokkia</strong> (mm. Veturi- ja T&K-vientiyhtiöt <em>Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Patria, Kempower, RELEX</em>; teollisuus- ja varustamotuet <em>UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Finnlines, Tallink Silja, Finnair</em>; T&K-/pilottivaiheen tukikohteet <em>Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio</em>; sekä tuettomat yhteisöveronmaksajat <em>OP Ryhmä, Supercell, Sampo, Kesko, Elisa, Nokian Renkaat, Puuilo, Harvia, Marimekko, Olvi</em>).",
    kpi1_lbl: "Julkiset tuet & verotuet yhteensä",
    kpi1_sub: "Suorat yritys-, energia-, maatalous- ja järjestötuet (~7,5 mrd. €) sekä toimialaverotuet (~4,0 mrd. €)",
    click_explain: "Klikkaa: Mistä 11,5 mrd. € koostuu? →",
    kpi2_lbl: "Tunnistettu sopeutuspotentiaali",
    kpi2_sub: "Rakenteellinen säästö 6 tukikokonaisuudesta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin",
    click_explain2: "Klikkaa: Miten säästö syntyy? →",
    kpi3_lbl: "T&K-ekosysteemi- ja konsortioklusterit",
    kpi3_sub: "Otaniemen puhtaan siirtymän keskittymä, biokuitu-/kiertotalouskonsortiot ja Keilasataman Veturi-ekosysteemi",
    click_explain3: "Klikkaa: Katso 3 T&K-klusteria →",
    kpi4_lbl: "STEA 2026 Jatkuvat Ak- ja Ay-avustukset",
    kpi4_sub: "686 järjestöä (273,9 M€): 212,2 M€ (77,5 %) jatkuvaa Ak-toimintatukea + 58,2 M€ (21,3 %) Ay-yleisavustusta",
    click_explain4: "Klikkaa: Katso STEA 2026 -erittely →",
    lbl_search: "Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 47 suuryritystä & tukikohdetta)",
    lbl_scenario: "Valitse Kehysriihi 2027 -tukiuudistuksen laajuus",
    opt_base: "Perustaso: Karsitaan matalan lisäisyyden tuet, lomajärjestöt ja Ay-yleisavustuksia (1,55 mrd. €/v)",
    opt_med: "Rakenneuudistus: Puolitetaan säilyttävät elinkeino- ja yleisavustukset (2,25 mrd. €/v)",
    opt_max: "Laaja markkinauudistus: Poistetaan kilpailua vääristävät yritystuet (3,00 mrd. €/v)",
    chip_lbl: "Pikavalinnat:",
    chip_all: "Näytä kaikki",
    s4_title: "1. Yritystukien verovasteanalyysi: T&K-pilottivaiheen yhtiöt, säilyttävät suuryritystuet ja nettoveronmaksajat (47 yhtiötä)",
    s4_sub: "Klikkaa mitä tahansa yhtiökorttia tai alla olevan kokonaistaulukon riviä nähdäksesi vertailun: kuinka paljon yhtiö sai julkista tukea (Business Finland, TEM, ELY, sähköistämistuki tai merenkulun miehistötuki), mikä oli yhteisöverokertymä 5 vuodessa ja miltä tulos näyttää ennen julkisia tukia.",
    corp_tbl_title: "Yritysaineiston kokonaistaulukko: Kaikki 47 yhtiötä & veronmaksajaverrokkia (Klikkaa otsikkoa lajitellaksesi tai riviä avataksesi)",
    corp_csv_btn: "⬇ Vie suodatettu yritysaineisto (.csv)",
    corp_xlsx_btn: "⬇ Lataa Excel (Välilehti 02)",
    th_c_name: "Yritys & Y-tunnus",
    th_c_tol: "TOL",
    th_c_mom: "Momentti",
    th_c_sub: "Julkinen tuki 5v (€)",
    th_c_tax: "Yhteisövero 5v (€)",
    th_c_roi: "Vero-ROI",
    th_c_cls: "Luokitus",
    th_c_cut: "Esitetty säästö (€)",
    s3_title: "2. Järjestöavustusten rakenneanalyysi: STEA 2026 kaikki 686 järjestöä (273,91 milj. € / 1 288 päätöstä) ja OKM",
    s3_sub: "Vuoden 2026 virallisista STEA-avustuksista (273 912 000 € / 1 288 avustuspäätöstä 1 527 hakemuksesta) tasan <strong>212 203 929 € (77,5 %)</strong> on jatkuvia kohdennettuja <code>Ak</code>-toiminta-avustuksia, <strong>58 214 068 € (21,3 %)</strong> on järjestöjen perustoimintaan myönnettäviä <code>Ay</code>-yleisavustuksia ja <strong>3 494 003 € (1,3 %)</strong> on <code>C/B</code>-hankeavustuksia. Klikkaa mitä tahansa järjestökorttia tai riviä alla nähdäksesi järjestön kaikki vuoden 2026 avustuspäätökset.",
    stea_tbl_title: "Virallinen STEA 2026 -kokoaineisto: Kaikki 686 avustusta saavaa järjestöä (Klikkaa otsikkoa lajitellaksesi tai riviä avataksesi)",
    stea_csv_btn: "⬇ Vie suodatettu STEA-aineisto (.csv)",
    stea_xlsx_btn: "⬇ Lataa kaikki 686 järjestöä Excelissä (Välilehti 06)",
    th_org: "Järjestö (STEA 2026 virallinen rekisteri)",
    th_tot: "Myönnetty 2026 (€)",
    th_ak: "Ak-toiminta-avustus (€)",
    th_akpct: "Ak-Osuus (%)",
    th_proj: "Muut lajit Ay/C/B (€)",
    th_purp: "Päätökset & suurin avustuskohde (2026)",
    s2_title: "3. Kuusi valtion budjettikokonaisuutta, joista tunnistetaan 1,55–3,00 miljardin €/v sopeutuspotentiaali",
    s2_sub: "Klikkaa mitä tahansa budjettikorttia nähdäksesi selkokielellä, mitä kyseisiltä momenteilta karsitaan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.",
    s1_title: "4. Julkisten T&K-tukien keskittyminen ekosysteemi- ja konsortioklustereihin (3 klusteria · 132,2 M€)",
    s1_sub: "Julkiset T&K- ja puhtaan siirtymän investointituet keskittyvät maantieteellisiin ja temaattisiin innovaatioklustereihin (kuten Otaniemen Tekniikantie, biokuitu-/kiertotalouskonsortiot ja Keilasataman Veturi-ekosysteemi).",
    f1_step: "Vaihe 1 · Klikkaa",
    f1_title: "Tukivaltuuksien kohdentuminen",
    f1_desc: "Valtio myöntää satoja miljoonia euroja kehittämis- ja investointiavustuksia ilman sitovaa jälkikäteistä verovasteseurantaa.",
    f2_step: "Vaihe 2 · Klikkaa",
    f2_title: "Konsortio- ja ekosysteemirakenne",
    f2_desc: "Veturi-, RRF- ja EU-ohjelmissa tuki kanavoidaan laajoihin yritys- ja tutkimuskonsortioihin sekä ekosysteemihankkeisiin.",
    f3_step: "Vaihe 3 · Tilinpäätös",
    f3_title: "Avustusten kirjaus (KPL / IAS 20)",
    f3_desc: "Kehitysvaiheen yhtiö kirjaa avustukset kirjanpitolain mukaisesti liiketoiminnan muihin tuottoihin tai aktivoi kehittämismenoja.",
    f4_step: "Vaihe 4 · Verovaste",
    f4_title: "Kaupallistamisriski & 0 € yhteisövero",
    f4_desc: "Mikäli pilottivaiheen teknologia ei skaalaudu kaupallisesti (esim. Infinited Fiber tai Woodio), yhteisöverovaste jää 0 euroon.",
    rings_heading: "Klikkaa tunnistettua T&K-klusteria lukeaksesi yhtiökohtaisen erittelyn:"
  }},
  en: {{
    brand_title: "Finnish Economic Institute (STI) · Public Finance Audit",
    brand_sub: "2026 Empirical Report · All 686 STEA NGOs (1,288 Decisions) & 47 Real Finnish Corporations",
    nav_sister: "Study II: Public Procurement (€38.7B) →",
    nav_xlsx: "⬇ Download Full Excel Dataset (.xlsx)",
    hero_kicker: "PUBLIC FINANCE · RESEARCH REPORT 2026 · 100% REAL STATUTORY DATA",
    hero_title: "Empirical Tax-Return & Effectiveness Analysis of Finland's Corporate & NGO Subsidies (€11.5B/yr)",
    hero_lead: "Finland allocates approximately €11.5 billion per year across direct corporate grants, agricultural/energy subsidies, sectoral tax expenditures, and NGO funding. By linking official grant decisions (TEM Corporate Subsidy Database, Business Finland, ELY, Traficom, and all 686 STEA 2026 NGOs) to Tax Administration corporate tax records and PRH registry addresses, this study identifies <strong>€1.55B–€3.00B/year</strong> in structural savings without cutting frontline schools, hospitals, or police.",
    summary_box_title: "What Does This Report & Excel Workbook (.xlsx) Contain?",
    summary_box_body: "This dataset contains <strong>all 686 real 2026 STEA grant-receiving NGOs (all 1,288 funded decisions out of 1,527 applications = €273.91M: €212.20M targeted Ak operating grants, €58.21M Ay general grants, and €3.49M C/B project grants)</strong> plus <strong>47 real Finnish corporate grant recipients and net-taxpayer benchmarks</strong> (Veturi & R&D exporters <em>Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Patria, Kempower, RELEX</em>; industrial & maritime subsidies <em>UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Finnlines, Tallink Silja, Finnair</em>; R&D/pilot ventures <em>Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio</em>; and unsubsidized corporate taxpayers <em>OP Financial Group, Supercell, Sampo, Kesko, Elisa, Nokian Tyres, Puuilo, Harvia, Marimekko, Olvi</em>).",
    kpi1_lbl: "Total Public Subsidies & Tax Aid",
    kpi1_sub: "Direct corporate, energy, agri & NGO grants (~€7.5B) plus sectoral tax expenditures (~€4.0B)",
    click_explain: "Click: What makes up the €11.5B? →",
    kpi2_lbl: "Identified Structural Savings",
    kpi2_sub: "Structural reform across 6 budget groups with zero cuts to schools, hospitals, or police",
    click_explain2: "Click: How are savings achieved? →",
    kpi3_lbl: "R&D Ecosystem & Consortium Clusters",
    kpi3_sub: "Otaniemi clean-transition hub, biofiber/circular consortia, and Keilasatama Veturi ecosystem",
    click_explain3: "Click: Inspect the 3 R&D clusters →",
    kpi4_lbl: "STEA 2026 Continuous Ak & Ay Grants",
    kpi4_sub: "Across all 686 NGOs (€273.9M): €212.2M (77.5%) targeted Ak operating grants + €58.2M (21.3%) Ay general grants",
    click_explain4: "Click: Inspect STEA 2026 breakdown →",
    lbl_search: "Search any company, NGO, Business ID, or topic (686 NGOs + 47 major corporations & grant targets)",
    lbl_scenario: "Choose 2027 Budget Reform Scope",
    opt_base: "Baseline: Cut low-additionality subsidies, holiday associations & Ay general grants (€1.55B/yr)",
    opt_med: "Structural Reform: Halve low-return business & general subsidies (€2.25B/yr)",
    opt_max: "Broad Market Reform: Phase out market-distorting subsidies (€3.00B/yr)",
    chip_lbl: "Quick filters:",
    chip_all: "Show all",
    s4_title: "1. Corporate Tax-Return Analysis: R&D Pilot Ventures, Incumbent Subsidies & Net Taxpayers (47 Corporations)",
    s4_sub: "Click any company card or row in the full table below for a plain-English comparison: how much public subsidy it received, how its 5-year corporate income tax performed, and what its earnings look like before subsidies.",
    corp_tbl_title: "Full Corporate Registry Table: All 47 Corporations & Net Taxpayer Benchmarks (Click Header to Sort or Row to Open)",
    corp_csv_btn: "⬇ Export Filtered Corporate CSV (.csv)",
    corp_xlsx_btn: "⬇ Download Excel (Tab 02)",
    th_c_name: "Company & Business ID",
    th_c_tol: "NACE",
    th_c_mom: "Budget Line",
    th_c_sub: "5-Yr Subsidy (€)",
    th_c_tax: "5-Yr Corp Tax (€)",
    th_c_roi: "Tax ROI",
    th_c_cls: "Classification",
    th_c_cut: "Proposed Cut (€)",
    s3_title: "2. NGO Grant Structure Analysis: All 686 Real 2026 STEA Organizations (€273.91M / 1,288 Decisions) & Ministry Grants",
    s3_sub: "Out of all official 2026 STEA grants (€273,912,000 across 1,288 funded decisions out of 1,527 applications), <strong>€212,203,929 (77.5%)</strong> is distributed as continuous targeted <code>Ak</code> operating grants, <strong>€58,214,068 (21.3%)</strong> as <code>Ay</code> general organizational grants, and <strong>€3,494,003 (1.3%)</strong> as <code>C/B</code> project/investment grants. Click any card or row below to inspect all 2026 decisions for that NGO.",
    stea_tbl_title: "Official 2026 STEA Full Registry: All 686 Funded Organizations (Click Header to Sort or Row to Open)",
    stea_csv_btn: "⬇ Export Filtered STEA CSV (.csv)",
    stea_xlsx_btn: "⬇ Download All 686 NGOs in Excel (Tab 06)",
    th_org: "Organization (Official 2026 STEA Registry)",
    th_tot: "Granted 2026 (€)",
    th_ak: "Ak Operating Grant (€)",
    th_akpct: "Ak Share (%)",
    th_proj: "Other Ay/C/B Grants (€)",
    th_purp: "Decisions & Primary Grant Target (2026)",
    s2_title: "3. Six State Budget Groups With €1.55B–€3.00B/Year Structural Savings Potential",
    s2_sub: "Click any budget card to see in plain English what is reformed in that budget line, which real companies or NGOs are included, and why frontline services are untouched.",
    s1_title: "4. Concentration of Public R&D Subsidies in Ecosystem & Consortium Hubs (3 Clusters · €132.2M)",
    s1_sub: "Public R&D and clean-transition subsidies concentrate into regional and thematic innovation hubs (such as Tekniikantie in Otaniemi, biofiber/circular consortia, and Keilasatama in Espoo).",
    f1_step: "Step 1 · Click",
    f1_title: "Grant Allocation",
    f1_desc: "The state awards hundreds of millions in R&D and investment grants without binding ex-post corporate tax tracking.",
    f2_step: "Step 2 · Click",
    f2_title: "Consortium & Ecosystem Structure",
    f2_desc: "In Veturi, RRF, and EU programs, public funding is channeled into multi-company research consortia and ecosystem projects.",
    f3_step: "Step 3 · Accounting",
    f3_title: "Statutory Grant Booking (IAS 20 / KPL)",
    f3_desc: "Development-stage ventures lawfully book grants into Other Operating Income or capitalize development expenses under IAS 20 / KPL.",
    f4_step: "Step 4 · Tax Return",
    f4_title: "Commercialization Risk & €0 Corp. Tax",
    f4_desc: "If pilot-scale technology fails to scale commercially (e.g. Infinited Fiber or Woodio), the 5-year corporate income tax return remains €0.",
    rings_heading: "Click any detected R&D cluster to inspect the companies and figures:"
  }}
}};

const MOMENTTI_META = [
  {{
    code: "32.20.40",
    fi_name: "Business Finlandin T&K- ja innovaatioavustukset",
    en_name: "Business Finland Corporate R&D & Innovation Grants",
    current: 470000000,
    base_cut: 211500000,
    fi_short: "Kohdennetaan T&K-rahoitus (2026 myöntämisvaltuus 637,4 M€, arviomääräraha ~470 M€) korkean verovasteen vienti- ja Veturi-hankkeisiin (Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Kempower). Karsitaan tukia kohteilta, joilla ei ole 5v yhteisöverovastetta (Infinited Fiber 12,4 M€, Solar Foods 18,2 M€, Spinnova 14,8 M€, Meyer Turku 54 M€, Woodio 4,2 M€).",
    en_short: "Focus R&D funding (2026 authorization €637.4M, cash budget ~€470M) on high-tax-return exporters and Veturi programs (Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Kempower); phase out grants to €0-tax recipients (Infinited Fiber €12.4M, Solar Foods €18.2M, Spinnova €14.8M, Meyer Turku €54M, Woodio €4.2M).",
    fi_deep: "Valtion talousarviossa 2026 momentin 32.20.40 myöntämisvaltuus on 637,4 milj. € ja vuotuinen maksatusmääräraha noin 470 milj. €. Aineistomme (47 suuryritystä ja tukikohdetta) osoittaa selkeän eron: vakiintuneet vienti- ja Veturi-yhtiöt (Nokia Oyj, KONE Oyj, Orion Oyj, Wärtsilä Oyj Abp, Konecranes Oyj, Vaisala Oyj, Ponsse Oyj, Patria Oyj, Kempower Oyj, RELEX Oy) muuttavat T&K-panokset vahvaksi yhteisöverokertymäksi Suomeen, kun taas pitkittyneen pilottivaiheen hankkeet (Infinited Fiber Company Oy 12,4 M€ -> pilottituotannon sopeutus ja 0 € yhteisöveroa, Spinnova Oyj 14,8 M€ -> 0 € yhteisöveroa, Solar Foods Oyj 18,2 M€ -> 0 € yhteisöveroa, Sulapac Oy 5,4 M€ -> 0 € yhteisöveroa, Woodio Oy 4,2 M€ -> yrityssaneeraus/konkurssi ja 0 € yhteisöveroa) eivät ole tuottaneet tarkastelujaksolla yhteisöveroa.",
    en_deep: "In the 2026 State Budget, line 32.20.40 carries a €637.4M authorization and ~€470M annual cash outlay. Established exporters and Veturi flagships (Nokia, KONE, Orion, Wärtsilä, Konecranes, Vaisala, Ponsse, Patria, Kempower, RELEX) generate strong domestic corporate income tax returns, whereas prolonged pilot-stage ventures (Infinited Fiber €12.4M -> €0 tax, Spinnova €14.8M -> €0 tax, Solar Foods €18.2M -> €0 tax, Woodio €4.2M -> €0 tax) have generated €0 in corporate income tax over the 5-year observation window."
  }},
  {{
    code: "32.20.83",
    fi_name: "Lainat tutkimus- ja innovaatiotoimintaan (BF)",
    en_name: "Business Finland R&D & Innovation Soft Loans",
    current: 180000000,
    base_cut: 90000000,
    fi_short: "Tiukennetaan vakuudettomien tuotekehityslainojen ehtoja ja yksityisen pääoman vastinrahoitusvaatimusta.",
    en_short: "Tighten terms and private co-financing requirements for unsecured R&D soft loans.",
    fi_deep: "Valtio myöntää momentilta 32.20.83 (Lainat tutkimus- ja innovaatiotoimintaan) vuosittain noin 157–180 miljoonaa euroa vakuudettomia tuotekehityslainoja. Mikäli tuettu kehityshanke ei johda kaupallisesti kannattavaan liiketoimintaan, lainapääomaa voidaan jättää perimättä valtion luottotappioksi.",
    en_deep: "Under budget line 32.20.83, the state issues €157M–€180M/year in unsecured R&D loans that carry credit-loss risk for taxpayers when pilot projects fail to commercialize."
  }},
  {{
    code: "31.20.43 / 32.30.42",
    fi_name: "Varustamoiden miehistötuet (LVM) & ELY-kehittämisavustukset (TEM)",
    en_name: "Maritime Crew Subsidies (31.20.43) & ELY Regional Grants (32.30.42)",
    current: 340000000,
    base_cut: 174000000,
    fi_short: "Tarkastellaan varustamoiden miehistötukia (LVM 31.20.43: ~89 M€/v; TEM 2020–2025 suorat tuet Viking Line 129 M€, Finnlines 93 M€, Tallink Silja 71 M€) sekä yrityskohtaisia ELY- ja liikennetukia (TEM 32.30.42, mm. Betolar 6,9 M€, Finnair 85 M€).",
    en_short: "Reform maritime crew subsidies (LVM 31.20.43: ~€89M/yr; TEM 2020–2025 direct aid Viking Line €129M, Finnlines €93M, Tallink Silja €71M) and firm-specific ELY/transport grants (Betolar €6.9M, Finnair €85M).",
    fi_deep: "Valtio maksaa LVM:n momentilta 31.20.43 (Meriliikenteessä käytettävien alusten kilpailukyvyn parantaminen) vuosittain noin 89 miljoonaa euroa miehistökustannusten palautustukea varustamoille (TEM Yritystukien tietopalvelun 2020–2025 kumulatiiviset suorat tuet: Viking Line Abp 129 M€, Finnlines Oyj 93 M€ ja Tallink Silja Oy 71 M€) sekä TEM:n luvusta 32.30 (32.30.42 Yritysten kehittämishankkeiden tukeminen) alueellisia yritystukia, joiden vaikuttavuutta ja kilpailuvaikutuksia VATT on suositellut arvioimaan kriittisesti.",
    en_deep: "Around €89M/year flows under LVM line 31.20.43 to shipping lines (TEM 2020–2025 cumulative direct subsidies: Viking Line Abp €129M, Finnlines Oyj €93M, Tallink Silja Oy €71M) alongside regional ELY business-development grants under TEM chapter 32.30 (32.30.42)."
  }},
  {{
    code: "33.90.50",
    fi_name: "STEA-järjestöavustukset (Ay-yleisavustukset 58,2 M€, Ak-toimintatuet 212,2 M€ & lomajärjestöt)",
    en_name: "STEA NGO Grants (€58.2M Ay General Grants, €212.2M Ak Operating Grants & Holidays)",
    current: 410000000,
    base_cut: 209000000,
    fi_short: "STEA:n vuoden 2026 kaikista 686 järjestöstä (273,91 M€) tasan 212,20 M€ (77,5 %) on jatkuvaa kohdennettua Ak-toiminta-avustusta ja 58,21 M€ (21,3 %) Ay-yleisavustusta. Sopeutus kohdistetaan Ay-yleisavustuksiin, kattojärjestörakenteisiin ja ei-lakisääteiseen lomatoimintaan (Loma ja Terveys 2,68 M€, Hyvinvointilomat 2,10 M€) suojaten kriisityön.",
    en_short: "Across all 686 STEA 2026 NGOs (€273.91M), €212.20M (77.5%) is Ak targeted operating grants and €58.21M (21.3%) is Ay general grants. Savings target Ay general overhead, umbrella advocacy, and holiday associations (€4.79M/yr) while protecting crisis work.",
    fi_deep: "Julkaisu sisältää STEA:n koko vuoden 2026 virallisen avustusrekisterin (kaikki 686 järjestöä ja kaikki 1 288 myönteistä avustuspäätöstä 1 527 hakemuksesta = 273 912 000 € STM:n luvusta 33.90). Virallisessa avustuslajittelussa 212 203 929 € (77,5 %) on jatkuvia kohdennettuja Ak-toiminta-avustuksia, 58 214 068 € (21,3 %) on järjestöjen yleishyödylliseen perustoimintaan ja hallintoon myönnettäviä Ay-yleisavustuksia, ja 3 494 003 € (1,3 %) on C/B-hanke- ja investointiavustuksia. Rakenteellinen säästö kohdistetaan Ay-yleisavustuksiin, valtakunnallisiin katto- ja vaikuttamisjärjestöihin (esim. SOSTE ry 2,81 M€), ei-lakisääteisiin lomajärjestöihin (Loma ja Terveys ry 2,68 M€, Hyvinvointilomat ry 2,10 M€) sekä sote-palvelutuottajien yleisavustusten ja kilpailutetun palvelumyynnin rajanvetoon—suojaten samalla matalan kynnyksen kriisi- ja auttamistyön (kuten MIELI ry:n Kriisipuhelimen, MLL:n auttavat puhelimet ja turvakotityön).",
    en_deep: "Our full dataset of all 686 STEA 2026 organizations (all 1,288 funded decisions out of 1,527 applications = €273,912,000 under STM chapter 33.90) distinguishes continuous targeted Ak operating grants (€212,203,929 / 77.5%), Ay general organizational grants (€58,214,068 / 21.3%), and C/B project grants (€3,494,003 / 1.3%). Structural savings focus on Ay general grants, national umbrella advocacy (SOSTE €2.81M), non-statutory holiday associations (€4.79M), and competitive neutrality in commercial Sote service groups—while protecting frontline crisis helplines and domestic-violence shelters."
  }},
  {{
    code: "29.80.50 / 29.90.50 / 29.91.50",
    fi_name: "OKM:n kulttuuri-, liikunta- ja nuorisoalan kattojärjestöavustukset",
    en_name: "Ministry of Education Cultural, Sports & Youth Umbrella Grants",
    current: 420000000,
    base_cut: 168000000,
    fi_short: "Karsitaan valtakunnallisten katto- ja edunvalvontajärjestöjen (kuten Allianssi ry 1,95 M€/v momentilta 29.91.50) yleisavustuksia ja monikanavarahoituksen päällekkäisyyksiä. Suojataan paikallinen lasten ja nuorten seuratoiminta.",
    en_short: "Reduce national umbrella & advocacy grants (e.g. Allianssi ry €1.95M/yr under 29.91.50) across OKM chapters 29.80, 29.90 & 29.91 while protecting local youth clubs.",
    fi_deep: "Opetus- ja kulttuuriministeriön luvuista 29.80 (taide ja kulttuuri), 29.90 (liikunta) ja 29.91 (nuorisotyö, mm. 29.91.50) jaetaan satoja miljoonia euroja järjestöavustuksia, joista merkittävä osa ohjautuu valtakunnallisille katto-, liitto- ja edunvalvontajärjestöille. Kun keskushallinnon yleisavustuksia karsitaan, säästyy 168 miljoonaa euroa vuodessa koskematta paikallisiin lasten ja nuorten urheiluseuroihin.",
    en_deep: "Reducing central-office and national umbrella advocacy subsidies across OKM chapters 29.80, 29.90, and 29.91 saves €168M/year without touching local youth sports clubs."
  }},
  {{
    code: "32.20.43 / 32.60.40 / 30.20.40",
    fi_name: "Suurteollisuuden sähköistämistuki, energiatuet ja kansalliset säilytystuet",
    en_name: "Large Industrial Electrification, Energy & National Incumbent Subsidies",
    current: 1740000000,
    base_cut: 696000000,
    fi_short: "Puretaan vakiintuneiden suuryritysten (TEM 2020–2025: UPM-Kymmene 140 M€, Stora Enso 96 M€, Neste 68,5 M€, Outokumpu 62 M€, SSAB 48 M€, Metsä Fibre 44 M€, Fortum 34 M€, Kemira 19,5 M€) matalan lisäisyyden sähköistämis-, energia- ja säilytystuet.",
    en_short: "Phase out low-additionality incumbent energy and electrification subsidies to profitable large corporations (UPM €140M, Stora Enso €96M, Neste €68.5M, Outokumpu €62M, SSAB €48M, Metsä Fibre €44M, Fortum €34M, Kemira €19.5M).",
    fi_deep: "VATT:n ja Etlan yritystukitutkimusten mukaisesti energiaintensiivisen teollisuuden sähköistämistuki (32.20.43 / 32.40.43), energiatuet (32.60.40), kansalliset maataloustuet (30.20.40) ja teollisuuden verotuet ohjautuvat valtaosin vakiintuneille suuryrityksille hankkeisiin ja tuotantolaitoksiin, joiden investointipäätöksiin tuella on matala lisäisyysvaikutus (kuolleen painon tuki). Kun näitä säilyttäviä tukia karsitaan, säästyy perustasolla 696 miljoonaa euroa vuodessa.",
    en_deep: "Economic research (VATT & Etla) shows that industrial electrification subsidies (32.20.43), energy aid (32.60.40), and national production subsidies flow predominantly to large incumbents with low additionality. Phasing them out saves €696M/year in the baseline scenario."
  }}
];

function setHashQuietly(hashStr) {{
  if (history.replaceState) {{
    history.replaceState(null, '', '#' + hashStr);
  }} else {{
    window.location.hash = hashStr;
  }}
}}

function copyDirectLink(btn) {{
  navigator.clipboard.writeText(window.location.href);
  const orig = btn.textContent;
  btn.textContent = LANG === 'fi' ? '✓ Suora linkki kopioitu!' : '✓ Direct Link Copied!';
  setTimeout(() => {{ btn.textContent = orig; }}, 1800);
}}

function downloadTextFile(filename, textContent) {{
  const blob = new Blob([textContent], {{ type: 'text/plain;charset=utf-8' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}

function openModalHtml(title, subtitle, sectionsHtml, hashId) {{
  if (hashId) setHashQuietly(hashId);
  const fi = LANG === 'fi';
  document.getElementById('modal-content').innerHTML = `
    <h2>${{title}}</h2>
    <div class="modal-sub">${{subtitle}}</div>
    <div class="modal-toolbar">
      <button type="button" class="btn-secondary" onclick="copyDirectLink(this)">${{fi ? '🔗 Kopioi suora linkki tähän kohteeseen' : '🔗 Copy Direct Link to This Item'}}</button>
      <button type="button" class="btn-secondary" onclick="window.print()">${{fi ? '🖨 Tulosta / Tallenna PDF' : '🖨 Print / Save as PDF'}}</button>
    </div>
    ${{sectionsHtml}}
  `;
  document.getElementById('detail-modal').classList.add('open');
}}

function closeModal() {{
  document.getElementById('detail-modal').classList.remove('open');
  if (history.replaceState) {{
    history.replaceState(null, '', window.location.pathname + window.location.search);
  }}
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
          ? "Suomen julkinen sektori jakaa joka vuosi noin 11,5 miljardia euroa suoria yritystukia, maatalous- ja energiatukia, järjestöavustuksia sekä toimialakohtaisia verotukia (lähteet: Valtion talousarvio 2026, TEM yritystukitilasto, VM verotukikartoitus, VATT & Tilastokeskus). Tukia myöntävät kymmenet eri virastot (Business Finland, ELY-keskukset, Traficom, STEA, OKM, MMM ja TEM) tarkistamatta, syntyykö tuesta lisäarvoa tai verotuloja."
          : "Finland's public sector distributes ~€11.5 billion every year across direct corporate grants, energy/agricultural subsidies, NGO payouts, and sectoral tax expenditures (State Budget 2026, TEM, VM & VATT)."}}</p>
      </div>
      <div class="modal-section">
        <h4>${{fi ? "Pääerät valtion talousarviossa, kunnissa ja verotuissa" : "Major Components of the €11.5B Pool"}}</h4>
        <ul>
          <li><strong>${{fi ? "Suorat yritystuet, T&K-avustukset/lainat, merenkulkutuet ja ELY:" : "Direct Corporate, R&D, Maritime & ELY Subsidies:"}}</strong> ~1,8 mrd. €/v</li>
          <li><strong>${{fi ? "Järjestö- ja säätiöavustukset (STEA 273,9 M€ / luku 33.90, OKM, kunnat):" : "NGO & Foundation Grants (STEA, OKM, Municipalities):"}}</strong> ~2,2 mrd. €/v</li>
          <li><strong>${{fi ? "Teollisuuden sähköistämis-/energiatuet sekä maatalouden kansalliset ja EU-tuet:" : "Industrial Energy/Electrification & Agricultural Subsidies:"}}</strong> ~3,5 mrd. €/v</li>
          <li><strong>${{fi ? "Toimialakohtaiset elinkeino- ja energiaverotuet (VM verotukikartoitus):" : "Sectoral Corporate & Energy Tax Expenditures (VM):"}}</strong> ~4,0 mrd. €/v</li>
        </ul>
      </div>`,
      'kpi-total'
    );
  }} else if (key === 'savings_pool') {{
    openModalHtml(
      fi ? "Miten 1,55–3,00 miljardia euroa säästetään ilman leikkauksia peruspalveluihin?" : "How €1.55B–€3.00B Is Saved Without Touching Frontline Services",
      fi ? "Suomen Talousinstituutin kehysriihimalli 2027 (6 valtion budjettikokonaisuutta)" : "STI 2027 State Budget Reform Schedule (6 Budget Groups)",
      `<div class="modal-section">
        <h4>${{fi ? "Tarkka säästöerittely (Perustaso 1,55 mrd. €/v)" : "Exact Savings Breakdown (Baseline €1.55B/yr)"}}</h4>
        <ul>
          <li><strong>Momentti 32.20.40 (Business Finland T&amp;K-avustukset):</strong> -211,50 milj. €/v</li>
          <li><strong>Momentti 32.20.83 (Lainat tutkimus- ja innovaatiotoimintaan):</strong> -90,00 milj. €/v</li>
          <li><strong>Momentit 31.20.43 / 32.30.42 (Varustamoiden miehistötuet &amp; ELY-yritystuet):</strong> -174,00 milj. €/v</li>
          <li><strong>Momentti 33.90.50 (STEA jatkuvat Ak-toimintatuet &amp; lomajärjestöt):</strong> -209,00 milj. €/v</li>
          <li><strong>Momentit 29.80.50 / 29.90.50 / 29.91.50 (OKM katto- ja yleisavustukset):</strong> -168,00 milj. €/v</li>
          <li><strong>Momentit 32.20.43 / 32.60.40 / 30.20.40 (Suurteollisuuden sähköistämis-, energia- ja säilytystuet):</strong> -696,00 milj. €/v</li>
        </ul>
      </div>`,
      'kpi-savings'
    );
  }} else if (key === 'rings_pool') {{
    const listHtml = DATA.rings.map(r => `<li><strong>${{r.shared_address_or_agent}} (${{r.ring_signature}}):</strong> ${{r.entity_count}} ${{fi ? "yhtiötä" : "companies"}} (${{r.company_names.join(' · ')}}) — ${{fi ? "nostettu julkinen tuki" : "public grants"}} <strong>${{fmtM(r.total_subsidy_eur)}}</strong>, ${{fi ? "5v yhteisöverokertymä" : "5-yr corporate tax"}} <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong>.</li>`).join('');
    openModalHtml(
      fi ? "Kolme oikeaa tuki- ja konsortioklusteria (132,2 milj. € tukia)" : "Three Real Grant & Consortium Clusters (€132.2M in Grants)",
      fi ? "PRH YTJ -osoitteiden, Business Finland Veturi-konsortioiden ja verotietojen yhdistelmä" : "Cross-Join of PRH Registry Addresses, Consortium Programs & Tax Records",
      `<div class="modal-section">
        <h4>${{fi ? "Tunnistetut klusterit aineistossa" : "Audited Clusters in the Dataset"}}</h4>
        <ul>${{listHtml}}</ul>
      </div>`,
      'kpi-rings'
    );
  }} else if (key === 'ngo_pool') {{
    openModalHtml(
      fi ? "Mitä STEA:n vuoden 2026 kaikki 686 järjestöä todistavat?" : "What All 686 Real 2026 STEA Organizations Prove",
      fi ? "Lähde: avustukset.stea.fi · 1 288 virallista avustuspäätöstä (1 527 hakemuksesta) vuodelle 2026 = 273 912 000 €" : "Source: avustukset.stea.fi · 1,288 Funded Decisions (out of 1,527 Applications) = €273,912,000",
      `<div class="modal-section">
        <h4>${{fi ? "Kiistaton rekisteritodiste (Lataa myös Excelin välilehti 06)" : "Hard Registry Proof (Also in Excel Tab 06)"}}</h4>
        <ul>
          <li><strong>${{fi ? "Kaikki STEA-avustukset 2026 yhteensä:" : "Total 2026 STEA Grants:"}}</strong> 273 912 000 € (686 järjestöä, 1 288 myönteistä avustuspäätöstä 1 527 hakemuksesta)</li>
          <li><strong>${{fi ? "Siitä jatkuvia kohdennettuja Ak-toiminta-avustuksia:" : "Of Which Continuous Targeted Ak Operating Grants:"}}</strong> <strong style="color:var(--red)">212 203 929 € (77,5 %)</strong></li>
          <li><strong>${{fi ? "Siitä järjestöjen perustoimintaan myönnettäviä Ay-yleisavustuksia:" : "Of Which Ay General Organizational Grants:"}}</strong> <strong>58 214 068 € (21,3 %)</strong></li>
          <li><strong>${{fi ? "Siitä C/B-hanke- ja investointiavustuksia:" : "Of Which C/B Project & Investment Grants:"}}</strong> 3 494 003 € (1,3 %)</li>
          <li><strong>${{fi ? "Tuetut lomajärjestöt (100 % Ak, STM/VM-karsintakohde):" : "Taxpayer-Subsidized Holiday Associations (100% Ak):"}}</strong> Loma ja Terveys ry (2 684 710 €) + Hyvinvointilomat ry (2 103 947 €) = <strong>4 788 657 €/v</strong></li>
          <li><strong>${{fi ? "Suurimmat STEA-avustusten saajat 2026:" : "Largest STEA Grant Recipients 2026:"}}</strong> MIELI ry (5,00 M€ Ak + 1,02 M€ Ay), EHYT ry (2,87 M€ Ak + 1,26 M€ Ay/C), Suomen Punainen Risti (3,03 M€ Ak + 0,52 M€ C), Mielenterveyden Keskusliitto ry (1,84 M€ Ak + 1,16 M€ Ay), Näkövammaisten liitto ry (2,25 M€ Ak + 0,73 M€ Ay), A-klinikkasäätiö (1,96 M€ Ak + 0,91 M€ Ay/C), SOSTE ry (1,62 M€ Ak + 1,18 M€ Ay).</li>
        </ul>
      </div>`,
      'kpi-ngos'
    );
  }}
}}

function openFlowModal(step) {{
  const fi = LANG === 'fi';
  const steps = {{
    1: {{
      t: fi ? "Vaihe 1: Tukivaltuuksien kohdentuminen ilman verovasteseurantaa" : "Step 1: Grant Allocation Without Tax-Return Tracking",
      s: fi ? "11,50 miljardia euroa vuodessa eri hallinnonalojen kautta" : "€11.50 Billion/Year Across Multiple Ministries and Agencies",
      b: fi ? "Valtion budjetista ja verotuista kohdennetaan vuosittain noin 11,5 miljardia euroa yritys-, energia-, maatalous- ja järjestötukiin. Tukiviranomaisilla ei ole yhtenäistä velvoitetta verrata myönnettyjä tukia Verohallinnon toteutuneeseen yhteisöverokertymään."
            : "€11.5B/year is distributed across grant agencies and tax expenditures without systematic ex-post comparison against realized corporate income tax returns."
    }},
    2: {{
      t: fi ? "Vaihe 2: Konsortio- ja ekosysteemirakenne" : "Step 2: Consortium and Ecosystem Structure",
      s: fi ? "Esimerkkinä Business Finland Veturi-, RRF- ja EU-konsortiot" : "Business Finland Veturi, RRF & EU Grant Consortia",
      b: fi ? "Julkisissa T&K- ja vihreän siirtymän ohjelmissa rahoitus kanavoidaan usein laajoihin yritys- ja tutkimuskonsortioihin sekä ekosysteemiklustereihin, joiden hakemuksia ja yhteishankkeita koordinoivat myös erikoistuneet innovaatiokonsulttiyhtiöt."
            : "In public R&D and clean-transition programs, funding is channeled into multi-company consortia and regional innovation hubs."
    }},
    3: {{
      t: fi ? "Vaihe 3: Avustusten tilinpäätöskäsittely (KPL / IAS 20)" : "Step 3: Statutory Accounting of Public Grants (IAS 20 / KPL)",
      s: fi ? "Liiketoiminnan muut tuotot ja kehittämismenojen aktivointi" : "Other Operating Income and R&D Capitalizations",
      b: fi ? "Kirjanpitolain (1336/1997) ja IFRS-standardien (IAS 20) mukaisesti julkiset kehittämisavustukset kirjataan Liiketoiminnan muihin tuottoihin tai vähennetään aktivoiduista kehittämismenoista. Siksi kehitysvaiheen yhtiön omavaraista kassavirtaa arvioitaessa julkiset avustuserät oikaistaan erikseen."
            : "Under the Finnish Accounting Act (KPL) and IAS 20, public grants are lawfully booked into Other Operating Income or netted against capitalized R&D. Adjusting for these items reveals standalone commercial cash flow."
    }},
    4: {{
      t: fi ? "Vaihe 4: Kaupallistamisriski ja yhteisöverovaste" : "Step 4: Commercialization Risk & Corporate Tax Return",
      s: fi ? "Esimerkkinä pilottivaiheen sopeutukset vs. vahvat yhteisöveronmaksajat" : "Case Example: Pilot Wind-Downs vs. Major Corporate Taxpayers",
      b: fi ? "Mikäli tuettu teknologia ei skaalaudu kaupallisesti (esim. Infinited Fiber Company Oy:n pilottituotannon sopeutus 12,4 M€ tukien jälkeen tai Woodio Oy:n yrityssaneeraus/konkurssimenettely 4,2 M€ tukien jälkeen), yhteisöverokertymä jää 0 euroon. Samaan aikaan suomalaiset suuret yhteisöveronmaksajat (kuten OP Ryhmä >1 450 M€, Supercell Oy >850 M€, Kesko Oyj >550 M€, KONE Oyj >485 M€, Nokia Oyj >420 M€, Sampo Oyj >350 M€ ja Orion Oyj >340 M€) rahoittavat julkisen talouden peruspalveluita."
            : "When grant-supported pilot ventures fail to scale commercially (e.g. Infinited Fiber Company Oy or Woodio Oy), corporate income tax return remains €0, whereas major net taxpayers generate billions in domestic corporate tax revenue."
    }}
  }};
  const item = steps[step];
  openModalHtml(item.t, item.s, `<div class="modal-section"><h4>${{fi ? "Analyysi" : "Analysis"}}</h4><p>${{item.b}}</p></div>`, `flow-${{step}}`);
}}

function openRingModal(idx) {{
  const r = DATA.rings[idx];
  if (!r) return;
  const fi = LANG === 'fi';
  const members = DATA.corporate_evals.filter(c => r.y_tunnus_list.includes(c.y_tunnus));
  const memberRows = members.map(m => `<li><strong>${{m.company_name}} (${{m.y_tunnus}}):</strong> ${{fi ? "Myönnetty tuki" : "Grant received"}} <strong>${{fmtEUR(m.subsidy_received_eur)}}</strong> (${{m.grant_agency.replace('_',' ')}}) · ${{fi ? "5v yhteisöveron muutos:" : "5-yr corporate tax delta:"}} <strong>${{fmtEUR(m.five_yr_tax_delta_eur)}}</strong>.</li>`).join('');
  openModalHtml(
    `${{r.shared_address_or_agent}} (${{r.ring_signature}})`,
    fi ? `T&K-ekosysteemi- ja konsortioklusteri · ${{r.entity_count}} oikeaa yhtiötä` : `R&D Ecosystem & Consortium Cluster · ${{r.entity_count}} Real Companies`,
    `<div class="modal-section">
      <h4>${{fi ? "Klusterin kokonaiskuva" : "Cluster Summary"}}</h4>
      <p>${{fi
        ? `Nämä ${{r.entity_count}} yhtiötä sijoittuvat samaan maantieteelliseen T&K-keskittymään tai konsortio-ohjelmaan (<strong>${{r.shared_address_or_agent}}</strong>). Yhtiöille on myönnetty yhteensä <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> julkisia avustuksia ja lainoja. Viiden vuoden tarkastelujaksolla klusterin yhteenlaskettu yhteisöveron muutos oli <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong>.`
        : `These ${{r.entity_count}} companies belong to the same R&D address hub or consortium program (<strong>${{r.shared_address_or_agent}}</strong>), receiving <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> in public subsidies with <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong> in 5-year corporate tax change.`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Klusterin yhtiöt (PRH YTJ Y-tunnus)" : "Companies in This Cluster"}}</h4>
      <ul>${{memberRows}}</ul>
    </div>`,
    `ring-${{idx}}`
  );
}}

function openMomenttiModal(idx) {{
  const m = MOMENTTI_META[idx];
  if (!m) return;
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');
  const save = Math.min(m.current, m.base_cut * mult);
  const fi = LANG === 'fi';
  openModalHtml(
    `${{fi ? m.fi_name : m.en_name}} (${{m.code}})`,
    fi ? `Nykyinen määräraha: ${{fmtM(m.current)}} · Tunnistettu vuosisäästö: -${{fmtM(save)}}` : `Current Budget: ${{fmtM(m.current)}} · Identified Annual Saving: -${{fmtM(save)}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Mihin sopeutus kohdistuu ja mihin viranomaisaineistoon se perustuu?" : "What Is Reformed and What Empirical Evidence Supports It?"}}</h4>
      <p>${{fi ? m.fi_deep : m.en_deep}}</p>
    </div>`,
    `momentti-${{idx}}`
  );
}}

function openNgoModal(idx) {{
  const n = DATA.ngo_evals[idx];
  if (!n) return;
  const fi = LANG === 'fi';
  const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
  const steaMatch = DATA.stea_all.find(s => s.y_tunnus === n.y_tunnus);
  const allPurposesHtml = steaMatch && steaMatch.top_purposes && steaMatch.top_purposes.length
    ? `<div class="modal-section">
        <h4>${{fi ? `Kaikki vuoden 2026 viralliset STEA-avustuspäätökset (${{steaMatch.decision_count_2026}} kpl)` : `All Official 2026 STEA Grant Decisions (${{steaMatch.decision_count_2026}})`}}</h4>
        <ul>${{steaMatch.top_purposes.map(p => `<li>${{escHtml(p)}}</li>`).join('')}}</ul>
      </div>`
    : '';
  openModalHtml(
    `${{n.ngo_name}} (Y-tunnus: ${{n.y_tunnus}})`,
    `${{n.grant_source}} (Momentti ${{n.vm_momentti}}) · ${{fi ? "Avustuslajit" : "Grant Classes"}}: ${{n.grant_class_code}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Järjestön julkisen rahoituksen rakenne (STEA 2026 / OKM)" : "Public Funding Structure (STEA 2026 / OKM)"}}</h4>
      <p>${{fi
        ? `<strong>${{n.ngo_name}}</strong> saa vuonna 2026 suoraa valtionavustusta yhteensä <strong>${{fmtEUR(n.annual_grant_eur)}}</strong>. Tästä yleisavustusten (<code>Ay</code>), kattojärjestötoiminnan tai ei-lakisääteisen karsintakohteen osuus on <strong>${{n.overhead_and_lobbying_pct}} %</strong> (${{fmtEUR(n.hq_admin_comms_lobbying_spend_eur)}}) ja kohdennetun kenttä-/toiminta-avustuksen (<code>Ak</code>) osuus on <strong>${{fmtEUR(n.direct_frontline_aid_spend_eur)}}</strong>.${{n.public_sote_procurement_sales_eur > 0 ? ` Lisäksi järjestökonserni tuottaa hyvinvointialueille ja julkiselle sektorille ostopalveluita arviolta <strong>${{fmtEUR(n.public_sote_procurement_sales_eur)}}</strong>/v.` : ''}}`
        : `<strong>${{n.ngo_name}}</strong> receives <strong>${{fmtEUR(n.annual_grant_eur)}}</strong>/year in 2026 direct grants, of which <strong>${{n.overhead_and_lobbying_pct}}%</strong> (${{fmtEUR(n.hq_admin_comms_lobbying_spend_eur)}}) represents Ay general grants, umbrella operations, or non-statutory holiday subsidies, and <strong>${{fmtEUR(n.direct_frontline_aid_spend_eur)}}</strong> represents targeted frontline Ak operating grants.${{n.public_sote_procurement_sales_eur > 0 ? ` The group also provides <strong>${{fmtEUR(n.public_sote_procurement_sales_eur)}}</strong>/year in Sote services.` : ''}}`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Tarkat luvut (2026)" : "Exact 2026 Figures"}}</h4>
      <ul>
        <li><strong>${{fi ? "Vuosiavustus 2026 (STEA/OKM):" : "2026 Annual Grant:"}}</strong> ${{fmtEUR(n.annual_grant_eur)}}</li>
        <li><strong>${{fi ? "Kohdennettu kenttä- ja kriisityö (suojattu osuus):" : "Targeted Frontline Work (Protected):"}}</strong> ${{fmtEUR(n.direct_frontline_aid_spend_eur)}}</li>
        <li><strong>${{fi ? "Yleisavustus (Ay) / kattojärjestö- / lomatoimintaosuus:" : "Ay General Grant / Umbrella / Holiday Share:"}}</strong> ${{fmtEUR(n.hq_admin_comms_lobbying_spend_eur)}} (${{n.overhead_and_lobbying_pct}} %)</li>
        <li><strong>${{fi ? "Julkinen sote- ja palvelumyynti:" : "Public Sote Service Sales:"}}</strong> ${{fmtEUR(n.public_sote_procurement_sales_eur)}}</li>
        <li><strong>${{fi ? "Avustuserittely:" : "Grant Breakdown:"}}</strong> ${{(n.political_board_insiders || []).join(', ') || 'Kohdennettu kenttätyö'}}</li>
        <li><strong>${{fi ? "Tarkasteltava Ay- / kohdesäästö:" : "Evaluated Ay / Non-Statutory Saving:"}}</strong> <strong style="color:${{isCut ? 'var(--red)' : 'var(--accent-dark)'}}">${{fmtEUR(n.recoverable_cut_eur)}}</strong></li>
      </ul>
    </div>
    ${{allPurposesHtml}}`,
    `ngo-${{n.y_tunnus}}`
  );
}}

function openSteaRawModal(orgId) {{
  const org = DATA.stea_all.find(x => x.org_id === orgId);
  if (!org) return;
  const fi = LANG === 'fi';
  const akPct = org.granted_2026_eur > 0 ? ((org.ak_general_2026_eur / org.granted_2026_eur) * 100).toFixed(1) : '0.0';
  const purpHtml = (org.top_purposes || []).map(p => `<li>${{escHtml(p)}}</li>`).join('');
  const yStr = org.y_tunnus ? ` · Y-tunnus: ${{org.y_tunnus}}` : '';
  const foiText = `ASIAKIRJA- JA TILINTARKASTUSPYYNTÖ (JULKISUUSLAKI 621/1999 13 § & VALTIONAVUSTUSLAKI 688/2001)\nVastaanottaja: Sosiaali- ja terveysjärjestöjen avustuskeskus (STEA) / Sosiaali- ja terveysministeriön kirjaamo (kirjaamo.stm@gov.fi)\nKohde: ${{org.ngo_name}} (STEA Organisaatio-ID: ${{org.org_id}}${{yStr}})\nVuoden 2026 myönnetty STEA-avustus: ${{fmtEUR(org.granted_2026_eur)}} (josta jatkuvaa kohdennettua Ak-toiminta-avustusta ${{fmtEUR(org.ak_general_2026_eur)}}, eli ${{akPct}} %, ja Ay/C/B-avustuksia ${{fmtEUR(org.targeted_2026_eur)}})\n\nPyydän julkisuuslain (621/1999) 9 §:n ja 13 §:n nojalla toimittamaan sähköisesti ja maksutta (16.3 §):\n1. ${{org.ngo_name}} -järjestölle vuodelle 2026 myönnettyjen avustuspäätösten (${{org.decision_count_2026}} kpl, yhteensä ${{fmtEUR(org.granted_2026_eur)}}) julkiset talousarvioerittelyt sekä hallinto- ja yleiskustannusten osuuden.\n2. Viimeisimmän STEA:lle toimitetun julkisen vuosiselvityksen valtionavustuksen käytöstä ja vaikuttavuudesta.\n\nPyydän toimittamaan asiakirjat sähköpostitse 14 vuorokauden lakisääteisessä määräajassa (JulkL 14.4 §).`;

  openModalHtml(
    `${{org.ngo_name}} (STEA ID: ${{org.org_id}}${{yStr}})`,
    fi ? `Virallinen STEA 2026 -avustuspäätösrekisteri · Kaikki ${{org.decision_count_2026}} myönteistä avustuspäätöstä vuonna 2026` : `Official 2026 STEA Grant Registry · All ${{org.decision_count_2026}} Funded Decisions in 2026`,
    `<div class="modal-section">
      <h4>${{fi ? "Vuoden 2026 viralliset STEA-avustusluvut" : "Official 2026 STEA Grant Breakdown"}}</h4>
      <ul>
        <li><strong>${{fi ? "Haettu STEA-avustus 2026:" : "Requested 2026 Grant:"}}</strong> ${{fmtEUR(org.requested_2026_eur)}}</li>
        <li><strong>${{fi ? "Myönnetty STEA-avustus 2026 yhteensä:" : "Total Granted 2026:"}}</strong> <strong>${{fmtEUR(org.granted_2026_eur)}}</strong></li>
        <li><strong>${{fi ? "Siitä jatkuva kohdennettu Ak-toiminta-avustus:" : "Of Which Continuous Targeted Ak Operating Grant:"}}</strong> <strong style="color:var(--red)">${{fmtEUR(org.ak_general_2026_eur)}} (${{akPct}} %)</strong></li>
        <li><strong>${{fi ? "Siitä muut avustuslajit (Ay-yleisavustukset sekä C/B-hanke- ja investointiavustukset):" : "Of Which Other Categories (Ay General + C/B Project/Investment Grants):"}}</strong> <strong style="color:var(--accent-dark)">${{fmtEUR(org.targeted_2026_eur)}}</strong></li>
      </ul>
    </div>
    <div class="modal-section">
      <h4>${{fi ? `Kaikki viralliset avustuskohteet vuonna 2026 (${{(org.top_purposes || []).length}} päätöstä)` : `All Official 2026 Grant Decisions (${{(org.top_purposes || []).length}} Decisions)`}}</h4>
      <ul>${{purpHtml}}</ul>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Valmis 0,00 € Julkisuuslaki-tietopyyntö STEA:lle / STM:lle" : "Turnkey €0.00 FOI Audit Request to STEA / Ministry"}}</h4>
      <div class="legal-box" id="stea-foi-box">${{escHtml(foiText)}}</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button type="button" class="btn-primary" onclick="navigator.clipboard.writeText(document.getElementById('stea-foi-box').textContent);this.textContent='✓ Tietopyyntö kopioitu!';">${{fi ? '📋 Kopioi tietopyyntö' : '📋 Copy FOI Request'}}</button>
        <button type="button" class="btn-secondary" onclick="downloadTextFile('STEA_Tietopyynto_${{org.org_id}}.txt', document.getElementById('stea-foi-box').textContent)">${{fi ? '⬇ Lataa .txt-asiakirja' : '⬇ Download .txt'}}</button>
        <a class="btn-secondary" href="mailto:kirjaamo.stm@gov.fi?subject=${{encodeURIComponent('Julkisuuslain mukainen tietopyyntö: ' + org.ngo_name + ' (STEA ' + org.org_id + ')')}}&body=${{encodeURIComponent(foiText)}}">${{fi ? '✉️ Avaa sähköpostissa (kirjaamo.stm@gov.fi)' : '✉️ Open in Email Client'}}</a>
      </div>
    </div>`,
    `stea-${{org.org_id}}`
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
          ? `<strong>${{b.company_name}}</strong> on esimerkki markkinaehtoisesta suomalaisesta yrityksestä, joka ei ole nostanut merkittäviä suoria elinkeino- tai teollisuustukia ja on maksanut Suomeen <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> yhteisöveroa 5 vuoden tarkastelujaksolla (Verohallinnon julkiset yhteisöverotiedot).`
          : `<strong>${{b.company_name}}</strong> is a market-driven Finnish taxpayer benchmark that paid <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> in Finnish corporate income taxes over 5 years without relying on industrial subsidies.`}}</p>
      </div>`,
      `corp-${{b.y_tunnus}}`
    );
    return;
  }}
  if (!c) return;

  const momDisp = fmtCorpMomentti(c);
  const foiCorpText = `JULKISUUSLAIN MUKAINEN TIETOPYYNTÖ YRITYSTUISTA JA VAIKUTTAVUUSARVIOINNISTA (JULKL 621/1999 13 §)\nVastaanottaja: Business Finland / Työ- ja elinkeinoministeriön kirjaamo (kirjaamo.tem@gov.fi)\nKohdeyritys: ${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})\nBudjettimomentti: ${{momDisp}} · Tarkasteltu julkinen tuki (5v): ${{fmtEUR(c.subsidy_received_eur)}} · 5v yhteisöverovaste: ${{fmtEUR(c.five_yr_tax_delta_eur)}}\n\nPyydän julkisuuslain (621/1999) 9 §:n ja 13 §:n nojalla toimittamaan sähköisesti ja maksutta (16.3 §):\n1. Yhtiölle ${{c.company_name}} (${{c.y_tunnus}}) myönnettyjen julkisten avustusten ja lainojen tukipäätökset, maksatuserittelyt sekä hakemusvaiheen vaikuttavuus- ja verotuottoennusteet.\n2. Viranomaisen jälkiarvioinnin (ex-post) siitä, miten myönnetty julkinen tuki on täyttänyt valtionavustuslain (688/2001) 7 §:n mukaiset tuloksellisuus- ja markkinavääristymättömyysedellytykset.\n\nPyydän toimittamaan asiakirjat sähköpostitse 14 vuorokauden lakisääteisessä määräajassa (JulkL 14.4 §).`;

  openModalHtml(
    `${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})`,
    `${{c.grant_agency.replace('_',' ')}} (Momentti ${{momDisp}}) · TOL ${{c.nace_code}} · ${{c.postal_or_co_address}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Julkisen tuen ja yhteisöverovasteen vertailu (5 v)" : "Public Subsidy vs. Corporate Tax Response (5-Yr Comparison)"}}</h4>
      <ul>
        <li><strong>${{fi ? "Myönnetty/maksettu julkinen yritystuki (5v):" : "Public Subsidy Received (5-Yr):"}}</strong> <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong></li>
        <li><strong>${{fi ? "Yhtiön yhteisöverokertymä / -muutos (5v):" : "Recipient 5-Yr Corporate Tax / Delta:"}}</strong> <strong>${{fmtEUR(c.five_yr_tax_delta_eur)}}</strong></li>
        <li><strong>${{fi ? "Tuettoman toimialaverrokin verovaste (5v):" : "Matched Unsubsidized Peer 5-Yr Tax Benchmark:"}}</strong> ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}</li>
        <li><strong>${{fi ? "Laskennallinen DiD Vero-ROI:" : "Calculated DiD Tax ROI:"}}</strong> <strong>${{c.causal_did_roi.toFixed(2)}}x</strong></li>
        <li><strong>${{fi ? "Tarkasteltava tukisopeutus:" : "Evaluated Subsidy Adjustment:"}}</strong> <strong style="color:${{c.recommended_cut_eur > 0 ? 'var(--red)' : 'var(--accent-dark)'}}">${{fmtEUR(c.recommended_cut_eur)}}</strong></li>
      </ul>
    </div>
    ${{qoe ? `<div class="modal-section">
      <h4>${{fi ? "Tilinpäätöksen avustuserien ja T&K-aktivointien oikaisu (IFRS / KPL)" : "Financial Statement Grant & R&D Capitalization Adjustment (IFRS / KPL)"}}</h4>
      <p>${{fi
        ? `Raportoitu liikevaihto: <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> · Raportoitu käyttökate (EBITDA): <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong>. Kirjanpitolain ja IFRS-standardien (IAS 20) mukaisesti julkiset avustukset (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) kirjataan Liiketoiminnan muihin tuottoihin ja kehittämismenoja aktivoidaan taseeseen. Kun nämä erät oikaistaan, omavarainen käyttökate ennen julkisia tukia on <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`
        : `Reported revenue: <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> · Reported EBITDA: <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong>. Adjusting for statutory IAS 20 / KPL public grants booked in Other Operating Income (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) and capitalized development payroll yields a standalone commercial EBITDA before subsidies of <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`}}</p>
    </div>` : ''}}
    <div class="modal-section">
      <h4>${{fi ? "Valmis 0,00 € Julkisuuslaki-tietopyyntö (TEM / Business Finland)" : "Turnkey €0.00 FOI Audit Request (TEM / Business Finland)"}}</h4>
      <div class="legal-box" id="corp-foi-box">${{escHtml(foiCorpText)}}</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button type="button" class="btn-primary" onclick="navigator.clipboard.writeText(document.getElementById('corp-foi-box').textContent);this.textContent='✓ Tietopyyntö kopioitu!';">${{fi ? '📋 Kopioi tietopyyntö' : '📋 Copy FOI Request'}}</button>
        <button type="button" class="btn-secondary" onclick="downloadTextFile('Yritystuki_Tietopyynto_${{c.y_tunnus}}.txt', document.getElementById('corp-foi-box').textContent)">${{fi ? '⬇ Lataa .txt-asiakirja' : '⬇ Download .txt'}}</button>
        <a class="btn-secondary" href="mailto:kirjaamo.tem@gov.fi?subject=${{encodeURIComponent('Julkisuuslain mukainen tietopyyntö yritystuista: ' + c.y_tunnus)}}&body=${{encodeURIComponent(foiCorpText)}}">${{fi ? '✉️ Avaa sähköpostissa (kirjaamo.tem@gov.fi)' : '✉️ Open in Email Client'}}</a>
      </div>
    </div>`,
    `corp-${{c.y_tunnus}}`
  );
}}

function sortCorpTable(col) {{
  if (CORP_SORT.col === col) {{
    CORP_SORT.asc = !CORP_SORT.asc;
  }} else {{
    CORP_SORT.col = col;
    CORP_SORT.asc = (col === 'company_name' || col === 'nace_code' || col === 'vm_momentti' || col === 'classification');
  }}
  renderAll();
}}

function sortSteaTable(col) {{
  if (STEA_SORT.col === col) {{
    STEA_SORT.asc = !STEA_SORT.asc;
  }} else {{
    STEA_SORT.col = col;
    STEA_SORT.asc = (col === 'ngo_name');
  }}
  renderAll();
}}

function exportFilteredCorpsCsv() {{
  const headers = ['Sija', 'Y-tunnus', 'Yritys', 'TOL', 'Osoite', 'Rahoittaja', 'Momentti', 'Julkinen_tuki_5v_EUR', 'Yhteisovero_5v_EUR', 'DiD_Vero_ROI', 'Luokitus', 'Esitetty_saasto_EUR'];
  const lines = [headers.join(';')];
  LAST_FILTERED_CORPS.forEach((c, idx) => {{
    lines.push([
      idx + 1,
      `"${{c.y_tunnus}}"`,
      `"${{String(c.company_name).replace(/"/g, '""')}}"`,
      `"${{c.nace_code}}"`,
      `"${{String(c.postal_or_co_address || '').replace(/"/g, '""')}}"`,
      `"${{c.grant_agency}}"`,
      `"${{fmtCorpMomentti(c)}}"`,
      Math.round(c.subsidy_received_eur),
      Math.round(c.five_yr_tax_delta_eur),
      c.causal_did_roi,
      `"${{c.classification}}"`,
      Math.round(c.recommended_cut_eur)
    ].join(';'));
  }});
  const blob = new Blob(['\\uFEFF' + lines.join('\\r\\n')], {{ type: 'text/csv;charset=utf-8;' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'STI_Yritystuet_2026_Suodatettu.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}

function exportFilteredSteaCsv() {{
  const headers = ['Sija', 'STEA_ID', 'Y_tunnus', 'Jarjesto', 'Myonnetty_2026_EUR', 'Jatkuva_Ak_avustus_2026_EUR', 'Ak_Osuus_Pct', 'Muut_Ay_C_B_2026_EUR', 'Paatosten_lkm_2026', 'Kaikki_2026_avustuskohteet'];
  const lines = [headers.join(';')];
  LAST_FILTERED_STEA.forEach((o, idx) => {{
    const akPct = o.granted_2026_eur > 0 ? ((o.ak_general_2026_eur / o.granted_2026_eur) * 100).toFixed(1) : '0.0';
    lines.push([
      idx + 1,
      o.org_id,
      `"${{o.y_tunnus || ''}}"`,
      `"${{String(o.ngo_name).replace(/"/g, '""')}}"`,
      Math.round(o.granted_2026_eur),
      Math.round(o.ak_general_2026_eur),
      akPct,
      Math.round(o.targeted_2026_eur),
      o.decision_count_2026,
      `"${{String((o.top_purposes || []).join(' | ')).replace(/"/g, '""')}}"`,
    ].join(';'));
  }});
  const blob = new Blob(['\\uFEFF' + lines.join('\\r\\n')], {{ type: 'text/csv;charset=utf-8;' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'STI_STEA_2026_Kaikki_Jarjestot.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}

function setSearch(val) {{
  const box = document.getElementById('search-box');
  box.value = val;
  document.querySelectorAll('.chip').forEach(btn => {{
    const txt = btn.textContent.trim().toLowerCase();
    btn.classList.toggle('active', (val === '' && (txt.includes('kaikki') || txt.includes('all'))) || (val !== '' && txt.includes(val.split('|')[0].trim().toLowerCase())));
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
  const safeQ = escHtml(rawQ);
  const qTerms = rawQ.toLowerCase().split('|').map(s => s.trim()).filter(Boolean);
  const matchQuery = (hay) => qTerms.length === 0 || qTerms.some(t => hay.includes(t));
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');
  const fi = LANG === 'fi';

  // Update KPI total savings based on scenario
  const totalBaseSave = MOMENTTI_META.reduce((acc, m) => acc + Math.min(m.current, m.base_cut * mult), 0);
  document.getElementById('kpi-save-val').textContent = (totalBaseSave / 1e9).toLocaleString('fi-FI', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + (fi ? ' mrd. €/v' : 'B €/yr');

  // 1. Corporate Cards & Sortable Table (All 37 Real Subsidy Recipients + 10 Real Unsubsidized Benchmarks = 47 Real Companies)
  const allCorps = [
    ...DATA.corporate_evals.map(c => ({{ ...c, isBenchmark: false }})),
    ...DATA.benchmarks.map(b => ({{
      y_tunnus: b.y_tunnus,
      company_name: b.company_name,
      nace_code: b.nace_code,
      postal_or_co_address: b.postal_address,
      grant_agency: fi ? 'NETTOVERONMAKSAJAVERROKKI' : 'NET TAXPAYER BENCHMARK',
      vm_momentti: '0 €',
      subsidy_received_eur: 0,
      five_yr_tax_delta_eur: b.five_yr_corporate_tax_paid_eur,
      matched_peer_five_yr_tax_delta_eur: b.five_yr_corporate_tax_paid_eur,
      causal_did_roi: 99.9,
      classification: 'BENCHMARK_TAXPAYER',
      recommended_cut_eur: 0,
      isBenchmark: true
    }}))
  ];

  const filteredCorps = allCorps.filter(c => {{
    const hay = `${{c.company_name}} ${{c.y_tunnus}} ${{c.grant_agency}} ${{c.postal_or_co_address}} ${{c.nace_code}} ${{c.vm_momentti}} ${{fmtCorpMomentti(c)}} ${{c.classification}}`.toLowerCase();
    return matchQuery(hay);
  }});

  let corpHtml = '';
  filteredCorps.forEach(c => {{
    const isZombie = c.classification === 'BLACKLIST_ZOMBIE';
    const isDead = c.classification === 'DEADWEIGHT_CROWD_OUT' || c.classification === 'LOW_YIELD_REVIEW';
    const accent = isZombie ? 'red-accent' : (isDead ? 'amber-accent' : 'green-accent');
    const badge = isZombie
      ? `<span class="badge badge-red">${{fi ? 'Nollavero · Leikataan 100 %' : 'Zero-Tax · Cut 100%'}}</span>`
      : (isDead ? `<span class="badge badge-amber">${{fi ? 'Säilyttävä tuki' : 'Deadweight Subsidy'}}</span>`
                : `<span class="badge badge-green">${{c.isBenchmark ? (fi ? 'Nettoveronmaksaja' : 'Net Taxpayer Benchmark') : (fi ? 'Vahva verotuotto' : 'High Tax Return')}}</span>`);

    const tParts = splitTitle(c.company_name);
    const subText = tParts.sub || (c.isBenchmark ? (fi ? 'Markkinaehtoinen veronmaksajaverrokki' : 'Market Taxpayer Benchmark') : c.grant_agency.replace(/_/g, ' '));
    const momClean = fmtCorpMomentti(c);
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
      <span>${{fi ? `Ei yritysosumia haulle ”${{safeQ}}”. Katso löytyneet järjestöt alla olevasta osiosta 2 tai tyhjennä haku.` : `No corporate matches for "${{safeQ}}". Check Section 2 below for matching NGOs or clear search.`}}</span>
      <button type="button" class="btn-secondary" onclick="setSearch('')">${{fi ? 'Näytä kaikki 47 yhtiötä' : 'Show all 47 corporations'}}</button>
    </div>`;
  }}
  document.getElementById('corp-cards').innerHTML = corpHtml;

  // Sort & Render Corporate Table
  const sortedCorps = [...filteredCorps].sort((a, b) => {{
    const va = a[CORP_SORT.col];
    const vb = b[CORP_SORT.col];
    let cmp = 0;
    if (typeof va === 'number' && typeof vb === 'number') cmp = va - vb;
    else cmp = String(va || '').localeCompare(String(vb || ''), 'fi');
    return CORP_SORT.asc ? cmp : -cmp;
  }});
  LAST_FILTERED_CORPS = sortedCorps;

  ['company_name', 'nace_code', 'vm_momentti', 'subsidy_received_eur', 'five_yr_tax_delta_eur', 'causal_did_roi', 'classification', 'recommended_cut_eur'].forEach(col => {{
    const el = document.getElementById('sort-corp-' + col);
    if (el) el.textContent = CORP_SORT.col === col ? (CORP_SORT.asc ? '▲' : '▼') : '';
  }});

  const sumCorpSub = sortedCorps.reduce((a, b) => a + b.subsidy_received_eur, 0);
  const sumCorpCut = sortedCorps.reduce((a, b) => a + b.recommended_cut_eur, 0);
  document.getElementById('corp-count-sub').textContent = fi
    ? `Näytetään ${{sortedCorps.length}} / ${{allCorps.length}} yhtiötä · Tarkastellut tuet yht. ${{fmtEUR(sumCorpSub)}} · Esitetty leikkaus yht. ${{fmtEUR(sumCorpCut)}}`
    : `Showing ${{sortedCorps.length}} / ${{allCorps.length}} corporations · Audited subsidies ${{fmtEUR(sumCorpSub)}} · Proposed cuts ${{fmtEUR(sumCorpCut)}}`;

  const corpTbody = document.getElementById('corp-all-tbody');
  if (sortedCorps.length === 0) {{
    corpTbody.innerHTML = `<tr><td colspan="9" style="text-align:center;padding:18px;color:var(--muted);">${{fi ? `Ei yritysosumia haulle ”${{safeQ}}”.` : `No corporations matching "${{safeQ}}".`}}</td></tr>`;
  }} else {{
    corpTbody.innerHTML = sortedCorps.map((c, idx) => {{
      const tParts = splitTitle(c.company_name);
      const isZombie = c.classification === 'BLACKLIST_ZOMBIE';
      const isDead = c.classification === 'DEADWEIGHT_CROWD_OUT';
      const clsBadge = isZombie
        ? `<span class="badge badge-red">${{fi ? 'Nollavero (Leikataan)' : 'Zero-Tax'}}</span>`
        : (isDead ? `<span class="badge badge-amber">${{fi ? 'Säilyttävä tuki' : 'Deadweight'}}</span>`
                  : `<span class="badge badge-green">${{c.isBenchmark ? (fi ? 'Nettoveronmaksaja' : 'Benchmark') : (fi ? 'Posit. ulkoisvaikutus' : 'Keep R&D')}}</span>`);
      const roiStr = c.isBenchmark ? (fi ? 'Veronmaksaja' : 'Taxpayer') : `${{c.causal_did_roi.toFixed(2)}}x`;
      return `<tr class="clickable-row" onclick="openCorpModal('${{c.y_tunnus}}')">
        <td>${{idx + 1}}</td>
        <td><strong>${{escHtml(tParts.main)}}</strong><br/><span style="font-size:11.5px;color:var(--muted);">Y: ${{c.y_tunnus}}</span></td>
        <td>${{c.nace_code}}</td>
        <td>${{fmtCorpMomentti(c)}}</td>
        <td><strong>${{fmtEUR(c.subsidy_received_eur)}}</strong></td>
        <td style="color:${{c.five_yr_tax_delta_eur > 0 ? 'var(--accent-dark)' : 'var(--red)'}};font-weight:600;">${{fmtEUR(c.five_yr_tax_delta_eur)}}</td>
        <td>${{roiStr}}</td>
        <td>${{clsBadge}}</td>
        <td style="color:${{c.recommended_cut_eur > 0 ? 'var(--red)' : 'var(--muted)'}};font-weight:700;">${{c.recommended_cut_eur > 0 ? '-' + fmtEUR(c.recommended_cut_eur) : '0 €'}}</td>
      </tr>`;
    }}).join('');
  }}

  // 2. NGO Story Cards + All 686 Real 2026 STEA Organizations Table
  let ngoCardMatches = 0;
  let ngoHtml = '';
  DATA.ngo_evals.forEach((n, idx) => {{
    const hay = `${{n.ngo_name}} ${{n.y_tunnus}} ${{n.grant_source}} ${{n.vm_momentti}} ${{(n.political_board_insiders || []).join(' ')}}`.toLowerCase();
    if (!matchQuery(hay)) return;
    ngoCardMatches++;
    const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
    const accent = isCut ? 'red-accent' : 'green-accent';
    const badge = isCut
      ? `<span class="badge badge-red">${{fi ? 'Tarkasteltava Ay-/kohdeosuus' : 'Review Ay / Non-Statutory Share'}}</span>`
      : `<span class="badge badge-green">${{fi ? 'Suojattu kenttätyö' : 'Frontline Aid (€0 Cut)'}}</span>`;
    const nParts = splitTitle(n.ngo_name);
    const nSub = nParts.sub || `${{n.grant_source}} · Momentti ${{n.vm_momentti}} (${{n.grant_class_code}})`;
    const commentary = fi
      ? `Yleisavustus- (Ay) / kattojärjestö- / lomatoimintaosuus: ${{n.overhead_and_lobbying_pct}} %. ${{n.public_sote_procurement_sales_eur > 0 ? `Tuottaa lisäksi sote-palveluita ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/v.` : (n.political_board_insiders[0] || '')}}`
      : `Ay general / umbrella / holiday share: ${{n.overhead_and_lobbying_pct}}%. ${{n.public_sote_procurement_sales_eur > 0 ? `Also provides Sote services ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/yr.` : ''}}`;

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
      <span>${{fi ? `Ei osumia pääjärjestökorteissa haulle ”${{safeQ}}”. Katso alla oleva kaikkien 686 STEA-järjestön hakutaulukko tai osion 1 yritykset.` : `No matches in featured NGO cards for "${{safeQ}}". Check the 686-NGO table below or Section 1 corporations.`}}</span>
      <button type="button" class="btn-secondary" onclick="setSearch('')">${{fi ? 'Näytä kaikki järjestöt' : 'Show all NGOs'}}</button>
    </div>`;
  }}
  document.getElementById('ngo-cards').innerHTML = ngoHtml;

  // Render & Sort 686 STEA Table
  const filteredStea = DATA.stea_all.filter(o => {{
    if (qTerms.length === 0) return true;
    const hay = `${{o.ngo_name}} ${{o.org_id}} ${{o.y_tunnus || ''}} ${{(o.top_purposes || []).join(' ')}}`.toLowerCase();
    return matchQuery(hay);
  }}).map(o => ({{
    ...o,
    ak_pct: o.granted_2026_eur > 0 ? (o.ak_general_2026_eur / o.granted_2026_eur) * 100.0 : 0.0
  }}));

  const sortedStea = [...filteredStea].sort((a, b) => {{
    const va = a[STEA_SORT.col];
    const vb = b[STEA_SORT.col];
    let cmp = 0;
    if (typeof va === 'number' && typeof vb === 'number') cmp = va - vb;
    else cmp = String(va || '').localeCompare(String(vb || ''), 'fi');
    return STEA_SORT.asc ? cmp : -cmp;
  }});
  LAST_FILTERED_STEA = sortedStea;

  ['ngo_name', 'granted_2026_eur', 'ak_general_2026_eur', 'ak_pct', 'targeted_2026_eur', 'decision_count_2026'].forEach(col => {{
    const el = document.getElementById('sort-stea-' + col);
    if (el) el.textContent = STEA_SORT.col === col ? (STEA_SORT.asc ? '▲' : '▼') : '';
  }});

  const steaSub = document.getElementById('stea-count-sub');
  const sumFilteredStea = sortedStea.reduce((a, b) => a + b.granted_2026_eur, 0);
  const sumFilteredAk = sortedStea.reduce((a, b) => a + b.ak_general_2026_eur, 0);
  steaSub.textContent = fi
    ? `Näytetään ${{sortedStea.length}} / 686 STEA-järjestöä · Myönnetty yhteensä ${{fmtEUR(sumFilteredStea)}}, josta jatkuvaa Ak-toimintatukea ${{fmtEUR(sumFilteredAk)}}`
    : `Showing ${{sortedStea.length}} / 686 STEA NGOs · Total granted ${{fmtEUR(sumFilteredStea)}}, of which continuous Ak operating grants ${{fmtEUR(sumFilteredAk)}}`;

  const steaTbody = document.getElementById('stea-all-tbody');
  if (sortedStea.length === 0) {{
    steaTbody.innerHTML = `<tr><td colspan="7" style="text-align:center;padding:18px;color:var(--muted);">${{fi ? `Ei STEA-järjestöosumia haulle ”${{safeQ}}”.` : `No STEA NGOs matching "${{safeQ}}".`}}</td></tr>`;
  }} else {{
    steaTbody.innerHTML = sortedStea.map((o, idx) => {{
      const akPct = o.ak_pct.toFixed(1);
      const yBadge = o.y_tunnus ? `<br/><span style="font-size:11.5px;color:var(--muted);">Y: ${{o.y_tunnus}} · STEA #${{o.org_id}}</span>` : `<br/><span style="font-size:11.5px;color:var(--muted);">STEA #${{o.org_id}}</span>`;
      return `<tr class="clickable-row" onclick="openSteaRawModal(${{o.org_id}})">
        <td>${{idx + 1}}</td>
        <td><strong>${{escHtml(o.ngo_name)}}</strong>${{yBadge}}</td>
        <td><strong>${{fmtEUR(o.granted_2026_eur)}}</strong></td>
        <td style="color:${{o.ak_general_2026_eur > 0 ? 'var(--red)' : 'var(--muted)'}};font-weight:600;">${{fmtEUR(o.ak_general_2026_eur)}}</td>
        <td><span class="badge ${{parseFloat(akPct) >= 50 ? 'badge-red' : 'badge-green'}}">${{akPct}} %</span></td>
        <td>${{fmtEUR(o.targeted_2026_eur)}}</td>
        <td style="font-size:12.5px;color:var(--body);"><strong>${{o.decision_count_2026}} kpl:</strong> ${{escHtml((o.top_purposes && o.top_purposes[0]) || '—')}}</td>
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
          ? `Klusterin ${{r.entity_count}} yhtiötä nostivat yhteensä ${{fmtM(r.total_subsidy_eur)}} julkista tukea. 5 vuoden yhteisöverokertymä: ${{fmtEUR(r.total_five_yr_tax_delta_eur)}}.`
          : `Cluster of ${{r.entity_count}} firms collected ${{fmtM(r.total_subsidy_eur)}} in public grants. 5-yr corporate tax: ${{fmtEUR(r.total_five_yr_tax_delta_eur)}}.`}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nostettu tuki' : 'Grants Taken'}}</span><strong style="color:var(--red)">${{fmtCardM(r.total_subsidy_eur)}}</strong></div>
          <div><span>${{fi ? 'Yhteisövero 5v' : '5-Yr Tax'}}</span><strong>${{fmtCardM(r.total_five_yr_tax_delta_eur)}}</strong></div>
          <div><span>${{fi ? 'Koordinointi (20%)' : '20% Fee Est.'}}</span><strong style="color:var(--amber)">${{fmtCardM(r.estimated_20pct_consultant_cut_eur)}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Klusterin yhtiöt ja luvut →' : 'Click: Inspect cluster member companies →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('ring-cards').innerHTML = ringHtml;

  // Update Search Status Banner
  const statusEl = document.getElementById('search-status');
  const totalNgoMatches = Math.max(sortedStea.length, ngoCardMatches);
  if (qTerms.length > 0) {{
    statusEl.style.display = 'block';
    statusEl.innerHTML = fi
      ? `Hakutulokset haulle <strong>”${{safeQ}}”</strong>: löytyi <strong>${{sortedCorps.length}}</strong> yritystä (Osio 1) sekä <strong>${{totalNgoMatches}}</strong> STEA/OKM-järjestöä (Osio 2). <a href="javascript:void(0)" onclick="setSearch('')" style="color:var(--accent-dark);margin-left:10px;">✕ Tyhjennä haku</a>`
      : `Search results for <strong>"${{safeQ}}"</strong>: found <strong>${{sortedCorps.length}}</strong> corporations (Section 1) and <strong>${{totalNgoMatches}}</strong> STEA/OKM NGOs (Section 2). <a href="javascript:void(0)" onclick="setSearch('')" style="color:var(--accent-dark);margin-left:10px;">✕ Clear search</a>`;
  }} else {{
    statusEl.style.display = 'none';
  }}
}}

function handleHashRoute() {{
  const h = (window.location.hash || '').replace(/^#/, '');
  if (!h) return;
  if (h.startsWith('corp-')) {{
    openCorpModal(h.slice(5));
  }} else if (h.startsWith('ngo-')) {{
    const yid = h.slice(4);
    const idx = DATA.ngo_evals.findIndex(n => n.y_tunnus === yid);
    if (idx !== -1) openNgoModal(idx);
  }} else if (h.startsWith('stea-')) {{
    const oid = parseInt(h.slice(5), 10);
    if (!isNaN(oid)) openSteaRawModal(oid);
  }} else if (h.startsWith('momentti-')) {{
    const midx = parseInt(h.slice(9), 10);
    if (!isNaN(midx)) openMomenttiModal(midx);
  }} else if (h.startsWith('ring-')) {{
    const ridx = parseInt(h.slice(5), 10);
    if (!isNaN(ridx)) openRingModal(ridx);
  }} else if (h.startsWith('q=')) {{
    setSearch(decodeURIComponent(h.slice(2)));
  }}
}}

document.getElementById('search-box').addEventListener('input', renderAll);
document.getElementById('scenario-select').addEventListener('change', renderAll);
window.addEventListener('hashchange', handleHashRoute);
renderAll();
handleHashRoute();
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

    zombies = [c for c in corporate_evals if c["classification"] == "BLACKLIST_ZOMBIE"]
    deadweights = [c for c in corporate_evals if c["classification"] == "DEADWEIGHT_CROWD_OUT"]
    keepers = [c for c in corporate_evals if c["classification"] == "POSITIVE_EXTERNALITY_KEEP"]

    zombie_rows = "\n".join(
        f"| `{c['y_tunnus']}` | {c['company_name']} | `{c['vm_momentti']}` | €{float(c['subsidy_received_eur']):,.0f} | €{float(c['five_yr_tax_delta_eur']):,.0f} | `{c['causal_did_roi']:.2f}x` | **-€{float(c['recommended_cut_eur']):,.0f}** |"
        for c in zombies
    )
    deadweight_rows = "\n".join(
        f"| `{c['y_tunnus']}` | {c['company_name']} | `{c['vm_momentti']}` | €{float(c['subsidy_received_eur']):,.0f} | €{float(c['five_yr_tax_delta_eur']):,.0f} | `{c['causal_did_roi']:.2f}x` | **-€{float(c['recommended_cut_eur']):,.0f}** |"
        for c in deadweights
    )
    keeper_rows = "\n".join(
        f"| `{c['y_tunnus']}` | {c['company_name']} | `{c['vm_momentti']}` | €{float(c['subsidy_received_eur']):,.0f} | €{float(c['five_yr_tax_delta_eur']):,.0f} | **`+{c['causal_did_roi']:.2f}x`** | €0 (Keep) |"
        for c in keepers
    )
    ring_rows = "\n".join(
        f"| `{r['ring_id']}` | **{r['ring_signature']}** ({r['shared_address_or_agent']}) | {r['entity_count']} | €{float(r['total_subsidy_eur']):,.0f} | €{float(r['total_five_yr_tax_delta_eur']):,.0f} | €{float(r['estimated_20pct_consultant_cut_eur']):,.0f} |"
        for r in rings
    )
    qoe_rows = "\n".join(
        f"| `{q['y_tunnus']}` | {q['company_name']} | €{float(q['reported_revenue_eur']):,.0f} | €{float(q['reported_ebitda_eur']):,.0f} | €{float(q['subsidy_and_related_party_ebitda_inflation_eur']):,.0f} | **€{float(q['true_subsidy_stripped_core_ebitda_eur']):,.0f}** | `{q['qoe_verdict']}` |"
        for q in qoe_reports
    )
    ngo_rows = "\n".join(
        f"| `{n['y_tunnus']}` | {n['ngo_name']} | `{n['grant_source']} ({n['grant_class_code']})` | €{float(n['annual_grant_eur']):,.0f} | {n['overhead_and_lobbying_pct']}% | €{float(n['public_sote_procurement_sales_eur']):,.0f} | **-€{float(n['recoverable_cut_eur']):,.0f}** |"
        for n in ngo_evals
    )

    md = f"""# Suomen Talousinstituutti (STI) — Yritys- ja järjestötukien vaikuttavuus- ja budjettianalyysi 2026–2027

* **Data Provenance:** 100% Real Statutory Public Open Data (`STEA 2026 All 686 NGOs / 1,288 Positive Decisions out of 1,527 Applications = €273,912,000`, `TEM Yritystukien tietopalvelu`, `Tutkiavustuksia.fi`, `Business Finland Avoin Data`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)
* **Interactive Explorer:** <https://libertaari-suomalainen.github.io/tukipalkkio-purku/>
* **Workbook:** `dist/VM_Tukipalkkio_Leikkuri_2027.xlsx` (6 worksheets, zero external dependencies)

---

## 1. Executive Summary: State Budget 2027 Structural Reform Schedule (`€1.55B–€3.00B/yr`)

Finland allocates approximately **€11.50 billion per year** across direct corporate grants, energy and agricultural subsidies, NGO payouts, and sectoral tax expenditures. By cross-joining official grant payouts (`Business Finland`, `ELY`, `TEM`, `LVM`, `STEA`, `OKM`) with 5-year corporate income tax records (`Verohallinto`) and PRH registry addresses (`YTJ`), this study identifies **€1,548,500,000 per year** (Baseline) up to **€3,000,000,000 per year** (Broad Market Reform) in structural savings without cutting frontline healthcare, schools, police, or national defense.

| VM Momentti | Budget Line Description | Current Budget (`€/yr`) | Baseline Annual Saving (`€1.55B`) | Audited Sample Adjustment (`€`) |
| :--- | :--- | ---: | ---: | ---: |
| **`32.20.40`** | Business Finland R&D & Innovation Grants (2026 authorization €637.4M, cash ~€470M) | `€470,000,000` | **`-€211,500,000`** | `€{momentti_summary.get("32.20.40", 0.0):,.2f}` |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€180,000,000` | **`-€90,000,000`** | `€{momentti_summary.get("32.20.83", 0.0):,.2f}` |
| **`31.20.43 / 32.30.42`** | LVM Maritime Crew Subsidies (`31.20.43`) & TEM ELY Development Grants (`32.30.42`) | `€340,000,000` | **`-€174,000,000`** | `€{momentti_summary.get("32.30.42", 0.0):,.2f}` |
| **`33.90.50`** | STEA Grants (`€212.20M` `Ak` Operating Grants & `€58.21M` `Ay` General Grants across 686 NGOs) | `€410,000,000` | **`-€209,000,000`** | `€{momentti_summary.get("33.90.50", 0.0):,.2f}` |
| **`29.80.50 / 29.90.50 / 29.91.50`** | OKM National Umbrella, Cultural, Sports & Youth Advocacy Grants | `€420,000,000` | **`-€168,000,000`** | `€{momentti_summary.get("29.80.50", 0.0):,.2f}` |
| **`32.20.43 / 32.60.40 / 30.20.40`** | Industrial Electrification, Energy & National Incumbent Subsidies | `€1,740,000,000` | **`-€696,000,000`** | `€{momentti_summary.get("30.10.40_32.60.40", 0.0):,.2f}` |
| **TOTAL** | **KEHYSRIIHI 2027 STRUCTURAL REFORM (6 BUDGET GROUPS)** | **`€3,560,000,000`** | **`-€1,548,500,000 / yr`** | **`€{sum(momentti_summary.values()):,.2f}`** |

---

## 2. Development & Pilot-Stage Grant Recipients With €0 Corporate Tax in 5-Year Window

These development- and pilot-stage ventures or state-supported enterprises received significant public R&D, investment, or operating subsidies while generating **€0** in Finnish corporate income tax over the 5-year observation window:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Evaluated Adjustment |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{zombie_rows}

---

## 3. Incumbent Industrial, Maritime & Energy Subsidies With Low Additionality (`DiD ROI < 0.50x`)

Established corporations and shipping lines receiving automatic or preservation subsidies with low causal tax additionality (`< 0.50x`) relative to unsubsidized market peers:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Evaluated Adjustment |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{deadweight_rows}

---

## 4. High-Externality R&D & Veturi Exporters (`POSITIVE_EXTERNALITY_KEEP` — Protect)

Industrial and technology exporters whose R&D investments and Business Finland Veturi ecosystems translate into strong domestic corporate tax returns (`DiD ROI > 1.20x`):

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Recommended Action |
| :--- | :--- | :--- | ---: | ---: | ---: | :--- |
{keeper_rows}

---

## 5. R&D Ecosystem & Consortium Clusters (`€{total_ring_subsidy:,.0f}` Total Subsidies)

Multi-registry entity resolution across PRH `YTJ` street addresses, consortium identifiers, and shared ecosystem hubs:

| Cluster ID | Cluster Name & Address Hub | Entities | Total Public Subsidies | 5-Yr Corporate Tax Delta | Est. 20% Admin/Coordination Allocation |
| :--- | :--- | ---: | ---: | ---: | ---: |
{ring_rows}

* **Total Cluster Subsidies:** `€{total_ring_subsidy:,.0f}` (Calculated 20% coordination/administrative allocation: `€{total_consultant_cut:,.0f}`).

---

## 6. Financial Statement Grant & R&D Capitalization Adjustment (`IFRS / KPL`)

Adjusting for `Other Operating Income` (`Liiketoiminnan muut tuotot`) public grants and capitalized development expenses (`Kehittämismenojen aktivoinnit`) under `KPL / IAS 20` shows standalone commercial cash EBITDA before subsidies:

| Y-tunnus | Company Name | Reported Revenue | Reported EBITDA | Statutory Grant & R&D Capitalization Items | Standalone Cash EBITDA Before Subsidies | Classification |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
{qoe_rows}

---

## 7. STEA 2026 Full Registry Breakdown (`686` NGOs = `€273,912,000`) & Audited Major NGOs

Across all **686 organizations** and **1,288 funded decisions** (out of 1,527 applications) in the official 2026 STEA registry (`avustukset.stea.fi`):
* **Total 2026 STEA Grants:** `€273,912,000`
* **Continuous Targeted `Ak` Operating Grants (`Kohdennetut toiminta-avustukset`):** `€212,203,929` (**`77.5%`**)
* **General `Ay` Organizational Grants (`Yleisavustukset`):** `€58,214,068` (**`21.3%`**)
* **Project & Investment `C/B` Grants (`Hanke- ja investointiavustukset`):** `€3,494,003` (**`1.3%`**)
* **Taxpayer-Subsidized Holiday Associations (`100% Ak`):** `Loma ja Terveys ry` (`€2,684,710`) + `Hyvinvointilomat ry` (`€2,103,947`) = **`€4,788,657/yr`**

| Y-tunnus | Organization Name | Grant Source & Class | 2026 Annual Grant | Ay General / Umbrella / Holiday Share | Public Sote Service Sales (`€/yr`) | Evaluated Annual Saving (`€/yr`) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{ngo_rows}

* **Total Evaluated Saving Across Featured NGO Cases:** `€{total_ngo_cut:,.0f}/yr`
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    return output_path
