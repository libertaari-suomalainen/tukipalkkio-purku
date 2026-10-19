"""
Compilers for:
  1. `dist/Veronmaksajan_Tuomioistuin_2026.html` (`dist/index.html`) — Suomen Talousinstituutti (STI) Editorial Research Report & Interactive Case Explorer
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
    padding: 12px 20px;
  }}
  .topbar-inner {{
    max-width: 1140px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--text);
  }}
  .brand-mark {{
    width: 36px;
    height: 36px;
    border-radius: 6px;
    background: var(--accent);
    color: #fff;
    font-family: 'DM Sans', sans-serif;
    font-weight: 800;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .brand-text strong {{
    display: block;
    font-family: 'DM Sans', sans-serif;
    font-size: 15.5px;
    font-weight: 700;
    line-height: 1.2;
  }}
  .brand-text span {{
    display: block;
    font-size: 12px;
    color: var(--muted);
  }}
  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .lang-btn {{
    background: var(--stone);
    border: 1px solid var(--border-strong);
    color: var(--text);
    padding: 8px 13px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    min-height: 40px;
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
    padding: 9px 15px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    min-height: 40px;
    border: none;
    cursor: pointer;
  }}
  .btn-primary:hover {{ background: var(--accent-dark); }}
  .btn-secondary {{
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border-strong);
    text-decoration: none;
    padding: 9px 14px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    min-height: 40px;
  }}
  .btn-secondary:hover {{ background: var(--stone); }}
  .container {{
    max-width: 1140px;
    margin: 0 auto;
    padding: 32px 20px 80px;
  }}
  .hero-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 40px;
    box-shadow: var(--shadow);
    margin-bottom: 32px;
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
    font-size: clamp(26px, 4vw, 40px);
    line-height: 1.16;
    font-weight: 800;
    margin-bottom: 16px;
  }}
  .hero-lead {{
    font-size: clamp(16px, 2vw, 18.5px);
    color: var(--body);
    max-width: 860px;
    margin-bottom: 24px;
  }}
  .callout-stone {{
    background: var(--stone);
    border-left: 4px solid var(--accent);
    padding: 18px 22px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 28px;
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
  .section-head p {{ font-size: 15.5px; color: var(--muted); max-width: 820px; }}
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
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 18px;
  }}
  .story-card {{
    background: var(--bg);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .story-card.red-accent {{ border-left: 4px solid var(--red); }}
  .story-card.amber-accent {{ border-left: 4px solid var(--amber); }}
  .story-card.green-accent {{ border-left: 4px solid var(--accent); }}
  .story-top {{ margin-bottom: 14px; }}
  .story-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 8px;
  }}
  .story-card h3 {{ font-size: 18px; line-height: 1.3; }}
  .story-meta {{ font-size: 13px; color: var(--muted); margin-bottom: 10px; }}
  .story-commentary {{ font-size: 14.5px; color: var(--body); margin-bottom: 14px; }}
  .metrics-strip {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
  }}
  .metrics-strip div span {{ display: block; font-size: 11px; color: var(--muted); }}
  .metrics-strip div strong {{ font-family: 'DM Sans', sans-serif; font-size: 14.5px; color: var(--text); }}
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
  .filter-bar {{
    background: var(--stone);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
  }}
  .filter-col {{ flex: 1; min-width: 240px; }}
  .filter-col label {{
    display: block;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 4px;
  }}
  .input-box, .select-box {{
    width: 100%;
    min-height: 44px;
    padding: 10px 14px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--surface);
    color: var(--text);
    font-size: 15px;
  }}
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
    max-width: 720px;
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
  .modal-card h2 {{ font-size: 24px; margin-bottom: 8px; padding-right: 44px; }}
  .modal-sub {{ font-size: 14px; color: var(--muted); margin-bottom: 20px; }}
  .modal-section {{
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 18px 20px;
    margin-bottom: 16px;
  }}
  .modal-section h4 {{
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent-dark);
    margin-bottom: 8px;
  }}
  .modal-section p, .modal-section li {{ font-size: 15px; color: var(--body); line-height: 1.6; }}
  .modal-section ul {{ padding-left: 20px; }}
  .modal-section li {{ margin-bottom: 6px; }}
  footer {{
    max-width: 1140px;
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
  @media (max-width: 900px) {{
    .flow-steps {{ grid-template-columns: 1fr; }}
    .hero-card, .section-block {{ padding: 22px 18px; }}
  }}
  @media (max-width: 640px) {{
    .container {{ padding: 18px 12px 56px; }}
    .modal-backdrop {{ padding: 10px; align-items: flex-end; }}
    .modal-card {{ padding: 22px 18px; max-height: 92vh; border-radius: 12px 12px 0 0; }}
    .metrics-strip {{ grid-template-columns: 1fr; }}
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
        <span data-i18n="brand_sub">Tutkimusraportti · Klikkaa mitä tahansa korttia avataksesi selkokielisen analyysin</span>
      </div>
    </a>
    <div class="nav-actions">
      <button class="lang-btn active" id="btn-fi" onclick="setLang('fi')">Suomi</button>
      <button class="lang-btn" id="btn-en" onclick="setLang('en')">English</button>
      <a class="btn-secondary" href="https://libertaari-suomalainen.github.io/kartelli-tutka/" data-i18n="nav_sister">Tutkimus II: Hankintakartellit (38,7 mrd. €) →</a>
      <a class="btn-primary" href="VM_Tukipalkkio_Leikkuri_2027.xlsx" download data-i18n="nav_xlsx">Lataa Excel-malli (.xlsx)</a>
    </div>
  </div>
</header>

<main class="container">
  <section class="hero-card">
    <div class="kicker" data-i18n="hero_kicker">VALTIONTALOUS · TUTKIMUSRAPORTTI 2026</div>
    <h1 class="hero-title" data-i18n="hero_title">Mihin katoaa 11,5 miljardia euroa? Suomen yritys- ja järjestötukien läpivalaisu</h1>
    <p class="hero-lead" data-i18n="hero_lead">
      Suomi jakaa joka vuosi 11,5 miljardia euroa yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Kun julkiset tukipäätökset yhdistetään Verohallinnon verotietoihin ja kaupparekisteriin, paljastuu, miten valtion budjetista voidaan säästää <strong>1,55–3,00 miljardia euroa vuodessa</strong> leikkaamatta yhdeltäkään sairaanhoitajalta, opettajalta tai poliisilta.
    </p>
    <div class="callout-stone">
      <h3 data-i18n="summary_box_title">Miten luet tätä julkaisua? (Kaikki kortit ovat klikattavia)</h3>
      <p data-i18n="summary_box_body">
        Tämä sivu ei ole virkamiesrekisteri, vaan kansantajuinen tutkimusraportti. <strong>Klikkaa mitä tahansa alla olevaa lukukorttia, kaavion vaihetta, tukirinkiä, järjestöä tai yritystä</strong>, niin saat esiin selkokielisen selityksen: kuka rahaa saa, miten järjestely toimii käytännössä ja miksi se tuhlaa veronmaksajien rahoja.
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
          <div class="kpi-val green">1,55–3,00 mrd. €</div>
          <div class="kpi-sub" data-i18n="kpi2_sub">Välitön säästö ilman yhtäkään leikkausta kouluihin, sairaaloihin tai poliisiin</div>
        </div>
        <div class="click-hint" data-i18n="click_explain2">Klikkaa: Miten säästö syntyy? →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('rings_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi3_lbl">Havaitut tukikonsultti- ja sisäpiiriringit</div>
          <div class="kpi-val red" id="kpi-ring-val">3 Rinkiä · 475 milj. €/v</div>
          <div class="kpi-sub" data-i18n="kpi3_sub">Sama c/o-postilokero tai hakemustehdas: miljoonatuet sisään, 0 € yhteisöveroa ulos</div>
        </div>
        <div class="click-hint" data-i18n="click_explain3">Klikkaa: Katso 3 esimerkkitapausta →</div>
      </div>
      <div class="kpi-card clickable-card" onclick="openKpiModal('ngo_pool')">
        <div>
          <div class="kpi-label" data-i18n="kpi4_lbl">Järjestöjen hallintopöhö & tuplalaskutus</div>
          <div class="kpi-val red">377 milj. €/v</div>
          <div class="kpi-sub" data-i18n="kpi4_sub">77,5 % STEA-tuista on vapaata keskushallintorahaa — mukana tuetut lomat ja sote-myyjät</div>
        </div>
        <div class="click-hint" data-i18n="click_explain4">Klikkaa: Katso STEA-läpivalaisu →</div>
      </div>
    </div>
  </section>

  <section class="section-block" id="sec-rings">
    <div class="section-head">
      <h2 data-i18n="s1_title">1. Miten tukirinki toimii? (Klikkaa vaihetta tai rinkiä)</h2>
      <p data-i18n="s1_sub">
        Suomessa toimii kymmeniä yksityisiä ”tukikonsultteja”, jotka perustavat tai keräävät useita pöytälaatikkoyhtiöitä samaan postilokeroon (c/o-osoite) ja hakevat niille maksimituet Business Finlandilta ja ELY-keskuksilta.
      </p>
    </div>
    <div class="flow-steps">
      <div class="flow-step clickable-card" onclick="openFlowModal(1)">
        <span class="flow-badge" data-i18n="f1_step">Vaihe 1 · Klikkaa</span>
        <h4 data-i18n="f1_title">Veronmaksajan raha</h4>
        <p data-i18n="f1_desc">Valtio jakaa satoja miljoonia euroja ”kehittämisavustuksina” tarkistamatta, syntyykö tuesta koskaan verotettavaa liiketoimintaa.</p>
      </div>
      <div class="flow-step clickable-card" onclick="openFlowModal(2)">
        <span class="flow-badge" data-i18n="f2_step">Vaihe 2 · Klikkaa</span>
        <h4 data-i18n="f2_title">Tukikonsultti kirjoittaa hakemuksen</h4>
        <p data-i18n="f2_desc">Konsultti lupaa yritykselle ”ilmaista rahaa” avaimet käteen -periaatteella ja veloittaa onnistuneesta tukipäätöksestä 15–25 % provision.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(3)">
        <span class="flow-badge" data-i18n="f3_step">Vaihe 3 · Vuotokohta</span>
        <h4 data-i18n="f3_title">Saman postilokeron yhtiörinki</h4>
        <p data-i18n="f3_desc">Samassa c/o-osoitteessa toimii useita aputoiminimiä tai holdingyhtiöitä, jotka ostavat konsultointia toisiltaan tukirahoilla.</p>
      </div>
      <div class="flow-step danger clickable-card" onclick="openFlowModal(4)">
        <span class="flow-badge" data-i18n="f4_step">Vaihe 4 · Lopputulos</span>
        <h4 data-i18n="f4_title">5 vuoden jälkeen 0 € yhteisöveroa</h4>
        <p data-i18n="f4_desc">Kun tuki loppuu, yhtiö ei maksa euroakaan yhteisöveroa, kun taas ilman tukia toimiva kilpailija maksaa satoja tuhansia veroja.</p>
      </div>
    </div>
    <h3 style="font-size:19px; margin: 22px 0 12px;" data-i18n="rings_heading">Klikkaa havaittua tukirinkiä lukeaksesi tarkan kuvauksen:</h3>
    <div class="cards-grid" id="ring-cards"></div>
  </section>

  <section class="section-block" id="sec-budget">
    <div class="section-head">
      <h2 data-i18n="s2_title">2. Kuusi kohdetta, joista säästetään 1,55–3,00 miljardia €/v</h2>
      <p data-i18n="s2_sub">
        Valitse säästötaso tai hae nimellä. Klikkaa mitä tahansa budjettikohdetta nähdäksesi selkokielellä, mitä kyseiseltä momentilta leikataan ja miksi peruspalvelut eivät kärsi.
      </p>
    </div>
    <div class="filter-bar">
      <div class="filter-col">
        <label for="scenario-select" data-i18n="lbl_scenario">Valitse säästöohjelman laajuus</label>
        <select id="scenario-select" class="select-box">
          <option value="1.0" data-i18n="opt_base">Perustaso: Leikkaa vain nollatuottoiset zombituet ja hallintopöhö (1,55 mrd. €/v)</option>
          <option value="1.45" data-i18n="opt_med">Rakenneuudistus: Puolita tehottomat elinkeinotuet (2,25 mrd. €/v)</option>
          <option value="1.94" data-i18n="opt_max">Täysi markkinauudistus: Poista kaikki kilpailua vääristävät tuet (3,00 mrd. €/v)</option>
        </select>
      </div>
      <div class="filter-col">
        <label for="search-box" data-i18n="lbl_search">Hae yritystä, järjestöä tai aihetta</label>
        <input id="search-box" type="text" class="input-box" placeholder="Hae esim. Loma ja Terveys, Sininauha, AI-Tuki..." />
      </div>
    </div>
    <div class="cards-grid" id="momentti-cards"></div>
  </section>

  <section class="section-block" id="sec-ngos">
    <div class="section-head">
      <h2 data-i18n="s3_title">3. Järjestötukien läpivalaisu: Tuetut lomat, keskushallinto ja sote-tuplalaskutus</h2>
      <p data-i18n="s3_sub">
        Klikkaa mitä tahansa järjestökorttia nähdäksesi, kuinka suuri osa sen STEA- tai ministeriöavustuksesta kuluu keskushallintoon ja myykö sama organisaatio samaan aikaan palveluita hyvinvointialueille.
      </p>
    </div>
    <div class="cards-grid" id="ngo-cards"></div>
  </section>

  <section class="section-block" id="sec-corps">
    <div class="section-head">
      <h2 data-i18n="s4_title">4. Yritystukien totuus: Zombiyritykset vs. aidot veronmaksajat</h2>
      <p data-i18n="s4_sub">
        Klikkaa yrityskorttia nähdäksesi selkokielisen vertailun: kuinka paljon yritys sai julkista tukea, paljonko se maksoi yhteisöveroa 5 vuoden aikana ja miten sen tilinpäätös muuttuu, kun valtion tuki riisutaan pois.
      </p>
    </div>
    <div class="cards-grid" id="corp-cards"></div>
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
    Perustuu 100 % julkisiin viranomaisrekistereihin: Tutkiavustuksia.fi, STEA 2026, Business Finland, Verohallinto & PRH YTJ.
  </div>
  <div>
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
    html += f"""
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
        <h4>${{fi ? "Mitä luku tarkoittaa käytännössä?" : "What Does This Number Mean in Plain English?"}}</h4>
        <p>${{fi
          ? "Suomen julkinen sektori jakaa joka vuosi 11,5 miljardia euroa suoria yritystukia, maatalous- ja energiatukia sekä järjestöavustuksia. Tämä vastaa lähes koko Suomen maksaman yhteisöveron ja kunnallisveron kasvusummaa. Rahaa jakavat kymmenet eri virastot (Business Finland, ELY-keskukset, STEA, OKM, MMM ja TEM) ilman yhteistä seurantaa siitä, saako veronmaksaja rahoilleen vastinetta."
          : "Finland's public sector hands out €11.5 billion every year across business grants, agricultural/energy subsidies, and NGO payouts. Dozens of separate agencies distribute the money without any shared check on whether taxpayers get anything back."}}</p>
      </div>
      <div class="modal-section">
        <h4>${{fi ? "Pääerät valtion ja julkisyhteisöjen budjeteissa" : "Major Components of the €11.5B Pool"}}</h4>
        <ul>
          <li><strong>${{fi ? "Suorat yritystuet, T&K-avustukset ja ELY-tuet:" : "Direct Corporate & R&D Grants (Business Finland & ELY):"}}</strong> ~1,8 mrd. €/v</li>
          <li><strong>${{fi ? "Järjestö- ja säätiöavustukset (STEA, OKM, kunnat):" : "NGO & Foundation Grants (STEA, Ministries, Municipalities):"}}</strong> ~2,2 mrd. €/v</li>
          <li><strong>${{fi ? "Teollisuuden, energian ja maatalouden kansalliset säilytystuet:" : "Industrial, Energy & Agricultural Subsidies:"}}</strong> ~4,5 mrd. €/v</li>
          <li><strong>${{fi ? "Verotuet ja toimialakohtaiset huojennukset:" : "Sectoral Tax Rebates & Exemptions:"}}</strong> ~3,0 mrd. €/v</li>
        </ul>
      </div>`
    );
  }} else if (key === 'savings_pool') {{
    openModalHtml(
      fi ? "Miten 1,55–3,00 miljardia euroa säästetään ilman leikkauksia peruspalveluihin?" : "How €1.55B–€3.00B Is Saved Without Touching Public Services",
      fi ? "Suomen Talousinstituutin kehysriihimalli 2027" : "Finnish Economic Institute Budget Reform Model 2027",
      `<div class="modal-section">
        <h4>${{fi ? "Miksi yhtäkään hoitajaa tai opettajaa ei tarvitse irtisanoa?" : "Why Zero Nurses or Teachers Need to Be Cut"}}</h4>
        <p>${{fi
          ? "Julkisessa keskustelussa väitetään usein, että valtiontalouden sopeuttaminen tarkoittaa väistämättä sairaaloiden, koulujen tai poliisin leikkauksia. Tutkimuksemme osoittaa päinvastaisen: pelkästään lakkauttamalla nollatuottoiset yritystukiringit (475 milj. €), järjestöjen keskushallintopöhö ja tuetut lomat (377 milj. €) sekä suuryritysten tehottomat säilytystuet (696 milj. €) säästetään heti 1,55 miljardia euroa vuodessa."
          : "Public debate often claims budget cuts must hurt schools or hospitals. Our data proves that simply ending zero-tax corporate grant rings (€475M), NGO HQ bloat and holiday subsidies (€377M), and deadweight corporate rebates (€696M) saves €1.55B/year immediately."}}</p>
      </div>`
    );
  }} else if (key === 'rings_pool') {{
    const listHtml = DATA.rings.map(r => `<li><strong>${{r.shared_address_or_agent}} (${{r.ring_signature}}):</strong> ${{r.entity_count}} ${{fi ? "yhtiötä samassa osoitteessa" : "companies at the same address"}} (${{r.member_names.join(', ')}}) — ${{fi ? "nostettu tuki" : "grants received"}} <strong>${{fmtM(r.total_subsidy_eur)}}</strong>, ${{fi ? "maksettu yhteisövero 5 vuodessa" : "5-yr corporate tax"}} <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong>, ${{fi ? "arvioitu konsulttipalkkio" : "est. 20% consultant fee"}} <strong>${{fmtEUR(r.estimated_20pct_consultant_cut_eur)}}</strong>.</li>`).join('');
    openModalHtml(
      fi ? "Mitä ovat tukikonsultti- ja sisäpiiriringit? (3 tunnistettua rinkiä)" : "What Are Grant-Consultant & Insider Rings? (3 Detected Clusters)",
      fi ? "Kaupparekisterin (PRH YTJ) c/o-osoitteiden ja tukipäätösten ristiinajo" : "Cross-Reference of PRH Registry c/o Addresses and Public Grant Payouts",
      `<div class="modal-section">
        <h4>${{fi ? "Ilmiön selitys selkokielellä" : "How the Racket Works in Plain English"}}</h4>
        <p>${{fi
          ? "Kun yhdistimme julkiset yritystukipäätökset kaupparekisterin postiosoitteisiin, havaitsimme yhtiöryppäitä, jotka on rekisteröity täsmälleen samaan c/o-postilokeroon (usein tukikonsulttitoimiston tai tilitoimiston osoitteeseen). Nämä yhtiöt nostavat satoja tuhansia tai miljoonia euroja kehittämisavustuksia, maksavat tukikonsultille ~20 % palkkion ja ostavat tukirahoilla alihankintaa toisiltaan — mutta eivät maksa viiden vuoden seurannassa lainkaan yhteisöveroa."
          : "Cross-referencing grant payouts with Business Registry postal addresses reveals clusters of shell companies registered at the exact same c/o mailbox. They harvest millions in development grants, pay a ~20% commission to the grant consultant, and pay near-zero corporate income tax over 5 years."}}</p>
      </div>
      <div class="modal-section">
        <h4>${{fi ? "Otoksen 3 tukirinkiä (Klikkaa myös yksittäisiä kortteja sivulla)" : "The 3 Audited Ring Clusters"}}</h4>
        <ul>${{listHtml}}</ul>
      </div>`
    );
  }} else if (key === 'ngo_pool') {{
    openModalHtml(
      fi ? "Järjestöjen hallintopöhö, tuetut lomat ja sote-tuplalaskutus (377 milj. €/v)" : "NGO Admin Bloat, Subsidized Holidays & Sote Double-Billing (€377M/yr)",
      fi ? "Virallinen STEA 2026 -avustusaineisto (686 järjestöä, 273,9 milj. €) + OKM" : "Official STEA 2026 Grant Registry (686 NGOs, €273.9M) + Ministry Grants",
      `<div class="modal-section">
        <h4>${{fi ? "Kolme suurinta ongelmaa järjestötuissa" : "The Three Core Problems in NGO Funding"}}</h4>
        <ul>
          <li><strong>${{fi ? "1. Keskushallinnon yleisavustukset (77,5 % STEA-rahoista):" : "1. Unrestricted HQ Slush Money (77.5% of STEA):"}}</strong> ${{fi ? "Vuonna 2026 STEA jakaa 273,9 miljoonasta eurosta peräti 212,2 miljoonaa euroa ns. yleisavustuksina (Ak), jotka menevät järjestöjen omaan keskushallintoon, johdon palkkoihin, Helsingin keskustan toimistovuokriin ja viestintään." : "Out of €273.9M in 2026 STEA grants, €212.2M (77.5%) is handed out as unrestricted general HQ funding (Ak)."}}</li>
          <li><strong>${{fi ? "2. Valtion tukemat lomajärjestöt (4,79 milj. €/v):" : "2. Taxpayer-Subsidized Holiday Associations (€4.79M/yr):"}}</strong> ${{fi ? "Pelkästään kaksi lomajärjestöä (Loma ja Terveys ry 2,68 milj. € ja Hyvinvointilomat ry 2,10 milj. €) saa lähes 5 miljoonaa euroa vuodessa lomatoiminnan pyörittämiseen." : "Just two holiday associations (Loma ja Terveys ry €2.68M and Hyvinvointilomat ry €2.10M) absorb €4.79M/yr."}}</li>
          <li><strong>${{fi ? "3. Sote-konsernien tuplalaskutus:" : "3. Commercial Sote Double-Billing:"}}</strong> ${{fi ? "Suuret säätiöt (kuten Sininauhasäätiö ja A-klinikkasäätiö) nostavat miljoonia verovapaata STEA-avustusta samalla kun niiden konserniyhtiöt myyvät kymmenillä miljoonilla euroilla asumis- ja päihdepalveluita hyvinvointialueille." : "Large foundations collect tax-free STEA grants while simultaneously billing Wellbeing Counties tens of millions for commercial services."}}</li>
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
      s: fi ? "11,50 miljardia euroa vuodessa ilman tulosvastuuta" : "€11.50 Billion/Year With Zero Tax-Return Accountability",
      b: fi ? "Suomalainen palkansaaja ja tavallinen yrittäjä maksaa korkeaa veroa, jotta valtio voi rahoittaa koulutusta, terveydenhuoltoa ja turvallisuutta. Silti valtion budjetista lohkaistaan joka vuosi 11,5 miljardia euroa erilaisiin yritys- ja järjestötukiin. Mikään laki ei tällä hetkellä velvoita tukivirastoja tarkistamaan, maksoiko tukea saanut yritys koskaan veroja takaisin yhteiskunnalle."
            : "Ordinary workers and unsubsidized businesses pay high taxes to fund schools, healthcare, and security—yet €11.5B/year is diverted into grants with zero requirement to check whether recipients ever pay corporate taxes back."
    }},
    2: {{
      t: fi ? "Vaihe 2: Tukikonsultti kirjoittaa hakemuksen 20 % provisiolla" : "Step 2: Grant Consultant Writes the Application for a 20% Fee",
      s: fi ? "Ammattimainen hakemustehdas tuntee viraston muotokielen" : "Professional Application Factories Know the Bureaucratic Buzzwords",
      b: fi ? "Yksityiset tukikonsultit markkinoivat yrityksille palvelua, jossa konsultti laatii Business Finlandin tai ELY-keskuksen hakemuksen ”avaimet käteen” -periaatteella. Kun virasto myöntää esimerkiksi 500 000 euron tuen, tukikonsultti laskuttaa yritykseltä heti 100 000 euroa (20 %) onnistumispalkkiona. Veronmaksajan rahoista viidennes katoaa siis jo ensimmäisenä päivänä konsultin taskuun."
            : "Private grant consultants write Business Finland or ELY applications on a contingency basis. When a €500,000 grant is approved, the consultant immediately invoices €100,000 (20%) straight out of taxpayer funds."
    }},
    3: {{
      t: fi ? "Vaihe 3: Saman c/o-postilokeron yhtiörinki kierrättää tukirahan" : "Step 3: Co-Located c/o Shell Companies Recycle the Grant Money",
      s: fi ? "Sama postilokero, samat vastuuhenkilöt, eri Y-tunnukset" : "Same Mailbox, Same Insiders, Multiple Business IDs",
      b: fi ? "Koska yksittäiselle yritykselle myönnettävällä tuella on ylärajat (esim. de minimis -sääntö), tukikonsultti tai sijoittajaryhmä rekisteröi samaan c/o-osoitteeseen useita rinnakkaisia osakeyhtiöitä. Jokainen yhtiö hakee erikseen maksimituet ja ostaa ”kehittämispalveluita” saman ringin muilta yhtiöiltä."
            : "To bypass per-company grant caps, insiders register multiple shell companies at the exact same c/o address. Each shell applies for maximum grants and buys 'consulting services' from sister shells in the same ring."
    }},
    4: {{
      t: fi ? "Vaihe 4: Lopputulos — 0 € uutta yhteisöveroa 5 vuodessa" : "Step 4: The Outcome — €0 New Corporate Tax After 5 Years",
      s: fi ? "Tukizombi elää vain seuraavasta avustuspäätöksestä" : "The Subsidy Zombie Survives Only on the Next Grant",
      b: fi ? "Kun tarkastelimme tukirinkeihin kuuluvien yhtiöiden verotietoja viiden vuoden ajalta tuen myöntämisen jälkeen, yhteisöverokertymän kasvu oli nolla tai negatiivinen. Samaan aikaan saman toimialan tavalliset ohjelmisto- ja teknologiayritykset — jotka eivät hakeneet euroakaan tukea — kasvattivat maksamiaan yhteisöveroja sadoilla tuhansilla euroilla."
            : "Five years after receiving grants, companies inside these rings show zero or negative corporate tax growth—while matched unsubsidized firms in the same industry paid hundreds of thousands in new corporate income taxes."
    }}
  }};
  const item = steps[step];
  openModalHtml(item.t, item.s, `<div class="modal-section"><h4>${{fi ? "Mitä tässä vaiheessa tapahtuu?" : "What Happens in This Step?"}}</h4><p>${{item.b}}</p></div>`);
}}

function openRingModal(idx) {{
  const r = DATA.rings[idx];
  const fi = LANG === 'fi';
  const members = DATA.corporate_evals.filter(c => r.member_ytunnus.includes(c.y_tunnus));
  const memberRows = members.map(m => `<li><strong>${{m.company_name}} (${{m.y_tunnus}}):</strong> ${{fi ? "Nostettu tuki" : "Grant received"}} <strong>${{fmtEUR(m.subsidy_received_eur)}}</strong> (${{m.grant_agency.replace('_',' ')}}) · ${{fi ? "Maksettu yhteisöveron kasvu 5 vuodessa:" : "5-yr corporate tax growth:"}} <strong>${{fmtEUR(m.recipient_five_yr_tax_delta_eur)}}</strong> (${{fi ? "tueton verrokki maksoi" : "unsubsidized peer paid"}} ${{fmtEUR(m.matched_peer_five_yr_tax_delta_eur)}}).</li>`).join('');
  openModalHtml(
    `${{r.shared_address_or_agent}} (${{r.ring_signature}})`,
    fi ? `Havaittu yritystukirinki · ${{r.entity_count}} yhtiötä samassa osoitteessa tai hakemuspohjassa` : `Detected Grant Ring · ${{r.entity_count}} Co-Located Companies`,
    `<div class="modal-section">
      <h4>${{fi ? "Miksi tämä rinki nousi esiin läpivalaisussa?" : "Why Was This Ring Flagged?"}}</h4>
      <p>${{fi
        ? `Nämä ${{r.entity_count}} yritystä jakavat saman kaupparekisteriin ilmoitetun c/o-osoitteen tai tukihakemuspohjan (<strong>${{r.shared_address_or_agent}}</strong>). Yhtiöt ovat nostaneet yhteensä <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> julkisia kehittämisavustuksia, josta arviolta <strong>${{fmtEUR(r.estimated_20pct_consultant_cut_eur)}}</strong> (20 %) on kulunut tukikonsulttien palkkioihin. Viiden vuoden seuranta-aikana koko rinki on tuottanut vain <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong> uutta yhteisöveroa.`
        : `These ${{r.entity_count}} companies share the same registry address or consultant signature (<strong>${{r.shared_address_or_agent}}</strong>). Together they collected <strong>${{fmtEUR(r.total_subsidy_eur)}}</strong> in public grants, leaking an estimated <strong>${{fmtEUR(r.estimated_20pct_consultant_cut_eur)}}</strong> (20%) to grant consultants while generating only <strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong> in 5-year corporate tax growth.`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Rinkiin kuuluvat yhtiöt ja niiden luvut" : "Companies Inside This Ring"}}</h4>
      <ul>${{memberRows}}</ul>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Suomen Talousinstituutin toimenpide-esitys" : "Recommended Policy Action"}}</h4>
      <p>${{fi
        ? "Estetään automaattisesti uusien Business Finland- ja ELY-tukien maksaminen yhtiöille, jotka toimivat c/o-postilokeroissa ja joiden aiemmat tuet eivät ole synnyttäneet lainkaan yhteisöverokertymää."
        : "Automatically block new Business Finland and ELY grants to c/o shell clusters whose prior grants generated zero corporate tax return."}}</p>
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
    fi ? `Nykyinen budjettitaso: ${{fmtM(m.current)}} · Esitetty vuosisäästö: -${{fmtM(save)}}` : `Current Budget: ${{fmtM(m.current)}} · Proposed Annual Saving: -${{fmtM(save)}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Mitä tältä budjettimomentilta leikataan?" : "What Is Cut from This Budget Line?"}}</h4>
      <p>${{fi ? m.fi_deep : m.en_deep}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Vaikutus tavalliseen kansalaiseen ja peruspalveluihin" : "Impact on Citizens and Frontline Services"}}</h4>
      <p>${{fi
        ? "Ei heikennä yhdenkään koulun, sairaalan tai poliisilaitoksen rahoitusta. Päinvastoin: kun tehottomat yritys- ja hallintotuet karsitaan, terveet suomalaiset yritykset voivat kilpailla reilusti ilman valtion vääristämää markkinaa."
        : "Zero impact on schools, hospitals, or police. Ending unproductive subsidies restores fair market competition for unsubsidized taxpayers."}}</p>
    </div>`
  );
}}

function openNgoModal(idx) {{
  const n = DATA.ngo_evals[idx];
  const fi = LANG === 'fi';
  const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
  openModalHtml(
    `${{n.ngo_name}} (Y-tunnus: ${{n.y_tunnus}})`,
    `${{n.primary_ministry}} · ${{fi ? "Avustustyyppi" : "Grant Type"}}: ${{n.grant_type_code}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Selkokielinen analyysi järjestön rahoituksesta" : "Plain-English Analysis of This Organization's Funding"}}</h4>
      <p>${{fi
        ? `<strong>${{n.ngo_name}}</strong> saa julkisia avustuksia yhteensä <strong>${{fmtEUR(n.annual_grant_eur)}}</strong> vuodessa. Aineiston perusteella järjestön hallinnon, johdon, toimitilojen ja viestinnän osuus on <strong>${{(n.non_frontline_overhead_share * 100).toFixed(1)}} %</strong>.${{n.commercial_sote_revenue_eur > 0 ? ` Lisäksi sama konserni myy hyvinvointialueille ja kunnille kaupallisia palveluita <strong>${{fmtEUR(n.commercial_sote_revenue_eur)}}</strong> edestä vuodessa — eli se kilpailee verovapaan avustuksen turvin yksityisten hoiva- ja palveluyritysten kanssa.` : ''}}`
        : `<strong>${{n.ngo_name}}</strong> receives <strong>${{fmtEUR(n.annual_grant_eur)}}</strong>/year in public grants, with <strong>${{(n.non_frontline_overhead_share * 100).toFixed(1)}}%</strong> absorbed by non-frontline overhead.${{n.commercial_sote_revenue_eur > 0 ? ` Simultaneously, it bills public Wellbeing Counties <strong>${{fmtEUR(n.commercial_sote_revenue_eur)}}</strong>/year for commercial services.` : ''}}`}}</p>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Rahoituksen avainluvut" : "Key Financial Breakdown"}}</h4>
      <ul>
        <li><strong>${{fi ? "Julkiset avustukset yhteensä:" : "Total Annual Public Grants:"}}</strong> ${{fmtEUR(n.annual_grant_eur)}}</li>
        <li><strong>${{fi ? "Kaupallinen myynti hyvinvointialueille:" : "Commercial Sales to Wellbeing Counties:"}}</strong> ${{fmtEUR(n.commercial_sote_revenue_eur)}}</li>
        <li><strong>${{fi ? "Keskushallinnon ja yleistuen osuus:" : "HQ, Comms & Unrestricted Overhead Share:"}}</strong> ${{(n.non_frontline_overhead_share * 100).toFixed(1)}} %</li>
        <li><strong>${{fi ? "Esitetty vuosisäästö veronmaksajille:" : "Proposed Annual Taxpayer Saving:"}}</strong> <strong style="color:var(--red)">${{fmtEUR(n.recoverable_cut_eur)}}</strong></li>
      </ul>
    </div>
    <div class="modal-section">
      <h4>${{fi ? "Johtopäätös" : "Policy Verdict"}}</h4>
      <p>${{isCut
        ? (fi ? "Suomen Talousinstituutti esittää keskushallinnon yleisavustuksen ja päällekkäisen tuen leikkaamista. Jos järjestö harjoittaa kaupallista sote-palvelumyyntiä, sen tulee toimia samojen verolainsäädännön ja kilpailusääntöjen alla kuin muidenkin yritysten." : "Cut unrestricted HQ slush funding and eliminate tax-free subsidy advantages for commercial healthcare service vendors.")
        : (fi ? "Järjestön rahoitus ohjautuu tehokkaasti suoraan kenttätyöhön ja kriisiajoneuvo-/auttamistoimintaan ilman kaupallista tuplalaskutusta. Rahoitus säilytetään ennallaan." : "Funding goes directly to frontline aid with low overhead and zero commercial double-billing. Keep intact.")}}</p>
    </div>`
  );
}}

function openCorpModal(idx) {{
  const c = DATA.corporate_evals[idx];
  const qoe = DATA.qoe_reports.find(x => x.y_tunnus === c.y_tunnus);
  const fi = LANG === 'fi';
  openModalHtml(
    `${{c.company_name}} (Y-tunnus: ${{c.y_tunnus}})`,
    `${{c.grant_agency.replace('_',' ')}} · ${{fi ? "Toimiala" : "Industry NACE"}}: ${{c.nace_code}}`,
    `<div class="modal-section">
      <h4>${{fi ? "Mitä tämä yritystuki sai aikaan?" : "What Did This Corporate Grant Achieve?"}}</h4>
      <p>${{c.classification === 'BLACKLIST_ZOMBIE'
        ? (fi ? `<strong>${{c.company_name}}</strong> on nostanut <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong> julkista yritystukea, mutta viiden vuoden seuranta-aikana sen maksama yhteisövero kasvoi vain <strong>${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}</strong>. Samaan aikaan saman toimialan tueton verrokkiyritys — joka ei saanut euroakaan tukea — kasvatti maksamiaan yhteisöveroja <strong>${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}</strong>.`
              : `<strong>${{c.company_name}}</strong> took <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong> in public grants, yet its 5-year corporate income tax grew by only <strong>${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}</strong>—compared to <strong>${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}</strong> paid by a matched unsubsidized peer.`)
        : (fi ? `Vertailussa <strong>${{c.company_name}}</strong> sai <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong> tukea ja kasvatti 5 vuoden aikana maksamiaan yhteisöveroja <strong>${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}</strong> (tuettoman verrokin verokasvu ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}).`
              : `<strong>${{c.company_name}}</strong> received <strong>${{fmtEUR(c.subsidy_received_eur)}}</strong> and generated <strong>${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}</strong> in 5-year corporate tax growth (vs. ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}} for its unsubsidized peer).`)}}</p>
    </div>
    ${{qoe ? `<div class="modal-section">
      <h4>${{fi ? "Tilinpäätöksen läpivalaisu: Mitä tapahtuu, kun valtion tuki poistetaan tuloksesta?" : "Financial Strip-Down: What Happens When State Subsidies Are Removed?"}}</h4>
      <p>${{fi
        ? `Yhtiö raportoi tilinpäätöksessään <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> liikevaihdon ja <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong> käyttökatteen. Kun tuloksesta kuitenkin vähennetään ”liiketoiminnan muihin tuottoihin” kirjatut suorat avustukset (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) ja julkisten näennäismarkkinoiden kate, yhtiön todellinen liiketaloudellinen käyttökate on <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`
        : `The company reports <strong>${{fmtEUR(qoe.reported_revenue_eur)}}</strong> in revenue and <strong>${{fmtEUR(qoe.reported_ebitda_eur)}}</strong> in EBITDA. Once direct state grants booked as 'other income' (<strong>${{fmtEUR(qoe.direct_grants_in_other_income_eur)}}</strong>) and public quasi-monopoly margins are stripped out, true standalone EBITDA is <strong style="color:var(--red)">${{fmtEUR(qoe.true_standalone_ebitda_eur)}}</strong>.`}}</p>
    </div>` : ''}}`
  );
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
  const q = (document.getElementById('search-box').value || '').toLowerCase().trim();
  const mult = parseFloat(document.getElementById('scenario-select').value || '1.0');
  const fi = LANG === 'fi';

  // 1. Ring Story Cards
  let ringHtml = '';
  DATA.rings.forEach((r, idx) => {{
    const text = (r.ring_signature + ' ' + r.shared_address_or_agent + ' ' + r.member_names.join(' ')).toLowerCase();
    if (q && !text.includes(q)) return;
    ringHtml += `<div class="story-card red-accent clickable-card" onclick="openRingModal(${{idx}})">
      <div class="story-top">
        <div class="story-header">
          <h3>${{r.shared_address_or_agent}}</h3>
          <span class="badge badge-red">${{r.entity_count}} ${{fi ? 'yhtiötä' : 'firms'}}</span>
        </div>
        <div class="story-meta">${{fi ? 'Rinkitunniste:' : 'Cluster ID:'}} ${{r.ring_signature}} · ${{r.member_names.join(', ')}}</div>
        <p class="story-commentary">${{fi
          ? `Samaan c/o-osoitteeseen rekisteröidyt ${{r.entity_count}} yhtiötä nostivat yhteensä ${{fmtEUR(r.total_subsidy_eur)}} tukea, mutta maksoivat 5 vuodessa vain ${{fmtEUR(r.total_five_yr_tax_delta_eur)}} uutta yhteisöveroa.`
          : `Co-located cluster of ${{r.entity_count}} firms collected ${{fmtEUR(r.total_subsidy_eur)}} in public grants while paying only ${{fmtEUR(r.total_five_yr_tax_delta_eur)}} in 5-yr corporate tax.`}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nostettu tuki' : 'Grants Taken'}}</span><strong style="color:var(--red)">${{fmtM(r.total_subsidy_eur)}}</strong></div>
          <div><span>${{fi ? 'Yhteisövero 5v' : '5-Yr Tax Paid'}}</span><strong>${{fmtEUR(r.total_five_yr_tax_delta_eur)}}</strong></div>
          <div><span>${{fi ? 'Konsultti (20%)' : '20% Agent Fee'}}</span><strong style="color:var(--amber)">${{fmtEUR(r.estimated_20pct_consultant_cut_eur)}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Avaa ringin yhtiöt ja analyysi →' : 'Click: Inspect member firms & full analysis →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('ring-cards').innerHTML = ringHtml;

  // 2. Momentti Cards
  let momHtml = '';
  MOMENTTI_META.forEach((m, idx) => {{
    const text = (m.code + ' ' + m.fi_name + ' ' + m.en_name + ' ' + m.fi_short).toLowerCase();
    if (q && !text.includes(q)) return;
    const save = Math.min(m.current, m.base_cut * mult);
    momHtml += `<div class="story-card green-accent clickable-card" onclick="openMomenttiModal(${{idx}})">
      <div class="story-top">
        <div class="story-header">
          <h3>${{fi ? m.fi_name : m.en_name}}</h3>
          <span class="badge badge-red">-${{fmtM(save)}}</span>
        </div>
        <div class="story-meta">${{fi ? 'Valtion budjettimomentti' : 'State Budget Line'}} ${{m.code}}</div>
        <p class="story-commentary">${{fi ? m.fi_short : m.en_short}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nykyinen budjetti' : 'Current Spend'}}</span><strong>${{fmtM(m.current)}}</strong></div>
          <div><span>${{fi ? 'Vuosisäästö' : 'Annual Saving'}}</span><strong style="color:var(--red)">-${{fmtM(save)}}</strong></div>
          <div><span>${{fi ? 'Leikkausosuus' : 'Cut Share'}}</span><strong>${{((save / m.current) * 100).toFixed(0)}} %</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Lue perustelut ja vaikutusarvio →' : 'Click: Read policy rationale & impact →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('momentti-cards').innerHTML = momHtml;

  // 3. NGO Story Cards
  let ngoHtml = '';
  DATA.ngo_evals.forEach((n, idx) => {{
    const text = (n.ngo_name + ' ' + n.y_tunnus + ' ' + n.primary_ministry).toLowerCase();
    if (q && !text.includes(q)) return;
    const isCut = n.classification === 'GUILLOTINE_ADMIN_BLOAT';
    const accent = isCut ? 'red-accent' : 'green-accent';
    const badge = isCut
      ? `<span class="badge badge-red">${{fi ? 'Leikataan hallintopöhö' : 'Cut Admin Bloat'}}</span>`
      : `<span class="badge badge-green">${{fi ? 'Tehokas kenttätyö' : 'Efficient Frontline'}}</span>`;
    const commentary = isCut
      ? (fi
          ? `Järjestön rahoituksesta ${{(n.non_frontline_overhead_share * 100).toFixed(0)}} % kuluu hallintoon ja yleiskuluihin.${{n.commercial_sote_revenue_eur > 0 ? ` Lisäksi se myy sote-palveluita ${{fmtM(n.commercial_sote_revenue_eur)}}/v.` : ''}}`
          : `${{(n.non_frontline_overhead_share * 100).toFixed(0)}}% goes to overhead/general funding.${{n.commercial_sote_revenue_eur > 0 ? ` Also sells ${{fmtM(n.commercial_sote_revenue_eur)}}/yr in commercial Sote services.` : ''}}`)
      : (fi
          ? `Matala hallinto-osuus (${{(n.non_frontline_overhead_share * 100).toFixed(0)}} %) ja suora kenttätoiminta ilman kaupallista sote-tuplalaskutusta.`
          : `Low overhead (${{(n.non_frontline_overhead_share * 100).toFixed(0)}}%) focused on direct citizen aid with zero commercial double-billing.`);
    ngoHtml += `<div class="story-card ${{accent}} clickable-card" onclick="openNgoModal(${{idx}})">
      <div class="story-top">
        <div class="story-header">
          <h3>${{n.ngo_name}}</h3>
          ${{badge}}
        </div>
        <div class="story-meta">Y-tunnus: ${{n.y_tunnus}} · ${{n.primary_ministry}} (${{n.grant_type_code}})</div>
        <p class="story-commentary">${{commentary}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Avustukset / v' : 'Annual Grants'}}</span><strong>${{fmtM(n.annual_grant_eur)}}</strong></div>
          <div><span>${{fi ? 'Sote-myynti' : 'Sote Sales'}}</span><strong>${{n.commercial_sote_revenue_eur > 0 ? fmtM(n.commercial_sote_revenue_eur) : '0 €'}}</strong></div>
          <div><span>${{fi ? 'Esitetty säästö' : 'Proposed Cut'}}</span><strong style="color:${{isCut ? 'var(--red)' : 'var(--accent-dark)'}}">${{fmtM(n.recoverable_cut_eur)}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Avaa järjestön rahoitusanalyysi →' : 'Click: Open full NGO funding audit →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('ngo-cards').innerHTML = ngoHtml;

  // 4. Corporate Story Cards
  let corpHtml = '';
  DATA.corporate_evals.forEach((c, idx) => {{
    const text = (c.company_name + ' ' + c.y_tunnus + ' ' + c.grant_agency).toLowerCase();
    if (q && !text.includes(q)) return;
    const isZombie = c.classification === 'BLACKLIST_ZOMBIE';
    const isDead = c.classification === 'DEADWEIGHT_CROWD_OUT';
    const accent = isZombie ? 'red-accent' : (isDead ? 'amber-accent' : 'green-accent');
    const badge = isZombie
      ? `<span class="badge badge-red">${{fi ? 'Tukizombi (0 € verokasvu)' : 'Subsidy Zombie'}}</span>`
      : (isDead ? `<span class="badge badge-amber">${{fi ? 'Tehoton säilytystuki' : 'Deadweight'}}</span>`
                : `<span class="badge badge-green">${{fi ? 'Aito veronmaksaja' : 'Real Tax Growth'}}</span>`);
    const commentary = isZombie
      ? (fi
          ? `Nosti ${{fmtEUR(c.subsidy_received_eur)}} tukea, mutta yhteisöveron kasvu 5 vuodessa oli ${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}} (tueton verrokki maksoi ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}).`
          : `Took ${{fmtEUR(c.subsidy_received_eur)}} in grants but paid ${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}} in 5-yr tax growth (vs. ${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}} by unsubsidized peer).`)
      : (fi
          ? `Sai ${{fmtEUR(c.subsidy_received_eur)}} tukea ja kasvatti 5 vuoden yhteisöverokertymää ${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}.`
          : `Received ${{fmtEUR(c.subsidy_received_eur)}} and generated ${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}} in 5-yr corporate tax growth.`);
    corpHtml += `<div class="story-card ${{accent}} clickable-card" onclick="openCorpModal(${{idx}})">
      <div class="story-top">
        <div class="story-header">
          <h3>${{c.company_name}}</h3>
          ${{badge}}
        </div>
        <div class="story-meta">Y-tunnus: ${{c.y_tunnus}} · ${{c.grant_agency.replace('_',' ')}}</div>
        <p class="story-commentary">${{commentary}}</p>
      </div>
      <div>
        <div class="metrics-strip">
          <div><span>${{fi ? 'Nostettu tuki' : 'Subsidy'}}</span><strong>${{fmtEUR(c.subsidy_received_eur)}}</strong></div>
          <div><span>${{fi ? 'Vero 5v' : '5-Yr Tax'}}</span><strong>${{fmtEUR(c.recipient_five_yr_tax_delta_eur)}}</strong></div>
          <div><span>${{fi ? 'Verrokki 5v' : 'Peer Tax'}}</span><strong style="color:var(--accent-dark)">${{fmtEUR(c.matched_peer_five_yr_tax_delta_eur)}}</strong></div>
        </div>
        <div class="click-hint">${{fi ? 'Klikkaa: Katso tilinpäätös- ja verovertailu →' : 'Click: Inspect tax & earnings strip-down →'}}</div>
      </div>
    </div>`;
  }});
  document.getElementById('corp-cards').innerHTML = corpHtml;
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

    md = f"""# Veronmaksajan Tuomioistuin 2026 — Turnkey VM Kehysriihi & Media Firestorm Dossiers

* **Generated Automatically by:** `Veronmaksajan Tuomioistuin` v2.0
* **Data Provenance:** 100% Statutory Public Open Data (`Tutkiavustuksia.fi`, `Business Finland Avoin Data`, `STEA avustukset.stea.fi`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)

| VM Momentti | Budget Line Description | National Annual Cut (`€1.55B` Base) | Audited Cohort Cut (`€`) |
| :--- | :--- | ---: | ---: |
| **`32.20.40`** | Business Finland R&D Grants | `€211,500,000` | `€{momentti_summary.get("32.20.40", 0.0):,.2f}` |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€90,000,000` | `€{momentti_summary.get("32.20.83", 0.0):,.2f}` |
| **`32.30.42`** | ELY Regional Development Grants | `€174,000,000` | `€{momentti_summary.get("32.30.42", 0.0):,.2f}` |
| **`33.90.50`** | STEA Grants (`Ak` General HQ Slush) | `€209,000,000` | `€{momentti_summary.get("33.90.50", 0.0):,.2f}` |
| **`29.80.50`** | OKM General & Advocacy NGO Grants | `€168,000,000` | `€{momentti_summary.get("29.80.50", 0.0):,.2f}` |
| **`30.10.40 / 32.60.40`** | National Agri & Industrial Energy Subsidies | `€696,000,000` | `€{momentti_summary.get("30.10.40_32.60.40", 0.0):,.2f}` |
| **TOTAL** | **KEHYSRIIHI 2027 SUBSIDY GUILLOTINE** | **`€1,548,500,000 / yr`** | **`€{sum(momentti_summary.values()):,.2f}`** |

* Ring subsidy total: €{total_ring_subsidy:,.0f} (Consultant 20% fee: €{total_consultant_cut:,.0f}, NGO cut: €{total_ngo_cut:,.0f})
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    return output_path
