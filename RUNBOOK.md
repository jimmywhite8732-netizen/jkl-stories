# Daily Story Runbook — @jimmyknowsloans

Runs Monday–Friday at ~6:00am CT. Goal: one Instagram + Facebook Story (educational or news),
queued in Metricool to auto-publish at **8:00am CT**.

## 0. News or educational? (alternate 50/50 — Jimmy's call, Nov 19 2026)
- Check the `Type` column of the last row in `log.md` and do the **opposite** type today
  (last row NEWS → today EDU; last row EDU → today NEWS).
- **No repeat data themes:** do not use a theme (pending sales, existing-home sales, inventory /
  supply, buyers vs. sellers, home prices, builder sentiment, mortgage applications, Fed) that
  appears in any of the last 10 log rows. If every fresh news story repeats a recent theme,
  make it an EDU day instead.

### Educational (EDU) days
- One evergreen lesson for first-time buyers, backed by one real number from an authoritative
  source (myFICO, CFPB, Fannie Mae / Freddie Mac, HUD / FHA, IHDA, VA, NAR Profile of Buyers,
  Illinois Realtors, county/city sites). Verify the number on the source page.
- Topic ideas (don't repeat one already in `log.md`): credit score factors, credit utilization,
  pre-qualified vs. pre-approved, what documents you need to apply, debt-to-income explained,
  why not to open new credit before closing, what closing costs include, earnest money,
  home inspection vs. appraisal, IHDA programs, gift funds, FHA vs. conventional basics,
  how long pre-approval lasts, Illinois property tax basics / homestead exemption,
  first-time buyer tax facts, PMI basics (no amounts), rent vs. own timeline.
- Same compliance guardrails apply: still no specific rates, APRs, payments, down payment
  amounts or loan terms.
- `source` can be `Outlet, Page title (updated Mon YYYY)` for evergreen pages.

## 1. Pick the story (NEWS days)
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
