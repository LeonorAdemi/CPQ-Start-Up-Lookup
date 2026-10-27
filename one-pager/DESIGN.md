# Design-Grundlage

Der One Pager übernimmt die Formensprache von [Magic UI](https://github.com/magicuidesign/magicui) (MIT-Lizenz, © Magic UI), statisch für den PDF-Export umgesetzt:

- Farb- und Radius-Tokens aus `apps/www/styles/globals.css` (shadcn/ui, neutrale Grautöne), Schriften Geist und Geist Mono
- Grid-Pattern mit radialer Maske (`registry/magicui/grid-pattern.tsx`)
- Ankündigungs-Pille mit Verlaufsrand (`registry/example/animated-gradient-text-demo.tsx`)
- Aurora-Text-Verlauf `#FF0080 → #7928CA → #0070F3 → #38BDF8` (`registry/magicui/aurora-text.tsx`)
- Bento-Karten mit Schichtschatten (`registry/magicui/bento-grid.tsx`)
- Border-Beam `#ffaa40 → #9c40ff` und Shine-Border als statische Randverläufe (`border-beam.tsx`, `shine-border.tsx`)

PDF neu erzeugen: `one-pager.html` mit Chromium/Playwright als A4 drucken (`printBackground: true`).
