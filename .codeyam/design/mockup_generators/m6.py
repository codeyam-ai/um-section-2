from html import escape as e
from common import *

COUNTS = [38, 54, 41, 27, 33, 19, 46, 22, 17, 12, 15, 29]
check = '<svg class="ck" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
tiles = "\n".join(
    f'<button type="button" class="tile{" on" if l == SELECTED else ""}" aria-pressed="{"true" if l == SELECTED else "false"}">'
    f'{icon(k, 28, 1.7)}<span class="l">{e(l)}</span><span class="n">{n} people</span>{check if l == SELECTED else ""}</button>'
    for (k, l), n in zip(AREAS, COUNTS))

stack = "".join(f'<span class="av ph-{i}" role="img" aria-label="{e(PEOPLE[i]["name"])}"></span>' for i in range(5))

preview = "\n".join(f'''<li>
  <span class="photo ph-{i}" role="img" aria-label="Photo of {e(p["name"])}"></span>
  <div class="who"><strong>{e(p["name"])}</strong><span>{e(p["role"])}, {e(p["org"])}</span></div>
  <p>{e(p["helps"])}</p>
  <span class="price{" free" if p["free"] else ""}">{e(price_text(p))}</span>
</li>''' for i, p in list(enumerate(PEOPLE))[:4])

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Sky blue, guided first steps</title>
<style>
:root {{
  --field: #c7dbff;
  --surface: #ffffff;
  --ink: #13233a;
  --muted: #4a5d78;
  --line: #a9c1ea;
  --rule: #dbe5f5;
  --butter: #ffe066;
  --on-accent: #13233a;
  --shadow: 0 24px 48px -24px rgba(19, 35, 58, 0.35);
  --display: 'Avenir Next Condensed', 'Roboto Condensed', 'Arial Narrow', 'Helvetica Neue', sans-serif;
  --body: 'Avenir Next', 'Segoe UI', system-ui, sans-serif;
  --r: 14px;
}}
:root[data-theme="dark"] {{
  --field: #142238;
  --surface: #1b2c45;
  --ink: #e8effa;
  --muted: #a6b6cc;
  --line: #2b4060;
  --rule: #243752;
  --butter: #ffe066;
  --on-accent: #13233a;
  --shadow: 0 24px 48px -24px rgba(0, 0, 0, 0.7);
  color-scheme: dark;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--surface); color: var(--ink); font: 16px/1.5 var(--body); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
button {{ font: inherit; color: inherit; cursor: pointer; }}
:focus-visible {{ outline: 3px solid var(--ink); outline-offset: 3px; }}

.field {{ background: var(--field); padding-bottom: 72px; }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 40px; }}
header {{ height: 72px; display: flex; align-items: center; justify-content: space-between; }}
.brand {{ font-family: var(--display); font-stretch: condensed; font-weight: 800; font-size: 28px; letter-spacing: -0.01em; }}
header a.out {{ font-size: 15px; font-weight: 600; }}

.progress {{ display: flex; justify-content: center; gap: 10px; margin: 24px 0 36px; padding: 0; list-style: none; }}
.progress li {{ display: flex; flex-direction: column; gap: 8px; width: 150px; font-size: 13px; font-weight: 600; color: var(--muted); }}
.progress li::before {{ content: ""; height: 6px; border-radius: 3px; background: var(--line); }}
.progress li.now {{ color: var(--ink); }}
.progress li.now::before {{ background: var(--ink); }}

h1 {{ font-family: var(--display); font-stretch: condensed; font-weight: 800; text-align: center; font-size: 84px; line-height: .95; letter-spacing: -0.02em; text-wrap: balance; max-width: 14ch; margin: 0 auto; }}
.lede {{ text-align: center; color: var(--muted); font-size: 18px; margin: 18px auto 44px; max-width: 46ch; }}

.grid {{ display: grid; grid-template-columns: repeat(4, 1fr); background: var(--line); gap: 1px; border-radius: var(--r); overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--line); }}
.tile {{ position: relative; background: var(--surface); border: 0; padding: 22px 20px 20px; text-align: left; display: grid; gap: 4px; min-height: 132px; align-content: end; transition: background .15s; }}
.tile svg:first-child {{ color: var(--muted); margin-bottom: auto; }}
.tile:hover {{ background: color-mix(in srgb, var(--field) 35%, var(--surface)); }}
.tile .l {{ font-family: var(--display); font-stretch: condensed; font-weight: 700; font-size: 24px; line-height: 1.05; letter-spacing: -0.01em; }}
.tile .n {{ font-size: 13px; color: var(--muted); font-variant-numeric: tabular-nums; }}
.tile.on {{ background: var(--ink); color: var(--surface); }}
.tile.on svg:first-child, .tile.on .n {{ color: var(--butter); }}
.ck {{ position: absolute; top: 18px; right: 18px; color: var(--on-accent); background: var(--butter); border-radius: 50%; padding: 3px; width: 28px; height: 28px; }}

.bar {{ margin: 22px auto 0; display: flex; align-items: center; gap: 18px; background: var(--surface); border-radius: 999px; padding: 10px 10px 10px 16px; box-shadow: var(--shadow); width: fit-content; }}
.av {{ width: 38px; height: 38px; border-radius: 50%; border: 3px solid var(--surface); margin-left: -14px; display: inline-block; }}
.av:first-child {{ margin-left: 0; }}
.bar p {{ font-size: 15px; }}
.bar p b {{ font-weight: 700; }}
.next {{ background: var(--butter); color: var(--on-accent); font-weight: 700; padding: 12px 22px; border-radius: 999px; white-space: nowrap; }}
.next:active {{ transform: scale(.98); }}

.peek {{ padding: 72px 0 40px; display: grid; grid-template-columns: 300px 1fr; gap: 56px; }}
h2 {{ font-family: var(--display); font-stretch: condensed; font-weight: 800; font-size: 44px; line-height: 1; letter-spacing: -0.01em; text-wrap: balance; }}
.peek .side p {{ color: var(--muted); margin-top: 14px; }}
.list {{ list-style: none; padding: 0; }}
.list li {{ display: grid; grid-template-columns: 56px 1.1fr 1.3fr auto; gap: 20px; align-items: center; padding: 18px 0; border-top: 1px solid var(--rule); }}
.list li:last-child {{ border-bottom: 1px solid var(--rule); }}
.list .photo {{ width: 56px; height: 56px; border-radius: 50%; }}
.who strong {{ display: block; font-size: 17px; }}
.who span {{ font-size: 14px; color: var(--muted); }}
.list p {{ font-size: 15px; color: var(--muted); }}
.price {{ font-weight: 700; font-variant-numeric: tabular-nums; white-space: nowrap; font-size: 15px; }}
.price.free {{ background: var(--butter); color: var(--on-accent); padding: 3px 10px; border-radius: 999px; }}

footer {{ padding: 24px 0 40px; color: var(--muted); font-size: 14px; display: flex; justify-content: space-between; }}
@media (max-width: 900px) {{
  .wrap {{ padding: 0 16px; }}
  h1 {{ font-size: 52px; }}
  .grid {{ grid-template-columns: repeat(2, 1fr); }}
  .peek {{ grid-template-columns: 1fr; }}
  .list li {{ grid-template-columns: 48px 1fr auto; }}
  .list p {{ display: none; }}
  .bar {{ border-radius: var(--r); flex-wrap: wrap; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
{portraits_css(w=200, h=200)}
</style>
</head>
<body>
<section class="field">
  <div class="wrap">
    <header>
      <a class="brand" href="#">Hallway</a>
      <a class="out" href="#">I already have an account</a>
    </header>
    <ol class="progress" aria-label="Getting started">
      <li class="now">Pick a field</li>
      <li>Pick a person</li>
      <li>Book a chat</li>
    </ol>
    <h1>What could you see yourself doing?</h1>
    <p class="lede">Pick a field and we&rsquo;ll introduce you to people who work in it. Not sure yet? Pick the one you&rsquo;re most curious about.</p>
    <div class="grid">
{tiles}
    </div>
    <div class="bar">
      <span>{stack}</span>
      <p><b>38 people in Product design.</b> 14 offer a free first chat.</p>
      <a class="next" href="#">Pick a person</a>
    </div>
  </div>
</section>

<div class="wrap">
  <section class="peek">
    <div class="side">
      <h2>A few people you could talk to</h2>
      <p>Each one sets their own price. Free intros are 20 minutes.</p>
    </div>
    <ul class="list">
{preview}
    </ul>
  </section>
  <footer><span>Hallway</span><span>Are you a professional? <a href="#"><b>Offer advice</b></a></span></footer>
</div>
</body>
</html>
'''
write("06-offcatalog-mockup.html", html)
