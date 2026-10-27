# 2 Algebra

## Læringsmål

Når du har arbeidet med kapittelet, skal du kunne:

- forenkle algebraiske uttrykk ved å samle ledd av samme type
- bruke distribusjonsregelen og regne med parenteser
- bruke kvadratsetningene begge veier
- faktorisere algebraiske uttrykk ved å trekke ut felles faktor og bruke kvadratsetningene
- forenkle algebraiske brøkuttrykk og oppgi hvilke verdier som ikke er tillatt
- løse likninger ved å bruke faktorisering når det passer

Algebra handler om å regne med bokstaver i tillegg til tall. Bokstavene kan stå for ukjente tall eller tall som kan variere. Målet er å kunne omskrive uttrykk uten å endre verdien.

## 1. Algebraiske uttrykk

Et algebraisk uttrykk består av tall, bokstaver og regneoperasjoner. I uttrykket \(3x+5\) er \(x\) en variabel, \(3\) er koeffisienten foran \(x\), og \(5\) er et konstantledd.

### Samle ledd av samme type

Du kan bare samle ledd som har samme bokstavdel og samme eksponent.

!!! important "Huskeregel"

    \[
    3x+5x=8x
    \]

    \[
    4x^2+2x^2=6x^2
    \]

    Men \(3x+2x^2\) kan ikke samles til ett ledd, fordi \(x\) og \(x^2\) er ulike typer ledd.

!!! example "Eksempel 1 – Forenkle et uttrykk"

    Forenkle

    \[
    4x+3-2x+7.
    \]

    **Steg 1:** Samle leddene med \(x\).

    \[
    4x-2x=2x
    \]

    **Steg 2:** Samle konstantleddene.

    \[
    3+7=10
    \]

    **Svar:**

    \[
    \underline{\underline{2x+10}}
    \]

### Regnerekkefølge og fortegn

Når et minustegn står foran en parentes, skifter alle leddene i parentesen fortegn når parentesen fjernes.

!!! example "Eksempel 2 – Minus foran parentes"

    Forenkle

    \[
    5x-(2x-4).
    \]

    Minustegnet foran parentesen gjelder både \(2x\) og \(-4\):

    \[
    5x-2x+4=3x+4.
    \]

    **Svar:**

    \[
    \underline{\underline{3x+4}}
    \]

!!! question "Oppgave 1 – Samle ledd"

    Forenkle uttrykkene så langt som mulig.

    a) \(7x+2x-4\)

    b) \(5a-3+2a+8\)

    c) \(6x^2-2x+3x^2+5x\)

    d) \(8y-(3y-6)\)

    e) \(4a+2b-3a+5b\)

## 2. Parenteser og distribusjonsregelen

For å gange et tall eller et uttrykk inn i en parentes må hvert ledd i parentesen ganges.

!!! important "Distribusjonsregelen"

    \[
    a(b+c)=ab+ac
    \]

    \[
    a(b-c)=ab-ac
    \]

!!! example "Eksempel 3 – Gange inn i parentes"

    Regn ut og forenkle

    \[
    3(2x-5)+2(x+4).
    \]

    **Steg 1:** Gang inn i begge parentesene.

    \[
    3(2x-5)=6x-15
    \]

    \[
    2(x+4)=2x+8
    \]

    **Steg 2:** Fjern parentesene og samle ledd.

    \[
    6x-15+2x+8=8x-7
    \]

    **Svar:**

    \[
    \underline{\underline{8x-7}}
    \]

!!! question "Oppgave 2 – Parentesregning"

    Regn ut og forenkle.

    a) \(4(x+3)\)

    b) \(2(3x-5)\)

    c) \(5(2a-1)-3a\)

    d) \(3(x+2)-2(x-4)\)

    e) \(2(3x-1)-4(x+2)\)

## 3. Kvadratsetningene

Kvadratsetningene gjør det mulig å gange parenteser raskt og sikkert. Du bør kunne bruke dem både fra venstre mot høyre og fra høyre mot venstre.

!!! important "De tre kvadratsetningene"
    **Første kvadratsetning**

    \[
    (a+b)^2=a^2+2ab+b^2
    \]

    **Andre kvadratsetning**

    \[
    (a-b)^2=a^2-2ab+b^2
    \]

    **Konjugatsetningen**

    \[
    (a+b)(a-b)=a^2-b^2
    \]

### Hvorfor kommer det et midterledd?

Se på \((x+3)^2\). Det betyr \((x+3)(x+3)\), ikke bare at hvert ledd opphøyes i andre.

\[
\begin{aligned}
(x+3)^2&=(x+3)(x+3)\\
&=x^2+3x+3x+9\\
&=x^2+6x+9
\end{aligned}
\]

Midterleddet kommer fra de to produktene \(3x\) og \(3x\).

!!! example "Eksempel 4 – Bruk første kvadratsetning"

    Utvid \((2x+5)^2\).

    Her er \(a=2x\) og \(b=5\).

    \[
    (a+b)^2=a^2+2ab+b^2
    \]

    Sett inn:

    \[
    (2x)^2+2\cdot2x\cdot5+5^2
    \]

    Regn ut hvert ledd:

    \[
    4x^2+20x+25
    \]

    **Svar:**

    \[
    \underline{\underline{4x^2+20x+25}}
    \]

!!! example "Eksempel 5 – Bruk konjugatsetningen"

    Regn ut

    \[
    (3x+4)(3x-4).
    \]

    Dette er konjugatsetningen med \(a=3x\) og \(b=4\):

    \[
    (3x)^2-4^2=9x^2-16.
    \]

    **Svar:**

    \[
    \underline{\underline{9x^2-16}}
    \]

!!! question "Oppgave 3 – Kvadratsetningene"

    Regn ut og forenkle.

    a) \((x+4)^2\)

    b) \((x-6)^2\)

    c) \((2x+3)^2\)

    d) \((3x-2)^2\)

    e) \((x+7)(x-7)\)

    f) \((5a+2)(5a-2)\)

## 4. Faktorisering

Å faktorisere betyr å skrive et uttrykk som et produkt av faktorer. Det er på mange måter det motsatte av å gange inn i parenteser.

For eksempel kan \(6x+12\) skrives som \(6(x+2)\). Begge uttrykkene har samme verdi, men den faktoriserte formen viser produktet tydelig.

### Trekk ut felles faktor

Se først etter en faktor som alle leddene har til felles.

!!! example "Eksempel 6 – Trekk ut felles faktor"

    Faktoriser

    \[
    8x^2+12x.
    \]

    Begge leddene kan deles på \(4x\).

    \[
    8x^2+12x=4x(2x+3)
    \]

    **Svar:**

    \[
    \underline{\underline{4x(2x+3)}}
    \]

    **Kontroll:** Ganger vi \(4x\) inn igjen, får vi \(8x^2+12x\).

### Faktoriser ved hjelp av kvadratsetningene

Kvadratsetningene kan også brukes baklengs:

\[
x^2+2ax+a^2=(x+a)^2
\]

\[
x^2-2ax+a^2=(x-a)^2
\]

\[
x^2-a^2=(x+a)(x-a)
\]

!!! example "Eksempel 7 – Faktoriser en differanse av kvadrater"

    Faktoriser

    \[
    9x^2-25.
    \]

    Begge leddene er kvadrater:

    \[
    9x^2=(3x)^2,\qquad 25=5^2.
    \]

    Bruk konjugatsetningen baklengs:

    \[
    (3x)^2-5^2=(3x+5)(3x-5).
    \]

    **Svar:**

    \[
    \underline{\underline{(3x+5)(3x-5)}}
    \]

### En god rekkefølge for faktorisering

1. Se om du kan trekke ut en felles faktor.
2. Se etter en kvadratsetning.
3. Kontroller ved å gange faktorene sammen igjen.

!!! question "Oppgave 4 – Faktoriser"

    Faktoriser så langt som mulig.

    a) \(6x+18\)

    b) \(10x^2-15x\)

    c) \(x^2+8x+16\)

    d) \(x^2-10x+25\)

    e) \(x^2-49\)

    f) \(4x^2-81\)

    g) \(3x^2+12x\)

## 5. Algebraiske brøkuttrykk

En algebraisk brøk fungerer som en vanlig brøk, men teller og nevner kan inneholde bokstaver. Du må huske at nevneren aldri kan være lik null.

!!! important "Viktig regel"
    En brøk med nevner \(x-3\) er ikke definert når \(x=3\), fordi

    \[
    x-3=0 \quad\text{når}\quad x=3.
    \]

### Forkort faktorer – ikke ledd

Du kan forkorte når teller og nevner har en felles faktor. Du kan ikke forkorte deler av en sum.

!!! example "Eksempel 8 – Forkort en algebraisk brøk"

    Forkort

    \[
    \frac{6x^2}{9x}.
    \]

    Skriv teller og nevner som produkter:

    \[
    \frac{6\cdot x\cdot x}{9\cdot x}.
    \]

    Forkort med \(3x\), forutsatt at \(x\ne0\):

    \[
    \frac{6x^2}{9x}=\frac{2x}{3}.
    \]

    **Svar:**

    \[
    \underline{\underline{\frac{2x}{3}}},\qquad x\ne0
    \]

    Betingelsen \(x\ne0\) må stå igjen fordi den opprinnelige brøken ikke er definert for \(x=0\).

!!! example "Eksempel 9 – Faktoriser før du forkorter"

    Forenkle

    \[
    \frac{x^2-9}{x-3}.
    \]

    **Steg 1:** Faktoriser telleren ved hjelp av konjugatsetningen.

    \[
    x^2-9=(x-3)(x+3)
    \]

    **Steg 2:** Forkort den felles faktoren \(x-3\).

    \[
    \frac{(x-3)(x+3)}{x-3}=x+3
    \]

    **Svar:**

    \[
    \underline{\underline{x+3}},\qquad x\ne3
    \]

    Selv om uttrykket blir \(x+3\), er den opprinnelige brøken fortsatt ikke definert når \(x=3\).

!!! question "Oppgave 5 – Algebraiske brøker"

    Forenkle så langt som mulig. Oppgi hvilke verdier av \(x\) som ikke er tillatt.

    a) \(\dfrac{8x}{12x}\)

    b) \(\dfrac{x^2-16}{x-4}\)

    c) \(\dfrac{x^2+5x}{x}\)

    d) \(\dfrac{3x^2-12x}{3x}\)

    e) Forklar hvorfor \(\dfrac{x+2}{x}\) ikke kan forkortes til \(2\).

## 6. Likninger og faktorisering

En likning sier at to uttrykk er like. Når du løser en likning, finner du verdiene som gjør likheten sann.

For å løse en likning kan du gjøre samme regneoperasjon på begge sider. Når en andregradslikning kan faktoriseres, kan vi ofte bruke regelen om at et produkt er null.

!!! important "Nullproduktregelen"
    Hvis

    \[
    A\cdot B=0,
    \]

    må minst én av faktorene være null:

    \[
    A=0 \quad\text{eller}\quad B=0.
    \]

!!! example "Eksempel 10 – Løs en likning ved faktorisering"

    Løs

    \[
    x^2-5x+6=0.
    \]

    **Steg 1:** Faktoriser uttrykket.

    Vi trenger to tall som har produkt \(6\) og sum \(-5\). Tallene er \(-2\) og \(-3\).

    \[
    x^2-5x+6=(x-2)(x-3)
    \]

    **Steg 2:** Bruk nullproduktregelen.

    \[
    (x-2)(x-3)=0
    \]

    Dermed må

    \[
    x-2=0 \quad\text{eller}\quad x-3=0.
    \]

    **Steg 3:** Løs begge likningene.

    \[
    x=2 \quad\text{eller}\quad x=3
    \]

    **Svar:**

    \[
    \underline{\underline{x=2\ \text{eller}\ x=3}}
    \]

!!! question "Oppgave 6 – Likninger"

    Løs likningene. Vis framgangsmåten.

    a) \(3x+7=22\)

    b) \(2(x-4)=10\)

    c) \(x^2-16=0\)

    d) \(x^2-7x+12=0\)

    e) \(x^2+2x-8=0\)

## 7. Blandede oppgaver

Her får du oppgaver der du selv må velge hvilken regel eller metode som passer best.

!!! question "Oppgave 7 – Velg riktig metode"

    a) Forenkle \(2(x+3)+4x-5\).

    b) Utvid \((x-5)^2\).

    c) Faktoriser \(x^2-36\).

    d) Faktoriser \(6x^2+9x\).

    e) Forenkle \(\dfrac{x^2-25}{x+5}\), og oppgi betingelsen for \(x\).

    f) Løs \(x^2-9x+20=0\).

!!! question "Oppgave 8 – Finn feilen"

    En elev skriver:

    \[
    (x+4)^2=x^2+16
    \]

    a) Forklar hva eleven har glemt.

    b) Skriv det riktige uttrykket.

    c) Vis hvordan du kan kontrollere svaret ved å gange parentesene sammen.

!!! question "Oppgave 9 – Utfordring"

    Forenkle uttrykket så langt som mulig:

    \[
    \frac{x^2-4}{x^2+4x+4}.
    \]

    a) Faktoriser teller og nevner.

    b) Forkort uttrykket hvis det er mulig.

    c) Oppgi hvilke verdier av \(x\) som ikke er tillatt i det opprinnelige uttrykket.

## 8. Fasit

Prøv oppgavene først. Åpne fasiten når du har gjort et ordentlig forsøk. På oppgaver der det står «forklar», kan andre formuleringer også være riktige dersom forklaringen er matematisk korrekt.

??? note "Fasit – oppgave 1"

    a) \(9x-4\)

    b) \(7a+5\)

    c) \(9x^2+3x\)

    d) \(5y+6\)

    e) \(a+7b\)

??? note "Fasit – oppgave 2"

    a) \(4x+12\)

    b) \(6x-10\)

    c) \(7a-5\)

    d) \(x+14\)

    e) \(2x-10\)

??? note "Fasit – oppgave 3"

    a) \(x^2+8x+16\)

    b) \(x^2-12x+36\)

    c) \(4x^2+12x+9\)

    d) \(9x^2-12x+4\)

    e) \(x^2-49\)

    f) \(25a^2-4\)

??? note "Fasit – oppgave 4"

    a) \(6(x+3)\)

    b) \(5x(2x-3)\)

    c) \((x+4)^2\)

    d) \((x-5)^2\)

    e) \((x+7)(x-7)\)

    f) \((2x+9)(2x-9)\)

    g) \(3x(x+4)\)

??? note "Fasit – oppgave 5"

    a) \(\dfrac{2}{3}\), \(x\ne0\)

    b) \(x+4\), \(x\ne4\)

    c) \(x+5\), \(x\ne0\)

    d) \(x-4\), \(x\ne0\)

    e) Teller og nevner har ingen felles faktor som kan forkortes generelt. Uttrykket er dessuten ikke definert for \(x=0\).

??? note "Fasit – oppgave 6"

    a) \(x=5\)

    b) \(x=9\)

    c) \(x=-4\) eller \(x=4\)

    d) \(x=3\) eller \(x=4\)

    e) \(x=-4\) eller \(x=2\)

??? note "Fasit – oppgave 7"

    a) \(6x+1\)

    b) \(x^2-10x+25\)

    c) \((x+6)(x-6)\)

    d) \(3x(2x+3)\)

    e) \(x-5\), \(x\ne-5\)

    f) \(x=4\) eller \(x=5\)

??? note "Fasit – oppgave 8"

    a) Eleven har glemt midterleddet \(2\cdot x\cdot4=8x\).

    b) \((x+4)^2=x^2+8x+16\).

    c) \((x+4)(x+4)=x^2+4x+4x+16=x^2+8x+16\).

??? note "Fasit – oppgave 9"

    a) \(x^2-4=(x-2)(x+2)\) og \(x^2+4x+4=(x+2)^2\).

    b) \(\dfrac{x-2}{x+2}\).

    c) \(x\ne-2\), fordi nevneren i det opprinnelige uttrykket blir null når \(x=-2\).

---

## Før prøven

Du bør kunne gjøre følgende uten å se på eksemplene:

- [ ] Samle ledd av samme type og håndtere minustegn foran parenteser.
- [ ] Gange inn i parenteser og bruke kvadratsetningene.
- [ ] Faktorisere ved å trekke ut felles faktor.
- [ ] Kjenne igjen kvadratsetningene baklengs.
- [ ] Forkorte algebraiske brøker uten å miste betingelser.
- [ ] Løse enkle andregradslikninger ved faktorisering.

