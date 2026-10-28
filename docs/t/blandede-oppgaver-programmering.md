# Blandede oppgaver – Programmering i Python

Her blander du funksjoner, lister, løkker og enkel regning. Velg selv hvordan du vil dele opp problemet. Skriv kode, test den, og forklar kort hva den gjør.

## Nivå 1 – Grunnleggende

!!! question "Oppgave 1 – Funksjon med parameter"
    Skriv funksjonen `pluss_to(tall)`, som returnerer tallet pluss 2. Kall funksjonen med 8 og skriv ut resultatet.

!!! question "Oppgave 2 – Liste og indeks"
    Gitt listen `temperatur = [12, 15, 11, 18]`:

    a) Skriv ut det første elementet.

    b) Skriv ut det siste elementet ved å bruke indeks 3.

    c) Legg til tallet 20 bakerst.

!!! question "Oppgave 3 – Funksjon som bruker en liste"
    Lag funksjonen `antall_elementer(liste)`, som returnerer hvor mange elementer listen inneholder. Test med `[4, 8, 12]`.

## Nivå 2 – Kombiner flere ideer

!!! question "Oppgave 4 – Summen av en liste"
    Lag funksjonen `sum_liste(tall)`, som returnerer summen av alle tallene i listen. Bruk en `for`-løkke. Test med `[3, 5, 2]`.

!!! question "Oppgave 5 – Tell positive tall"
    Lag funksjonen `tell_positive(tall)`, som teller hvor mange elementer i en liste som er større enn 0. Test med `[-2, 4, 0, 7, -1, 3]`.

!!! question "Oppgave 6 – Lag en ny liste"
    Lag funksjonen `doble_liste(tall)`, som returnerer en ny liste der hvert element er dobbelt så stort som i den opprinnelige listen. For eksempel skal `[2, 5, 1]` gi `[4, 10, 2]`. Ikke endre den opprinnelige listen.

## Nivå 3 – Utfordring

!!! question "Oppgave 7 – Gjennomsnitt"
    Lag funksjonen `gjennomsnitt(tall)`, som returnerer gjennomsnittet av tallene i en liste.

    a) Test med `[4, 6, 8]`.

    b) Hva kan gå galt dersom listen er tom? Endre funksjonen slik at den håndterer en tom liste på en fornuftig måte, og forklar valget ditt.

!!! question "Oppgave 8 – Filtrer etter grense"
    Lag funksjonen `over_grense(tall, grense)`, som returnerer en ny liste med bare tallene som er større enn `grense`. Rekkefølgen skal bevares.

    Eksempel: `over_grense([3, 8, 2, 10], 5)` skal gi `[8, 10]`.

!!! question "Oppgave 9 – Feilsøking"
    En elev har skrevet denne funksjonen:

    ```python
    def tell_større(liste, grense):
        antall = 0
        for tall in liste:
            if tall > grense:
                antall = antall + 1
            return antall
    ```

    Funksjonen gir feil resultat for `tell_større([7, 2, 9, 4], 5)`.

    a) Forklar feilen.

    b) Rett koden.

    c) Hva skal funksjonen returnere for eksempelet over?

??? note "Fasit – nivå 1"
    **1.**

    ```python
    def pluss_to(tall):
        return tall + 2

    print(pluss_to(8))  # 10
    ```

    **2.** a) `12` b) `18` c) `temperatur.append(20)`

    **3.**

    ```python
    def antall_elementer(liste):
        return len(liste)

    print(antall_elementer([4, 8, 12]))  # 3
    ```

??? note "Fasit – nivå 2"
    **4.**

    ```python
    def sum_liste(tall):
        sum = 0
        for x in tall:
            sum += x
        return sum

    print(sum_liste([3, 5, 2]))  # 10
    ```

    **5.**

    ```python
    def tell_positive(tall):
        antall = 0
        for x in tall:
            if x > 0:
                antall += 1
        return antall

    print(tell_positive([-2, 4, 0, 7, -1, 3]))  # 3
    ```

    **6.**

    ```python
    def doble_liste(tall):
        ny = []
        for x in tall:
            ny.append(2 * x)
        return ny
    ```

??? note "Fasit – nivå 3"
    **7.**

    ```python
    def gjennomsnitt(tall):
        if len(tall) == 0:
            return None
        sum_tall = 0
        for x in tall:
            sum_tall += x
        return sum_tall / len(tall)
    ```

    En tom liste har ingen gjennomsnittsverdi. Her returnerer funksjonen `None` for å markere at resultatet ikke finnes.

    **8.**

    ```python
    def over_grense(tall, grense):
        ny = []
        for x in tall:
            if x > grense:
                ny.append(x)
        return ny
    ```

    **9.** `return antall` ligger inne i løkken, slik at funksjonen avsluttes etter første element. Flytt `return antall` ut av løkken. Resultatet skal være `2`.

