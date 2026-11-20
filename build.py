#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du profil GitHub (Uramix2/uramix2).

  Tout le visuel reprend le thème du site uramix2.github.io :
  fond espace sombre (#0a0a0f), accent rouge sakura (#b05060), la vraie
  image de lune (moon-blossom.webp) et les feuilles d'érable animées.

  COMMENT MODIFIER (sans rien casser) :
    1. Édite UNIQUEMENT le bloc « DONNÉES À MODIFIER » ci-dessous
       (focus, toolbox, write-ups, textes de l'en-tête).
    2. Lance :   python3 build.py
    3. Tous les .svg sont régénérés. Le texte de présentation (About)
       se modifie directement dans README.md.

  Pour changer l'image de lune : remplace moon-blossom.webp puis relance.
"""

import base64
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
#  PALETTE (identique au site) — à ne changer que pour retoucher le thème
# =====================================================================
BG        = "#0a0a0f"   # fond espace
CARD      = "#12121a"   # fond des cartes
CARD_IN   = "#0d0d16"   # fond des badges
BORDER    = "#1e1e30"   # bordures
BORDER_IN = "#2a2a40"   # bordures des badges
ACCENT    = "#b05060"   # rouge sakura (accent principal)
ACCENT_LT = "#d06878"   # rouge clair (hover / actif)
TAG       = "#c9707f"   # rose des étiquettes de write-up
TXT       = "#f0ecf5"   # texte principal
TXT2      = "#c8c3d8"   # texte secondaire
MUTED     = "#8a85a0"   # texte discret
FAINT     = "#6a6580"   # texte très discret

MONO = "'JetBrains Mono', 'SFMono-Regular', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"

# Chemin de feuille d'érable (momiji), réutilisé partout.
LEAF = ("M0 3 L-0.72 2.23 Q-1.3 2.16 -3.12 2.81 Q-2.28 1.06 -2.44 0.89 L-2.44 0.89 "
        "Q-3.94 1.06 -6.8 -0.24 Q-3.86 -1.33 -2.36 -1.1 L-2.36 -1.1 Q-4.63 -2.78 -6.02 -6.69 "
        "Q-2.28 -4.89 -0.93 -2.43 L-0.93 -2.43 Q-1.75 -5.74 0.0 -10.0 Q1.75 -5.74 0.93 -2.43 "
        "L0.93 -2.43 Q2.28 -4.89 6.02 -6.69 Q4.63 -2.78 2.36 -1.1 L2.36 -1.1 Q3.86 -1.33 6.8 -0.24 "
        "Q3.94 1.06 2.44 0.89 L2.44 0.89 Q2.28 1.06 3.12 2.81 Q1.3 2.16 0.72 2.23 Z")
LEAF_COLORS = ["#e2452b", "#d2331f", "#c22a22", "#a81f16", "#ee5a30", "#e8703a"]


# =====================================================================
# ====================  DONNÉES À MODIFIER  ===========================
# =====================================================================

# ---- En-tête ----
HEADER = {
    "name":     "Uramix",
    "subtitle": "offensive security student",
    "tagline":  "red team · web · active directory · pwn · crypto",
    "motd":     "cat /etc/motd",
}

# ---- Focus : 3 cartes (titre -> liste de techniques) ----
#   Ajoute/retire des lignes librement (jusqu'à 6 par carte).
FOCUS = [
    ("Web exploitation",    ["SQL injection", "XSS", "SSRF", "CSRF", "LFI", "JWT"]),
    ("Binary exploitation", ["ret2win", "shellcode", "ASM", "BOF", "format string"]),
    ("Red team",            ["DLL hijacking", "C2 controller", "lateral movement", "UAC bypass"]),
]

# ---- Toolbox : catégorie -> liste d'outils ----
TOOLBOX = [
    ("web",       ["Burp Suite", "curl", "Nmap", "gobuster / ffuf", "Metasploit"]),
    ("privesc",   ["Potato", "LinPEAS", "Docker", "CVEs"]),
    ("pwn",       ["GDB / gef", "IDA", "cyclic"]),
    ("ad",        ["BloodHound", "Impacket", "nxc"]),
    ("languages", ["Python", "Bash", "C", "ASM", "PowerShell"]),
]

# ---- Write-ups : titre, sous-titre, url (relative à uramix2.github.io),
#      étiquettes, date (jj/mm/aa), nom du fichier .svg ----
WRITEUPS = [
    {
        "title":    "Corporate",
        "subtitle": "Chained web flaws to a foothold, then pivoted through Docker and Proxmox to root.",
        "url":      "https://uramix2.github.io/posts/corporate-htb/",
        "tags":     ["HTB", "INSANE"],
        "date":     "02/11/26",
        "file":     "wu-corporate.svg",
    },
    {
        "title":    "Pwn Project — Buffer Overflow & Shellcode",
        "subtitle": "Integer truncation, stack overflow, then shellcode in an RWX page.",
        "url":      "https://uramix2.github.io/posts/pwn-project-ftp/",
        "tags":     ["PWN"],
        "date":     "01/06/26",
        "file":     "wu-pwn-project-ftp.svg",
    },
    {
        "title":    "This is fine",
        "subtitle": "CPython small-integer caching and Vieta's formulas.",
        "url":      "https://uramix2.github.io/posts/this-is-fine/",
        "tags":     ["MISC"],
        "date":     "12/04/26",
        "file":     "wu-this-is-fine.svg",
    },
    {
        "title":    "Secure AES",
        "subtitle": "Timing attack on the IV, then a padding oracle on a custom AES-CBC.",
        "url":      "https://uramix2.github.io/posts/secure-aes-write-up/",
        "tags":     ["CRYPTO"],
        "date":     "15/02/26",
        "file":     "wu-secure-aes.svg",
    },
    {
        "title":    "What is d?",
        "subtitle": "A Mersenne prime in an RSA modulus, and a flag hidden in the private key.",
        "url":      "https://uramix2.github.io/posts/cnc-crypto-write-up/",
        "tags":     ["CRYPTO"],
        "date":     "01/02/26",
        "file":     "wu-what-is-d.svg",
    },
]

# =====================================================================
# ==================  FIN DES DONNÉES À MODIFIER  =====================
# =====================================================================


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#x27;"))


def mono(x, y, size, fill, text, weight=None, anchor=None, spacing=None, opacity=None):
    attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{MONO}"', f'font-size="{size}"', f'fill="{fill}"']
    if weight:  attrs.append(f'font-weight="{weight}"')
    if anchor:  attrs.append(f'text-anchor="{anchor}"')
    if spacing: attrs.append(f'letter-spacing="{spacing}"')
    if opacity: attrs.append(f'opacity="{opacity}"')
    return f'<text {" ".join(attrs)}>{esc(text)}</text>'


def sans(x, y, size, fill, text):
    return (f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" '
            f'fill="{fill}">{esc(text)}</text>')


# ---------------------------------------------------------------------
#  EN-TÊTE  (vraie image de lune + fond espace + feuilles animées)
# ---------------------------------------------------------------------
def build_header() -> str:
    # Image de lune encodée en base64 -> l'SVG est autonome (aucune
    # ressource externe, rien à proxifier côté GitHub).
    with open(os.path.join(HERE, "moon-blossom.webp"), "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    href = f"data:image/webp;base64,{b64}"

    # Placement de l'image (ratio 706/650), ancrée au bord droit, lune en haut.
    iw = 560
    ih = iw * 650 / 706                     # hauteur affichée
    ix = 1240 - iw                          # déborde un peu à droite (coupé par le cadre)
    iy = -72                                 # remonte : le bas de l'image est coupé par le cadre
    mx = ix + 350 / 706 * iw               # centre de la lune (x)
    my = iy + 232 / 650 * ih               # centre de la lune (y)

    # Champ d'étoiles déterministe (même rendu à chaque build).
    rnd = random.Random(7)
    stars = []
    for _ in range(70):
        sx = round(rnd.uniform(20, 660), 0)        # surtout à gauche, sous le texte
        sy = round(rnd.uniform(8, 292), 0)
        r = rnd.choice([0.6, 0.8, 1.0, 1.3])
        op = round(rnd.uniform(0.2, 0.68), 2)
        stars.append(f'<circle cx="{sx}" cy="{sy}" r="{r}" opacity="{op}"/>')
    stars_svg = "".join(stars)

    # Feuilles d'érable qui tombent (comme sur le site, discrètes).
    rnd2 = random.Random(21)
    fall = []
    for _ in range(7):
        startx = round(rnd2.uniform(120, 620))
        dur = round(rnd2.uniform(11, 16), 1)
        delay = round(rnd2.uniform(-9, -1), 1)
        spind = round(rnd2.uniform(3.6, 5.4), 1)
        sc = round(rnd2.uniform(0.8, 1.3), 2)
        col = rnd2.choice(LEAF_COLORS)
        fall.append(
            f'<g class="fall" style="animation-duration:{dur}s;animation-delay:{delay}s">'
            f'<g transform="translate({startx} 0)">'
            f'<use href="#leaf" class="spin" style="animation-duration:{spind}s" '
            f'transform="scale({sc})" fill="{col}" opacity="0.85"/></g></g>'
        )
    fall_svg = "".join(fall)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="Uramix — offensive security student: red team, web exploitation, privilege escalation, Active Directory, pwn">
  <defs>
    <radialGradient id="neb1" cx="10%" cy="22%" r="55%"><stop offset="0" stop-color="#78203a" stop-opacity="0.38"/><stop offset="1" stop-color="#78203a" stop-opacity="0"/></radialGradient>
    <radialGradient id="neb2" cx="72%" cy="78%" r="60%"><stop offset="0" stop-color="#3e2f86" stop-opacity="0.30"/><stop offset="1" stop-color="#3e2f86" stop-opacity="0"/></radialGradient>
    <linearGradient id="rule" x1="0" x2="1"><stop offset="0" stop-color="{ACCENT}"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
    <!-- L'image de lune, définie une fois (réutilisée pour l'affichage ET comme masque). -->
    <image id="moonimg" href="{href}" x="{ix:.0f}" y="{iy:.0f}" width="{iw:.0f}" height="{ih:.0f}" preserveAspectRatio="xMidYMid slice"/>
    <!-- Fondus des bords (gauche + bas) pour qu'aucun bord droit ne soit net. -->
    <linearGradient id="gleft" gradientUnits="userSpaceOnUse" x1="815" y1="0" x2="955" y2="0"><stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>
    <linearGradient id="gbot" gradientUnits="userSpaceOnUse" x1="0" y1="205" x2="0" y2="300"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
    <radialGradient id="goval" cx="{mx:.0f}" cy="{my:.0f}" r="330" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="0.6" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>
    <!-- Masque « screen » : la luminance de l'image sert d'opacité -> le noir devient transparent. -->
    <mask id="mlum" maskContentUnits="userSpaceOnUse"><use href="#moonimg"/></mask>
    <mask id="medge" maskContentUnits="userSpaceOnUse">
      <rect width="1200" height="300" fill="url(#gleft)"/>
    </mask>
    <mask id="moval" maskContentUnits="userSpaceOnUse">
      <rect width="1200" height="300" fill="url(#goval)"/>
    </mask>
    <mask id="mbot" maskContentUnits="userSpaceOnUse">
      <rect width="1200" height="300" fill="url(#gbot)"/>
    </mask>
    <clipPath id="frame"><rect width="1200" height="300" rx="16"/></clipPath>
    <path id="leaf" d="{LEAF}"/>
    <style>
      .fall {{ animation: fall linear infinite; }}
      .spin {{ animation: spin linear infinite; transform-box: fill-box; transform-origin: center; }}
      @keyframes fall {{ from {{ transform: translate(50px, -40px); }} to {{ transform: translate(-80px, 340px); }} }}
      @keyframes spin {{ from {{ rotate: 0deg; }} to {{ rotate: 360deg; }} }}
      @media (prefers-reduced-motion: reduce) {{ .fall, .spin {{ animation: none; }} .fall {{ display: none; }} }}
    </style>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="1200" height="300" fill="{BG}"/>
    <rect width="1200" height="300" fill="url(#neb1)"/>
    <rect width="1200" height="300" fill="url(#neb2)"/>
    <g fill="#eef0ff">{stars_svg}</g>

    <!-- vraie image de lune : fondue dans le fond (noir rendu transparent) + bords estompés.
         Masques imbriqués = intersection (luminance ∩ oval ∩ gauche ∩ bas). -->
    <g mask="url(#medge)"><g mask="url(#mbot)"><g mask="url(#moval)"><g mask="url(#mlum)">
      <use href="#moonimg" opacity="0.98"/>
    </g></g></g></g>

    <!-- feuilles qui tombent -->
    {fall_svg}

    <!-- texte -->
    <text x="72" y="128" font-family="{MONO}" font-size="64" font-weight="700" fill="{TXT}"><tspan fill="{ACCENT}">&gt; </tspan>{esc(HEADER["name"])}</text>
    <rect x="74" y="150" width="330" height="2" fill="url(#rule)"/>
    {mono(74, 186, 19, TXT2, HEADER["subtitle"])}
    {mono(74, 216, 15.5, MUTED, HEADER["tagline"])}
    <text x="74" y="256" font-family="{MONO}" font-size="13" fill="{FAINT}"><tspan fill="#a9c7ee" font-weight="700">❯</tspan> {esc(HEADER["motd"])}</text>
  </g>
</svg>
'''


# ---------------------------------------------------------------------
#  TITRES DE SECTION  (## Nom + filet dégradé)
# ---------------------------------------------------------------------
def build_heading(label: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 46" width="900" height="46" role="img" aria-label="{esc(label)}">
  <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{ACCENT}"/><stop offset="0.14" stop-color="{ACCENT}" stop-opacity="0.4"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0.06"/></linearGradient></defs>
  {mono(2, 27, 24, ACCENT, "##", weight=700)}
  {mono(44, 27, 24, TXT, label, weight=700)}
  <rect x="0" y="42" width="900" height="1.5" fill="url(#g)"/>
</svg>
'''


# ---------------------------------------------------------------------
#  FOCUS  (3 cartes)
# ---------------------------------------------------------------------
def build_focus() -> str:
    card_w, gap = 284.5, 22.5
    height = 252
    cards = []
    for i, (title, items) in enumerate(FOCUS):
        tx = i * (card_w + gap)
        parts = [f'<g transform="translate({tx:.0f} 0)">']
        parts.append(f'<rect x="0.75" y="0.75" width="{card_w}" height="{height - 1.5}" rx="12" fill="{CARD}" stroke="{BORDER}" stroke-width="1.5"/>')
        parts.append(f'<rect x="20" y="0.75" width="64" height="2.5" rx="1.25" fill="{ACCENT}"/>')
        parts.append(mono(20, 44, 12, ACCENT, f"{i + 1:02d}", spacing=1))
        parts.append(mono(20, 72, 18.5, TXT, title, weight=700))
        y = 103
        for it in items:
            parts.append(f'<path d="M22 {y} l4 -4 l4 4 l-4 4 z" fill="{ACCENT}" opacity="0.85"/>')
            parts.append(sans(40, y + 5, 14.5, TXT2, it))
            y += 26
        parts.append('</g>')
        cards.append("".join(parts))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" width="900" height="{height}" '
            f'role="img" aria-label="Focus: web exploitation, binary exploitation, red team">\n  '
            + "\n  ".join(cards) + "\n</svg>\n")


# ---------------------------------------------------------------------
#  TOOLBOX  (lignes catégorie -> badges)
# ---------------------------------------------------------------------
def build_toolbox() -> str:
    rows = TOOLBOX
    row_h = 42
    height = 18 + row_h * len(rows)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" width="900" height="{height}" role="img" aria-label="Toolbox">']
    out.append(f'<rect x="0.75" y="0.75" width="898.5" height="{height - 1.5}" rx="12" fill="{CARD}" stroke="{BORDER}" stroke-width="1.5"/>')
    for i, (label, tools) in enumerate(rows):
        base = 18 + i * row_h
        out.append(mono(22, base + 17, 12.5, MUTED, label))
        x = 200
        for t in tools:
            w = round(7.3 * len(t) + 30, 1)
            cx = x + w / 2
            out.append(f'<rect x="{x}" y="{base}" width="{w}" height="24" rx="6" fill="{CARD_IN}" stroke="{BORDER_IN}"/>')
            out.append(mono(round(cx, 1), base + 16.5, 12.5, TXT2, t, anchor="middle"))
            x += w + 8
        if i < len(rows) - 1:
            out.append(f'<rect x="20" y="{base + 33}" width="860" height="1" fill="{BORDER}"/>')
    out.append('</svg>\n')
    return "\n  ".join(out)


# ---------------------------------------------------------------------
#  WRITE-UP  (une barre par article)
# ---------------------------------------------------------------------
def build_writeup(wu: dict) -> str:
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 70" width="900" height="70" role="img" aria-label="{esc(wu["title"] + " — " + wu["subtitle"])}">']
    out.append(f'<rect x="0.75" y="3.75" width="898.5" height="62.5" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1.5"/>')
    out.append(f'<rect x="0.75" y="16" width="2.5" height="38" rx="1.25" fill="{ACCENT}"/>')
    out.append(mono(22, 31, 15.5, TXT, wu["title"], weight=700))
    out.append(sans(22, 52, 13, MUTED, wu["subtitle"]))
    # étiquettes, posées depuis la droite
    x_right = 882.0
    for tag in reversed(wu["tags"]):
        w = round(8.0 * len(tag) + 16, 1)
        x = round(x_right - w, 1)
        cx = round(x + w / 2, 1)
        out.append(f'<rect x="{x}" y="13" width="{w}" height="20" rx="4" fill="none" stroke="{TAG}" stroke-opacity="0.55"/>')
        out.append(mono(cx, 27, 10.5, TAG, tag, weight=600, anchor="middle", spacing=0.5))
        x_right = x - 9
    out.append(mono(882, 54, 11, FAINT, wu["date"], anchor="end"))
    out.append('</svg>\n')
    return "\n  ".join(out)


# ---------------------------------------------------------------------
#  FOOTER  (filet + quelques feuilles)
# ---------------------------------------------------------------------
def build_footer() -> str:
    leaves = [
        (140, 22, 30, 1.1, "#e2452b"), (330, 14, 200, 0.8, "#d2331f"),
        (610, 26, 120, 1.2, "#d2331f"), (880, 12, 300, 0.9, "#e2452b"),
        (1060, 24, 60, 1.1, "#c22a22"),
    ]
    uses = "".join(
        f'<use href="#leaf" transform="translate({x} {y}) rotate({r}) scale({s})" fill="{c}"/>'
        for x, y, r, s, c in leaves)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="1200" height="60" role="img" aria-label="">
  <defs>
    <linearGradient id="r" x1="0" x2="1"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset="0.5" stop-color="{ACCENT}" stop-opacity="0.7"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
    <path id="leaf" d="{LEAF}"/>
  </defs>
  <rect x="100" y="36" width="1000" height="1.5" fill="url(#r)"/>
  {uses}
</svg>
'''


def write(name: str, content: str):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {name}")


def main():
    print("Génération des SVG du profil…")
    write("header.svg", build_header())
    write("h-about.svg", build_heading("About"))
    write("h-focus.svg", build_heading("Focus"))
    write("h-writeups.svg", build_heading("Write-ups"))
    write("h-toolbox.svg", build_heading("Toolbox"))
    write("focus.svg", build_focus())
    write("toolbox.svg", build_toolbox())
    for wu in WRITEUPS:
        write(wu["file"], build_writeup(wu))
    write("footer.svg", build_footer())
    # nettoyage d'anciens fichiers qui ne sont plus référencés
    for old in ["wu-tf-cipher.svg"]:
        p = os.path.join(HERE, old)
        if os.path.exists(p):
            os.remove(p)
            print(f"  removed {old}")
    print("Terminé. Pense à régénérer après toute modif des DONNÉES.")


if __name__ == "__main__":
    main()
