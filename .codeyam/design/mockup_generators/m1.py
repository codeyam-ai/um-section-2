from html import escape as e
from common import *

chips = "\n".join(
    f'<button class="chip{" on" if label == SELECTED else ""}" type="button" '
    f'aria-pressed="{"true" if label == SELECTED else "false"}">{icon(k, 18)}<span>{e(label)}</span></button>'
    for k, label in AREAS)

def card(i, p, big=False):
    price = f'<span class="price{" free" if p["free"] else ""}">{e(price_text(p))}</span>'
    return f'''<article class="person{" big" if big else ""}">
  <div class="photo ph-{i}" role="img" aria-label="Photo of {e(p["name"])}"></div>
  <div class="who">
    <h3>{e(p["name"])}</h3>
    <p class="role">{e(p["role"])}, {e(p["org"])}</p>
  </div>
  <p class="helps">{e(p["helps"])}</p>
  <div class="foot">{price}<span class="chats">{p["chats"]} chats</span><a class="btn btn-dark sm" href="#">Book a chat</a></div>
</article>'''

cards = "\n".join(card(i, p, i == 0) for i, p in enumerate(PEOPLE))
deck = "\n".join(
    f'<div class="deck-card d{i}"><div class="photo ph-{i}" role="img" aria-label="Photo of {e(p["name"])}"></div>'
    f'<div><strong>{e(p["name"])}</strong><span>{e(p["role"])}</span></div>'
    f'<span class="price{" free" if p["free"] else ""}">{e(price_text(p))}</span></div>'
    for i, p in list(enumerate(PEOPLE))[:3])

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Soft cards, warm and tidy</title>
<style>
:root {{
  --canvas: #f5f2f0;
  --surface: #ffffff;
  --text: #333333;
  --ink: #1c1c1c;
  --border: #d6d6d6;
  --muted: #7b7b7b;
  --accent: #bcd49a;
  --accent-soft: #e6efd9;
  --highlight: #91e0ff;
  --on-accent: #1c1c1c;
  --positive: #2d6a3a;
  --shadow-md: rgba(0, 0, 0, 0.04) 0px 8px 16px 0px;
  --shadow-subtle: rgba(16, 24, 40, 0.05) 0px 1px 2px 0px;
  --font-display: 'Bricolage Grotesque', 'Avenir Next', 'Segoe UI', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --r-card: 24px;
  --r-btn: 10px;
  --r-large: 42px;
}}
:root[data-theme="dark"] {{
  --canvas: #1a1817;
  --surface: #242120;
  --text: #d4d2cf;
  --ink: #ffffff;
  --border: #3a3735;
  --muted: #9a9794;
  --accent: #bcd49a;
  --accent-soft: #33392b;
  --highlight: #4fa9c9;
  --on-accent: #1a1817;
  --positive: #8fbf95;
  --shadow-md: rgba(0, 0, 0, 0.5) 0px 8px 24px 0px;
  --shadow-subtle: rgba(0, 0, 0, 0.3) 0px 1px 2px 0px;
  color-scheme: dark;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--canvas); color: var(--text); font: 15px/1.55 var(--font-body); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
button {{ font: inherit; color: inherit; cursor: pointer; }}
:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 3px; }}
.wrap {{ max-width: 1200px; margin: 0 auto; padding: 0 40px; }}

header {{ display: flex; align-items: center; justify-content: space-between; height: 72px; }}
.brand {{ font-family: var(--font-display); font-weight: 700; font-size: 22px; color: var(--ink); letter-spacing: -0.02em; display: flex; align-items: center; gap: 10px; }}
.brand i {{ width: 26px; height: 26px; border-radius: 8px; background: var(--accent); display: inline-block; position: relative; }}
.brand i::after {{ content: ""; position: absolute; left: 7px; right: 7px; top: 6px; bottom: 6px; border-left: 2.5px solid var(--on-accent); border-right: 2.5px solid var(--on-accent); }}
nav {{ display: flex; align-items: center; gap: 28px; font-size: 14px; }}
nav a:not(.btn) {{ color: var(--muted); }}
nav a:not(.btn):hover {{ color: var(--ink); }}

.btn {{ display: inline-flex; align-items: center; gap: 8px; font-weight: 600; font-size: 15px; border: 0; border-radius: var(--r-btn); padding: 13px 20px; white-space: nowrap; transition: transform .12s ease; }}
.btn:active {{ transform: translateY(1px); }}
.btn-accent {{ background: var(--accent); color: var(--on-accent); }}
.btn-dark {{ background: var(--ink); color: var(--surface); }}
.btn-outline {{ background: transparent; border: 1px solid var(--ink); color: var(--ink); border-radius: 0; padding: 12px 20px; }}
.btn.sm {{ padding: 8px 14px; font-size: 13px; }}

.hero {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 56px; align-items: center; padding: 48px 0 56px; }}
h1 {{ font-family: var(--font-display); font-weight: 650; color: var(--ink); font-size: clamp(44px, 5.4vw, 70px); line-height: 1.02; letter-spacing: -0.035em; text-wrap: balance; }}
h1 em {{ font-style: italic; position: relative; z-index: 0; white-space: nowrap; }}
h1 em::after {{ content: ""; position: absolute; left: 3%; right: 3%; bottom: 6px; height: 14px; background: var(--accent); z-index: -1; border-radius: 4px; transform: skewX(-4deg); }}
.lede {{ font-size: 18px; max-width: 46ch; margin: 22px 0 32px; color: var(--text); }}
.ctas {{ display: flex; gap: 14px; align-items: center; }}

.deck {{ position: relative; height: 330px; }}
.deck-card {{ position: absolute; left: 0; right: 0; display: grid; grid-template-columns: 64px 1fr auto; gap: 16px; align-items: center; background: var(--surface); border-radius: var(--r-card); padding: 18px 22px; box-shadow: var(--shadow-md); }}
.deck-card .photo {{ width: 64px; height: 64px; border-radius: 18px; }}
.deck-card strong {{ display: block; font-family: var(--font-display); font-size: 19px; color: var(--ink); letter-spacing: -0.01em; }}
.deck-card span {{ font-size: 13px; color: var(--muted); }}
.deck-card .price {{ font-size: 12px; }}
.d0 {{ top: 0; transform: rotate(-2deg) translateX(-8px); z-index: 3; }}
.d1 {{ top: 112px; transform: rotate(1.5deg) translateX(28px); z-index: 2; }}
.d2 {{ top: 224px; transform: rotate(-1deg) translateX(4px); z-index: 1; }}

.price {{ font-family: var(--font-mono); font-size: 12px; font-variant-numeric: tabular-nums; color: var(--ink); background: var(--canvas); border: 1px solid var(--border); border-radius: var(--r-btn); padding: 4px 9px; white-space: nowrap; }}
.price.free {{ background: var(--accent-soft); border-color: transparent; color: var(--positive); }}

.picker {{ background: var(--surface); border-radius: var(--r-large); padding: 40px; box-shadow: var(--shadow-md); margin-bottom: 64px; }}
.picker-head {{ display: flex; align-items: baseline; justify-content: space-between; gap: 24px; margin-bottom: 22px; }}
h2 {{ font-family: var(--font-display); font-weight: 650; color: var(--ink); font-size: 32px; letter-spacing: -0.025em; line-height: 1.1; text-wrap: balance; }}
.hint {{ font-size: 14px; color: var(--muted); }}
.chips {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.chip {{ display: inline-flex; align-items: center; gap: 8px; background: var(--canvas); border: 1px solid transparent; border-radius: var(--r-btn); padding: 10px 14px; font-size: 14px; font-weight: 500; color: var(--ink); transition: border-color .15s; }}
.chip svg {{ color: var(--muted); }}
.chip:hover {{ border-color: var(--border); }}
.chip.on {{ background: var(--accent); color: var(--on-accent); }}
.chip.on svg {{ color: var(--on-accent); }}

.results {{ margin-top: 36px; padding-top: 32px; border-top: 1px solid var(--border); }}
.results-head {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 20px; }}
.results-head h3 {{ font-family: var(--font-display); font-size: 22px; color: var(--ink); letter-spacing: -0.015em; font-weight: 600; }}
.sort {{ font-size: 13px; color: var(--muted); }}
.sort b {{ color: var(--ink); font-weight: 600; }}
.grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
.person {{ background: var(--canvas); border-radius: var(--r-card); padding: 20px; display: flex; flex-direction: column; gap: 14px; }}
.person .photo {{ width: 56px; height: 56px; border-radius: 16px; }}
.person h3 {{ font-family: var(--font-display); font-size: 18px; color: var(--ink); letter-spacing: -0.01em; font-weight: 600; }}
.role {{ font-size: 13px; color: var(--muted); }}
.helps {{ font-size: 14px; color: var(--text); flex: 1; }}
.foot {{ display: flex; align-items: center; gap: 10px; }}
.chats {{ font-family: var(--font-mono); font-size: 11px; color: var(--muted); font-variant-numeric: tabular-nums; margin-right: auto; }}
.person.big {{ grid-row: span 2; background: var(--accent-soft); }}
.person.big .photo {{ width: 100%; height: auto; aspect-ratio: 4 / 3.4; border-radius: 18px; }}
.person.big h3 {{ font-size: 26px; }}
.person.big .helps {{ font-size: 16px; }}
.person.big .price {{ background: var(--surface); }}

footer {{ display: flex; justify-content: space-between; font-size: 13px; color: var(--muted); padding: 0 0 40px; }}
@media (max-width: 860px) {{
  .hero {{ grid-template-columns: 1fr; }}
  .deck {{ display: none; }}
  .grid {{ grid-template-columns: 1fr; }}
  .person.big {{ grid-row: auto; }}
  nav a:not(.btn) {{ display: none; }}
  .wrap {{ padding: 0 16px; }}
  .picker {{ padding: 24px; border-radius: var(--r-card); }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
{portraits_css()}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <a class="brand" href="#"><i aria-hidden="true"></i>Hallway</a>
    <nav>
      <a href="#">How it works</a>
      <a href="#">For professionals</a>
      <a href="#">Log in</a>
      <a class="btn btn-dark sm" href="#">Sign up</a>
    </nav>
  </header>

  <section class="hero">
    <div>
      <h1>Ask someone who&rsquo;s <em>already there</em>.</h1>
      <p class="lede">Pick a field you&rsquo;re curious about, then book a short chat with a professional who works in it.</p>
      <div class="ctas">
        <a class="btn btn-accent" href="#pick">Find someone</a>
        <a class="btn btn-outline" href="#">Offer advice</a>
      </div>
    </div>
    <div class="deck" aria-hidden="true">
{deck}
    </div>
  </section>

  <section class="picker" id="pick">
    <div class="picker-head">
      <h2>What are you curious about?</h2>
      <span class="hint">Pick one to start. You can change it anytime.</span>
    </div>
    <div class="chips">
{chips}
    </div>

    <div class="results">
      <div class="results-head">
        <h3>6 people in Product design</h3>
        <span class="sort">Sorted by <b>most helpful</b></span>
      </div>
      <div class="grid">
{cards}
      </div>
    </div>
  </section>

  <footer><span>Hallway</span><span>Professionals set their own price. Many offer a free first chat.</span></footer>
</div>
</body>
</html>
'''
write("01-letters-to-sean-mockup.html", html)
