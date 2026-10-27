from html import escape as e
from common import *

COUNTS = [38, 54, 41, 27, 33, 19, 46, 22, 17, 12, 15, 29]
fields = "\n".join(
    f'<li><a href="#" class="{"on" if l == SELECTED else ""}">'
    f'{icon(k, 18, 1.6)}<span>{e(l)}</span><b>{n}</b></a></li>' for (k, l), n in zip(AREAS, COUNTS))

rows = "\n".join(f'''<tr>
  <td><div class="who"><span class="photo ph-{i}" role="img" aria-label="Photo of {e(p["name"])}"></span><span><strong>{e(p["name"])}</strong><small>{e(p["role"])}, {e(p["org"])}</small></span></div></td>
  <td class="num">{e(p["years"].split()[0])}</td>
  <td class="helps">{e(p["helps"])}</td>
  <td class="num">{p["chats"]}</td>
  <td class="num price{" free" if p["free"] else ""}">{e(p["price"] if p["free"] else p["price"])}<small>{"" if p["free"] else " / 30 min"}</small></td>
  <td class="act"><a href="#" class="book">Book</a></td>
</tr>''' for i, p in enumerate(PEOPLE))

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="codeyam-viewport" content="desktop">
<title>Evening directory, two panes</title>
<style>
:root {{
  color-scheme: dark;
  --bg: #10201e;
  --pane: #142624;
  --surface: #182d2a;
  --raised: #1f3632;
  --text: #e8efe9;
  --muted: #98aea6;
  --faint: #6c837b;
  --line: #2a423d;
  --dot: rgba(232, 239, 233, 0.07);
  --accent: #f4b183;
  --accent-soft: rgba(244, 177, 131, 0.14);
  --on-accent: #10201e;
  --font: 'Helvetica Neue', Helvetica, Arial, system-ui, sans-serif;
  --r: 6px;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--bg); background-image: radial-gradient(var(--dot) 1px, transparent 1.2px); background-size: 22px 22px; color: var(--text); font: 14px/1.45 var(--font); -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; text-decoration: none; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}

header {{ height: 64px; display: flex; align-items: center; justify-content: space-between; padding: 0 32px; border-bottom: 1px solid var(--line); background: var(--bg); }}
.brand {{ font-weight: 700; font-size: 19px; letter-spacing: -0.02em; display: flex; align-items: center; gap: 10px; }}
.brand i {{ width: 22px; height: 22px; border: 2px solid var(--accent); border-radius: 50%; position: relative; }}
.brand i::after {{ content: ""; position: absolute; inset: 4px; background: var(--accent); border-radius: 50%; }}
nav {{ display: flex; align-items: center; gap: 24px; color: var(--muted); }}
.btn {{ display: inline-block; background: var(--accent); color: var(--on-accent); font-weight: 700; padding: 9px 16px; border-radius: var(--r); white-space: nowrap; }}
.btn.line {{ background: transparent; color: var(--text); box-shadow: inset 0 0 0 1px var(--line); }}

.app {{ display: grid; grid-template-columns: 360px 1fr; min-height: calc(100vh - 64px); }}
aside {{ background: var(--pane); border-right: 1px solid var(--line); padding: 36px 28px; }}
h1 {{ font-size: 34px; line-height: 1.08; letter-spacing: -0.03em; font-weight: 700; text-wrap: balance; }}
aside .lede {{ color: var(--muted); font-size: 15px; margin: 14px 0 26px; max-width: 32ch; }}
label {{ display: block; font-size: 13px; color: var(--muted); margin-bottom: 8px; }}
.search {{ display: flex; align-items: center; gap: 10px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r); padding: 10px 12px; color: var(--faint); }}
.search span {{ color: var(--faint); }}
.fields {{ list-style: none; padding: 0; margin: 22px -12px 0; }}
.fields a {{ display: grid; grid-template-columns: 20px 1fr auto; gap: 12px; align-items: center; padding: 10px 12px; border-radius: var(--r); color: var(--muted); font-size: 15px; }}
.fields a:hover {{ background: var(--surface); color: var(--text); }}
.fields a b {{ font-weight: 400; font-variant-numeric: tabular-nums; color: var(--faint); font-size: 13px; }}
.fields a.on {{ background: var(--accent-soft); color: var(--text); font-weight: 700; box-shadow: inset 3px 0 0 var(--accent); }}
.fields a.on svg, .fields a.on b {{ color: var(--accent); }}

main {{ padding: 36px 40px; }}
.steps {{ display: flex; gap: 0; margin-bottom: 32px; border: 1px solid var(--line); border-radius: var(--r); overflow: hidden; width: fit-content; background: var(--surface); }}
.steps li {{ list-style: none; padding: 10px 18px; font-size: 13px; color: var(--faint); border-right: 1px solid var(--line); display: flex; gap: 8px; align-items: center; }}
.steps li:last-child {{ border-right: 0; }}
.steps li b {{ font-variant-numeric: tabular-nums; }}
.steps li.done {{ color: var(--muted); }}
.steps li.now {{ color: var(--text); background: var(--raised); }}
.steps li.now b {{ color: var(--accent); }}
.steps {{ padding: 0; }}

.head {{ display: flex; align-items: end; justify-content: space-between; gap: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--line); }}
h2 {{ font-size: 44px; letter-spacing: -0.035em; line-height: 1; font-weight: 700; }}
.head p {{ color: var(--muted); margin-top: 10px; font-size: 15px; }}
.filters {{ display: flex; gap: 6px; }}
.filters a {{ padding: 7px 12px; border-radius: var(--r); color: var(--muted); box-shadow: inset 0 0 0 1px var(--line); font-size: 13px; white-space: nowrap; }}
.filters a.on {{ background: var(--text); color: var(--bg); box-shadow: none; font-weight: 700; }}

table {{ width: 100%; border-collapse: collapse; margin-top: 4px; }}
th {{ text-align: left; font-weight: 400; color: var(--faint); font-size: 12px; padding: 14px 12px 10px; }}
th.num, td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
td {{ padding: 14px 12px; border-bottom: 1px solid var(--line); vertical-align: middle; }}
tbody tr:hover td {{ background: var(--surface); }}
.who {{ display: flex; align-items: center; gap: 14px; }}
.who .photo {{ width: 44px; height: 44px; border-radius: var(--r); flex: none; }}
.who strong {{ display: block; font-size: 15px; }}
.who small {{ color: var(--muted); font-size: 13px; }}
td.helps {{ color: var(--muted); max-width: 30ch; }}
td.price {{ font-weight: 700; font-size: 15px; white-space: nowrap; }}
td.price small {{ font-weight: 400; color: var(--faint); font-size: 12px; }}
td.price.free {{ color: var(--accent); }}
td.act {{ text-align: right; width: 1%; }}
.book {{ display: inline-block; padding: 7px 14px; border-radius: var(--r); box-shadow: inset 0 0 0 1px var(--accent); color: var(--accent); font-weight: 700; font-size: 13px; }}
.book:hover {{ background: var(--accent); color: var(--on-accent); }}
.note {{ margin-top: 22px; color: var(--faint); font-size: 13px; display: flex; justify-content: space-between; }}
.note a {{ color: var(--text); border-bottom: 1px solid var(--line); }}

@media (max-width: 900px) {{
  .app {{ grid-template-columns: 1fr; }}
  aside, main {{ padding: 24px 16px; }}
  header {{ padding: 0 16px; }}
  nav a:not(.btn) {{ display: none; }}
  .head {{ flex-direction: column; align-items: start; }}
  td.helps, th.helps, td:nth-child(4), th:nth-child(4) {{ display: none; }}
}}
{portraits_css(w=160, h=160)}
</style>
</head>
<body>
<header>
  <a class="brand" href="#"><i aria-hidden="true"></i>Hallway</a>
  <nav><a href="#">For professionals</a><a href="#">Log in</a><a class="btn" href="#">Sign up</a></nav>
</header>
<div class="app">
  <aside>
    <h1>Career advice from people doing the work.</h1>
    <p class="lede">Pick a field, then book a short chat with someone in it.</p>
    <label for="q">Search fields or people</label>
    <div class="search" id="q"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><span>Try &ldquo;nursing&rdquo; or &ldquo;UX&rdquo;</span></div>
    <ul class="fields">
{fields}
    </ul>
  </aside>
  <main>
    <ol class="steps">
      <li class="done"><b>1</b> Pick a field</li>
      <li class="now"><b>2</b> Pick a person</li>
      <li><b>3</b> Book a chat</li>
    </ol>
    <div class="head">
      <div>
        <h2>Product design</h2>
        <p>38 professionals. 14 offer a free first chat.</p>
      </div>
      <div class="filters" role="group" aria-label="Filter">
        <a class="on" href="#">Everyone</a><a href="#">Free first chat</a><a href="#">Under $30</a><a href="#">Recent grads</a>
      </div>
    </div>
    <table>
      <thead><tr><th>Person</th><th class="num">Years</th><th class="helps">Can help with</th><th class="num">Chats</th><th class="num">Price</th><th><span class="sr" hidden>Action</span></th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
    <p class="note"><span>Showing 6 of 38. Sorted by most chats.</span><a href="#">Show 32 more</a></p>
  </main>
</div>
</body>
</html>
'''
write("04-offcatalog-mockup.html", html)
