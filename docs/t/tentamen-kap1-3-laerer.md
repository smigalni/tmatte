<div class="print-cover" aria-label="MathPlatform">
  <div class="print-cover__identity">
    <div class="print-cover__mark">M</div>
    <div class="print-cover__name">MathPlatform</div>
    <div class="print-cover__tagline">Matematikk · forståelse · mestring</div>
  </div>
</div>

<div class="chapter-toolbar" markdown="1">
  <span class="chapter-label">MATHPLATFORM · T-MATTE · TENTAMEN KAPITTEL 1–3 · LÆRER</span>
  <button class="print-button" type="button" data-print-page>Skriv ut lærerveiledningen</button>
</div>

# Tentamenstrening – kapittel 1–3

**Lærerveiledning · T-matte 1T · 2-timers økt**

## Forslag til tidsplan

| Tid | Oppgaver | Hovedfokus |
|---|---|---|
| 0–25 min | 1–5 | Tallmengder og intervaller |
| 25–45 min | 6–8 | Figurtall og generalisering |
| 45–65 min | 9–12 | Programmering |
| 65–100 min | 13–18 | Funksjonsgrad og grafer |
| 100–115 min | 19–20 | Modellering |
| 115–120 min | 21 / oppsummering | Hva må repeteres? |

Eleven er usikker og blander begreper. Be eleven forklare før du gir hint. Noter *hvilken* misforståelse som oppstår, ikke bare om svaret er feil. Oppgavene 1–20 er kjernen; oppgave 21 er ekstra.

## Oppgave 1–5 – Tallmengder og intervaller

!!! note "Oppgave 1.1.1 – fasit"

    a) \(7\): \(\mathbb N\).  

    b) \(-4\): \(\mathbb Z\).  

    c) \(\frac35\): \(\mathbb Q\).  

    d) \(\sqrt2\): \(\mathbb R\), men ikke \(\mathbb Q\).  

    e) \(0\): \(\mathbb N\), etter konvensjonen i elevheftet.  

    f) \(-12/3=-4\): \(\mathbb Z\).

!!! note "Oppgave 1.1.2 – fasit"

    a) Sant: heltall kan skrives som brøk med nevner 1.  

    b) Usant: \(1/2\) er rasjonalt, men ikke heltall.  

    c) Sant: \(\sqrt9=3\).  

    d) Usant: \(\pi\) er irrasjonalt.  

    e) Sant: tallmengdene er nøstet; et naturlig tall er også heltall, rasjonalt og reelt.

!!! note "Oppgave 1.1.3 – fasit"

    a) \(2\leq x<7\).

    b) Intervallnotasjon: \([2,7[\). Den venstre klammen viser at 2 er med; den høyre, vendte klammen viser at 7 ikke er med.

    c) \(\{2,3,4,5,6\}\).

!!! note "Oppgave 1.1.4 – fasit"

    a) Ulikhet: \(-2\leq x<3\). Intervall: \([-2,3[\). Listeform: \(\{-2,-1,0,1,2\}\).

    b) Ulikhet: \(1<x\leq6\). Intervall: \(]1,6]\). Listeform: \(\{2,3,4,5,6\}\).

    c) Ulikhet: \(-3\leq x\leq2\). Intervall: \([-3,2]\). Listeform: \(\{-3,-2,-1,0,1,2\}\).

    d) Ulikhet: \(x>4\). Intervall: \(]4,\infty[\). Heltallene er \(\{5,6,7,\ldots\}\). Pil mot høyre viser at intervallet fortsetter uten øvre grense.

!!! note "Oppgave 1.1.5 – fasit"

    a) Ulikheten er riktig. Feilen er at 4 er tatt med i listeformen, selv om \(x<4\).

    b) \(\{-2,-1,0,1,2,3\}\).

    c) Intervallnotasjon: \([-2,4[\). Den venstre klammen betyr at \(-2\) er med. Den høyre, vendte klammen betyr at 4 ikke er med.

## Oppgave 6–8 – Figurtall

!!! note "Oppgave 2.1.1 – fasit"
    Figuren gir 1, 3, 5, 7 brikker.  

    a) 1, 3, 5, 7.  

    b) Tallfølgen \(1,3,5,7,\ldots\).  

    c) Figur 8: \(2\cdot8-1=15\).  

    d) \(F(n)=2n-1\). Det legges til 2 brikker for hver ny figur.

!!! note "Oppgave 2.1.2 – fasit"

    a) 2, 6, 12, 20 prikker.

    b) Figur 5 har \(5\cdot6=30\) prikker.

    c) Figur \(n\) har \(n\) rader og \(n+1\) kolonner:
    \[
    F(n)=n(n+1).
    \]

    d) Differansene er 4, 6, 8, 10, ... Økningen fra figur til figur blir 2 større hver gang.

!!! note "Oppgave 2.1.3 – fasit"

    a) Differansen er 3.  

    b) \(a_n=3n+1\).  

    c) \(3n+1=40\Rightarrow n=13\).  

    d) Nei. \(3n+1=41\Rightarrow n=40/3\), ikke et helt figurnummer.

## Oppgave 9–12 – Programmering

!!! note "Oppgave 2.2.1 – fasit"

    a) \(n=1,2,3,4\).  

    b) total blir 2, 6, 12, 20.  

    c) Skriver ut 20.  

    d)
    ~~~python
    total = 0
    for n in range(1, 11):
        total = total + 2*n
    print(total)
    ~~~
    Resultatet er 110.

!!! note "Oppgave 2.2.2 – fasit"

    a) Skriver ut 2, 6, 12, 20, 30.  

    b) \(n\) er parameteren/figurindeksen.  

    c) Bruk \(range(1, 11)\).  

    d) Funksjonen samler regelen ett sted og kan brukes med flere verdier.

!!! note "Oppgave 2.2.3 – fasit"

    a) Skriver ut 1, 4, 9, 16.  

    b) Øvre grense i \(range\) er ikke med.  

    c) Bruk \(range(1, 6)\).

!!! note "Oppgave 2.2.4 – fasit"

    a) \(T(1)=1,T(2)=3,T(3)=6,T(4)=10,T(5)=15\).  

    b)
    ~~~python
    def T(n):
        return n*(n+1)/2

    for n in range(1, 6):
        print(T(n))
    ~~~

    c) \(T(20)=20\cdot21/2=210\). Spør gjerne hvorfor formelen deler på 2.

## Oppgave 13–18 – Funksjoner

!!! note "Oppgave 3.1.1 – fasit"

    a) Høyeste eksponent er 1. Funksjonen er førstegrad.

    b) Høyeste eksponent er 2. Funksjonen er andregrad.

    c) Høyeste eksponent er 3. Funksjonen er tredjegrad.

    d) Skriv gjerne uttrykket i synkende rekkefølge først:
    \[
    p(x)=x^3-3x^2+7.
    \]
    Høyeste eksponent er 3. Funksjonen er tredjegrad. Rekkefølgen leddene står i, endrer ikke graden.

!!! note "Oppgave 3.1.2 – fasit"

    a) Graf A er førstegrad: grafen er en rett linje.

    b) Graf B er andregrad: grafen er en parabel.

    c) Graf C er tredjegrad: den kubiske kurven går ned mot venstre og opp mot høyre.

    d) Graf B har et bunnpunkt.

    e) Graf B er en parabel og har en krum form. En førstegradsfunksjon har alltid en rett linje som graf.

!!! note "Oppgave 3.1.3 – fasit"

    a)
    \[
    \begin{aligned}
    f(-1)&=-6,\\
    f(0)&=-4,\\
    f(1)&=-2,\\
    f(2)&=0,\\
    f(3)&=2.
    \end{aligned}
    \]

    b) Rett linje gjennom punktene \((-1,-6)\), \((0,-4)\), \((1,-2)\), \((2,0)\) og \((3,2)\).

    c) Skjæring med y-aksen: \((0,-4)\).  

    d) Nullpunkt: \(x=2\), punktet \((2,0)\).  

    e) Når x øker med 1, øker funksjonsverdien med 2.

!!! note "Oppgave 3.1.4 – fasit"

    a) For \(x=-3,-2,-1,0,1,2,3\) får vi \(5,0,-3,-4,-3,0,5\).  

    b) \(x^2-4=(x-2)(x+2)=0\), nullpunktene er \(-2\) og \(2\).  

    c) Bunnpunkt \((0,-4)\).  

    d) Parabel gjennom tabellpunktene.  

    e) \(g(-x)=g(x)\), derfor er grafen symmetrisk om y-aksen.

!!! note "Oppgave 3.1.5 – fasit"

    a) \(h(-2)=-2\), \(h(-1)=2\), \(h(0)=0\), \(h(1)=-2\), \(h(2)=2\).  

    b) \(h(x)=x(x^2-3)\). Nullpunktene er \(-\sqrt3,0,\sqrt3\).  

    c) Skissen krysser x-aksen i disse tre nullpunktene og går gjennom tabellpunktene.  

    d) Når \(x\to-\infty\), går \(h(x)\to-\infty\); når \(x\to\infty\), går \(h(x)\to\infty\).

!!! note "Oppgave 3.1.6 – fasit"

    a) \(f\) førstegrad, \(g\) andregrad, \(h\) tredjegrad.  

    b) \(f(2)=5\), \(g(2)=5\), \(h(2)=9\).  

    c) Alle tre går gjennom \((0,1)\).  

    d) Konstantleddet bestemmer y-akseskjæringen, mens de andre leddene former grafen.

## Oppgave 19–21 – Modellering

!!! note "Oppgave 3.2.1 – fasit"

    a) \(P(x)=75+18x\).  

    b) \(P(12)=291\) kr.  

    c) \(75+18x=300\Rightarrow x=12,5\) km.  

    d) 75 kr er startpris; 18 kr er pris per kilometer.

!!! note "Oppgave 3.2.2 – fasit"

    a) Høyden øker, når et toppunkt og avtar; en parabel kan modellere dette.  

    b) \(H(0)=1\) meter.  

    c) Toppunkt ved \(t=-\frac{20}{2(-5)}=2\) sekunder.  

    d) \(H(2)=-20+40+1=21\) meter.  

    e) Negativ høyde er ikke fysisk mulig; modellen gjelder bare i et begrenset tidsrom.

!!! note "Oppgave 3.2.3 – fasit"

    a) \(p(x)=x(x-2)(x+2)\).  

    b) Nullpunktene er \(-2,0,2\).  

    c) Alle tre funksjonsverdiene er 0.  

    d) Grafen krysser x-aksen i hvert av disse enkle nullpunktene.

## Observasjonsskjema

| Område | Mestring | Konkret feil / notat |
|---|---|---|
| Tallmengder | ☐ Sikker ☐ Usikker | |
| Intervaller | ☐ Sikker ☐ Usikker | |
| Figurtall | ☐ Sikker ☐ Usikker | |
| Programmering | ☐ Sikker ☐ Usikker | |
| Førstegrad | ☐ Sikker ☐ Usikker | |
| Andregrad | ☐ Sikker ☐ Usikker | |
| Tredjegrad | ☐ Sikker ☐ Usikker | |
| Modellering | ☐ Sikker ☐ Usikker | |

Etter timen: velg 3–5 hjemmeoppgaver fra områdene der eleven faktisk gjorde feil. Ikke gi mer av alt; gi målrettet repetisjon.
