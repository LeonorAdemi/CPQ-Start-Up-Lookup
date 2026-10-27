# Design-Grundlage

Stilrichtung: technischer KI-Look für Industrie und Maschinenbau, inspiriert von der Bildsprache von dryft.ai. Übernommen wurden nur Stilmittel, keine Logos, Texte oder Grafiken:

- Farbpalette nach lio.ai: Nachtblau `#0C1824` / `#182430`, Fast-Schwarz `#010203`, Petrol-Akzent `#3F7275` mit verwischten Petrol-Lichtern (`#487878`–`#609090`), kühles Grau `#9CA3AF`, heller Grund `#F6F7F8`, leichtes Korn
- Feine Strichzeichnung einer konfigurierbaren Maschine mit blauen Bauteil-Labels (eigene Zeichnung)
- KI-Konsole mit Protokollzeilen, Rahmen mit Eckmarken, vollflächiger blauer Block mit Raster
- ASCII-Feld als Dekor, eckige Buttons in Mono-Großbuchstaben (`> TERMIN VEREINBAREN`)
- Schriften: Manrope (Text), IBM Plex Mono (Labels, Zahlen, Konsole), beide über Google Fonts

Box-Rahmen der Merkmal-Kacheln und der Konsole: Box-Utility aus [WebTUI](https://github.com/webtui/webtui) (`packages/css/src/utils/box.css`, MIT-Lizenz, © 2025 WebTUI), inline übernommen.

PDF neu erzeugen: `one-pager.html` mit Chromium/Playwright als A4 drucken (`printBackground: true`).

## Name und Logo (Entwurf)

**Quoro** – aus *Quote* (Angebot) und *Chor/Kollegium*: ein Team aus KI-Agenten, das gemeinsam Angebote erstellt.
Bildmarke: ein „Q“, dessen Schweif aus drei parallelen Linien unterschiedlicher Länge besteht – die parallel arbeitenden Agenten.
Schriftzug: Manrope SemiBold (SIL Open Font License), in Pfade umgewandelt. Dateien in `logo/`, neu erzeugen mit `python3 logo/build_logo.py <Manrope-SemiBold.ttf> logo/`.

Vor Verwendung prüfen: Marken- und Domain-Recherche (DPMA/EUIPO, quoro.de/.ai/.com). Eine kurze Websuche fand keinen Anbieter namens „Quoro“, aber ähnlich klingende Firmen (Qoro Quantum, Quorso).
