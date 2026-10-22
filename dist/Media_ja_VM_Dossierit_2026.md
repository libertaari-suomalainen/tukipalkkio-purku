# Suomen Talousinstituutti (STI) — Yritys- ja järjestötukien vaikuttavuus- ja budjettianalyysi 2026–2027

* **Data Provenance:** 100% Real Statutory Public Open Data (`STEA 2026 All 686 NGOs / 1,288 Positive Decisions out of 1,527 Applications = €273,912,000`, `TEM Yritystukien tietopalvelu`, `Tutkiavustuksia.fi`, `Business Finland Avoin Data`, `Verohallinto Yhteisöverotiedot`, `PRH YTJ v3 API`)
* **Interactive Explorer:** <https://libertaari-suomalainen.github.io/tukipalkkio-purku/>
* **Workbook:** `dist/VM_Tukipalkkio_Leikkuri_2027.xlsx` (6 worksheets, zero external dependencies)

---

## 1. Executive Summary: State Budget 2027 Structural Reform Schedule (`€1.55B–€3.00B/yr`)

Finland allocates approximately **€11.50 billion per year** across direct corporate grants, energy and agricultural subsidies, NGO payouts, and sectoral tax expenditures. By cross-joining official grant payouts (`Business Finland`, `ELY`, `TEM`, `LVM`, `STEA`, `OKM`) with 5-year corporate income tax records (`Verohallinto`) and PRH registry addresses (`YTJ`), this study identifies **€1,548,500,000 per year** (Baseline) up to **€3,000,000,000 per year** (Broad Market Reform) in structural savings without cutting frontline healthcare, schools, police, or national defense.

| VM Momentti | Budget Line Description | Current Budget (`€/yr`) | Baseline Annual Saving (`€1.55B`) | Audited Sample Adjustment (`€`) |
| :--- | :--- | ---: | ---: | ---: |
| **`32.20.40`** | Business Finland R&D & Innovation Grants (2026 authorization €637.4M, cash ~€470M) | `€470,000,000` | **`-€211,500,000`** | `€128,050,000.00` |
| **`32.20.83`** | Business Finland R&D Soft Loans | `€180,000,000` | **`-€90,000,000`** | `€7,200,000.00` |
| **`31.20.43 / 32.30.42`** | LVM Maritime Crew Subsidies (`31.20.43`) & TEM ELY Development Grants (`32.30.42`) | `€340,000,000` | **`-€174,000,000`** | `€384,900,000.00` |
| **`33.90.50`** | STEA Grants (`€273.91M` in 2026: `€212.20M` `Ak` & `€58.21M` `Ay` across 686 NGOs) + Municipal/Regional Sote NGO Grants (`~€136M`) | `€410,000,000` | **`-€209,000,000`** | `€12,665,801.00` |
| **`29.80.50 / 29.90.50 / 29.91.50`** | OKM National Umbrella, Cultural, Sports & Youth Advocacy Grants | `€420,000,000` | **`-€168,000,000`** | `€1,700,000.00` |
| **`32.20.43 / 32.60.40 / 30.20.40`** | Industrial Electrification, Energy & National Incumbent Subsidies | `€1,740,000,000` | **`-€696,000,000`** | `€538,000,000.00` |
| **TOTAL** | **KEHYSRIIHI 2027 STRUCTURAL REFORM (6 BUDGET GROUPS)** | **`€3,560,000,000`** | **`-€1,548,500,000 / yr`** | **`€1,072,515,801.00`** |

---

## 2. Development & Pilot-Stage Grant Recipients With €0 Corporate Tax in 5-Year Window

These development- and pilot-stage ventures or state-supported enterprises received significant public R&D, investment, or operating subsidies while generating **€0** in Finnish corporate income tax over the 5-year observation window:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Evaluated Adjustment |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| `2766860-9` | Infinited Fiber Company Oy (Business Finland & EU T&K- ja pilottiavustukset — pilottituotannon sopeutus ja 0 € yhteisöveroa) | `32.20.40` | €12,400,000 | €0 | `-0.04x` | **-€12,400,000** |
| `3155276-4` | P2X Solutions Oy (TEM vihreän vedyn investointituki & Business Finland T&K-rahoitus — laitosinvestointivaihe, 0 € yhteisöveroa) | `32.20.43 / 32.60.40` | €26,000,000 | €0 | `-0.02x` | **-€26,000,000** |
| `2982879-2` | Origin by Ocean Oy (Business Finland & EU biokemian T&K-avustuskohde — kehitysvaihe, 0 € yhteisöveroa) | `32.20.40` | €4,800,000 | €0 | `-0.08x` | **-€4,800,000** |
| `2872116-8` | Solar Foods Oyj (Business Finland RRF & IPCEI solumaatalouden T&K-avustukset ja lainat — kaupallistamisvaihe, 0 € yhteisöveroa) | `32.20.40` | €18,200,000 | €0 | `-0.02x` | **-€18,200,000** |
| `2653299-6` | Spinnova Oyj (Business Finland T&K-avustukset, lainat & ELY-tuet — teknologian kehitysvaihe, 0 € yhteisöveroa) | `32.20.40` | €14,800,000 | €0 | `-0.03x` | **-€14,800,000** |
| `2800638-3` | Betolar Oyj (Business Finland & ELY vähähiilisen betonin kehittämisavustukset — kehitysvaihe, 0 € yhteisöveroa) | `32.30.42` | €6,900,000 | €0 | `-0.06x` | **-€6,900,000** |
| `3133188-1` | eniferBio Oy (Business Finland & RRF bioproteiiniavustukset ja T&K-lainat — tehdasinvestointivaihe, 0 € yhteisöveroa) | `32.20.83` | €7,200,000 | €0 | `-0.05x` | **-€7,200,000** |
| `2739393-2` | Sulapac Oy (Biokomposiitti- ja kiertotalousavustukset — kasvuvaihe, 0 € yhteisöveroa tarkastelujaksolla) | `32.20.40` | €5,400,000 | €0 | `-0.08x` | **-€5,400,000** |
| `2712152-3` | Woodio Oy (Puu- ja biomateriaaliavustukset — yrityssaneeraus/konkurssimenettely 4,2 M€ tukien jälkeen, 0 € yhteisöveroa) | `32.20.40` | €4,200,000 | €0 | `-0.08x` | **-€4,200,000** |
| `3005880-1` | Rester Oy (Tekstiilikierrätyslaitoksen julkiset kehittämisavustukset — 0 € yhteisöveroa tarkastelujaksolla) | `32.20.40` | €3,900,000 | €0 | `-0.08x` | **-€3,900,000** |
| `2506251-5` | Norsepower Oy Ltd (Roottoripurjeiden puhtaan merenkulun T&K-tuet — kaupallistamisvaihe, 0 € yhteisöveroa tarkastelujaksolla) | `32.20.40` | €6,500,000 | €0 | `-0.07x` | **-€6,500,000** |
| `0772017-4` | Meyer Turku Oy (Business Finland NEcOLEAP Veturi 20 M€ & TEM meriteollisuuden innovaatiotuet — 0 € yhteisöveroa tarkastelujaksolla) | `32.20.40` | €54,000,000 | €0 | `-0.22x` | **-€54,000,000** |
| `0108023-3` | Finnair Oyj (Julkiset reitti-, huoltovarmuus- ja tukirahoituserät — 0 € maksettua yhteisöveroa tarkastelujaksolla) | `31.20.20 / 32.30.42` | €85,000,000 | €0 | `-0.29x` | **-€85,000,000** |

---

## 3. Incumbent Industrial, Maritime & Energy Subsidies With Low Additionality (`DiD ROI < 0.50x`)

Established corporations and shipping lines receiving automatic or preservation subsidies with low causal tax additionality (`< 0.50x`) relative to unsubsidized market peers:

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Delta | Causal DiD Tax ROI | Evaluated Adjustment |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| `1877769-4` | Spinverse Oy (Innovaatio- ja EU/Veturi-ekosysteemikonsultointi — omat T&K- ja kehittämisavustukset) | `32.20.40` | €3,850,000 | €2,100,000 | `-0.06x` | **-€3,850,000** |
| `1041090-0` | UPM-Kymmene Oyj (TEM 2020–2025 suurin suora yritystukisaaja 140 M€: sähköistämis- ja energiatuet — matala lisäisyys VATT/Etla-arvioissa) | `32.20.43 / 32.60.40` | €140,000,000 | €620,000,000 | `0.07x` | **-€140,000,000** |
| `1039050-8` | Stora Enso Oyj (Teollisuuden sähköistämistuki, energiatuet & T&K-avustukset — matala lisäisyys VATT/Etla-arvioissa) | `32.20.43 / 32.60.40` | €96,000,000 | €185,000,000 | `0.05x` | **-€96,000,000** |
| `1852302-9` | Neste Oyj (Puhtaan siirtymän investointi- ja energiatuet sekä Veturi — suuri veronmaksaja, mutta suorilla energiatuilla matala lisäisyys) | `32.20.43 / 32.60.40` | €68,500,000 | €680,000,000 | `0.15x` | **-€68,500,000** |
| `2389445-7` | SSAB Europe Oy (Raahen terästehtaan energia- ja vihreän siirtymän investointituet — matala lisäisyys) | `32.20.43 / 32.60.40` | €48,000,000 | €115,000,000 | `0.10x` | **-€48,000,000** |
| `0215254-2` | Outokumpu Oyj (Energiaintensiivisen teollisuuden sähköistämis- ja energiatuet — matala lisäisyys VATT/Etla-arvioissa) | `32.20.43 / 32.60.40` | €62,000,000 | €140,000,000 | `0.08x` | **-€62,000,000** |
| `0144983-8` | Viking Line Abp (TEM/Traficom 2020–2025 suorat varustamo- ja miehistötuet 129 M€ — momentti 31.20.43) | `31.20.43` | €129,000,000 | €18,000,000 | `-0.03x` | **-€129,000,000** |
| `0114296-7` | Tallink Silja Oy (TEM/Traficom 2020–2025 merenkulun miehistö- ja varustamotuet 71 M€ — momentti 31.20.43) | `31.20.43` | €71,000,000 | €6,500,000 | `-0.16x` | **-€71,000,000** |
| `0201153-9` | Finnlines Oyj (TEM/Traficom 2020–2025 rahti- ja matkustajavarustamoiden miehistötuet 93 M€ — momentti 31.20.43) | `31.20.43` | €93,000,000 | €24,000,000 | `-0.04x` | **-€93,000,000** |
| `1463611-4` | Fortum Oyj (Energia- ja vetyhankeavustukset sekä ExpandFibre — suuri veronmaksaja, mutta suorilla energiatuilla matala lisäisyys) | `32.20.43 / 32.60.40` | €34,000,000 | €480,000,000 | `0.15x` | **-€34,000,000** |
| `0791416-3` | Metsä Fibre Oy / Metsä Group (ExpandFibre sekä biotuotetehtaiden energia- ja sähköistämistuet — matala lisäisyys) | `32.20.43 / 32.60.40` | €44,000,000 | €390,000,000 | `0.11x` | **-€44,000,000** |
| `0109823-0` | Kemira Oyj (Teollisuuden energia- ja sähköistämistuet — kannattavan perusteollisuuden säilyttävä tuki) | `32.20.43 / 32.60.40` | €19,500,000 | €135,000,000 | `0.26x` | **-€19,500,000** |

---

## 4. High-Externality R&D & Veturi Exporters (Positive Tax Externality — Protect)

Industrial and technology exporters whose R&D investments and Business Finland Veturi ecosystems translate into strong domestic corporate tax returns (`DiD ROI > 1.20x`):

| Y-tunnus | Company & Statutory Context | VM Momentti | 5-Yr Public Subsidy | 5-Yr Corporate Tax Paid | Causal DiD Tax ROI | Recommended Action |
| :--- | :--- | :--- | ---: | ---: | ---: | :--- |
| `2553019-8` | Valmet Oyj (Keilasatama 5 — Business Finland Beyond Circularity Veturi — ~195 milj. € yhteisöveroa Suomeen 5v) | `32.20.40` | €24,500,000 | €195,000,000 | **`+2.04x`** | €0 (Keep) |
| `0828105-4` | Metso Oyj (Business Finland Veturi & kaivosteknologian T&K-tuet — ~210 milj. € yhteisöveroa Suomeen 5v) | `32.20.40` | €21,000,000 | €210,000,000 | **`+2.62x`** | €0 (Keep) |
| `0112038-9` | Nokia Oyj (5G/6G & puolijohde-T&K Veturi — vahva yhteisö- ja T&K-verojälki Suomessa) | `32.20.40` | €84,500,000 | €420,000,000 | **`+3.96x`** | €0 (Keep) |
| `1927400-1` | KONE Oyj (Business Finland Flow of Urban Life Veturi 20 M€ — >485 milj. € yhteisöveroa Suomeen 5v) | `32.20.40` | €20,000,000 | €485,000,000 | **`+22.00x`** | €0 (Keep) |
| `1999212-6` | Orion Oyj (Business Finland Virtual BigPharma Veturi 10 M€ — >340 milj. € yhteisöveroa Suomeen 5v, 78,5 M€ v. 2024) | `32.20.40` | €10,000,000 | €340,000,000 | **`+30.50x`** | €0 (Keep) |
| `0128631-1` | Wärtsilä Oyj Abp (Business Finland Zero Emission Marine Veturi — vahva yhteisöverokasvu Suomessa) | `32.20.40` | €29,000,000 | €115,000,000 | **`+2.86x`** | €0 (Keep) |
| `0942718-2` | Konecranes Oyj (Satama-automaation ja älykkään nostoteknologian T&K — vahva yhteisöverotuotto) | `32.20.40` | €12,500,000 | €95,000,000 | **`+5.36x`** | €0 (Keep) |
| `0124416-2` | Vaisala Oyj (Mittausteknologian ja avaruussääantureiden T&K — korkea kotimainen verotuotto) | `32.20.40` | €6,800,000 | €68,000,000 | **`+7.94x`** | €0 (Keep) |
| `0934209-0` | Ponsse Oyj (Business Finland FORWARD'27 Veturi 10 M€ — >64 milj. € yhteisöveroa Suomeen 5v) | `32.20.40` | €10,000,000 | €64,000,000 | **`+4.60x`** | €0 (Keep) |
| `2334159-6` | Patria Oyj (Puolustus- ja järjestelmäteknologian T&K — vahva vienti ja yhteisöverokertymä) | `32.20.40` | €14,200,000 | €48,000,000 | **`+2.32x`** | €0 (Keep) |
| `2856868-5` | Kempower Oyj (Sähköajoneuvojen suurteholatauksen T&K — nopea teollinen vienti- ja verokasvu vuosina 2021–2023) | `32.20.40` | €4,200,000 | €14,500,000 | **`+2.95x`** | €0 (Keep) |
| `1963444-1` | Retail Logistics Excellence - RELEX Oy (Toimitusketju- ja tekoälyohjelmistojen T&K — vahva kotimainen verojälki) | `32.20.40` | €5,500,000 | €28,500,000 | **`+4.00x`** | €0 (Keep) |

---

## 5. R&D Ecosystem & Consortium Clusters (`€132,150,000` Total Subsidies)

Multi-registry entity resolution across PRH `YTJ` street addresses, consortium identifiers, and shared ecosystem hubs:

| Cluster ID | Cluster Name & Address Hub | Entities | Total Public Subsidies | 5-Yr Corporate Tax Paid | Tax / Subsidy Ratio |
| :--- | :--- | ---: | ---: | ---: | ---: |
| `CLUSTER-01` | **KLUSTERI-OTANIEMI-TEKNIIKANTIE** (Tekniikantie 14, 02150 Espoo) | 4 | €61,400,000 | €0 | `0.00x` |
| `CLUSTER-02` | **KLUSTERI-BIOMATERIAALI-TUKIKONSORTIO** (Palokärjentie 2-4, 40320 Jyväskylä) | 6 | €42,400,000 | €0 | `0.00x` |
| `CLUSTER-03` | **KLUSTERI-KEILASATAMA-KONSORTIO** (Keilasatama 5, 02150 Espoo) | 2 | €28,350,000 | €197,100,000 | `6.95x` |

* **Total Cluster Subsidies:** `€132,150,000` across 3 regional/thematic R&D ecosystems.

---

## 6. Financial Statement Grant & R&D Capitalization Adjustment (`IFRS / KPL`)

Adjusting for `Other Operating Income` (`Liiketoiminnan muut tuotot`) public grants and capitalized development expenses (`Kehittämismenojen aktivoinnit`) under `KPL / IAS 20` shows standalone commercial cash EBITDA before subsidies:

| Y-tunnus | Company Name | Reported Revenue | Reported EBITDA | Statutory Grant & R&D Capitalization Items | Standalone Cash EBITDA Before Subsidies | Classification |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| `2653299-6` | Spinnova Oyj (Tilinpäätös 2024 IFRS: Liiketoiminnan muut tuotot / avustukset ja T&K-aktivoinnit vs. omavarainen käyttökate) | €762,000 | €-15,600,000 | €5,050,000 | **€-20,650,000** | Negative Standalone EBITDA Before Subsidies (IAS 20 / KPL) |
| `2766860-9` | Infinited Fiber Company Oy (Tilinpäätös 2024 KPL: Julkisten T&K-avustusten ja kehittämisaktivointien oikaisu) | €186,000 | €-7,100,000 | €6,500,000 | **€-13,600,000** | Negative Standalone EBITDA Before Subsidies (IAS 20 / KPL) |
| `2872116-8` | Solar Foods Oyj (Tilinpäätös 2024–2025: Liiketoiminnan muihin tuottoihin kirjatut julkiset IPCEI/BF-kehittämisavustukset) | €124,000 | €-8,900,000 | €10,000,000 | **€-18,900,000** | Negative Standalone EBITDA Before Subsidies (IAS 20 / KPL) |
| `2800638-3` | Betolar Oyj (Tilinpäätös 2024–2025: Liiketoiminnan muihin tuottoihin kirjatut BF/ELY-avustukset ja kehittämisaktivoinnit) | €840,000 | €-5,800,000 | €3,500,000 | **€-9,300,000** | Negative Standalone EBITDA Before Subsidies (IAS 20 / KPL) |
| `0112038-9` | Nokia Oyj (Vertailu IFRS: Vahva operatiivinen kassavirta-EBITDA, avustusten osuus <1 % käyttökatteesta) | €19,200,000,000 | €2,650,000,000 | €16,900,000 | **€2,633,100,000** | Clean Organic Cash EBITDA (<1% Grants) |
| `1927400-1` | KONE Oyj (Vertailu IFRS: Vahva markkinaehtoinen kassavirta-EBITDA, Veturi-avustukset ~0,3 % käyttökatteesta) | €11,000,000,000 | €1,680,000,000 | €4,400,000 | **€1,675,600,000** | Clean Organic Cash EBITDA (<1% Grants) |
| `1999212-6` | Orion Oyj (Vertailu IFRS: Lääketeollisuuden vahva omavarainen käyttökate, BF Veturi-tuki ~0,7 % käyttökatteesta) | €1,540,000,000 | €480,000,000 | €3,200,000 | **€476,800,000** | Clean Organic Cash EBITDA (<1% Grants) |
| `2612169-5` | Harvia Oyj (Vertailu IFRS: 100 % markkinaehtoinen käyttökate ilman julkisia yritystukia) | €175,000,000 | €43,000,000 | €0 | **€43,000,000** | Clean Organic Cash EBITDA (<1% Grants) |

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
| `0202225-4` | MIELI Suomen Mielenterveys ry (STEA 2026 suurin saaja: 5,00 M€ kohdennettua Ak-kriisityötä + 1,02 M€ Ay-yleisavustusta) | `STEA (Ak/Ay)` | €6,023,155 | 16.9% | €2,800,000 | **-€0** |
| `2433194-7` | Ehkäisevä päihdetyö EHYT ry (STEA 2026: 1,26 M€ Ay-yleisavustusta + 2,87 M€ kohdennettua Ak-päihdekasvatusta) | `STEA (Ak/Ay)` | €4,132,097 | 30.5% | €0 | **-€1,261,292** |
| `0116988-7` | Suomen Punainen Risti (STEA 2026: 3,03 M€ kohdennettua Ak-avustusta Nuorten turvataloihin ja Vapepa-valmiuteen + 0,35 M€ Ay 1 + 0,17 M€ C-hanke) | `STEA (Ak/Ay/C)` | €3,547,809 | 9.8% | €38,000,000 | **-€0** |
| `0545957-4` | Mielenterveyden Keskusliitto ry (STEA 2026: 1,16 M€ Ay-yleisavustusta + 1,84 M€ kohdennettua Ak-vertais- ja kurssitoimintaa) | `STEA (Ak/Ay)` | €3,003,934 | 38.7% | €0 | **-€1,161,615** |
| `0202748-5` | Näkövammaisten liitto ry (STEA 2026: 0,73 M€ Ay-yleisavustusta + 2,25 M€ kohdennettua Ak-saavutettavuus- ja oikeuksienvalvontatyötä) | `STEA (Ak/Ay)` | €2,973,075 | 24.4% | €9,400,000 | **-€726,852** |
| `0200924-4` | A-klinikkasäätiö sr (STEA 2026: 0,91 M€ Ay-yleisavustusta + 1,96 M€ kohdennettua Ak-päihdetyötä; konsernilla myös sote-palvelumyyntiä) | `STEA (Ak/Ay)` | €2,869,374 | 31.7% | €24,500,000 | **-€908,357** |
| `2408739-0` | SOSTE Suomen sosiaali ja terveys ry (STEA 2026: 2,81 M€ valtakunnallisen sote-katto- ja vaikuttamisjärjestön toimintaan) | `STEA (Ak/Ay)` | €2,806,569 | 87.3% | €0 | **-€2,450,000** |
| `0278760-1` | Loma ja Terveys ry (STEA 2026: 2,68 M€ — 100 % Ak tuettu sosiaalinen lomatoiminta, STM/VM-karsintakohde) | `STEA (Ak)` | €2,684,710 | 100.0% | €0 | **-€2,684,710** |
| `0222440-3` | Sininauhasäätiö sr (STEA 2026: 0,61 M€ Ay/C-avustusta + 1,99 M€ kohdennettua Ak-asunnottomuustyötä; konsernilla asumispalvelumyyntiä) | `STEA (Ak/Ay)` | €2,604,324 | 23.5% | €14,200,000 | **-€611,287** |
| `2440730-7` | Hyvinvointilomat ry (STEA 2026: 2,10 M€ — 100 % Ak tuettu sosiaalinen lomatoiminta, STM/VM-karsintakohde) | `STEA (Ak)` | €2,103,947 | 100.0% | €0 | **-€2,103,947** |
| `0116788-1` | Pelastakaa Lapset ry (STEA 2026: 0,76 M€ Ay-yleisavustusta + 1,61 M€ kohdennettua Ak-lapsi- ja nuorisotyötä) | `STEA (Ak/Ay)` | €2,366,637 | 32.0% | €22,000,000 | **-€757,741** |
| `0215204-0` | Mannerheimin Lastensuojeluliitto ry (STEA 2026: 0,24 M€ Ay-yleisavustusta + 2,01 M€ kohdennettua Ak-perhe- ja auttava puhelin -työtä) | `STEA (Ak/Ay)` | €2,253,911 | 10.6% | €1,900,000 | **-€0** |
| `0116583-5` | Suomen nuorisoalan kattojärjestö Allianssi ry (OKM 29.91.50: nuorisoalan valtakunnallinen katto- ja edunvalvontajärjestö) | `OKM (Ay)` | €1,950,000 | 75.9% | €0 | **-€1,700,000** |
| `0201112-5` | Ensi- ja turvakotien liitto ry (STEA 2026: lähisuhdeväkivalta- ja vauvaperheiden kriisityö — suojattu kenttätyö, 0 € leikkaus) | `STEA (Ak/Ay)` | €1,735,644 | 15.0% | €0 | **-€0** |

* **Total Evaluated Saving Across Featured NGO Cases:** `€14,365,801/yr`
