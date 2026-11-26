# Tentamenstrening – kapittel 1–3
## Lærerveiledning · T-matte 1T

<div class="home-hero">
  <p class="eyebrow">2-TIMERS ØKT · LÆRERUTGAVE</p>
  <h2>Fra tallmengder til funksjoner</h2>
  <p>Samme oppgaver og rekkefølge som elevheftet. Med løsningsforslag og observasjonspunkter.</p>
</div>

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

!!! note "Oppgave 1 – fasit"

    a) \(7\): \(\mathbb N\).  

    b) \(-4\): \(\mathbb Z\).  

    c) \(\frac35\): \(\mathbb Q\).  

    d) \(\sqrt2\): \(\mathbb R\), men ikke \(\mathbb Q\).  

    e) \(0\): \(\mathbb N\), etter konvensjonen i elevheftet.  

    f) \(-12/3=-4\): \(\mathbb Z\).

!!! note "Oppgave 2 – fasit"

    a) Sant: heltall kan skrives som brøk med nevner 1.  

    b) Usant: \(1/2\) er rasjonalt, men ikke heltall.  

    c) Sant: \(\sqrt9=3\).  

    d) Usant: \(\pi\) er irrasjonalt.  

    e) Sant: tallmengdene er nøstet; et naturlig tall er også heltall, rasjonalt og reelt.

!!! note "Oppgave 3 – fasit"

    a) \(2\leq x<7\).  

    b) \(2\leq x<7\).  

    c) \(\{2,3,4,5,6\}\).  
    Viktig: 2 er inkludert, 7 er ikke inkludert.

!!! note "Oppgave 4 – fasit"

    a) \(-2\leq x<3\), listeform \(\{-2,-1,0,1,2\}\).  

    b) \(1<x\leq6\), listeform \(\{2,3,4,5,6\}\) for heltall.  

    c) \([-3,2]\), ulikhet \(-3\leq x\leq2\).  

    d) \((4,\infty)\), ulikhet \(x>4\), heltallene \(\{5,6,7,\ldots\}\).

!!! note "Oppgave 5 – fasit"

    a) 4 skal ikke være med fordi høyre endepunkt er åpent.  

    b) \(\{-2,-1,0,1,2,3\}\).  

    c) Lukket endepunkt betyr inkludert; åpent betyr ekskludert.

## Oppgave 6–8 – Figurtall

!!! note "Oppgave 6 – fasit"
    Figuren gir 1, 3, 5, 7 brikker.  

    a) 1, 3, 5, 7.  

    b) Tallfølgen \(1,3,5,7,\ldots\).  

    c) Figur 8: \(2\cdot8-1=15\).  

    d) \(F(n)=2n-1\). Det legges til 2 brikker for hver ny figur.

!!! note "Oppgave 7 – fasit"

    a) 1, 4, 9.  

    b) Figur 5: \(5^2=25\).  

    c) \(F(n)=n^2\).  

    d) Differansene er 3, 5, 7, 9, ... og øker med 2; økningen er ikke konstant.

!!! note "Oppgave 8 – fasit"

    a) Differansen er 3.  

    b) \(a_n=3n+1\).  

    c) \(3n+1=40\Rightarrow n=13\).  

    d) Nei. \(3n+1=41\Rightarrow n=40/3\), ikke et helt figurnummer.

## Oppgave 9–12 – Programmering

!!! note "Oppgave 9 – fasit"

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

!!! note "Oppgave 10 – fasit"

    a) Skriver ut 2, 6, 12, 20, 30.  

    b) \(n\) er parameteren/figurindeksen.  

    c) Bruk \(range(1, 11)\).  

    d) Funksjonen samler regelen ett sted og kan brukes med flere verdier.

!!! note "Oppgave 11 – fasit"

    a) Skriver ut 1, 4, 9, 16.  

    b) Øvre grense i \(range\) er ikke med.  

    c) Bruk \(range(1, 6)\).

!!! note "Oppgave 12 – fasit"

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

!!! note "Oppgave 13 – fasit"

    a) Førstegrad.

    b) Andregrad.

    c) Tredjegrad.

    d) Tredjegrad. Graden bestemmes av høyeste eksponent, uavhengig av rekkefølgen på leddene.

!!! note "Oppgave 14 – fasit"

    a) A.

    b) B.

    c) C.

    d) B har bunnpunkt.

    e) En andregradsfunksjon har et \(x^2\)-ledd med koeffisient ulik null; grafen er en parabel.

!!! note "Oppgave 15 – fasit"

    a)
    | \(x\) | -1 | 0 | 1 | 2 | 3 |
    |---|---:|---:|---:|---:|---:|
    | \(f(x)\) | -6 | -4 | -2 | 0 | 2 |

    b) Rett linje gjennom punktene.  

    c) Skjæring med y-aksen: \((0,-4)\).  

    d) Nullpunkt: \(x=2\), punktet \((2,0)\).  

    e) Når x øker med 1, øker funksjonsverdien med 2.

!!! note "Oppgave 16 – fasit"

    a) For \(x=-3,-2,-1,0,1,2,3\) får vi \(5,0,-3,-4,-3,0,5\).  

    b) \(x^2-4=(x-2)(x+2)=0\), nullpunktene er \(-2\) og \(2\).  

    c) Bunnpunkt \((0,-4)\).  

    d) Parabel gjennom tabellpunktene.  

    e) \(g(-x)=g(x)\), derfor er grafen symmetrisk om y-aksen.

!!! note "Oppgave 17 – fasit"

    a) \(h(-2)=-2\), \(h(-1)=2\), \(h(0)=0\), \(h(1)=-2\), \(h(2)=2\).  

    b) \(h(x)=x(x^2-3)\). Nullpunktene er \(-\sqrt3,0,\sqrt3\).  

    c) Skissen krysser x-aksen i disse tre nullpunktene og går gjennom tabellpunktene.  

    d) Når \(x\to-\infty\), går \(h(x)\to-\infty\); når \(x\to\infty\), går \(h(x)\to\infty\).

!!! note "Oppgave 18 – fasit"

    a) \(f\) førstegrad, \(g\) andregrad, \(h\) tredjegrad.  

    b) \(f(2)=5\), \(g(2)=5\), \(h(2)=9\).  

    c) Alle tre går gjennom \((0,1)\).  

    d) Konstantleddet bestemmer y-akseskjæringen, mens de andre leddene former grafen.

## Oppgave 19–21 – Modellering

!!! note "Oppgave 19 – fasit"

    a) \(P(x)=75+18x\).  

    b) \(P(12)=291\) kr.  

    c) \(75+18x=300\Rightarrow x=12,5\) km.  

    d) 75 kr er startpris; 18 kr er pris per kilometer.

!!! note "Oppgave 20 – fasit"

    a) Høyden øker, når et toppunkt og avtar; en parabel kan modellere dette.  

    b) \(H(0)=1\) meter.  

    c) Toppunkt ved \(t=-\frac{20}{2(-5)}=2\) sekunder.  

    d) \(H(2)=-20+40+1=21\) meter.  

    e) Negativ høyde er ikke fysisk mulig; modellen gjelder bare i et begrenset tidsrom.

!!! note "Oppgave 21 – fasit"

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
