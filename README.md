# Suomen Talousinstituutti (STI) — Yritys- ja Järjestötukien Tutkimusraportti 2026 (`tukipalkkio-purku`)

### 🌐 **[AVAA LIVE-SOVELLUS SELAIMESSA: https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)**

* **Live-verkkosivu (GitHub Pages):** [https://libertaari-suomalainen.github.io/tukipalkkio-purku/](https://libertaari-suomalainen.github.io/tukipalkkio-purku/)
* **Valmis 6-välilehtinen VM Kehysriihi Excel-leikkuri (`.xlsx`):** [`dist/VM_Tukipalkkio_Leikkuri_2027.xlsx`](https://github.com/libertaari-suomalainen/tukipalkkio-purku/raw/main/dist/VM_Tukipalkkio_Leikkuri_2027.xlsx)
* **Tutkivan journalismin & VM-budjettiosaston muistio (`.md`):** [`dist/Media_ja_VM_Dossierit_2026.md`](dist/Media_ja_VM_Dossierit_2026.md)
* **Sisartyökalu (Julkisten hankintojen 38,7 mrd. €/v sidosyksikkö- ja kilpailuaineisto):** [`kartelli-tutka`](https://github.com/libertaari-suomalainen/kartelli-tutka) ([Live-sovellus](https://libertaari-suomalainen.github.io/kartelli-tutka/))
* **Lisenssi:** MIT (100 % vapaa avoin lähdekoodi, nolla ulkoista Python-riippuvuutta)

---

## 1. Aineiston Kattavuus & Keskeiset Tulokset (100 % Viranomaisdata)

Suomen julkinen sektori jakaa **noin 11,50 miljardia euroa vuodessa** suoria yritystukia, energia- ja maataloustukia, järjestöavustuksia (`~7,5 mrd. €`) sekä toimialakohtaisia verotukia (`~4,0 mrd. €`). Kun viralliset avustuspäätökset (`STEA 2026`, `Tutkiavustuksia.fi`, `Business Finland`, `TEM`, `ELY`, `LVM`) yhdistetään Y-tunnuksella (`Modulo-11`-tarkistettu) Verohallinnon yhteisöverotietoihin ja PRH:n YTJ-rekisteriin, paljastuu **1,55–3,00 miljardin euron vuotuinen säästöpotentiaali** ilman leikkauksia kouluihin, sairaaloihin, poliisiin tai maanpuolustukseen:

1. **STEA 2026 Kaikki 686 Järjestöä (`273 912 000 €` / `1 288` myönteistä avustuspäätöstä `1 527` hakemuksesta):**
   * **Jatkuvat `Ak`-toiminta-avustukset:** Tasan **`212 203 929 €` (`77,5 %`)** koko STEA-potista jaetaan jatkuvina yleisluontoisina toiminta-avustuksina pysyville järjestörakenteille.
   * **Muut avustuslajit (`Ay` / `C` / `B`):** `61 708 071 €` (`22,5 %`), josta `Ay`-yleisavustuksia on `58 214 068 €`.
   * **Veronmaksajien tukemat lomajärjestöt (`100 % Ak`):** `Loma ja Terveys ry` (`2 684 710 €`) ja `Hyvinvointilomat ry` (`2 103 947 €`) saavat yhteensä **`4 788 657 €/v`** jatkuvaa toimintatukea.
2. **47 Suomalaisen Suuryrityksen, Tukikohteen ja Nettoveronmaksajaverrokin Verovertailu (`DiD Vero-ROI`):**
   * **Nollaveron tukikohteet (`BLACKLIST_ZOMBIE`):** Yhtiöt, jotka ovat nostaneet miljoonien julkiset avustukset ja pehmolainat maksamatta euroakaan yhteisöveroa 5 vuoden tarkastelujaksolla (mm. `Infinited Fiber Company Oy` `12,4 M€`, `Solar Foods Oyj` `18,2 M€`, `Spinnova Oyj` `14,8 M€`, `P2X Solutions Oy` `26,0 M€`, `Betolar Oyj` `6,9 M€`, `Sulapac Oy` `5,4 M€`, `Woodio Oy` `4,2 M€`, `Meyer Turku Oy` `54,0 M€`, `Finnair Oyj` `85,0 M€`).
   * **Kannattavien suuryritysten säilyttävät kuolleen painon tuet (`DEADWEIGHT_CROWD_OUT`):** Sähköistämistuet, energiatuet ja varustamoiden miehistötuet (`LVM 31.20.43`), joissa kausaalinen `DiD Vero-ROI < 0.50x` (mm. `UPM-Kymmene Oyj` `142 M€`, `Stora Enso Oyj` `96 M€`, `Viking Line Abp` `115 M€`, `Tallink Silja Oy` `98 M€`, `Finnlines Oyj` `65 M€`, `Neste Oyj` `68,5 M€`, `Outokumpu Oyj` `62 M€`, `SSAB Europe Oy` `48 M€`).
   * **Aidot korkean verotuoton T&K-vientiyhtiöt (`POSITIVE_EXTERNALITY_KEEP`) & Nettoveronmaksajaverrokit (`10 kpl`):** Yhtiöt, joiden T&K-toiminta tuottaa moninkertaisen kotimaisen yhteisöverokertymän (`Nokia Oyj`, `Wärtsilä Oyj Abp`, `Konecranes Oyj`, `Vaisala Oyj`, `Patria Oyj`, `Kempower Oyj`, `ICEYE Oy`, `Revenio Group Oyj`, `Bittium Oyj`, `Ponsse Oyj`, `Supercell Oy`, `KONE Oyj`, `Orion Oyj`, `Kesko Oyj`, `Elisa Oyj`).

---

## 2. Tuotanto-ominaisuudet Selainsovelluksessa ja Excelissä

* **Kaksisuuntainen sarakelajittelu (`▲`/`▼`) & välitön CSV-vienti (`UTF-8 BOM`):** Sekä 47 yrityksen kokonaistaulukko että kaikkien 686 STEA-järjestön taulukko ovat lajiteltavissa minkä tahansa sarakkeen mukaan ja vietävissä suoraan `.csv`-tiedostoksi.
* **Suorat URL-syvälinkit (`#corp-<y_tunnus>`, `#stea-<org_id>`, `#ngo-<y_tunnus>`, `#momentti-<idx>`, `#ring-<idx>`):** Jokaisessa modaalissa on `🔗 Kopioi suora linkki` ja `🖨 Tulosta / Tallenna PDF` -toiminto sekä valmis `0,00 €` Julkisuuslain (`621/1999 13 §`) tietopyyntö.

---

## 3. Kääntäminen ja Testaus

```bash
# Käännä kaikki artefaktit (Excel + HTML + Media/VM-muistiot):
PYTHONPATH=src python3 -B -m tukipalkkio_purku.cli

# Aja yksikkötestit:
PYTHONPATH=src python3 -B -m unittest discover -s tests -v
```
