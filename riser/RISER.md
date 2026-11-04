# Real Estate Riser – newsletter assets

Used by the weekly "Riser weekly issue" scheduled task. The daily Stories files elsewhere in this repo are separate.

- `Real-Estate-Riser-Header-1200x400.png` – newsletter header (attach to every AE email)
- `card.html` + `jimmy_riser.png` – IG video thumbnail card template (navy, steel-blue arch, headshot, play button, WATCH NOW)
- `render_card.py` – renders one 600x600 card: `python3 riser/render_card.py "IG Video 01" "<short title>" out.png`

Fonts (install once per session if missing):
```
mkdir -p ~/.fonts && cd ~/.fonts
curl -sfLO https://raw.githubusercontent.com/google/fonts/main/ofl/barlow/Barlow-Medium.ttf
curl -sfLO https://raw.githubusercontent.com/google/fonts/main/ofl/barlow/Barlow-SemiBold.ttf
curl -sfLO https://raw.githubusercontent.com/google/fonts/main/ofl/barlowcondensed/BarlowCondensed-ExtraBold.ttf
fc-cache -f
```
