# Tentamenstrening – kapittel 1–3
## Elevhefte · T-matte 1T

<div class="home-hero">
  <p class="eyebrow">2-TIMERS ØKT · TENTAMEN</p>
  <h2>Fra tallmengder til funksjoner</h2>
  <p>Tren på begreper, figurer, programmering og funksjoner.</p>
</div>

## Målet med økten
Du skal kunne plassere tall i tallmengdene, skrive intervaller på ulike måter, finne regler for figurtall, følge enkel kode og tolke første-, andre- og tredjegradsfunksjoner.

Skriv mellomregning. Når du leser en figur, forklar hva du ser.

## Del 1 – Tallmengder og intervaller

!!! important "Tallmengdene"
    \[
    \mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}
    \]
    \(\mathbb N\): naturlige tall (her inkluderer vi 0).  
    \(\mathbb Z\): heltall.  
    \(\mathbb Q\): rasjonale tall, kan skrives som brøk.  
    \(\mathbb R\): reelle tall, alle tall på tallinja.

!!! question "Oppgave 1 – Hvilken tallmengde?"
    Oppgi den minste tallmengden tallet tilhører.

    a) \(7\)

    b) \(-4\)

    c) \(\frac35\)

    d) \(\sqrt2\)

    e) \(0\)

    f) \(-\frac{12}{3}\).

!!! question "Oppgave 2 – Sant eller usant?"
    Begrunn kort.

    a) Alle heltall er rasjonale tall.

    b) Alle rasjonale tall er heltall.

    c) \(\sqrt9\) er et naturlig tall.

    d) \(\pi\) er rasjonalt.

    e) Et tall kan tilhøre flere tallmengder samtidig.

!!! question "Oppgave 3 – Les av intervallet"
    <svg viewBox="0 0 620 100" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs><marker id="numberline-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto-start-reverse"><path d="M0 0L7 3.5L0 7Z" fill="currentColor"/></marker></defs>
      <line x1="35" y1="42" x2="585" y2="42" stroke="currentColor" stroke-width="2" marker-start="url(#numberline-arrow)" marker-end="url(#numberline-arrow)"/>
      <g stroke="currentColor"><path d="M35 36v12 M90 36v12 M145 36v12 M200 36v12 M255 36v12 M310 36v12 M365 36v12 M420 36v12 M475 36v12 M530 36v12 M585 36v12"/></g>
      <g fill="currentColor" font-size="12" text-anchor="middle"><text x="35" y="65">0</text><text x="90" y="65">1</text><text x="145" y="65">2</text><text x="200" y="65">3</text><text x="255" y="65">4</text><text x="310" y="65">5</text><text x="365" y="65">6</text><text x="420" y="65">7</text><text x="475" y="65">8</text><text x="530" y="65">9</text><text x="585" y="65">10</text><text x="600" y="28" font-style="italic">x</text></g>
      <line x1="145" y1="42" x2="420" y2="42" stroke="#168b83" stroke-width="7"/>
      <circle cx="145" cy="42" r="6" fill="#168b83" stroke="#168b83" stroke-width="3"/><circle cx="420" cy="42" r="6" fill="white" stroke="#168b83" stroke-width="3"/>
    </svg>

    a) Skriv som ulikhet.

    b) Forklar hvorfor 2 er med, mens 7 ikke er med.

    c) Skriv listeform for heltallene.

!!! question "Oppgave 4 – Oversett"
    Skriv listeform (heltall) og tegn hvert intervall på tallinja.

    a) \(-2\leq x<3\)

    b) \(1<x\leq6\)

    c) Alle heltall fra og med \(-3\) til og med \(2\).

    d) \(x>4\). Forklar hvorfor listeformen ikke er endelig.

!!! question "Oppgave 5 – Finn feilen"
    En elev skriver \(-2\leq x<4,\quad \{-2,-1,0,1,2,3,4\}\).

    a) Hva er feil?

    b) Skriv riktig listeform for heltall.

    c) Forklar åpent og lukket endepunkt.

## Del 2 – Figurtall

!!! important "Fra figur til formel"
    Se etter hvor mange elementer som legges til for hver ny figur. Er økningen konstant? Kan antallet i figur \(n\) beskrives med en formel?

!!! question "Oppgave 6 – Tell og generaliser"
    Hver prikk er én brikke.
    <svg viewBox="0 0 620 145" width="100%" xmlns="http://www.w3.org/2000/svg">
      <g fill="#168b83">
        <circle cx="65" cy="30" r="6"/>
        <circle cx="205" cy="20" r="6"/><circle cx="205" cy="45" r="6"/><circle cx="230" cy="45" r="6"/>
        <circle cx="350" cy="15" r="6"/><circle cx="350" cy="40" r="6"/><circle cx="350" cy="65" r="6"/><circle cx="375" cy="65" r="6"/><circle cx="400" cy="65" r="6"/>
        <circle cx="500" cy="10" r="6"/><circle cx="500" cy="35" r="6"/><circle cx="500" cy="60" r="6"/><circle cx="500" cy="85" r="6"/><circle cx="525" cy="85" r="6"/><circle cx="550" cy="85" r="6"/><circle cx="575" cy="85" r="6"/>
      </g>
      <g fill="currentColor" font-size="12" text-anchor="middle"><text x="65" y="125">Figur 1</text><text x="218" y="125">Figur 2</text><text x="375" y="125">Figur 3</text><text x="540" y="125">Figur 4</text></g>
    </svg>

    a) Tell brikkene i figur 1–4.

    b) Skriv tallfølgen.

    c) Hvor mange brikker har figur 8?

    d) Finn en formel for figur \(n\).

!!! question "Oppgave 7 – Kvadrattall"
    <svg viewBox="0 0 620 125" width="100%" xmlns="http://www.w3.org/2000/svg">
      <g fill="#168b83">
        <circle cx="70" cy="25" r="5"/>
        <circle cx="220" cy="15" r="5"/><circle cx="240" cy="15" r="5"/><circle cx="220" cy="35" r="5"/><circle cx="240" cy="35" r="5"/>
        <circle cx="370" cy="5" r="5"/><circle cx="390" cy="5" r="5"/><circle cx="410" cy="5" r="5"/><circle cx="370" cy="25" r="5"/><circle cx="390" cy="25" r="5"/><circle cx="410" cy="25" r="5"/><circle cx="370" cy="45" r="5"/><circle cx="390" cy="45" r="5"/><circle cx="410" cy="45" r="5"/>
      </g>
      <g fill="currentColor" font-size="12" text-anchor="middle"><text x="70" y="95">Figur 1</text><text x="230" y="95">Figur 2</text><text x="390" y="95">Figur 3</text></g>
    </svg>

    a) Skriv antall prikker i figur 1–3.

    b) Finn antallet i figur 5.

    c) Finn formelen for figur \(n\).

    d) Hvorfor er økningen ikke konstant?

!!! question "Oppgave 8 – Lag en regel"
    Et mønster har antall brikker \(4,7,10,13,\ldots\).

    a) Finn differansen.

    b) Finn formelen for ledd \(n\), der første ledd er \(n=1\).

    c) Hvilket figurnummer har 40 brikker?

    d) Kan mønsteret ha 41 brikker?

## Del 3 – Programmering

!!! important "Les kode systematisk"
    Følg programmet linje for linje. Noter verdiene til variablene etter hver runde. Husk at øvre grense i Python sin \(range\) ikke er med.

!!! question "Oppgave 9 – Følg løkka"
    ~~~python
    total = 0
    for n in range(1, 5):
        total = total + 2*n
    print(total)
    ~~~

    a) Hvilke verdier får \(n\)?

    b) Skriv verdien til total etter hver runde.

    c) Hva skrives ut?

    d) Endre programmet slik at det summerer partallene fra 2 til 20.

!!! question "Oppgave 10 – Programmer figurtall"
    Et figurtall er gitt ved \(F(n)=n^2+n\).
    ~~~python
    def F(n):
        return n*n + n

    for n in range(1, 6):
        print(F(n))
    ~~~

    a) Hva skriver programmet ut?

    b) Hva betyr parameteren \(n\)?

    c) Endre programmet til figur 1–10.

    d) Hvorfor er det nyttig å lage en funksjon?

!!! question "Oppgave 11 – Finn kodefeilen"
    Målet er å skrive ut kvadrattallene fra 1 til 5.
    ~~~python
    for n in range(1, 5):
        print(n*n)
    ~~~

    a) Hva skrives ut?

    b) Hvorfor mangler ett tall?

    c) Rett programmet.

!!! question "Oppgave 12 – Trekanttall"
    \(T(n)=\frac{n(n+1)}2\).

    a) Kontroller at de fem første verdiene er \(1,3,6,10,15\).

    b) Skriv kode som skriver ut de fem første verdiene.

    c) Finn \(T(20)\).

## Del 4 – Første-, andre- og tredjegradsfunksjoner

!!! important "Kjennetegn"
    Førstegrad: \(f(x)=ax+b\), rett linje.  
    Andregrad: \(f(x)=ax^2+bx+c\), parabel.  
    Tredjegrad: \(f(x)=ax^3+bx^2+cx+d\), kubisk kurve.

!!! question "Oppgave 13 – Bestem graden"

    a) \(f(x)=4x-7\)

    b) \(g(x)=2x^2-5x+1\)

    c) \(h(x)=-x^3+4x\)

    d) \(p(x)=7-3x^2+x^3\). Begrunn med høyeste eksponent.

!!! question "Oppgave 14 – Les av grafene"
    <svg viewBox="0 0 620 220" width="100%" xmlns="http://www.w3.org/2000/svg">
      <g stroke="currentColor" opacity=".22"><path d="M20 25H195 M20 65H195 M20 105H195 M20 145H195 M20 185H195 M60 10V195 M100 10V195 M140 10V195 M180 10V195 M220 25H395 M220 65H395 M220 105H395 M220 145H395 M220 185H395 M260 10V195 M300 10V195 M340 10V195 M380 10V195 M420 25H595 M420 65H595 M420 105H595 M420 145H595 M420 185H595 M460 10V195 M500 10V195 M540 10V195 M580 10V195"/></g>
      <defs><marker id="graph-axis-arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="currentColor"/></marker></defs>
      <g stroke="currentColor" stroke-width="1.5" fill="none">
        <path d="M20 105H195 M100 195V10 M220 105H395 M300 195V10 M420 105H595 M500 195V10" marker-end="url(#graph-axis-arrow)"/>
      </g>
      <g fill="currentColor" font-size="11" font-style="italic">
        <text x="185" y="98">x</text><text x="106" y="18">y</text>
        <text x="385" y="98">x</text><text x="306" y="18">y</text>
        <text x="585" y="98">x</text><text x="506" y="18">y</text>
      </g>
      <path d="M30 175L180 35" fill="none" stroke="#168b83" stroke-width="3"/>
      <path d="M235 35Q300 205 385 35" fill="none" stroke="#168b83" stroke-width="3"/>
      <path d="M430 175C465 175 470 105 500 105C530 105 535 35 585 35" fill="none" stroke="#168b83" stroke-width="3"/>
      <g fill="currentColor" font-size="13" text-anchor="middle"><text x="100" y="215">A</text><text x="300" y="215">B</text><text x="500" y="215">C</text></g>
    </svg>

    a) Hvilken er førstegrad?

    b) Hvilken er andregrad?

    c) Hvilken er tredjegrad?

    d) Hvilken har bunnpunkt?

    e) Hvorfor kan ikke en rett linje være en andregradsfunksjon?

!!! question "Oppgave 15 – Førstegrad"
    \(f(x)=2x-4\).

    a) Fyll ut tabellen for \(x=-1,0,1,2,3\).
    | \(x\) | -1 | 0 | 1 | 2 | 3 |
    |---|---:|---:|---:|---:|---:|
    | \(f(x)\) | | | | | |

    b) Tegn grafen.

    c) Finn skjæringen med y-aksen.

    d) Finn nullpunktet.

    e) Forklar stigningstallet.

!!! question "Oppgave 16 – Andregrad"
    \(g(x)=x^2-4\).

    a) Regn ut funksjonsverdiene for \(x=-3,-2,-1,0,1,2,3\).

    b) Finn nullpunktene.

    c) Finn bunnpunktet.

    d) Tegn grafen.

    e) Hvorfor er grafen symmetrisk om y-aksen?

!!! question "Oppgave 17 – Tredjegrad"
    \(h(x)=x^3-3x\).

    a) Regn ut \(h(-2),h(-1),h(0),h(1),h(2)\).

    b) Faktoriser og finn nullpunktene.

    c) Skisser grafen.

    d) Hva skjer med grafen når \(x\) går mot store negative og positive verdier?

!!! question "Oppgave 18 – Sammenlign"
    \(f(x)=2x+1,\quad g(x)=x^2+1,\quad h(x)=x^3+1\).

    a) Bestem graden.

    b) Regn ut alle tre for \(x=2\).

    c) Hvilke går gjennom \((0,1)\)?

    d) Forklar hvorfor samme konstantledd ikke gir samme graf.

## Del 5 – Blandede utfordringer

!!! question "Oppgave 19 – Fra tekst til funksjon"
    En taxi tar 75 kr i startpris og 18 kr per kilometer.

    a) Sett opp \(P(x)\).

    b) Hva koster 12 km?

    c) Hvor langt kan du kjøre for 300 kr?

    d) Forklar hva tallene i formelen betyr.

!!! question "Oppgave 20 – Andregradsmodell"
    En ballhøyde er modellert ved \(H(t)=-5t^2+20t+1\).

    a) Hvorfor passer en andregradsfunksjon?

    b) Finn starthøyden.

    c) Når er høyden størst?

    d) Finn maksimal høyde.

    e) Hva betyr negativ høyde i modellen?

!!! question "Oppgave 21 – Ekstra"
    \(p(x)=x^3-4x\).

    a) Faktoriser.

    b) Finn nullpunktene.

    c) Regn ut \(p(-2),p(0),p(2)\).

    d) Hvorfor krysser grafen x-aksen i nullpunktene?

## Egenvurdering
- [ ] Jeg kan skille mellom \(\mathbb N,\mathbb Z,\mathbb Q,\mathbb R\).
- [ ] Jeg kan skrive intervaller på ulike måter.
- [ ] Jeg kan finne en formel for et figurtall.
- [ ] Jeg kan følge og rette enkel kode.
- [ ] Jeg kan kjenne igjen og tolke første-, andre- og tredjegradsfunksjoner.
- [ ] Jeg kan bruke en funksjon til å modellere en situasjon.

Marker oppgavene du var usikker på. De brukes til å planlegge neste økt.
