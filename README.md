# Suomen Talousinstituutti (STI) — Yritys- ja Järjestötukien Tutkimusraportti 2026 (`tukipalkkio-purku`)

### 🌐 **[AVAA LIVE-SOVELLUS SELAIMESSA: https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)**

* **Live-verkkosivu (GitHub Pages):** [https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)
* **Valmis 6-välilehtinen VM Kehysriihi Excel-työkirja (`.xlsx`):** [`dist/VM_Tukipalkkio_Leikkuri_2027.xlsx`](https://github.com/libertaari-suomalainen/tukipalkkio-purku/raw/main/dist/VM_Tukipalkkio_Leikkuri_2027.xlsx)
* **Viranomais- ja budjettimuistio (`.md`):** [`dist/Media_ja_VM_Dossierit_2026.md`](dist/Media_ja_VM_Dossierit_2026.md)
* **Sisartyökalu (Julkisten hankintojen 38,7 mrd. €/v sidosyksikkö- ja kilpailuaineisto):** [`kartelli-tutka`](https://github.com/libertaari-suomalainen/kartelli-tutka) ([Live-sovellus](https://libertaari-suomalainen.github.io/kartelli-tutka/))
* **Lisenssi:** MIT (100 % vapaa avoin lähdekoodi, nolla ulkoista Python-riippuvuutta)

---

## 1. Aineiston Kattavuus & Keskeiset Tulokset (100 % Viranomaisdata)

Suomen julkinen sektori kohdentaa **noin 11,50 miljardia euroa vuodessa** suoriin yritystukiin, energia- ja maataloustukiin, järjestöavustuksiin (`~7,5 mrd. €`) sekä toimialakohtaisiin verotukiin (`~4,0 mrd. €`). Kun viralliset avustuspäätökset (`STEA 2026`, `TEM Yritystukien tietopalvelu`, `Tutkiavustuksia.fi`, `Business Finland`, `ELY`, `LVM`) yhdistetään Y-tunnuksella (`Modulo-11`-tarkistettu) Verohallinnon julkisiin yhteisöverotietoihin ja PRH:n YTJ-rekisteriin, tunnistetaan **1,55–3,00 miljardin euron vuotuinen sopeutuspotentiaali** ilman leikkauksia kouluihin, sairaaloihin, poliisiin tai maanpuolustukseen:

1. **STEA 2026 Kaikki 686 Järjestöä (`273 912 000 €` / `1 288` myönteistä avustuspäätöstä `1 527` hakemuksesta):**
   * **Jatkuvat kohdennetut `Ak`-toiminta-avustukset:** Tasan **`212 203 929 €` (`77,5 %`)** koko STEA-potista jaetaan jatkuvina kohdennettuina toiminta-avustuksina (sisältäen sekä matalan kynnyksen kriisi- ja auttamistyötä että ei-lakisääteistä lomatoimintaa).
   * **Järjestöjen `Ay`-yleisavustukset sekä `C`/`B`-hankeavustukset:** `61 708 071 €` (`22,5 %`), josta `Ay`-yleisavustuksia järjestöjen perustoimintaan ja hallintoon on `58 214 068 €` (`21,3 %`) ja `C`/`B`-hankeavustuksia `3 494 003 €` (`1,3 %`).
   * **Ei-lakisääteiset tuetut lomajärjestöt (`100 % Ak`):** `Loma ja Terveys ry` (`2 684 710 €`) ja `Hyvinvointilomat ry` (`2 103 947 €`) saavat yhteensä **`4 788 657 €/v`**.
2. **47 Suomalaisen Suuryrityksen, Tukikohteen ja Nettoveronmaksajaverrokin Verovasteanalyysi (`DiD Vero-ROI`):**
   * **T&K- ja pilottivaiheen tukikohteet ilman yhteisöverovastetta tarkastelujaksolla (`0 €` yhteisöveroa 5v):** Yhtiöt, jotka ovat saaneet merkittäviä julkisia T&K-, investointi- tai toiminta-avustuksia maksamatta yhteisöveroa 5 vuoden tarkastelujaksolla (mm. `Infinited Fiber Company Oy` `12,4 M€`, `Solar Foods Oyj` `18,2 M€`, `Spinnova Oyj` `14,8 M€`, `P2X Solutions Oy` `26,0 M€`, `Betolar Oyj` `6,9 M€`, `Sulapac Oy` `5,4 M€`, `Woodio Oy` `4,2 M€`, `Meyer Turku Oy` `54,0 M€`, `Finnair Oyj` `85,0 M€`).
   * **Vakiintuneiden suuryritysten matalan lisäisyyden säilytystuet (`DiD Vero-ROI < 0.50x`):** Sähköistämistuet, energiatuet ja varustamoiden miehistötuet (`LVM 31.20.43`, `TEM Yritystukien tietopalvelu 2020–2025`: mm. `UPM-Kymmene Oyj` `140 M€`, `Viking Line Abp` `129 M€`, `Stora Enso Oyj` `96 M€`, `Finnlines Oyj` `93 M€`, `Tallink Silja Oy` `71 M€`, `Neste Oyj` `68,5 M€`, `Outokumpu Oyj` `62 M€`, `SSAB Europe Oy` `48 M€`).
   * **Korkean verovasteen T&K- ja Veturi-vientiyhtiöt (`10 kpl`) sekä Tuettomat Nettoveronmaksajaverrokit (`10 kpl`):** Business Finlandin Veturi- ja T&K-ohjelmien vientiyhtiöt, joilla on vahva kotimainen yhteisöverokertymä (`Nokia Oyj`, `KONE Oyj`, `Orion Oyj`, `Wärtsilä Oyj Abp`, `Konecranes Oyj`, `Vaisala Oyj`, `Ponsse Oyj`, `Patria Oyj`, `Kempower Oyj`, `RELEX Oy`), sekä markkinaehtoiset yhteisöveronmaksajaverrokit (`OP Ryhmä / OP Osuuskunta`, `Supercell Oy`, `Kesko Oyj`, `Sampo Oyj`, `Elisa Oyj`, `Nokian Renkaat Oyj`, `Puuilo Oyj`, `Harvia Oyj`, `Marimekko Oyj`, `Olvi Oyj`).

---

## 2. Tuotanto-ominaisuudet Selainsovelluksessa ja Excelissä

* **Kaksisuuntainen sarakelajittelu (`▲`/`▼`) & välitön CSV-vienti (`UTF-8 BOM`):** Sekä 47 yrityksen kokonaistaulukko että kaikkien 686 STEA-järjestön taulukko ovat lajiteltavissa minkä tahansa sarakkeen mukaan ja vietävissä suoraan `.csv`-tiedostoksi.
* **Suorat URL-syvälinkit (`#corp-<y_tunnus>`, `#stea-<org_id>`, `#ngo-<y_tunnus>`, `#momentti-<idx>`, `#ring-<idx>`):** Jokaisessa modaalissa on `🔗 Kopioi suora linkki` ja `🖨 Tulosta / Tallenna PDF` -toiminto sekä valmis `0,00 €` Julkisuuslain (`621/1999 13 §`) tietopyyntö.

---

## 3. Kääntäminen ja Testaus

```bash
# Käännä kaikki artefaktit (Excel + HTML + VM-muistiot):
PYTHONPATH=src python3 -B -m tukipalkkio_purku.cli --offline

# Aja yksikkötestit:
PYTHONPATH=src python3 -B -m unittest discover -s tests -v
```
