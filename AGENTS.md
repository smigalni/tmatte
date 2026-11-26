# Arbeidsregler for T-matte

Disse reglene gjelder for dette bok-repoet og skal brukes automatisk på tvers av samtaler.

## Arbeidsflyt
- Arbeid på den branchen brukeren har angitt. For T-matte skal du bruke branchen brukeren har angitt; bruk main bare når ingen annen branch er valgt.
- Les denne filen og den felles standarden før endringer. Ikke be brukeren gjenta etablerte valg.
- Bevar eksisterende struktur, nummerering, navigasjon og innhold som ikke er del av oppgaven.
- Kontroller at endringer er lagret på riktig branch, og oppgi hvilke tester og bygg som faktisk ble kjørt.
- Ikke si at en side er ferdig bare fordi teksten er skrevet.

## Design og matematisk formatering
- Gjenbruk stilen som allerede finnes i T-matte og sammenlign med nærmeste ferdige side før du redigerer.
- Bruk tydelig visuell forskjell mellom eksempel og oppgave: turkise eksempelbokser, blå regel-/formelbokser og lilla oppgavebokser der dette er prosjektets etablerte mønster.
- Gjennomarbeidede eksempler skal stå i eksempelbokser, ikke som løs tekst under en vanlig Eksempel-overskrift.
- Bruk korrekt MathJax, vis mellomregning trinnvis og ikke hopp over viktige steg for elever.
- Endelige svar skal dobbeltunderstrekes med MathJax når dette er standarden på siden.
- Behold oppgavenivåer, nummerering og kapittelstruktur. Ikke lag nye kategorier uten at brukeren ber om det.
- Kontroller fasit, fortegn, parenteser, definisjonsmengder og samsvar mellom oppgaver og svar.
- Følg Zensical-konfigurasjonen og eksisterende navigasjon. Ikke finn opp en ny stil for hver side.

## Obligatorisk standard for oppgaver og figurer

- Deloppgaver a), b), c) osv. skal alltid stå på hver sin linje i elevtekst, fasit og løsningsforslag. Ikke legg inn ekstra punktmarkør foran bokstavene.
- Oppgavetekst, deloppgaver og tilhørende svar skal ha tydelig vertikal struktur. Formel eller figur skal stå visuelt sammen med deloppgaven den hører til.
- Alle koordinatsystemer skal ha tydelige pilspisser på aksene og etikettene x og y. Tallinjer skal vise retning med pilspisser og ha relevant variabelnavn.
- Figurer skal ha korrekt skala, lesbare akseverdier, tydelige markeringer og matematisk riktig kurve/geometri. Ikke lever en skisse som mangler nødvendige akseetiketter eller retning.
- Elev- og lærerversjon skal ha identisk oppgavenummerering, rekkefølge, ordlyd og figurer. Lærerversjonen skal i tillegg ha samsvarende fasit.
- Trykk/PDF: første side skal kun inneholde MathPlatform-logoen. Selve opplegget starter på side 2.
- Disse kravene skal kontrolleres automatisk der det er mulig, og deretter visuelt i nettvisning og utskrift. En grønn CI-kontroll erstatter ikke visuell kontroll.

## Felles kvalitetskontroll på tvers av bøker
- Den delte standarden og sjekkeren dokumenteres i https://github.com/smigalni/matte/blob/main/BOOK_QUALITY.md.
- Bokspesifikke innstillinger ligger i .book-quality.toml. Ikke kopier selve kontrollprogrammet hit.
- GitHub Actions kjører automatisk kontroll av endrede Markdown-filer ved push og pull request.
- Den automatiske kontrollen er et ekstra sikkerhetslag. Den erstatter ikke faglig kontroll, Zensical-bygg eller visuell kontroll av siden.
- Hvis en regel ikke passer T-matte, juster .book-quality.toml eksplisitt og begrunn unntaket; ikke ignorer regelen i den enkelte chat.

## Ekstra regler for lærer-/elevhefter og oppgaveformatering

- Sett alltid inn en tom linje rett etter overskriften på hver admonition-boks før innholdet begynner.
- Sett inn en tom linje før hver deloppgave a), b), c) osv. Deloppgaver skal være egne avsnitt, aldri flere på samme linje.
- MathJax skal bruke én vanlig omvendt skråstrek per avgrenser og kommando: `\(`, `\)`, `\frac`. Ikke lim inn dobbelt-escapede sekvenser som `\\(` eller `\\frac`.
- Når en oppgave legges til, skal oppgavebanken kontrolleres for identiske eller nesten identiske oppgaver. En ny grafoppgave skal ikke bare gjenta en eksisterende oppgave med samme punkter og samme funksjon.
- Ved endring av oppgaver skal elev- og lærerversjon oppdateres samlet. Lærerheftet skal inneholde nøyaktig samme oppgaver, ordlyd, rekkefølge og figurer som elevheftet, i tillegg til én fasitboks med samme oppgave-ID per oppgave.
- Figurenes bildetekster skal bruke riktig oppgavenummer, for eksempel `Figur 2.1.2.`. Alle figurer skal ha alternativ tekst/ARIA-beskrivelse. Bildeteksten skal ikke røpe metoden eller svaret.
- Fasit skal være skjult i lærerheftets nettvisning, men vises ved utskrift. Sluttsvar i fasitbokser med matematikk skal dobbeltunderstrekes.
- Før levering skal oppgave-ID-er, fasit-ID-er, figurreferanser og grafnøkler sammenlignes mellom heftene. Kontroller også at ingen erstattet oppgavetype fortsatt ligger igjen under et annet oppgavenummer.

## Obligatorisk kontroll før levering
1. Sammenlign design med en eksisterende ferdig side.
2. Kontroller matematikk, fasit, nummerering, lenker og bokser.
3. Kjør relevante tester og Zensical-bygg hvis miljøet er tilgjengelig.
4. Kontroller branch og endrede filer.
5. Si tydelig fra hvis bygg eller visuell kontroll ikke ble utført.
