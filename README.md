# T-matte – steg for steg

Digital pensumbok for matematikk 1T, bygget med Zensical.

## Lokal forhåndsvisning (Windows / PowerShell)

\`\`\`powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install zensical
zensical serve
\`\`\`

Åpne deretter http://localhost:8000 i nettleseren.

## Innhold

- \`docs/index.md\`: startsiden
- \`docs/t/kapittel-2-algebra.md\`: utkast til kapittel 2
- \`docs/stylesheets/extra.css\`: samme visuelle stil som matte-repoet
- \`zensical.toml\`: navigasjon og oppsett

Kapittelinnholdet er et førsteutkast. Kontroller avgrensningen mot læreboka og lærerens prøveplan før det brukes som endelig pensum.
