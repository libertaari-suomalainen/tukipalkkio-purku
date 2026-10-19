# Veronmaksajan Tuomioistuin (`tukipalkkio-purku` v2.0) — Yritys- ja Järjestötukien (11,5 Mrd €/v) Röntgen & Kehysriihi-Leikkuri

### 🌐 **[AVAA LIVE-SOVELLUS SELAIMESSA: https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)**

* **Live-verkkosivu (GitHub Pages):** [https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)
* **Valmis VM Kehysriihi Excel-leikkuri (`.xlsx`):** [`dist/VM_Tukipalkkio_Leikkuri_2027.xlsx`](https://github.com/libertaari-suomalainen/tukipalkkio-purku/raw/main/dist/VM_Tukipalkkio_Leikkuri_2027.xlsx)
* **Sisartyökalu (Julkisten hankintojen 38,7 Mrd €/v sidosyksikkö- ja kartellileikkuri):** [`kartelli-tutka`](https://github.com/libertaari-suomalainen/kartelli-tutka) ([Live-sovellus](https://libertaari-suomalainen.github.io/kartelli-tutka/))
* **Tekijä / Ylläpitäjä:** [`@libertaari-suomalainen`](https://github.com/libertaari-suomalainen) | **Lisenssi:** MIT (100 % vapaa avoin lähdekoodi)

---

## 1. Miksi tämä työkalu on olemassa?

Suomen julkinen sektori jakaa **11,5 miljardia euroa vuodessa** yritys-, maatalous-, energia- ja järjestötukia (`Tilastokeskus S.13: D.3 + D.7`), joista **1,5–3,0 miljardia euroa vuodessa** valuu negatiivisen tuoton zombitukiin ja poliittisiin järjestöautomaatteihin:

1. **Zombi-tukifarmaus & c/o-Tukikonsulttiringit (*Momentit 32.20.40, 32.20.83, 32.30.42*):**
   Sadat yritykset nostavat toistuvasti *Business Finlandin* ja *ELY-keskusten* avustuksia ammattimaisten tukikonsulttien (20 % provisio) kautta maksamatta 5 vuoden seuranta-aikana euroakaan yhteisöveroa verrattuna saman toimialan (`NACE`) tuettomiin kilpailijoihin.
2. **STEA- ja ministeriöjärjestöjen hallintopöhö & kaksoisrahoitus (*Momentit 33.90.50, 29.80.50*):**
   Verovapaita `Ak`-yleisavustuksia ohjataan järjestöille, joissa 35–75 % tuesta kuluu keskushallinnon palkkoihin, Helsingin keskustan toimistovuokriin ja poliittiseen edunvalvontaan — tai järjestö myy samanaikaisesti sote-palveluita hyvinvointialueille.

---

## 2. Lähdekoodin Moduulit (`0` ulkoista riippuvuutta)

* `src/tukipalkkio_purku/engine.py` — 5 vuoden Difference-in-Differences (DiD) yhteisöverolaskuri, `c/o`-osoite- ja konsortiorinkien verkostoalgoritmi, STEA/OKM-järjestöleikkuri sekä tuloksen laadun (`QoE`) tukiriisunta.
* `src/tukipalkkio_purku/ingest.py` — PRH YTJ v3 avoimen datan liitin ja relaatioyhdistäjä (`JOIN ON y_tunnus`: `Tutkiavustuksia.fi` × `Verohallinto` × `PRH YTJ`).
* `src/tukipalkkio_purku/excel_compiler.py` — Natiivi OpenXML `.xlsx` -taulukkolaskentakääntäjä (`dist/VM_Tukipalkkio_Leikkuri_2027.xlsx`).
* `src/tukipalkkio_purku/web_compiler.py` — Staattinen selainsovellus (`dist/index.html` & `dist/Veronmaksajan_Tuomioistuin_2026.html`) ja toimittajapaketit (`dist/Media_ja_VM_Dossierit_2026.md`).

---

## 3. Kääntäminen ja Testaus

```bash
# Käännä kaikki artefaktit (Excel + HTML + Media/VM-muistiot):
PYTHONPATH=src python3 -B -m tukipalkkio_purku.cli

# Aja yksikkötestit:
PYTHONPATH=src python3 -B -m unittest discover -s tests -v
```
