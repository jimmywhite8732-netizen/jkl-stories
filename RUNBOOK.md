# Daily Story Runbook — @jimmyknowsloans

Runs Monday–Friday at ~6:00am CT. Goal: one real estate news Instagram + Facebook Story,
queued in Metricool to auto-publish at **8:00am CT**.

## 1. Pick the story
- Search the last 24–72 hours of real estate / mortgage / housing news.
- Prefer, in order: (a) Chicagoland / Illinois / Will County housing news, (b) national news
  with a clear local angle (Fed, housing data releases, inventory, prices, programs like IHDA / DPA),
  (c) national headlines only if nothing better exists.
- Audience: first-time homebuyers and real estate agents in the Chicago southwest suburbs.
- Do not repeat a story already used — check `log.md`.
- Use reputable sources (major outlets, Redfin/Zillow/Realtor.com research, Illinois Realtors,
  Census, Freddie Mac, Fannie Mae, MBA, NAR, Fed). Skip SEO rate-blog content.

## 2. Write the content (`stories/YYYY-MM-DD.json`)
| Key | Rule |
|---|---|
| headline | ≤ 60 characters. Wrap 2–3 punchy words in `<em>…</em>` for the light-blue accent. |
| stat | One big number, ≤ 6 characters (e.g. `~10%`, `+4.3%`, `47`). Must come straight from the source. |
| stat_label | 3 short lines separated by `<br>`, each ≤ 24 characters. Says what the number measures. |
| takeaway | "What this means for you" — ≤ 115 characters, plain language, Jimmy's voice, local buyer angle. |
| source | `Outlet / Report, Mon DD, YYYY` |
| cta_line | ≤ 20 characters, e.g. "Buying this fall?" |
| keyword | One word, ALL CAPS, ≤ 10 characters, tied to the story. |

### Compliance guardrails (always)
- **No specific mortgage rates, APRs, payment amounts, down payment amounts or loan terms.**
  Say "rates eased" / "rates rose", never "7.14%". (Avoids Reg Z trigger terms.)
- No promises or guarantees ("you will qualify", "lowest rate").
- No NMLS line needed on the slide (it is on the profile).
- Never invent or round a statistic beyond what the source states.

## 3. Render
`python3 render.py stories/YYYY-MM-DD.json stories/YYYY-MM-DD.png`
The script prints `"ok": true/false`. If false, shorten the text and re-render.
Look at the PNG before publishing.

## 4. Publish the image
Commit the .json, .png and a line in `log.md`, then push to `main`.
Public image URL:
`https://raw.githubusercontent.com/jimmywhite8732-netizen/jkl-stories/main/stories/YYYY-MM-DD.png`

## 5. Schedule in Metricool
- Brand blogId: `7564408`, timezone `America/Chicago`
- `createScheduledPost`, date = today 08:00:00-05:00 (use -06:00 after DST ends Nov 1)
- providers: instagram + facebook; `instagramData.type = "STORY"`, `facebookData.type = "STORY"`
- media: the raw URL above; **no text** (Stories carry no caption); autoPublish true.

## 6. Notify Jimmy
Send a short message with the headline, the keyword, the source, and the Metricool planner link,
so he can edit or delete before 8:00am.
