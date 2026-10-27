from html import escape as e
from common import *

COUNTS = [38, 54, 41, 27, 33, 19, 46, 22, 17, 12, 15, 29]
WIDE = {"Software engineering", "Healthcare", "Teaching"}
TINTS = ["sun", "aqua", "coral", "sky", "plain", "sun", "aqua", "plain", "coral", "sky", "plain", "aqua"]

tiles = []
for (k, label), n, tint in zip(AREAS, COUNTS, TINTS):
    cls = "tile"
    if label == SELECTED:
        cls += " sel"
    elif label in WIDE:
        cls += " wide"
    cls += f" t-{tint}"
    pressed = "true" if label == SELECTED else "false"
    tiles.append(f'<button class="{cls}" type="button" aria-pressed="{pressed}">{icon(k, 26 if label == SELECTED else 22, 2)}'
                 f'<span class="name">{e(label)}</span><span class="n">{n} people</span></button>')
tiles = "\n".join(tiles)

RING = ["sun", "coral", "aqua", "sky", "sun", "coral"]
people = "\n".join(f'''<article class="pc">
  <div class="ring r-{RING[i]}"><div class="photo ph-{i}" role="img" aria-label="Photo of {e(p["name"])}"></div></div>
  <h3>{e(p["name"])}</h3>
  <p class="role">{e(p["role"])}<br>{e(p["org"])}</p>
  <p class="helps">{e(p["helps"])}</p>
  <div class="row"><span class="pill{" free" if p["free"] else ""}">{e(price_text(p))}</span><a class="go" href="#" aria-label="Say hi to {e(p["first"])}">Say hi</a></div>
</article>''' for i, p in enumerate(PEOPLE))

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Big bright tiles, pick a field</title>
<style>
:root {{
  --ink: #0c3a43;
  --canvas: #eaf7f3;
  --card: #ffffff;
  --muted-surface: #d4eee7;
  --text-2: #2d5a62;
  --soft-border: #a9d6cb;
  --coral: #ff7a6b;
  --sun: #ffd447;
  --aqua: #7fe3d0;
  --sky: #9cc9ff;
  --on-accent: #0c3a43;
  --shadow: 4px 4px 0 var(--ink);
  --shadow-sm: 3px 3px 0 var(--ink);
  --font: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --r-card: 16px;
  --r-cta: 4px;
}}
:root[data-theme="dark"] {{
  --ink: #e6f4f0;
  --canvas: #0b1d21;
  --card: #11292e;
  --muted-surface: #173439;
  --text-2: #a6c6c4;
  --soft-border: #2c4a50;
  --on-accent: #0b1d21;
  --shadow: 4px 4px 0 #3c6168;
  --shadow-sm: 3px 3px 0 #3c6168;
  color-scheme: dark;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--canvas); color: var(--ink); font: 15px/1.5 var(--font); font-feature-settings: "ss04", "ss11"; -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
button {{ font: inherit; color: inherit; cursor: pointer; }}
:focus-visible {{ outline: 3px solid var(--coral); outline-offset: 3px; }}
.wrap {{ max-width: 1240px; margin: 0 auto; padding: 0 40px; }}

header {{ display: flex; align-items: center; justify-content: space-between; height: 72px; }}
.logo {{ display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 20px; letter-spacing: -0.03em; }}
.logo b {{ width: 30px; height: 30px; border-radius: 50%; background: var(--sun); border: 1.5px solid var(--ink); display: grid; place-items: center; font-size: 15px; color: var(--on-accent); }}
nav {{ display: flex; gap: 8px; align-items: center; }}
nav a {{ padding: 8px 14px; border-radius: 999px; font-weight: 500; font-size: 14px; }}
nav a:hover {{ background: var(--muted-surface); }}
.cta {{ background: var(--ink); color: var(--canvas); border-radius: var(--r-cta); padding: 12px 20px; font-weight: 700; font-size: 15px; display: inline-block; box-shadow: var(--shadow-sm); border: 1.5px solid var(--ink); transition: transform .1s, box-shadow .1s; white-space: nowrap; }}
.cta:hover {{ transform: translate(-1px, -1px); box-shadow: 4px 4px 0 var(--coral); }}
.cta:active {{ transform: translate(2px, 2px); box-shadow: 1px 1px 0 var(--ink); }}
nav .cta {{ padding: 9px 16px; font-size: 14px; }}

.top {{ display: grid; grid-template-columns: 340px 1fr; gap: 48px; padding: 36px 0 64px; align-items: start; }}
h1 {{ font-size: 52px; line-height: 1.02; letter-spacing: -0.045em; font-weight: 700; text-wrap: balance; }}
.lede {{ font-size: 17px; color: var(--text-2); margin: 20px 0 28px; max-width: 32ch; }}
.how {{ margin-top: 40px; padding: 0; list-style: none; display: grid; gap: 12px; }}
.how li {{ display: grid; grid-template-columns: 28px 1fr; gap: 12px; align-items: start; font-size: 14px; color: var(--text-2); }}
.how b {{ width: 28px; height: 28px; border-radius: 50%; border: 1.5px solid var(--ink); display: grid; place-items: center; font-size: 13px; color: var(--ink); background: var(--card); }}
.how strong {{ color: var(--ink); display: block; font-size: 15px; }}

.bento {{ display: grid; grid-template-columns: repeat(6, 1fr); grid-auto-rows: 118px; gap: 12px; grid-auto-flow: dense; }}
.tile {{ position: relative; text-align: left; border: 1.5px solid var(--ink); border-radius: var(--r-card); background: var(--card); padding: 16px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: var(--shadow-sm); transition: transform .12s, box-shadow .12s; }}
.tile:hover {{ transform: translate(-2px, -2px); box-shadow: 5px 5px 0 var(--ink); }}
.tile .name {{ font-weight: 700; font-size: 16px; letter-spacing: -0.02em; line-height: 1.15; }}
.tile .n {{ font-size: 12px; color: var(--text-2); font-variant-numeric: tabular-nums; }}
.tile .name + .n {{ margin-top: -10px; }}
.wide {{ grid-column: span 2; }}
.t-sun {{ background: color-mix(in srgb, var(--sun) 38%, var(--card)); }}
.t-aqua {{ background: color-mix(in srgb, var(--aqua) 38%, var(--card)); }}
.t-coral {{ background: color-mix(in srgb, var(--coral) 26%, var(--card)); }}
.t-sky {{ background: color-mix(in srgb, var(--sky) 38%, var(--card)); }}
.sel {{ grid-column: span 2; grid-row: span 2; background: var(--sun); color: var(--on-accent); box-shadow: var(--shadow); padding: 22px; }}
.sel .name {{ font-size: 30px; letter-spacing: -0.04em; }}
.sel .n {{ color: var(--on-accent); font-size: 14px; font-weight: 600; }}
.sel::after {{ content: "Picked"; position: absolute; top: 18px; right: 18px; font-size: 12px; font-weight: 700; background: var(--ink); color: var(--sun); padding: 4px 10px; border-radius: 999px; }}

.strip-head {{ display: flex; align-items: end; justify-content: space-between; margin-bottom: 20px; }}
h2 {{ font-size: 34px; letter-spacing: -0.04em; font-weight: 700; line-height: 1.1; }}
h2 span {{ background: var(--sun); color: var(--on-accent); padding: 0 8px; border-radius: 8px; }}
.strip-head a {{ font-weight: 600; font-size: 14px; border-bottom: 1.5px solid var(--ink); }}
.strip {{ display: grid; grid-template-columns: repeat(6, minmax(220px, 1fr)); gap: 16px; overflow-x: auto; padding: 4px 6px 14px 2px; scroll-snap-type: x mandatory; }}
.pc {{ scroll-snap-align: start; background: var(--card); border: 1.5px solid var(--ink); border-radius: var(--r-card); padding: 18px; display: flex; flex-direction: column; gap: 8px; box-shadow: var(--shadow-sm); }}
.ring {{ width: 84px; height: 84px; border-radius: 50%; border: 1.5px solid var(--ink); padding: 5px; margin-bottom: 6px; }}
.r-sun {{ background: var(--sun); }} .r-coral {{ background: var(--coral); }} .r-aqua {{ background: var(--aqua); }} .r-sky {{ background: var(--sky); }}
.ring .photo {{ width: 100%; height: 100%; border-radius: 50%; border: 1.5px solid var(--ink); }}
.pc h3 {{ font-size: 17px; letter-spacing: -0.02em; }}
.pc .role {{ font-size: 13px; color: var(--text-2); line-height: 1.35; }}
.pc .helps {{ font-size: 14px; flex: 1; }}
.pc .row {{ display: flex; align-items: center; justify-content: space-between; margin-top: 6px; }}
.pill {{ font-size: 12px; font-weight: 700; border-radius: 999px; padding: 4px 10px; border: 1.5px solid var(--ink); font-variant-numeric: tabular-nums; white-space: nowrap; }}
.pill.free {{ background: var(--aqua); color: var(--on-accent); }}
.go {{ font-size: 13px; font-weight: 700; padding: 6px 12px; border-radius: var(--r-cta); background: var(--ink); color: var(--canvas); }}

.quotes {{ display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 16px; margin: 64px 0 48px; }}
blockquote {{ border-radius: var(--r-card); padding: 24px; font-size: 17px; line-height: 1.45; letter-spacing: -0.01em; font-weight: 500; }}
blockquote:nth-child(1) {{ background: var(--ink); color: var(--canvas); font-size: 22px; letter-spacing: -0.02em; }}
blockquote:nth-child(2) {{ background: var(--muted-surface); }}
blockquote:nth-child(3) {{ background: color-mix(in srgb, var(--coral) 24%, var(--canvas)); }}
cite {{ display: block; margin-top: 14px; font-style: normal; font-size: 13px; font-weight: 600; opacity: .8; }}

footer {{ border-top: 1.5px solid var(--ink); padding: 20px 0 36px; display: flex; justify-content: space-between; font-size: 13px; color: var(--text-2); }}
@media (max-width: 900px) {{
  .wrap {{ padding: 0 16px; }}
  .top {{ grid-template-columns: 1fr; }}
  .bento {{ grid-template-columns: repeat(2, 1fr); }}
  .quotes {{ grid-template-columns: 1fr; }}
  nav a:not(.cta) {{ display: none; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
{portraits_css()}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <a class="logo" href="#"><b>H</b>Hallway</a>
    <nav>
      <a href="#">How it works</a>
      <a href="#">For professionals</a>
      <a href="#">Log in</a>
      <a class="cta" href="#">Sign up</a>
    </nav>
  </header>

  <section class="top">
    <div>
      <h1>Pick a field. Meet someone in it.</h1>
      <p class="lede">Short, friendly chats with professionals who remember being where you are.</p>
      <a class="cta" href="#people">Find someone</a>
      <ol class="how">
        <li><b>1</b><span><strong>Pick a field</strong>Anything you&rsquo;re even a little curious about.</span></li>
        <li><b>2</b><span><strong>Pick a person</strong>Free intros or paid sessions, your call.</span></li>
        <li><b>3</b><span><strong>Say hi</strong>Book 20 to 30 minutes on a video call.</span></li>
      </ol>
    </div>
    <div class="bento">
{tiles}
    </div>
  </section>

  <section id="people">
    <div class="strip-head">
      <h2>People in <span>Product design</span></h2>
      <a href="#">See all 38</a>
    </div>
    <div class="strip">
{people}
    </div>
  </section>

  <section class="quotes">
    <blockquote>&ldquo;Maya looked at my portfolio for twenty minutes and told me exactly what to cut. I got the interview.&rdquo;<cite>Lucía Ortega, graduated in May</cite></blockquote>
    <blockquote>&ldquo;I didn&rsquo;t know UX research was a job until I talked to Priya.&rdquo;<cite>Sam Adeyemi, senior at Ohio State</cite></blockquote>
    <blockquote>&ldquo;I give two free chats a week. It&rsquo;s the best hour of my Tuesday.&rdquo;<cite>Tomás Lindqvist, freelance designer</cite></blockquote>
  </section>

  <footer><span>Hallway</span><span>Professionals set their own price. Many offer a free first chat.</span></footer>
</div>
</body>
</html>
'''
write("02-gummy-mockup.html", html)
