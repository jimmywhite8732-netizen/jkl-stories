"""Render a Real Estate Riser IG video thumbnail card (600x600 PNG).
Usage: python3 riser/render_card.py "IG Video 01" "Four lenders said no. I said yes." out.png
Needs Playwright + Chromium, and the Barlow / Barlow Condensed fonts installed
(see RISER.md). Keep titles to about 8 words so they fit in 5 lines."""
import os, sys, html, tempfile
from playwright.sync_api import sync_playwright
here = os.path.dirname(os.path.abspath(__file__))
label, title, out = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
src = open(os.path.join(here, 'card.html')).read()
page_html = src.replace('__LBL__', html.escape(label)).replace('__TTL__', html.escape(title))
tmp = os.path.join(here, '_card_tmp.html')
open(tmp, 'w').write(page_html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 600, 'height': 600})
    pg.goto('file://' + tmp); pg.wait_for_timeout(600)
    pg.screenshot(path=out); b.close()
os.remove(tmp)
print('ok', out)
