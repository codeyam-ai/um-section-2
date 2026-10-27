from html import escape as e
from common import *

options = "\n".join(
    f'<li><button type="button" class="opt{" on" if l == SELECTED else ""}" aria-pressed="{"true" if l == SELECTED else "false"}">'
    f'{icon(k, 18)}<span>{e(l)}</span></button></li>' for k, l in AREAS)

caret = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

featured = [0, 3, 1]
feat = "\n".join(f'''<article class="f f{n}">
  <div class="frame"><div class="photo ph-{i}" role="img" aria-label="Photo of {e(PEOPLE[i]["name"])}"></div></div>
  <h3>{e(PEOPLE[i]["name"])}</h3>
  <p class="role">{e(PEOPLE[i]["role"])} at {e(PEOPLE[i]["org"])}. {e(PEOPLE[i]["years"])}.</p>
  <p class="helps">Can help with: {e(PEOPLE[i]["helps"].lower())}.</p>
  <div class="row"><span class="price{" free" if PEOPLE[i]["free"] else ""}">{e(price_text(PEOPLE[i]))}</span><a class="link" href="#">Book a chat</a></div>
</article>''' for n, i in enumerate(featured))

rest = [i for i in range(len(PEOPLE)) if i not in featured]
avatars = "".join(f'<span class="av ph-{i}" role="img" aria-label="{e(PEOPLE[i]["name"])}"></span>' for i in rest)

paper = ("data:image/svg+xml;base64," + __import__("base64").b64encode(
    b'<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0.1  0 0 0 0 0.14  0 0 0 0 0.25  0 0 0 .07 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>').decode())

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Fill in the sentence</title>
<style>
:root {{
  --canvas: #f3f6fb;
  --surface: #ffffff;
  --tint: #dfe8f6;
  --ink: #1b2540;
  --text-2: #55607a;
  --line: #cfd8e6;
  --marigold: #f2b233;
  --marigold-soft: #fcebc4;
  --on-accent: #1b2540;
  --shadow: 0 18px 40px -18px rgba(27, 37, 64, 0.28);
  --font: 'SF Pro Rounded', ui-rounded, 'Nunito', 'Varela Round', 'Quicksand', system-ui, sans-serif;
  --r-lg: 28px;
  --r-md: 18px;
  --r-pill: 999px;
  --grain: url('{paper}');
}}
:root[data-theme="dark"] {{
  --canvas: #121826;
  --surface: #1b2233;
  --tint: #232c42;
  --ink: #eef2fa;
  --text-2: #a3adc4;
  --line: #313b54;
  --marigold: #f5c055;
  --marigold-soft: #3a3221;
  --on-accent: #121826;
  --shadow: 0 18px 40px -18px rgba(0, 0, 0, 0.6);
  color-scheme: dark;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--grain), var(--canvas); color: var(--ink); font: 17px/1.55 var(--font); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
button {{ font: inherit; color: inherit; cursor: pointer; background: none; border: 0; }}
:focus-visible {{ outline: 3px solid var(--marigold); outline-offset: 3px; border-radius: 8px; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 48px; }}

header {{ height: 76px; display: flex; align-items: center; justify-content: space-between; }}
.brand {{ font-weight: 800; font-size: 22px; letter-spacing: -0.02em; display: flex; gap: 8px; align-items: center; }}
.brand svg {{ color: var(--marigold); }}
nav {{ display: flex; gap: 26px; font-size: 15px; color: var(--text-2); align-items: center; }}
nav .btn {{ color: var(--on-accent); }}

.btn {{ display: inline-flex; align-items: center; gap: 10px; background: var(--marigold); color: var(--on-accent); font-weight: 700; border-radius: var(--r-pill); padding: 12px 22px; white-space: nowrap; transition: transform .12s; }}
.btn:active {{ transform: scale(.98); }}
.btn.big {{ font-size: 19px; padding: 16px 28px; }}
.btn.ghost {{ background: transparent; color: var(--ink); box-shadow: inset 0 0 0 2px var(--line); }}

.hero {{ padding: 56px 0 40px; position: relative; }}
.sentence {{ font-size: 54px; line-height: 1.32; font-weight: 700; letter-spacing: -0.03em; max-width: 22ch; }}
.sentence .quiet {{ color: var(--text-2); font-weight: 600; }}
.slot {{ display: inline-flex; align-items: center; gap: 6px; color: var(--ink); border-bottom: 5px solid var(--marigold); padding: 0 2px; line-height: 1.05; position: relative; }}
.slot svg {{ color: var(--marigold); }}
.slot.open {{ background: var(--marigold-soft); border-radius: 12px 12px 0 0; padding: 0 10px; }}
.anchor {{ position: relative; display: inline-block; }}
.menu {{ margin-top: 28px; max-width: 760px; background: var(--surface); border-radius: var(--r-lg); box-shadow: var(--shadow); padding: 18px; font-size: 16px; letter-spacing: 0; line-height: 1.3; }}
.menu .mt {{ font-size: 14px; color: var(--text-2); font-weight: 600; padding: 4px 10px 12px; }}
.menu ul {{ list-style: none; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; }}
.opt {{ width: 100%; display: flex; align-items: center; gap: 10px; padding: 10px; border-radius: 12px; font-weight: 600; text-align: left; }}
.opt svg {{ color: var(--text-2); flex: none; }}
.opt:hover {{ background: var(--tint); }}
.opt.on {{ background: var(--marigold); color: var(--on-accent); }}
.opt.on svg {{ color: var(--on-accent); }}
.go {{ margin-top: 32px; display: flex; gap: 14px; align-items: center; }}
.go small {{ color: var(--text-2); font-size: 15px; margin-left: 8px; }}

.results {{ padding: 72px 0 24px; }}
h2 {{ font-size: 34px; font-weight: 800; letter-spacing: -0.03em; line-height: 1.15; text-wrap: balance; }}
.sub {{ color: var(--text-2); margin-top: 8px; }}
.trio {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 44px; align-items: start; }}
.f1 {{ margin-top: 72px; }}
.f2 {{ margin-top: 28px; }}
.frame {{ position: relative; margin: 0 14px 22px 0; }}
.frame::before {{ content: ""; position: absolute; inset: 14px -14px -14px 14px; border-radius: var(--r-lg); background: var(--marigold-soft); }}
.f1 .frame::before {{ background: var(--tint); }}
.frame .photo {{ position: relative; aspect-ratio: 4 / 4.6; border-radius: var(--r-lg); }}
.f h3 {{ font-size: 24px; font-weight: 800; letter-spacing: -0.02em; }}
.role {{ color: var(--text-2); font-size: 15px; margin-top: 2px; }}
.helps {{ font-size: 16px; margin-top: 10px; }}
.row {{ display: flex; align-items: center; gap: 16px; margin-top: 16px; }}
.price {{ font-weight: 800; font-size: 15px; font-variant-numeric: tabular-nums; background: var(--surface); box-shadow: inset 0 0 0 2px var(--line); padding: 5px 12px; border-radius: var(--r-pill); white-space: nowrap; }}
.price.free {{ background: var(--marigold-soft); box-shadow: none; }}
.link {{ font-weight: 700; border-bottom: 2px solid var(--marigold); }}

.more {{ margin: 56px 0 0; display: flex; align-items: center; gap: 18px; background: var(--surface); border-radius: var(--r-pill); padding: 10px 12px 10px 14px; width: fit-content; box-shadow: var(--shadow); }}
.av {{ width: 44px; height: 44px; border-radius: 50%; border: 3px solid var(--surface); margin-left: -16px; }}
.av:first-child {{ margin-left: 0; }}
.more span.t {{ font-weight: 700; }}

.faq {{ margin: 88px 0 56px; display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 48px; }}
details {{ border-top: 2px solid var(--line); padding: 18px 0; }}
details:last-child {{ border-bottom: 2px solid var(--line); }}
summary {{ font-weight: 700; font-size: 19px; cursor: pointer; list-style: none; display: flex; justify-content: space-between; }}
summary::after {{ content: "+"; color: var(--marigold); font-weight: 800; }}
details[open] summary::after {{ content: "\\2212"; }}
details p {{ color: var(--text-2); margin-top: 8px; max-width: 56ch; }}

footer {{ padding: 24px 0 40px; color: var(--text-2); font-size: 14px; display: flex; justify-content: space-between; }}
@media (max-width: 900px) {{
  .wrap {{ padding: 0 16px; }}
  .sentence {{ font-size: 34px; }}
  .menu ul {{ grid-template-columns: 1fr 1fr; }}
  .trio, .faq {{ grid-template-columns: 1fr; }}
  .f1, .f2 {{ margin-top: 0; }}
  nav a:not(.btn) {{ display: none; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
{portraits_css()}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <a class="brand" href="#"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 20V4M19 20V4M5 12h14"/></svg>Hallway</a>
    <nav><a href="#">For professionals</a><a href="#">Log in</a><a class="btn" href="#">Sign up</a></nav>
  </header>

  <section class="hero">
    <div class="sentence">
      <span class="quiet">I&rsquo;m curious about</span>
      <span class="anchor"><button class="slot open" type="button" aria-expanded="true">Product design{caret}</button>
      </span>
      <span class="quiet">and want to talk with someone</span>
      <button class="slot" type="button">a few years in{caret}</button><span class="quiet">.</span>
    </div>
    <div class="menu" role="dialog" aria-label="Pick a field">
          <div class="mt">Pick the field you want to explore</div>
          <ul>
{options}
          </ul>
        </div>
    <div class="go">
      <a class="btn big" href="#people">Show me people</a>
      <small>Takes a minute. No account needed to look.</small>
    </div>
  </section>

  <section class="results" id="people">
    <h2>Three people who&rsquo;d be glad to talk</h2>
    <p class="sub">Picked from 38 professionals in Product design.</p>
    <div class="trio">
{feat}
    </div>
    <a class="more" href="#">{avatars}<span class="t">See 35 more in Product design</span></a>
  </section>

  <section class="faq">
    <h2>Good to know before your first chat</h2>
    <div>
      <details open><summary>What happens in a chat?</summary><p>You get 20 or 30 minutes on a video call. Bring a question, a portfolio or a job post. Most people leave with one clear next step.</p></details>
      <details><summary>Why do some people charge?</summary></details>
      <details><summary>Is the first chat really free?</summary></details>
      <details><summary>I&rsquo;m a professional. Can I help?</summary></details>
    </div>
  </section>

  <footer><span>Hallway</span><span>Professionals set their own price.</span></footer>
</div>
</body>
</html>
'''
write("03-offcatalog-mockup.html", html)
