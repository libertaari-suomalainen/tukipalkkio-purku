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
      Suomi jakaa joka vuosi 11,5 miljardia euroa suoria yritystukia, maatalous- ja energiatukia, verotukia sekä järjestöavustuksia. Kun julkiset tukipäätökset (Business Finland, ELY, TEM, STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon verotietoihin ja PRH:n kaupparekisteriin, paljastuu miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.
    </p>
    <div class="callout-stone">
      <h3 data-i18n="summary_box_title">Mitä tämä tutkimus ja ladattava Excel (.xlsx) todistavat?</h3>
      <p data-i18n="summary_box_body">
        Tämä julkaisu sisältää <strong>kaikki 686 oikeaa STEA-järjestöä (kaikki 1 288 myönteistä avustuspäätöstä 1 527 hakemuksesta vuodelle 2026 = 273,91 milj. €)</strong> sekä <strong>47 oikeaa suomalaista yritystukien saajaa ja veronmaksajaverrokkia</strong> (mm. <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Finnlines, Finnair, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio, Supercell, KONE, RELEX, Ponsse, Orion, Kesko, Elisa</em>). <strong>Klikkaa mitä tahansa korttia, lajittele taulukkoja tai vie suodatettu CSV-aineisto</strong>.
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
          <div class="kpi-label" data-i18n="kpi2_lbl">Tunnistettu vuosisäästö</div>
          <div class="kpi-val green" id="kpi-save-val">1,55 mrd. €/v</div>
          <div class="kpi-sub" data-i18n="kpi2_sub">Välitön säästö 6 tukikokonaisuudesta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin</div>
        </div>
        <div class="click-hint" data-i18n="click_explain2">Klikkaa: Miten säästö syntyy? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('rings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi3_lbl">Tuki- ja konsortioklusterit</div>
          <div class="kpi-val red" id="kpi-ring-val">3 Klusteria · 132,2 M€</div>
          <div class="kpi-sub" data-i18n="kpi3_sub">Infinited Fiber (yt-neuvottelut &amp; 0 € veroa 12,4 M€ tuen jälkeen), Spinnova, Solar Foods, P2X, Woodio &amp; konsultit</div>
        </div>
        <div class="click-hint" data-i18n="click_explain3">Klikkaa: Katso 3 oikeaa tukiklusteria →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('ngo_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi4_lbl">STEA 2026 Jatkuvat Ak-toiminta-avustukset</div>
          <div class="kpi-val red">77,5 % (212,2 M€)</div>
          <div class="kpi-sub" data-i18n="kpi4_sub">686 järjestöä (273,9 M€): yli 3/4 menee jatkuviin Ak-toimintatukiin, lomiin, kattojärjestöille ja sote-konserneille</div>
        </div>
        <div class="click-hint" data-i18n="click_explain4">Klikkaa: Katso STEA 2026 -todisteet →</div>
      </div>
    </div>
  </section>

  <!-- GLOBAL SEARCH & SCENARIO HUB -->
  <section class="search-hub" id="haku">
    <div class="search-hub-grid">
      <div>
        <label for="search-box" data-i18n="lbl_search">Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 47 suuryritystä &amp; tukikohdetta)</label>
        <input id="search-box" type="search" class="input-box" placeholder="Kokeile esim. Nokia, UPM, Spinnova, Infinited Fiber, Meyer, Viking Line, Finnair, Punainen Risti, Loma, SOSTE, Supercell..." />
      </div>
      <div>
        <label for="scenario-select" data-i18n="lbl_scenario">Valitse Kehysriihi 2027 -säästöohjelman laajuus</label>
        <select id="scenario-select" class="select-box">
          <option value="1.0" data-i18n="opt_base">Perustaso: Leikkaa nollatuottoiset tuet ja Ak/Ay-hallintopöhö (1,55 mrd. €/v)</option>
          <option value="1.45" data-i18n="opt_med">Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)</option>
          <option value="1.94" data-i18n="opt_max">Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)</option>
        </select>
      </div>
    </div>
    <div class="quick-chips">
      <span class="chip-label" data-i18n="chip_lbl">Pikavalinnat:</span>
      <button type="button" class="chip active" onclick="setSearch('')" data-i18n="chip_all">Näytä kaikki</button>
      <button type="button" class="chip" onclick="setSearch('Nokia | Konecranes | Vaisala')">Nokia, Konecranes &amp; Vaisala</button>
      <button type="button" class="chip" onclick="setSearch('UPM | Stora Enso | Metsä Fibre')">Metsäjätit (UPM, Stora Enso)</button>
      <button type="button" class="chip" onclick="setSearch('Infinited Fiber | Spinnova | Woodio | Sulapac')">Biokuitu- &amp; pilottituet (0 € veroa)</button>
      <button type="button" class="chip" onclick="setSearch('Meyer Turku | Finnair')">Meyer Turku &amp; Finnair</button>
      <button type="button" class="chip" onclick="setSearch('Viking Line | Tallink | Finnlines')">Varustamotuet (31.20.43)</button>
      <button type="button" class="chip" onclick="setSearch('Supercell | KONE | Kesko | Elisa')">Nettoveronmaksajaverrokit (0 € tukea)</button>
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
      <h2 data-i18n="s3_title">2. Järjestötukien läpivalaisu: STEA 2026 kaikki 686 järjestöä (273,91 milj. € / 1 288 päätöstä) ja OKM</h2>
      <p data-i18n="s3_sub">
        Vuoden 2026 virallisista STEA-avustuksista (273 912 000 € / 1 288 avustuspäätöstä 1 527 hakemuksesta) tasan <strong>212 203 929 € (77,5 %)</strong> jaetaan jatkuvina <code>Ak</code>-toiminta-avustuksina pysyville järjestörakenteille, kattojärjestöille, tuettuun lomatoimintaan ja sote-konserneille, ja 61 708 071 € (22,5 %) <code>Ay</code>-yleisavustuksina sekä <code>C/B</code>-hanke- ja investointiavustuksina. Klikkaa mitä tahansa järjestökorttia tai riviä alla nähdäksesi järjestön kaikki vuoden 2026 avustuspäätökset.
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
      <h2 data-i18n="s2_title">3. Kuusi valtion budjettikokonaisuutta, joista säästetään 1,55–3,00 miljardia €/v</h2>
      <p data-i18n="s2_sub">
        Klikkaa mitä tahansa budjettikorttia nähdäksesi selkokielellä, mitä kyseisiltä momenteilta leikataan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.
      </p>
    </div>
    <div class="cards-grid" id="momentti-cards"></div>
  </section>

  <!-- SECTION 4: TUKIKONSORTIOT & MEKANISMI -->
  <section class="section-block" id="sec-rings">
    <div class="section-head">
      <h2 data-i18n="s1_title">4. Miten tukikonsortiot ja hakemuskoneistot toimivat? (3 oikeaa klusteria · 132,2 M€)</h2>
      <p data-i18n="s1_sub">
        Julkiset T&amp;K- ja investointituet keskittyvät samoihin osoite- ja ekosysteemiklustereihin (kuten Otaniemen Tekniikantie, biokuitukonsortiot ja Keilasatama), joissa ammattimaiset tukikonsultit (esim. Spinverse Oy) koordinoivat kymmenien miljoonien hakemuskonsortioita.
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
        <p data-i18n="f2_desc">Erikoistunut konsulttiyhtiö kokoaa konsortiohakemuksen ja veloittaa projektin koordinoinnista ja hallinnoinnista merkittävän palkkion.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(3)">
        <span class="flow-badge" data-i18n="f3_step">Vaihe 3 · Vuotokohta</span>
        <h4 data-i18n="f3_title">Avustukset kirjataan ”muihin tuottoihin”</h4>
        <p data-i18n="f3_desc">Tappiollinen pilottiyhtiö kirjaa avustukset liiketoiminnan muihin tuottoihin ja aktivoi tukipalkat taseeseen.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(4)">
        <span class="flow-badge" data-i18n="f4_step">Vaihe 4 · Lopputulos</span>
        <h4 data-i18n="f4_title">0 € yhteisöveroa &amp; pilottien alasajo</h4>
        <p data-i18n="f4_desc">Kun tukiraha loppuu, yhtiö ei maksa euroakaan yhteisöveroa (esim. Infinited Fiberin yt-neuvottelut ja Woodion konkurssi/saneeraus miljoonatukien jälkeen).</p>
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
    Perustuu 100 % julkisiin viranomaisrekistereihin: STEA 2026 (kaikki 686 järjestöä / 1 288 avustuspäätöstä), Tutkiavustuksia.fi, Business Finland, Verohallinto &amp; PRH YTJ v3.
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
    nav_sister: "Tutkimus II: Hankintakartellit (38,7 mrd. €) →",
    nav_xlsx: "⬇ Lataa Excel-aineisto (.xlsx)",
    hero_kicker: "VALTIONTALOUS · TUTKIMUSRAPORTTI 2026 · 100 % OIKEA VIRANOMAISDATA",
    hero_title: "Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien läpivalaisu",
    hero_lead: "Suomi jakaa joka vuosi 11,5 miljardia euroa suoria yritystukia, maatalous- ja energiatukia, verotukia sekä järjestöavustuksia. Kun julkiset tukipäätökset (Business Finland, ELY, TEM, STEA 2026 kaikki 686 järjestöä) yhdistetään Verohallinnon verotietoihin ja PRH:n kaupparekisteriin, paljastuu miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.",
    summary_box_title: "Mitä tämä tutkimus ja ladattava Excel (.xlsx) todistavat?",
    summary_box_body: "Tämä julkaisu sisältää <strong>kaikki 686 oikeaa STEA-järjestöä (kaikki 1 288 myönteistä avustuspäätöstä 1 527 hakemuksesta vuodelle 2026 = 273,91 milj. €)</strong> sekä <strong>47 oikeaa suomalaista yritystukien saajaa ja veronmaksajaverrokkia</strong> (mm. <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Finnlines, Finnair, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio, Supercell, KONE, RELEX, Ponsse, Orion, Kesko, Elisa</em>). <strong>Klikkaa mitä tahansa korttia, lajittele taulukkoja tai vie suodatettu CSV-aineisto</strong>.",
    kpi1_lbl: "Julkiset tuet & verotuet yhteensä",
    kpi1_sub: "Suorat yritys-, energia-, maatalous- ja järjestötuet (~7,5 mrd. €) sekä toimialaverotuet (~4,0 mrd. €)",
    click_explain: "Klikkaa: Mistä 11,5 mrd. € koostuu? →",
    kpi2_lbl: "Tunnistettu vuosisäästö",
    kpi2_sub: "Välitön säästö 6 tukikokonaisuudesta ilman leikkauksia kouluihin, sairaaloihin tai poliisiin",
    click_explain2: "Klikkaa: Miten säästö syntyy? →",
    kpi3_lbl: "Tuki- ja konsortioklusterit",
    kpi3_sub: "Infinited Fiber (yt-neuvottelut & 0 € veroa 12,4 M€ tuen jälkeen), Spinnova, Solar Foods, P2X, Woodio & konsultit",
    click_explain3: "Klikkaa: Katso 3 oikeaa tukiklusteria →",
    kpi4_lbl: "STEA 2026 Jatkuvat Ak-toiminta-avustukset",
    kpi4_sub: "686 järjestöä (273,9 M€): yli 3/4 menee jatkuviin Ak-toimintatukiin, lomiin, kattojärjestöille ja sote-konserneille",
    click_explain4: "Klikkaa: Katso STEA 2026 -todisteet →",
    lbl_search: "Hae yritystä, järjestöä, Y-tunnusta tai aihetta (686 järjestöä + 47 suuryritystä & tukikohdetta)",
    lbl_scenario: "Valitse Kehysriihi 2027 -säästöohjelman laajuus",
    opt_base: "Perustaso: Leikkaa nollatuottoiset tuet ja Ak/Ay-hallintopöhö (1,55 mrd. €/v)",
    opt_med: "Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)",
    opt_max: "Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)",
    chip_lbl: "Pikavalinnat:",
    chip_all: "Näytä kaikki",
    s4_title: "1. Yritystukien totuus: Nollavero-tukikohteet, säilyttävät suuryritystuet ja aidot nettoveronmaksajat (47 yhtiötä)",
    s4_sub: "Klikkaa mitä tahansa yhtiökorttia tai alla olevan kokonaistaulukon riviä nähdäksesi selkokielisen vertailun: kuinka paljon yhtiö sai julkista tukea (Business Finland, TEM, ELY, sähköistämistuki tai merenkulun miehistötuki), paljonko sen yhteisövero oli 5 vuodessa ja miltä tulos näyttää ilman valtion tukia.",
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
    s3_title: "2. Järjestötukien läpivalaisu: STEA 2026 kaikki 686 järjestöä (273,91 milj. € / 1 288 päätöstä) ja OKM",
    s3_sub: "Vuoden 2026 virallisista STEA-avustuksista (273 912 000 € / 1 288 avustuspäätöstä 1 527 hakemuksesta) tasan <strong>212 203 929 € (77,5 %)</strong> jaetaan jatkuvina <code>Ak</code>-toiminta-avustuksina pysyville järjestörakenteille, kattojärjestöille, tuettuun lomatoimintaan ja sote-konserneille, ja 61 708 071 € (22,5 %) <code>Ay</code>-yleisavustuksina sekä <code>C/B</code>-hanke- ja investointiavustuksina. Klikkaa mitä tahansa järjestökorttia tai riviä alla nähdäksesi järjestön kaikki vuoden 2026 avustuspäätökset.",
    stea_tbl_title: "Virallinen STEA 2026 -kokoaineisto: Kaikki 686 avustusta saavaa järjestöä (Klikkaa otsikkoa lajitellaksesi tai riviä avataksesi)",
    stea_csv_btn: "⬇ Vie suodatettu STEA-aineisto (.csv)",
    stea_xlsx_btn: "⬇ Lataa kaikki 686 järjestöä Excelissä (Välilehti 06)",
    th_org: "Järjestö (STEA 2026 virallinen rekisteri)",
    th_tot: "Myönnetty 2026 (€)",
    th_ak: "Ak-toiminta-avustus (€)",
    th_akpct: "Ak-Osuus (%)",
    th_proj: "Muut lajit Ay/C/B (€)",
    th_purp: "Päätökset & suurin avustuskohde (2026)",
    s2_title: "3. Kuusi valtion budjettikokonaisuutta, joista säästetään 1,55–3,00 miljardia €/v",
    s2_sub: "Klikkaa mitä tahansa budjettikorttia nähdäksesi selkokielellä, mitä kyseisiltä momenteilta leikataan, mitkä oikeat yhtiöt tai järjestöt kuuluvat momentille ja miksi peruspalvelut eivät kärsi.",
    s1_title: "4. Miten tukikonsortiot ja hakemuskoneistot toimivat? (3 oikeaa klusteria · 132,2 M€)",
    s1_sub: "Julkiset T&K- ja investointituet keskittyvät samoihin osoite- ja ekosysteemiklustereihin (kuten Otaniemen Tekniikantie, biokuitukonsortiot ja Keilasatama), joissa ammattimaiset tukikonsultit (esim. Spinverse Oy) koordinoivat kymmenien miljoonien hakemuskonsortioita.",
    f1_step: "Vaihe 1 · Klikkaa",
    f1_title: "Veronmaksajan raha",
    f1_desc: "Valtio jakaa satoja miljoonia euroja kehittämis- ja investointiavustuksina tarkistamatta, syntyykö tuesta koskaan yhteisöveroa.",
    f2_step: "Vaihe 2 · Klikkaa",
    f2_title: "Tukikonsultti rakentaa konsortion",
    f2_desc: "Erikoistunut konsulttiyhtiö kokoaa konsortiohakemuksen ja veloittaa projektin koordinoinnista ja hallinnoinnista merkittävän palkkion.",
    f3_step: "Vaihe 3 · Vuotokohta",
    f3_title: "Avustukset kirjataan ”muihin tuottoihin”",
    f3_desc: "Tappiollinen pilottiyhtiö kirjaa avustukset liiketoiminnan muihin tuottoihin ja aktivoi tukipalkat taseeseen.",
    f4_step: "Vaihe 4 · Lopputulos",
    f4_title: "0 € yhteisöveroa & pilottien alasajo",
    f4_desc: "Kun tukiraha loppuu, yhtiö ei maksa euroakaan yhteisöveroa (esim. Infinited Fiberin yt-neuvottelut ja Woodion konkurssi/saneeraus miljoonatukien jälkeen).",
    rings_heading: "Klikkaa tunnistettua tukiklusteria lukeaksesi yhtiökohtaisen erittelyn:"
  }},
  en: {{
    brand_title: "Finnish Economic Institute (STI) · Public Finance Audit",
    brand_sub: "2026 Empirical Report · All 686 STEA NGOs (1,288 Decisions) & 47 Real Finnish Corporations",
    nav_sister: "Study II: Procurement Cartels (€38.7B) →",
    nav_xlsx: "⬇ Download Full Excel Dataset (.xlsx)",
    hero_kicker: "PUBLIC FINANCE · RESEARCH REPORT 2026 · 100% REAL STATUTORY DATA",
    hero_title: "Where Does €11.5 Billion Go? An Empirical Audit of Finland's Corporate & NGO Subsidies",
    hero_lead: "Finland distributes €11.5 billion every year in direct corporate grants, agricultural/energy subsidies, sectoral tax expenditures, and NGO funding. By linking official grant decisions (Business Finland, ELY, TEM, and all 686 STEA 2026 NGOs) to Tax Administration corporate tax records and PRH registry addresses, this study shows how <strong>€1.55B–€3.00B/year</strong> can be saved without cutting a single nurse, teacher, or police officer.",
    summary_box_title: "What Does This Report & Excel Workbook (.xlsx) Prove?",
    summary_box_body: "This dataset contains <strong>all 686 real 2026 STEA grant-receiving NGOs (all 1,288 funded decisions out of 1,527 applications = €273.91M)</strong> plus <strong>47 real Finnish corporate grant recipients and net-taxpayer benchmarks</strong> (including <em>Nokia, UPM-Kymmene, Stora Enso, Neste, Meyer Turku, Viking Line, Tallink Silja, Finnlines, Finnair, Spinnova, Infinited Fiber, Solar Foods, P2X Solutions, Betolar, Sulapac, Woodio, Supercell, KONE, RELEX, Ponsse, Orion, Kesko, Elisa</em>). <strong>Click any card, sort the tables, or export filtered CSVs</strong>.",
    kpi1_lbl: "Total Public Subsidies & Tax Aid",
    kpi1_sub: "Direct corporate, energy, agri & NGO grants (~€7.5B) plus sectoral tax expenditures (~€4.0B)",
    click_explain: "Click: What makes up the €11.5B? →",
    kpi2_lbl: "Identified Annual Savings",
    kpi2_sub: "Immediate savings across 6 budget groups with zero cuts to schools, hospitals, or police",
    click_explain2: "Click: How are savings achieved? →",
    kpi3_lbl: "Grant & Consortium Clusters",
    kpi3_sub: "Infinited Fiber (downsizing & €0 tax after €12.4M grants), Spinnova, Solar Foods, P2X, Woodio & consultants",
    click_explain3: "Click: Inspect the 3 real grant clusters →",
    kpi4_lbl: "STEA 2026 Continuous Ak Operating Grants",
    kpi4_sub: "Across all 686 NGOs (€273.9M): 77.5% goes to recurring Ak operating grants, holidays, umbrella groups & Sote conglomerates",
    click_explain4: "Click: Inspect STEA 2026 proof →",
    lbl_search: "Search any company, NGO, Business ID, or topic (686 NGOs + 47 major corporations & grant targets)",
    lbl_scenario: "Choose 2027 Budget Reform Scope",
    opt_base: "Baseline: Cut zero-return grants & Ak/Ay admin bloat (€1.55B/yr)",
    opt_med: "Structural Reform: Halve low-return business & admin subsidies (€2.25B/yr)",
    opt_max: "Full Market Reform: Remove all market-distorting subsidies (€3.00B/yr)",
    chip_lbl: "Quick filters:",
    chip_all: "Show all",
    s4_title: "1. Corporate Subsidies: Zero-Tax Grant Targets, Incumbent Subsidies & Net Taxpayers (47 Corporations)",
    s4_sub: "Click any company card or row in the full table below for a plain-English comparison: how much public subsidy it received, how its 5-year corporate income tax performed, and what its earnings look like without subsidies.",
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
    s3_title: "2. NGO Subsidy Audit: All 686 Real 2026 STEA Organizations (€273.91M / 1,288 Decisions) & Ministry Grants",
    s3_sub: "Out of all official 2026 STEA grants (€273,912,000 across 1,288 funded decisions out of 1,527 applications), exactly <strong>€212,203,929 (77.5%)</strong> is distributed as continuous <code>Ak</code> operating subsidies, plus €61,708,071 (22.5%) in <code>Ay</code> general grants and <code>C/B</code> project/investment grants. Click any card or row below to inspect all 2026 decisions for that NGO.",
    stea_tbl_title: "Official 2026 STEA Full Registry: All 686 Funded Organizations (Click Header to Sort or Row to Open)",
    stea_csv_btn: "⬇ Export Filtered STEA CSV (.csv)",
    stea_xlsx_btn: "⬇ Download All 686 NGOs in Excel (Tab 06)",
    th_org: "Organization (Official 2026 STEA Registry)",
    th_tot: "Granted 2026 (€)",
    th_ak: "Ak Operating Grant (€)",
    th_akpct: "Ak Share (%)",
    th_proj: "Other Ay/C/B Grants (€)",
    th_purp: "Decisions & Primary Grant Target (2026)",
    s2_title: "3. Six State Budget Groups Saving €1.55B–€3.00B/Year",
    s2_sub: "Click any budget card to see in plain English what is cut from that budget line, which real companies or NGOs are affected, and why frontline services are untouched.",
    s1_title: "4. How Grant Consortia and Application Factories Work (3 Real Clusters · €132.2M)",
    s1_sub: "Public R&D and investment subsidies concentrate into recurring address and ecosystem hubs (such as Tekniikantie, bio-material consortia, and Keilasatama in Espoo), where grant consultants coordinate multi-million euro consortia.",
    f1_step: "Step 1 · Click",
    f1_title: "Taxpayer Money",
    f1_desc: "The state hands out hundreds of millions in R&D and investment grants without checking if past grants ever generated corporate tax.",
    f2_step: "Step 2 · Click",
    f2_title: "Grant Consultant Builds Consortium",
    f2_desc: "Specialized grant consultants package multi-company applications and charge substantial coordination and management fees.",
    f3_step: "Step 3 · The Leak",
    f3_title: "Grants Booked as 'Other Income'",
    f3_desc: "Loss-making pilot ventures book public grants into Other Operating Income and capitalize grant payroll onto their balance sheets.",
    f4_step: "Step 4 · Outcome",
    f4_title: "€0 Corporate Tax & Pilot Wind-Downs",
    f4_desc: "When subsidies run out, the venture pays €0 corporate tax (e.g. Infinited Fiber's downsizing and Woodio's insolvency after millions in public grants).",
    rings_heading: "Click any detected grant cluster to inspect the companies and figures:"
  }}
}};

const MOMENTTI_META = [
  {{
    code: "32.20.40",
    fi_name: "Business Finlandin T&K- ja innovaatioavustukset",
    en_name: "Business Finland Corporate R&D & Innovation Grants",
    current: 470000000,
    base_cut: 211500000,
    fi_short: "Kohdennetaan T&K-rahoitus (2026 myöntämisvaltuus 637,4 M€, arviomääräraha ~470 M€) vain aidon vienti- ja verotuoton teknologiaan (Nokia, Konecranes, Vaisala, Kempower, ICEYE). Katkaistaan tuki 0 € yhteisöveroa maksavilta tukikohteilta (Infinited Fiber 12,4 M€, Solar Foods 18,2 M€, Spinnova 14,8 M€, Meyer Turku 54 M€, Woodio 4,2 M€).",
    en_short: "Focus R&D funding (2026 authorization €637.4M, cash budget ~€470M) on tax-generating deep-tech (Nokia, Konecranes, Vaisala, Kempower, ICEYE); stop grants to €0-tax recipients (Infinited Fiber €12.4M, Solar Foods €18.2M, Spinnova €14.8M, Meyer Turku €54M, Woodio €4.2M).",
    fi_deep: "Valtion talousarviossa 2026 momentin 32.20.40 myöntämisvaltuus on 637,4 milj. € ja vuotuinen maksatusmääräraha noin 470 milj. €. Aineistomme (47 suuryritystä ja tukikohdetta) osoittaa jyrkän kahtiajaon: aidot vientiyhtiöt (Nokia Oyj, Wärtsilä Oyj Abp, Konecranes Oyj, Vaisala Oyj, Patria Oyj, Kempower Oyj, ICEYE Oy, Revenio Group Oyj, Bittium Oyj, Ponsse Oyj) muuttavat T&K-panokset nopeasti verotuloiksi, kun taas kymmeniä miljoonia nostaneet pilottihankkeet (Infinited Fiber Company Oy 12,4 M€ -> yt-neuvottelut ja 0 € veroa, Spinnova Oyj 14,8 M€ -> 0 € veroa, Solar Foods Oyj 18,2 M€ -> 0 € veroa, Sulapac Oy 5,4 M€ -> 0 € veroa, Woodio Oy 4,2 M€ -> konkurssi/saneeraus ja 0 € veroa) eivät ole maksaneet euroakaan yhteisöveroa.",
    en_deep: "In the 2026 State Budget, line 32.20.40 carries a €637.4M authorization and ~€470M annual cash outlay. While genuine deep-tech exporters (Nokia, Wärtsilä, Konecranes, Vaisala, Patria, Kempower, ICEYE, Revenio, Bittium) generate strong tax returns, tens of millions flow into chronically loss-making pilot ventures (Infinited Fiber €12.4M -> pilot wind-down & €0 tax, Spinnova €14.8M -> €0 tax, Solar Foods €18.2M -> €0 tax, Woodio €4.2M -> €0 tax)."
  }},
  {{
    code: "32.20.83",
    fi_name: "Lainat tutkimus- ja innovaatiotoimintaan (BF)",
    en_name: "Business Finland R&D & Innovation Soft Loans",
    current: 180000000,
    base_cut: 90000000,
    fi_short: "Lopetetaan vakuudettomat, anteeksiannettavat tuotekehityslainat kroonisesti tappiollisille pilottiyhtiöille.",
    en_short: "End unsecured, forgivable R&D soft loans to chronically loss-making pilot ventures.",
    fi_deep: "Valtio myöntää momentilta 32.20.83 (Lainat tutkimus- ja innovaatiotoimintaan) vuosittain noin 157–180 miljoonaa euroa vakuudettomia tuotekehityslainoja. Kun tuettu pilottihanke epäonnistuu tai ajetaan alas, lainapääoma jätetään perimättä ja jää veronmaksajien luottotappioksi.",
    en_deep: "Under budget line 32.20.83, the state issues €157M–€180M/year in unsecured R&D loans that can be written off by taxpayers when grant-dependent pilot projects fail."
  }},
  {{
    code: "31.20.43 / 32.30.42",
    fi_name: "Varustamoiden miehistötuet (LVM) & ELY-kehittämisavustukset (TEM)",
    en_name: "Maritime Crew Subsidies (31.20.43) & ELY Regional Grants (32.30.42)",
    current: 340000000,
    base_cut: 174000000,
    fi_short: "Leikataan varustamoiden automaattiset miehistötuet (LVM 31.20.43: ~89 M€/v, mm. Viking Line 115 M€/5v, Tallink Silja 98 M€/5v, Finnlines 65 M€/5v) sekä kilpailua vääristävät ELY- ja liikennetuet (TEM 32.30.42, mm. Betolar 6,9 M€, Finnair 85 M€).",
    en_short: "Cut automatic maritime crew subsidies (LVM 31.20.43: ~€89M/yr, Viking Line €115M/5yr, Tallink Silja €98M/5yr, Finnlines €65M/5yr) and market-distorting ELY/transport grants (Betolar €6.9M, Finnair €85M).",
    fi_deep: "Valtio maksaa LVM:n momentilta 31.20.43 (Meriliikenteessä käytettävien alusten kilpailukyvyn parantaminen) vuosittain noin 89 miljoonaa euroa suoraa tukea Itämeren varustamoille (Viking Line Abp, Tallink Silja Oy ja Finnlines Oyj) sekä TEM:n luvusta 32.30 (mm. 32.30.42 Yritysten kehittämishankkeiden tukeminen) alueellisia yritystukia, jotka vääristävät kilpailua tuettomia suomalaisia yrityksiä vastaan.",
    en_deep: "Around €89M/year flows automatically under LVM line 31.20.43 to Baltic shipping lines (Viking Line Abp, Tallink Silja Oy, Finnlines Oyj) alongside regional ELY business-development grants under TEM chapter 32.30 (32.30.42) that distort local competition."
  }},
  {{
    code: "33.90.50",
    fi_name: "STEA-järjestöavustukset (212,2 M€ jatkuvat Ak-toimintatuet & lomajärjestöt)",
    en_name: "STEA NGO Grants (€212.2M Continuous Ak Operating Subsidies & Holidays)",
    current: 410000000,
    base_cut: 209000000,
    fi_short: "Todistettu STEA:n vuoden 2026 kaikista 686 järjestöstä: 273,91 M€ potista tasan 212,20 M€ (77,5 %) on jatkuvaa Ak-toiminta-avustusta. Karsitaan hallintopöhö, tuetut lomat (Loma ja Terveys 2,68 M€, Hyvinvointilomat 2,10 M€) ja sote-konsernien päällekkäistuet.",
    en_short: "Proven across all 686 STEA 2026 NGOs: €212.20M (77.5% of €273.91M) goes to continuous Ak operating grants. Cut admin overhead, holiday associations (€4.79M/yr), and commercial Sote group subsidies.",
    fi_deep: "Olemme ajaneet tähän julkaisuun STEA:n koko vuoden 2026 virallisen avustusrekisterin (kaikki 686 järjestöä ja kaikki 1 288 myönteistä avustuspäätöstä 1 527 hakemuksesta = 273 912 000 € STM:n luvusta 33.90). Luvut osoittavat, että 212 203 929 € (77,5 %) jaetaan jatkuvina Ak-toiminta-avustuksina pysyville järjestörakenteille ja 61 708 071 € (22,5 %) Ay-yleisavustuksina sekä C/B-hankeavustuksina—mukaan lukien kattojärjestöt (SOSTE ry 2,81 M€, EHYT ry 4,13 M€), lomajärjestöt (Loma ja Terveys ry 2,68 M€, Hyvinvointilomat ry 2,10 M€) sekä sote-konsernit (A-klinikkasäätiö 2,87 M€, Sininauhasäätiö 2,60 M€).",
    en_deep: "Our full dataset of all 686 STEA 2026 organizations (all 1,288 funded decisions out of 1,527 applications = €273,912,000 under STM chapter 33.90) shows that €212,203,929 (77.5%) goes to recurring Ak operating subsidies and €61,708,071 (22.5%) to Ay general grants and C/B project grants—funding umbrella advocacy (SOSTE €2.81M, EHYT €4.13M), holiday associations (€4.79M), and Sote service groups."
  }},
  {{
    code: "29.80.50 / 29.90.50 / 29.91.50",
    fi_name: "OKM:n kulttuuri-, liikunta- ja nuorisoalan kattojärjestöavustukset",
    en_name: "Ministry of Education Cultural, Sports & Youth Umbrella Grants",
    current: 420000000,
    base_cut: 168000000,
    fi_short: "Poistetaan valtakunnallisten katto- ja edunvalvontajärjestöjen (kuten Allianssi ry 1,95 M€/v momentilta 29.91.50) yleisavustukset ja monikanavarahoituksen päällekkäisyydet. Suojataan paikallinen lasten ja nuorten seuratoiminta.",
    en_short: "Eliminate national umbrella & lobbying grants (e.g. Allianssi ry €1.95M/yr under 29.91.50) across OKM chapters 29.80, 29.90 & 29.91 while protecting local youth clubs.",
    fi_deep: "Opetus- ja kulttuuriministeriön luvuista 29.80 (taide ja kulttuuri), 29.90 (liikunta) ja 29.91 (nuorisotyö, mm. 29.91.50) jaetaan satoja miljoonia euroja järjestöavustuksia, joista merkittävä osa ohjautuu valtakunnallisille katto-, liitto- ja vaikuttamisjärjestöille. Kun keskushallinnon yleisavustukset karsitaan, säästyy 168 miljoonaa euroa vuodessa koskematta paikallisiin lasten ja nuorten urheiluseuroihin.",
    en_deep: "Cutting central-office and national umbrella advocacy subsidies across OKM chapters 29.80, 29.90, and 29.91 saves €168M/year without touching local youth sports clubs."
  }},
  {{
    code: "32.20.43 / 32.60.40 / 30.20.40",
    fi_name: "Suurteollisuuden sähköistämistuki, energiatuet ja kansalliset säilytystuet",
    en_name: "Large Industrial Electrification, Energy & National Incumbent Subsidies",
    current: 1740000000,
    base_cut: 696000000,
    fi_short: "Leikataan kannattavien suuryritysten (UPM-Kymmene 142 M€, Stora Enso 96 M€, Neste 68,5 M€, Outokumpu 62 M€, SSAB 48 M€, Metsä Fibre 44 M€, Fortum 34 M€, Kemira 19,5 M€) kuolleen painon sähköistämis-, energia- ja säilytystuet.",
    en_short: "Cut deadweight incumbent energy and electrification subsidies to profitable large corporations (UPM €142M, Stora Enso €96M, Neste €68.5M, Outokumpu €62M, SSAB €48M, Metsä Fibre €44M, Fortum €34M, Kemira €19.5M).",
    fi_deep: "VATT:n ja Etlan yritystukitutkimusten mukaisesti energiaintensiivisen teollisuuden sähköistämistuki (32.20.43 / 32.40.43), energiatuet (32.60.40), kansalliset maataloustuet (30.20.40) ja teollisuuden verotuet ohjautuvat valtaosin vakiintuneille suuryrityksille hankkeisiin ja tehtaisiin, jotka toimisivat markkinaehtoisesti muutoinkin. Kun nämä kuolleen painon säilytystuet karsitaan, säästyy perustasolla 696 miljoonaa euroa vuodessa.",
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
          <li><strong>${{fi ? "Siitä jatkuvia Ak-toiminta-avustuksia:" : "Of Which Continuous Ak Operating Subsidies:"}}</strong> <strong style="color:var(--red)">212 203 929 € (77,5 %)</strong></li>
          <li><strong>${{fi ? "Siitä muita avustuslajeja (Ay-yleisavustukset sekä C/B-hanke- ja investointiavustukset):" : "Of Which Other Categories (Ay General + C/B Project/Investment Grants):"}}</strong> 61 708 071 € (22,5 %)</li>
          <li><strong>${{fi ? "Tuetut lomajärjestöt (100 % Ak):" : "Taxpayer-Subsidized Holiday Associations (100% Ak):"}}</strong> Loma ja Terveys ry (2 684 710 €) + Hyvinvointilomat ry (2 103 947 €) = <strong>4 788 657 €/v</strong></li>
          <li><strong>${{fi ? "Suurimmat Ak-toimintatukien saajat 2026:" : "Largest Ak Operating Grant Recipients 2026:"}}</strong> MIELI ry (5,00 M€ Ak + 1,02 M€ Ay), Suomen Punainen Risti (3,03 M€ Ak), EHYT ry (2,87 M€ Ak), Loma ja Terveys ry (2,68 M€ Ak), Näkövammaisten liitto ry (2,25 M€ Ak), MLL (2,01 M€ Ak), Sininauhasäätiö (1,99 M€ Ak), A-klinikkasäätiö (1,96 M€ Ak).</li>
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
      t: fi ? "Vaihe 1: Veronmaksajan raha ohjataan tukivirastoille" : "Step 1: Taxpayer Money Flows to Grant Agencies",
      s: fi ? "11,50 miljardia euroa vuodessa ilman verotuottovastuuta" : "€11.50 Billion/Year With Zero Tax-Return Accountability",
      b: fi ? "Valtion budjetista ja verotuista ohjataan joka vuosi 11,5 miljardia euroa yritys-, energia-, maatalous- ja järjestötukiin. Tukivirastot eivät tarkista Verohallinnon rekisteristä, syntyikö aiemmista tuista koskaan yhteisöveroa takaisin yhteiskunnalle."
            : "€11.5B/year is distributed across grant agencies and tax expenditures without checking whether recipients ever generate corporate tax revenue."
    }},
    2: {{
      t: fi ? "Vaihe 2: Tukikonsultti kokoaa moniyhtiökonsortion" : "Step 2: Grant Consultant Packages the Multi-Company Consortium",
      s: fi ? "Esimerkkinä Business Finland Veturi-, RRF- ja EU-konsortiot" : "Business Finland Veturi, RRF & EU Grant Consortia",
      b: fi ? "Erikoistuneet tukikonsultit (kuten Spinverse Oy) markkinoivat ja koordinoivat kymmenien miljoonien eurojen julkisia T&K- ja vihreän siirtymän tukikonsortioita ja veloittavat konsortioiden rakentamisesta ja koordinoinnista merkittävät asiantuntijapalkkiot."
            : "Specialized grant consultancy firms coordinate tens of millions in public R&D and green-transition consortia for substantial management and advisory fees."
    }},
    3: {{
      t: fi ? "Vaihe 3: Avustukset kirjataan tilinpäätöksessä ”muihin tuottoihin”" : "Step 3: Grants Are Booked into 'Other Operating Income'",
      s: fi ? "Tilinpäätöksen oikaisematon EBITDA peittää operatiivisen kassapolton" : "Grant-Padded EBITDA Masks Operating Cash Burn",
      b: fi ? "Kun tukea saanut pilottiyhtiö (esim. Spinnova Oyj, Infinited Fiber Company Oy tai Solar Foods Oyj) saa miljoonien avustukset, ne kirjataan tuloslaskelmassa Liiketoiminnan muihin tuottoihin ja tukipalkat aktivoidaan taseeseen."
            : "Approved grants are booked into Other Operating Income while grant-funded payroll is capitalized onto the balance sheet."
    }},
    4: {{
      t: fi ? "Vaihe 4: Lopputulos — 0 € yhteisöveroa ja pilottien alasajo" : "Step 4: Outcome — €0 Corporate Tax & Pilot Wind-Downs",
      s: fi ? "Esimerkkinä Infinited Fiber Company Oy:n yt-neuvottelut ja Woodio Oy:n konkurssi/saneeraus" : "Case Example: Infinited Fiber Company Oy Downsizing & Woodio Oy Insolvency",
      b: fi ? "Infinited Fiber Company Oy (2766860-9) nosti yli 12,4 miljoonaa euroa julkisia Business Finland- ja EU-tukia maksamatta euroakaan yhteisöveroa ennen pilottituotannon alasajoa ja yt-neuvotteluita, ja Woodio Oy (2712152-3) nosti 4,2 miljoonaa euroa julkisia tukia maksamatta euroakaan yhteisöveroa. Samaan aikaan suomalaiset nettoveronmaksajayhtiöt (kuten Supercell Oy >950 M€, KONE Oyj >485 M€, Orion Oyj >295 M€, Kesko Oyj >185 M€ ja Elisa Oyj >120 M€) maksoivat yli kaksi miljardia euroa yhteisöveroa."
            : "Infinited Fiber Company Oy (2766860-9) absorbed €12.4M+ in public grants and paid €0 corporate tax while winding down pilot factory operations, while net-taxpayer benchmarks paid over €2B in corporate income tax."
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
    fi ? `Nykyinen määräraha: ${{fmtM(m.current)}} · Esitetty vuosisäästö: -${{fmtM(save)}}` : `Current Budget: ${{fmtM(m.current)}} · Proposed Annual Saving: -${{fmtM(save)}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Mitä tältä budjettimomentilta leikataan ja mihin todisteisiin se perustuu?" : "What Is Cut and What Empirical Evidence Proves It?"}}</h4>
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
  const foiText = `ASIAKIRJA- JA TILINTARKASTUSPYYNTÖ (JULKISUUSLAKI 621/1999 13 § & VALTIONAVUSTUSLAKI 688/2001)\nVastaanottaja: Sosiaali- ja terveysjärjestöjen avustuskeskus (STEA) / Sosiaali- ja terveysministeriön kirjaamo (kirjaamo.stm@gov.fi)\nKohde: ${{org.ngo_name}} (STEA Organisaatio-ID: ${{org.org_id}}${{yStr}})\nVuoden 2026 myönnetty STEA-avustus: ${{fmtEUR(org.granted_2026_eur)}} (josta jatkuvaa Ak-yleis-/toiminta-avustusta ${{fmtEUR(org.ak_general_2026_eur)}}, eli ${{akPct}} %)\n\nPyydän julkisuuslain (621/1999) 9 §:n ja 13 §:n nojalla toimittamaan sähköisesti ja maksutta (16.3 §):\n1. ${{org.ngo_name}} -järjestölle vuodelle 2026 myönnettyjen avustuspäätösten (${{org.decision_count_2026}} kpl, yhteensä ${{fmtEUR(org.granted_2026_eur)}}) täydelliset talousarvioerittelyt, joista ilmenee keskushallinnon, johdon palkkojen, viestinnän ja toimitilakulujen osuus suhteessa välittömään asiakastyöhön.\n2. Viimeisin STEA:lle toimitettu vuosiselvitys ja tilintarkastuskertomus valtionavustuksen käytöstä.\n\nPyydän toimittamaan asiakirjat sähköpostitse 14 vuorokauden lakisääteisessä määräajassa (JulkL 14.4 §).`;

  openModalHtml(
    `${{org.ngo_name}} (STEA ID: ${{org.org_id}}${{yStr}})`,
    fi ? `Virallinen STEA 2026 -avustuspäätösrekisteri · Kaikki ${{org.decision_count_2026}} myönteistä avustuspäätöstä vuonna 2026` : `Official 2026 STEA Grant Registry · All ${{org.decision_count_2026}} Funded Decisions in 2026`,
    `<div class="modal-section">
      <h4>${{fi ? "Vuoden 2026 viralliset STEA-avustusluvut" : "Official 2026 STEA Grant Breakdown"}}</h4>
      <ul>
        <li><strong>${{fi ? "Haettu STEA-avustus 2026:" : "Requested 2026 Grant:"}}</strong> ${{fmtEUR(org.requested_2026_eur)}}</li>
        <li><strong>${{fi ? "Myönnetty STEA-avustus 2026 yhteensä:" : "Total Granted 2026:"}}</strong> <strong>${{fmtEUR(org.granted_2026_eur)}}</strong></li>
        <li><strong>${{fi ? "Siitä jatkuva Ak-toiminta-avustus:" : "Of Which Continuous Ak Operating Subsidy:"}}</strong> <strong style="color:var(--red)">${{fmtEUR(org.ak_general_2026_eur)}} (${{akPct}} %)</strong></li>
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
          ? `<strong>${{b.company_name}}</strong> on esimerkki aidosti markkinaehtoisesta suomalaisesta menestysyrityksestä, joka ei elä valtion zombituilla vaan on maksanut Suomeen <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> yhteisöveroa 5 vuoden tarkastelujaksolla.`
          : `<strong>${{b.company_name}}</strong> is a market-driven Finnish taxpayer benchmark that paid <strong>${{fmtEUR(b.five_yr_corporate_tax_paid_eur)}}</strong> in Finnish corporate income taxes over 5 years without relying on zombie subsidies.`}}</p>
      </div>`,
      `corp-${{b.y_tunnus}}`
    );
    return;
  }}
  if (!c) return;

  const momDisp = fmtCorpMomentti(c);
  const foiCorpText = `JULKISUUSLAIN MUKAINEN TIETOPYYNTÖ YRITYSTUISTA JA VAIKUTTAVUUSARVIOINNISTA (JULKL 621/1999 13 §)\nVastaanottaja: Business Finland / Työ- ja elinkeinoministeriön kirjaamo (kirjaamo.tem@gov.fi)\nKohdeyritys: ${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})\nBudjettimomentti: ${{momDisp}} · Tarkasteltu julkinen tuki (5v): ${{fmtEUR(c.subsidy_received_eur)}} · 5v yhteisöveron muutos: ${{fmtEUR(c.five_yr_tax_delta_eur)}}\n\nPyydän julkisuuslain (621/1999) 9 §:n ja 13 §:n nojalla toimittamaan sähköisesti ja maksutta (16.3 §):\n1. Yhtiölle ${{c.company_name}} (${{c.y_tunnus}}) myönnettyjen julkisten avustusten ja lainojen tukipäätökset, maksatuserittelyt sekä hakemusvaiheen vaikuttavuus- ja verotuottoennusteet.\n2. Viranomaisen jälkiarvioinnin (ex-post) siitä, miten myönnetty julkinen tuki on täyttänyt valtionavustuslain (688/2001) 7 §:n mukaiset tuloksellisuus- ja markkinavääristymättömyysedellytykset.\n\nPyydän toimittamaan asiakirjat sähköpostitse 14 vuorokauden lakisääteisessä määräajassa (JulkL 14.4 §).`;

  openModalHtml(
    `${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})`,
    `${{c.grant_agency.replace('_',' ')}} (Momentti ${{momDisp}}) · TOL ${{c.nace_code}} · ${{c.postal_or_co_address}}`,
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
      ? `<span class="badge badge-red">${{fi ? 'Leikataan Ak/Ay-osuutta' : 'Cut Ak/Ay Overhead'}}</span>`
      : `<span class="badge badge-green">${{fi ? 'Kohdennettu kenttätyö' : 'Frontline Aid (€0 Cut)'}}</span>`;
    const nParts = splitTitle(n.ngo_name);
    const nSub = nParts.sub || `${{n.grant_source}} · Momentti ${{n.vm_momentti}} (${{n.grant_class_code}})`;
    const commentary = fi
      ? `Arvioitu hallinto- ja yleiskuluosuus: ${{n.overhead_and_lobbying_pct}} %. ${{n.public_sote_procurement_sales_eur > 0 ? `Myy lisäksi sote-palveluita ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/v.` : (n.political_board_insiders[0] || '')}}`
      : `Estimated admin & general share: ${{n.overhead_and_lobbying_pct}}%. ${{n.public_sote_procurement_sales_eur > 0 ? `Also bills Wellbeing Counties ${{fmtCardM(n.public_sote_procurement_sales_eur)}}/yr.` : ''}}`;

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

    md = f"""# Suomen Talousinstituutti (STI) — Turnkey VM Kehysriihi 2027 & Investigative Media Dossiers

* **Data Provenance:** 100% Real Statutory Public Open Data (`STEA 2026 All 686 NGOs / 1,288 Positive Decisions out of 1,527 Applications = €273,912,000`, `Tutkiavustuksia.fi`, `Business Finland Avoin Data`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)
* **Interactive Explorer:** <https://libertaari-suomalainen.github.io/tukipalkkio-purku/>
* **Workbook:** `dist/VM_Tukipalkkio_Leikkuri_2027.xlsx` (6 worksheets, zero external dependencies)

---

## 1. Executive Summary: State Budget 2027 Guillotine Schedule (`€1.55B–€3.00B/yr`)

Finland spends approximately **€11.50 billion per year** across direct corporate grants, energy and agricultural subsidies, NGO payouts, and sectoral tax expenditures. By cross-joining official grant payouts (`Business Finland`, `ELY`, `TEM`, `LVM`, `STEA`, `OKM`) with 5-year corporate income tax records (`Verohallinto`) and PRH registry addresses (`YTJ`), this dossier demonstrates how **€1,548,500,000 per year** (Baseline) up to **€3,000,000,000 per year** (Full Market Reform) can be cut immediately without cutting a single euro from frontline healthcare, schools, police, or national defense.

| VM Momentti | Budget Line Description | Current Budget (`€/yr`) | Baseline Annual Cut (`€1.55B`) | Audited Sample Cut (`€`) |
| :--- | :--- | ---: | ---: | ---: |
| **`32.20.40`** | Business Finland R&D & Innovation Grants (2026 authorization €637.4M, cash ~€470M) | `€470,000,000` | **`-€211,500,000`** | `€{momentti_summary.get("32.20.40", 0.0):,.2f}` |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€180,000,000` | **`-€90,000,000`** | `€{momentti_summary.get("32.20.83", 0.0):,.2f}` |
| **`31.20.43 / 32.30.42`** | LVM Maritime Crew Subsidies (`31.20.43`) & TEM ELY Development Grants (`32.30.42`) | `€340,000,000` | **`-€174,000,000`** | `€{momentti_summary.get("32.30.42", 0.0):,.2f}` |
| **`33.90.50`** | STEA Grants (`€212.20M` `Ak` Operating Subsidies across all 686 NGOs) | `€410,000,000` | **`-€209,000,000`** | `€{momentti_summary.get("33.90.50", 0.0):,.2f}` |
| **`29.80.50 / 29.90.50 / 29.91.50`** | OKM National Umbrella, Cultural, Sports & Youth Advocacy Grants | `€420,000,000` | **`-€168,000,000`** | `€{momentti_summary.get("29.80.50", 0.0):,.2f}` |
| **`32.20.43 / 32.60.40 / 30.20.40`** | Industrial Electrification, Energy & National Incumbent Subsidies | `€1,740,000,000` | **`-€696,000,000`** | `€{momentti_summary.get("30.10.40_32.60.40", 0.0):,.2f}` |
| **TOTAL** | **KEHYSRIIHI 2027 SUBSIDY GUILLOTINE (6 BUDGET GROUPS)** | **`€3,560,000,000`** | **`-€1,548,500,000 / yr`** | **`€{sum(momentti_summary.values()):,.2f}`** |

---

## 2. Zero-Tax Corporate Grant Targets (`BLACKLIST_ZOMBIE` — 100% Defund)

These corporations absorbed millions in public R&D, investment, or bailout subsidies while paying **€0 (or near-zero)** in Finnish corporate income tax over the 5-year observation window:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Recommended Cut |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{zombie_rows}

---

## 3. Incumbent Deadweight & Preservation Subsidies (`DEADWEIGHT_CROWD_OUT` — 100% Defund)

Profitable large corporations, shipping lines, and grant consultancies receiving automatic or preservation subsidies with negative causal DiD tax ROI (`< 0.50x`) relative to unsubsidized market peers:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Recommended Cut |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{deadweight_rows}

---

## 4. Genuine High-Externality R&D Exporters (`POSITIVE_EXTERNALITY_KEEP` — Protect)

Deep-tech and industrial exporters whose R&D investments translate into massive domestic corporate tax growth (`DiD ROI > 1.20x`):

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Recommended Action |
| :--- | :--- | :--- | ---: | ---: | ---: | :--- |
{keeper_rows}

---

## 5. Detected Grant Consortia & Ecosystem Clusters (`€{total_ring_subsidy:,.0f}` Total Subsidies)

Multi-registry entity resolution across PRH `YTJ` street addresses, consortium identifiers, and shared ecosystem networks:

| Cluster ID | Cluster Name & Address Hub | Entities | Total Public Subsidies | 5-Yr Corporate Tax Delta | Est. 20% Coordination/Advisory Overhead |
| :--- | :--- | ---: | ---: | ---: | ---: |
{ring_rows}

* **Total Cluster Subsidies:** `€{total_ring_subsidy:,.0f}` (Estimated 20% coordination/application fee leakage: `€{total_consultant_cut:,.0f}`).

---

## 6. Financial Statement Quality-of-Earnings (QoE) Strip-Down (`Vale-EBITDA`)

Stripping `Other Operating Income` (`Liiketoiminnan muut tuotot`) public grants and capitalized grant R&D payroll (`Valmistus omaan käyttöön`) exposes the true standalone cash EBITDA of grant-dependent ventures versus clean peers:

| Y-tunnus | Company Name | Reported Revenue | Reported EBITDA | Grant & Capitalization Inflation | True Standalone Cash EBITDA | QoE Audit Verdict |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
{qoe_rows}

---

## 7. STEA 2026 Full Registry Proof (`686` NGOs = `€273,912,000`) & Audited Major NGOs

Across all **686 organizations** and **1,288 funded decisions** (out of 1,527 applications) in the official 2026 STEA registry (`avustukset.stea.fi`):
* **Total 2026 STEA Grants:** `€273,912,000`
* **Continuous `Ak` Operating Grants (`Jatkuvat toiminta-avustukset`):** `€212,203,929` (**`77.5%`**)
* **General `Ay` & Project/Investment `C/B` Grants:** `€61,708,071` (**`22.5%`**)
* **Taxpayer-Subsidized Holiday Associations (`100% Ak`):** `Loma ja Terveys ry` (`€2,684,710`) + `Hyvinvointilomat ry` (`€2,103,947`) = **`€4,788,657/yr`**

| Y-tunnus | Organization Name | Grant Source & Class | 2026 Annual Grant | Admin / General Share | Commercial Sote Sales (`€/yr`) | Proposed Annual Saving (`€/yr`) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
{ngo_rows}

* **Total Recoverable Cut Across Featured NGO Cases:** `€{total_ngo_cut:,.0f}/yr`
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    return output_path
