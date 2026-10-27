from html import escape as e
from common import *

fields = "\n".join(
    f'<a href="#" class="{"on" if l == SELECTED else ""}"{" aria-current=page" if l == SELECTED else ""}>{e(l)}</a>'
    for _, l in AREAS)

gallery = "\n".join(f'''<figure class="g g{n}">
  <div class="photo ph-{i}" role="img" aria-label="Photo of {e(PEOPLE[i]["name"])}"></div>
  <figcaption>
    <span class="nm">{e(PEOPLE[i]["name"])}</span>
    <span class="rl">{e(PEOPLE[i]["role"])}, {e(PEOPLE[i]["org"])}</span>
    <span class="pr{" free" if PEOPLE[i]["free"] else ""}">{e(price_text(PEOPLE[i]))}</span>
  </figcaption>
</figure>''' for n, i in enumerate([1, 2, 3, 4, 5]))

m = PEOPLE[0]
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Big portrait, one person first</title>
<style>
:root {{
  --bg: #eef0ec;
  --surface: #f8f9f6;
  --ink: #1e2721;
  --muted: #5b665e;
  --line: #d3d8d0;
  --accent: #2b4acb;
  --accent-soft: #e2e7fa;
  --on-accent: #ffffff;
  --serif: 'Iowan Old Style', 'Charter', 'Palatino Linotype', Palatino, Georgia, serif;
  --sans: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --r: 4px;
}}
:root[data-theme="dark"] {{
  --bg: #141815;
  --surface: #1b201c;
  --ink: #e9ece6;
  --muted: #a2aca4;
  --line: #2e352f;
  --accent: #8ea2ff;
  --accent-soft: #232a45;
  --on-accent: #141815;
  color-scheme: dark;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--bg); color: var(--ink); font: 16px/1.55 var(--sans); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 3px; }}
.wrap {{ max-width: 1280px; margin: 0 auto; padding: 0 40px; }}

header {{ height: 68px; display: flex; align-items: center; justify-content: space-between; }}
.brand {{ font-family: var(--serif); font-size: 24px; font-weight: 700; letter-spacing: -0.01em; }}
nav {{ display: flex; gap: 28px; align-items: center; font-size: 15px; color: var(--muted); }}
.btn {{ display: inline-block; background: var(--accent); color: var(--on-accent); padding: 13px 22px; border-radius: var(--r); font-weight: 600; white-space: nowrap; }}
.btn.sm {{ padding: 8px 14px; font-size: 14px; }}
.btn.text {{ background: none; color: var(--ink); padding: 13px 4px; border-bottom: 1px solid var(--ink); border-radius: 0; }}

.hero {{ display: grid; grid-template-columns: 7fr 5fr; gap: 56px; align-items: end; padding: 12px 0 0; }}
.ph-hero {{ aspect-ratio: 5 / 5.6; max-height: 680px; width: 100%; border-radius: var(--r); }}
.intro {{ padding-bottom: 12px; }}
.meet {{ display: flex; align-items: center; gap: 10px; font-size: 14px; color: var(--muted); margin-bottom: 22px; }}
.meet b {{ color: var(--ink); font-weight: 600; }}
h1 {{ font-family: var(--serif); font-weight: 500; font-size: 52px; line-height: 1.08; letter-spacing: -0.015em; text-wrap: balance; }}
.lede {{ font-size: 18px; color: var(--muted); margin: 22px 0 30px; max-width: 38ch; }}
.ctas {{ display: flex; gap: 22px; align-items: center; }}
.facts {{ margin-top: 40px; display: grid; grid-template-columns: repeat(3, auto); justify-content: start; gap: 36px; padding-top: 20px; border-top: 1px solid var(--line); }}
.facts dt {{ font-size: 13px; color: var(--muted); }}
.facts dd {{ font-family: var(--serif); font-size: 22px; font-variant-numeric: tabular-nums; margin: 0; }}

.fields {{ margin: 88px 0 0; }}
.fields h2, .gal-head h2 {{ font-family: var(--serif); font-weight: 500; font-size: 32px; letter-spacing: -0.01em; }}
.fields p {{ color: var(--muted); margin-top: 6px; }}
.field-row {{ display: flex; flex-wrap: wrap; gap: 6px 28px; margin-top: 24px; font-family: var(--serif); font-size: 26px; line-height: 1.5; }}
.field-row a {{ color: var(--muted); transition: color .15s; }}
.field-row a:hover {{ color: var(--ink); }}
.field-row a.on {{ color: var(--accent); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 6px; }}

.gal-head {{ display: flex; justify-content: space-between; align-items: baseline; margin: 80px 0 28px; }}
.gal-head a {{ font-size: 15px; border-bottom: 1px solid var(--ink); }}
.gallery {{ columns: 3; column-gap: 28px; }}
.g {{ break-inside: avoid; margin: 0 0 36px; }}
.g .photo {{ width: 100%; border-radius: var(--r); }}
.g0 .photo {{ aspect-ratio: 4 / 5; }}
.g1 .photo {{ aspect-ratio: 1 / 1; }}
.g2 .photo {{ aspect-ratio: 4 / 5.4; }}
.g3 .photo {{ aspect-ratio: 4 / 3.2; }}
.g4 .photo {{ aspect-ratio: 4 / 4.4; }}
figcaption {{ display: grid; grid-template-columns: 1fr auto; gap: 2px 16px; margin-top: 12px; }}
.nm {{ font-family: var(--serif); font-size: 21px; }}
.rl {{ grid-column: 1; color: var(--muted); font-size: 14px; }}
.pr {{ grid-column: 2; grid-row: 1 / span 2; align-self: start; font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; white-space: nowrap; padding-top: 4px; }}
.pr.free {{ color: var(--accent); }}

.voices {{ display: grid; grid-template-columns: 1fr 1fr; gap: 56px; margin: 48px 0 72px; padding-top: 40px; border-top: 1px solid var(--line); }}
blockquote {{ font-family: var(--serif); font-size: 26px; line-height: 1.35; }}
cite {{ display: block; font: 14px/1.4 var(--sans); color: var(--muted); font-style: normal; margin-top: 14px; }}

footer {{ padding: 24px 0 40px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; font-size: 14px; color: var(--muted); }}
@media (max-width: 900px) {{
  .wrap {{ padding: 0 16px; }}
  .hero, .voices {{ grid-template-columns: 1fr; }}
  h1 {{ font-size: 38px; }}
  .gallery {{ columns: 1; }}
  nav a:not(.btn) {{ display: none; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
{portrait_css(m, "ph-hero", 1000, 1120)}
{portraits_css(w=600, h=720)}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <a class="brand" href="#">Hallway</a>
    <nav><a href="#">How it works</a><a href="#">For professionals</a><a href="#">Log in</a><a class="btn sm" href="#">Sign up</a></nav>
  </header>

  <section class="hero">
    <div class="photo ph-hero" role="img" aria-label="Photo of {e(m["name"])}"></div>
    <div class="intro">
      <p class="meet"><b>{e(m["name"])}</b> {e(m["role"])} at {e(m["org"])}</p>
      <h1>Ask Maya how she got her first design job.</h1>
      <p class="lede">She&rsquo;s one of 38 product designers here who make time for students and new grads.</p>
      <div class="ctas">
        <a class="btn" href="#">Book a free intro</a>
        <a class="btn text" href="#fields">Pick another field</a>
      </div>
      <dl class="facts">
        <div><dt>In the field</dt><dd>7 years</dd></div>
        <div><dt>Chats so far</dt><dd>142</dd></div>
        <div><dt>First chat</dt><dd>Free</dd></div>
      </dl>
    </div>
  </section>

  <section class="fields" id="fields">
    <h2>Which field are you curious about?</h2>
    <p>Pick one and we&rsquo;ll show you who&rsquo;s there.</p>
    <div class="field-row">
{fields}
    </div>
  </section>

  <div class="gal-head">
    <h2>More people in Product design</h2>
    <a href="#">See all 38</a>
  </div>
  <section class="gallery">
{gallery}
  </section>

  <section class="voices">
    <blockquote>&ldquo;I was scared to message strangers on LinkedIn. Here, people actually expect you.&rdquo;<cite>Lucía Ortega, graduated in May</cite></blockquote>
    <blockquote>&ldquo;Grace walked me through my offer line by line. I asked for more and got it.&rdquo;<cite>Dev Malhotra, junior designer</cite></blockquote>
  </section>

  <footer><span>Hallway</span><span>Professionals set their own price. Many offer a free first chat.</span></footer>
</div>
</body>
</html>
'''
write("05-offcatalog-mockup.html", html)
