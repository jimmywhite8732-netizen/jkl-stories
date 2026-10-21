"""Render a daily story slide.  Usage: python3 render.py content.json out.png
content.json keys: headline (may use <em>..</em> for the blue accent words),
stat, stat_label (use <br> for line breaks), takeaway, source, cta_line, keyword."""
import json, os, sys, html
from playwright.sync_api import sync_playwright
here = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(sys.argv[1])); out = os.path.abspath(sys.argv[2])
t = open(os.path.join(here, 'template.html')).read()
for k in ['headline','stat','stat_label','takeaway','source','cta_line','keyword']:
    t = t.replace('{{%s}}' % k.upper(), c[k])
tmp = os.path.join(here, '_render.html'); open(tmp, 'w').write(t)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://' + tmp); pg.wait_for_timeout(400)
    bottom = pg.evaluate("document.querySelector('.foot').getBoundingClientRect().bottom")
    top = pg.evaluate("document.querySelector('.src').getBoundingClientRect().bottom")
    pg.screenshot(path=out); b.close()
os.remove(tmp)
# layout guard: content must not run into the footer/safe zone
print(json.dumps({"out": out, "footer_bottom": bottom, "source_bottom": top,
                  "ok": bottom <= 1662 and top < 1480}))
