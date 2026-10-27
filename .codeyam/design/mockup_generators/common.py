"""Shared content + imagery helpers for the Hallway mockups."""
import base64, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "project_mockups")

AREAS = [
    ("design", "Product design"),
    ("code", "Software engineering"),
    ("megaphone", "Marketing"),
    ("chart", "Finance"),
    ("heart", "Healthcare"),
    ("scale", "Law"),
    ("book", "Teaching"),
    ("dots", "Data science"),
    ("hands", "Nonprofits"),
    ("building", "Architecture"),
    ("pen", "Journalism"),
    ("compass", "Consulting"),
]
SELECTED = "Product design"

# name, role, company line, years, helps with, price, price_kind, chats, portrait params, photo keywords
PEOPLE = [
    dict(name="Maya Okafor", first="Maya", role="Senior product designer", org="Fernway, a travel app",
         years="7 years in", helps="Portfolio reviews and your first offer", price="Free intro",
         free=True, chats=142, skin="#8d5a3b", hair="#1f1410", shirt="#e9b949", bg="#d8e6e1",
         style="curls", kw="portrait,woman,smiling", lock=31),
    dict(name="Daniel Reyes", first="Daniel", role="Design lead", org="Brightwell Health",
         years="11 years in", helps="Moving from agency to in-house", price="$30", unit="30 min",
         free=False, chats=88, skin="#c58c62", hair="#2b1d16", shirt="#3d6b8f", bg="#e6dccd",
         style="short", kw="portrait,man,beard", lock=17),
    dict(name="Priya Nair", first="Priya", role="UX researcher", org="Tallgrass Bank",
         years="5 years in", helps="Research roles nobody tells you about", price="$20", unit="30 min",
         free=False, chats=61, skin="#a86f4c", hair="#120c0a", shirt="#7a3b52", bg="#e4e1ee",
         style="long", kw="portrait,woman,office", lock=44),
    dict(name="Tomás Lindqvist", first="Tomás", role="Freelance brand and product designer", org="Self-employed",
         years="9 years in", helps="Pricing your first freelance project", price="Free",
         free=True, chats=203, skin="#e6bfa0", hair="#b58a4e", shirt="#2f4a3a", bg="#dfe9d6",
         style="short", kw="portrait,man,glasses", lock=8),
    dict(name="Grace Whitfield", first="Grace", role="Head of design", org="Loop & Line, logistics",
         years="15 years in", helps="Reading a job offer and negotiating it", price="$45", unit="30 min",
         free=False, chats=37, skin="#f0cdb4", hair="#6b3a24", shirt="#1f2a44", bg="#efd9cf",
         style="bob", kw="portrait,woman,professional", lock=52),
    dict(name="Kenji Abe", first="Kenji", role="Product designer", org="Harbor Learning",
         years="2 years in", helps="What the job hunt looks like right now", price="Free",
         free=True, chats=29, skin="#d9a982", hair="#15110f", shirt="#d9663d", bg="#dbe4ef",
         style="swept", kw="portrait,young,man", lock=63),
]


def _hair(style, c):
    if style == "curls":
        return (f'<circle cx="100" cy="78" r="50" fill="{c}"/><circle cx="62" cy="96" r="22" fill="{c}"/>'
                f'<circle cx="138" cy="96" r="22" fill="{c}"/><circle cx="76" cy="58" r="22" fill="{c}"/>'
                f'<circle cx="124" cy="58" r="22" fill="{c}"/>')
    if style == "long":
        return (f'<path d="M50 96 C50 50 75 36 100 36 C125 36 150 50 150 96 L156 170 L44 170 Z" fill="{c}"/>')
    if style == "bob":
        return (f'<path d="M54 100 C52 56 76 40 100 40 C124 40 148 56 146 100 L148 128 L52 128 Z" fill="{c}"/>')
    if style == "swept":
        return (f'<path d="M60 86 C58 52 84 40 106 42 C130 44 146 58 142 86 C132 70 110 62 84 70 Z" fill="{c}"/>')
    return f'<path d="M62 84 C60 54 82 44 100 44 C120 44 140 54 138 84 C126 70 76 70 62 84 Z" fill="{c}"/>'


def portrait_svg(p):
    """A subject-accurate head-and-shoulders depiction: backdrop, shirt, neck, face, hair, soft light."""
    s = p["skin"]
    back_hair = _hair(p["style"], p["hair"]) if p["style"] in ("long", "bob", "curls") else ""
    front_hair = "" if back_hair else _hair(p["style"], p["hair"])
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
        '<defs><radialGradient id="l" cx="35%" cy="25%" r="80%"><stop offset="0" stop-color="#fff" stop-opacity=".55"/>'
        '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="f" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".18"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient></defs>'
        f'<rect width="200" height="200" fill="{p["bg"]}"/><rect width="200" height="200" fill="url(#l)"/>'
        f'{back_hair}'
        f'<path d="M28 200 C30 158 60 140 100 140 C140 140 170 158 172 200 Z" fill="{p["shirt"]}"/>'
        f'<path d="M84 122 L116 122 L114 148 C106 156 94 156 86 148 Z" fill="{s}"/>'
        f'<path d="M86 140 C94 150 106 150 114 140 L112 148 C104 156 96 156 88 148 Z" fill="#000" opacity=".12"/>'
        f'<ellipse cx="100" cy="96" rx="34" ry="40" fill="{s}"/>'
        f'<ellipse cx="66" cy="100" rx="6" ry="9" fill="{s}"/><ellipse cx="134" cy="100" rx="6" ry="9" fill="{s}"/>'
        '<ellipse cx="100" cy="96" rx="34" ry="40" fill="url(#f)"/>'
        f'{front_hair}'
        '<ellipse cx="87" cy="98" rx="3" ry="3.4" fill="#2a1d18"/><ellipse cx="113" cy="98" rx="3" ry="3.4" fill="#2a1d18"/>'
        '<path d="M89 117 C95 122 105 122 111 117" stroke="#5a2e22" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
        '</svg>'
    )
    return svg


def portrait_css(p, cls, w=480, h=480):
    b64 = base64.b64encode(portrait_svg(p).encode()).decode()
    sel = f".{cls},.photo.{cls}" if cls.startswith("ph-") else f".{cls}"
    return (f"{sel}{{background-image:url('https://loremflickr.com/{w}/{h}/{p['kw']}?lock={p['lock']}'),"
            f"url('data:image/svg+xml;base64,{b64}');background-size:cover;background-position:center}}")


def portraits_css(prefix="ph", w=480, h=480):
    return "\n".join(portrait_css(p, f"{prefix}-{i}", w, h) for i, p in enumerate(PEOPLE))


ICONS = {
    "design": '<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
    "code": '<path d="M8 7l-5 5 5 5"/><path d="M16 7l5 5-5 5"/>',
    "megaphone": '<path d="M3 10v4h4l8 4V6L7 10z"/><path d="M18 9a4 4 0 010 6"/>',
    "chart": '<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M21 20H3"/>',
    "heart": '<path d="M12 20s-7-4.5-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.5-7 10-7 10z"/>',
    "scale": '<path d="M12 4v16"/><path d="M5 8h14"/><path d="M5 8l-3 6h6z"/><path d="M19 8l-3 6h6z"/><path d="M8 20h8"/>',
    "book": '<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 19V5"/>',
    "dots": '<circle cx="6" cy="17" r="2"/><circle cx="11" cy="10" r="2"/><circle cx="17" cy="13" r="2"/><circle cx="19" cy="5" r="2"/>',
    "hands": '<path d="M12 21c-4-3-8-6-8-10a4 4 0 018-1 4 4 0 018 1c0 4-4 7-8 10z"/><path d="M9 12h6"/>',
    "building": '<path d="M4 21V7l8-4 8 4v14"/><path d="M9 21v-5h6v5"/><path d="M9 10h.01M15 10h.01"/>',
    "pen": '<path d="M5 4h14"/><path d="M5 9h14"/><path d="M5 14h9"/><path d="M5 19h6"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
}


def icon(key, size=20, sw=1.8):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>')


def price_text(p):
    return p["price"] if p["free"] else f'{p["price"]} / {p["unit"]}'


def write(name, html):
    path = os.path.join(OUT, name)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        f.write(html)
    os.replace(tmp, path)
    print("wrote", name, len(html))
