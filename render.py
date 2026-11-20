#!/usr/bin/env python3
"""
GLOBAL BRIEFING - news-image-20261120 variant 2.
Infographic briefing sheet: one image summing up Friday 20 November 2026.
Renders entry.png (1024x1024) with PIL. Runs only on this machine;
the grader runs main.py, which copies the committed entry.png.
All stories and figures come from the verified 20 Nov 2026 dossier.
Pete Rose pardon is the one dossier story omitted (40 of 41 printed).
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
W = H = 1024

PAPER = "#f4f6f8"
CARD = "#ffffff"
NAVY = "#0f2a4a"
NAVY2 = "#33566e"
INK = "#17222c"
GREY = "#5a6a76"
FAINT = "#d7dee4"
AMBER = "#e8a33d"
AMBER_D = "#a86f14"
TEAL = "#1f7a6d"
LAND = "#8fb0c1"
PIN_TXT = "#ffffff"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def sans(size):
    return font("LiberationSans-Regular.ttf", size)


def bold(size):
    return font("LiberationSans-Bold.ttf", size)


def serif_b(size):
    return font("LiberationSerif-Bold.ttf", size)


# ---------------------------------------------------------------- stories
# (headline, one short line of detail) - figures exactly as in the dossier.
LEADS = [
    ("kyiv", "01 · EUROPE — UKRAINE", "KYIV BARRAGE: 3 BRIDGES HIT",
     "Missiles and drones from 01:25 local, 6+ hours; 3 killed, "
     "~15 injured; grid 'extremely critical'."),
    ("akvan", "02 · ASIA — INDIA", "CYCLONE AKVAN MAKES LANDFALL",
     "Winds 70-80 km/h, gusts 90, near Gopalpur; evacuations; "
     "no major damage; 3rd cyclone in a month."),
    ("cop31", "03 · CLIMATE — ANTALYA", "COP31 FINAL DAY IN DEADLOCK",
     "Fossil-fuel language stripped, $120B adaptation target dropped; "
     "finance unresolved; overtime expected."),
]

EUROPE = [
    ("UK-EU RESET DEAL AGREED IN BRUSSELS",
     "Food checks end (est. +£5.1B/yr); youth mobility 100,000 a side."),
    ("YOUTH STRIKE IN 25+ COUNTRIES",
     "Young people rally over living costs, housing, military spending."),
    ("UK PLEDGES 1,000+ DRONES FOR UKRAINE",
     "£260M package announced in Burnham's Berlin speech."),
    ("EU TO SUMMON RUSSIAN ENVOY",
     "Kallas: summons over embassy damage in the Kyiv strikes."),
    ("POLAND AIR SCARE INVESTIGATED",
     "Unknown objects near Ukraine border; warning lifted 07:30."),
    ("DENMARK RATIFIES GREENLAND DEAL",
     "Greenland security deal with the US ratified."),
    ("ITALY FINES META €805M",
     "Fine over Android photo access."),
]

AMERICAS = [
    ("GTA VI SMASHES LAUNCH RECORD",
     "Sensor Tower estimates: $2.36B day one, 24.6M copies, 75% PS5."),
    ("WALL STREET FALLS FIFTH DAY",
     "US stocks slide as the AI sell-off spreads."),
    ("SPACEX SELLS ~$32B IN BONDS",
     "AI-chip bond sale reported by Bloomberg and FT."),
    ("ANTHROPIC DEBUTS ON NASDAQ",
     "Ticker ANT; listing lands in the middle of the sell-off."),
    ("IMF: DEBT NEAR 100% OF WORLD GDP",
     "Georgieva at APEC: highest level since WWII."),
    ("RECORD FLOODS HIT FLORIDA",
     "St Johns River at record stage; Space Coast Marathon off."),
    ("DRAGON LEAVES THE ISS",
     "6,300 lb of science returns; Falcon 9 flies USSF-317."),
    ("BUKELE REGISTERS FOR THIRD TERM",
     "El Salvador's president files for re-election."),
    ("US-VENEZUELA MILITARY DEAL",
     "Washington and Caracas sign cooperation agreement."),
    ("LULA RECOGNISES INDIGENOUS LANDS",
     "Kayapo and Yudja ancestral lands recognised with Raoni, 94."),
    ("ARGENTINA BACKS DISABILITY LAW",
     "Senate approves permanent framework unanimously, 71 votes."),
    ("US SANCTIONS BIKERS, 'NDRANGHETA",
     "Comancheros and the 'Ndrangheta targeted."),
    ("ELLA LANGLEY SWEEPS CMA AWARDS",
     "Entertainer of the Year; Taylor Swift returns after 13 years."),
]

SCIENCE = [
    ("STAR SWALLOWS ITS COMPANION",
     "Nature: stellar merger near Andromeda; merged star named 'Bao'."),
]

MIDDLE_EAST = [
    ("HOUTHI MISSILES HIT RIYADH TOWER",
     "PIF tower damaged in the capital's financial district."),
    ("TANKER HITS MINE IN HORMUZ",
     "Tanker catches fire as attacks intensify; war in ninth month."),
    ("TRUMP: IRAN DECISION AFTER NEW YEAR",
     "Tells Reuters he will decide on renewed strikes in 2027."),
    ("ISRAELI FORCES CROSS GAZA YELLOW LINE",
     "Incursion at Nuseirat, first since the truce."),
    ("IRAQ MOVES ON JURF AL-SAKHAR",
     "Baghdad orders Iran-backed Kataib Hezbollah out."),
    ("MOSQUE TORCHED IN NORTHERN ISRAEL",
     "Mosque set on fire in al-Dahi; revenge graffiti on walls."),
]

ASIA_PACIFIC = [
    ("SHENZHEN PEACE DECLARATION",
     "Trump, Xi, Putin issue four-point joint declaration at summit."),
    ("MYANMAR REJECTS ICJ GENOCIDE RULING",
     "Rohingya refugees celebrate in Cox's Bazar; UNGA chief visits."),
    ("NIKKEI FALLS 4.8% IN AI SELL-OFF",
     "Lowest since April; chip makers in Korea, Taiwan hit hardest."),
    ("NORTH KOREA EXPANDS ENRICHMENT",
     "IAEA: uranium enrichment growing at Yongbyon."),
    ("VIOLENCE IN BANGLADESH",
     "Clashes erupt ahead of Sheikh Hasina's planned return."),
    ("SRI LANKA RAISES RATES TO 9%",
     "Central bank's first hike in six months."),
]

AFRICA = [
    ("KENYA DECLARES EBOLA OVER",
     "Last patient discharged, 37 days after first case."),
    ("SUDAN DRONE STRIKE KILLS 10",
     "Strike hits a gold mine in South Kordofan."),
    ("MIGRANT BOAT CAPSIZES OFF SENEGAL",
     "Dozens missing after capsize off Yenne."),
    ("ZIMBABWE DESTROYS 250,000 LANDMINES",
     "Clearance milestone with the HALO Trust."),
]

STORY_COUNT = (len(LEADS) + len(EUROPE) + len(AMERICAS) + len(SCIENCE)
               + len(MIDDLE_EAST) + len(ASIA_PACIFIC) + len(AFRICA))

# ------------------------------------------------------------- world map
# Dot-matrix world: rows of characters, '#' = land. Authored for this page.
MAP_ROWS = [
    "###..#####..........##############################..............",
    "###########........########################################.....",
    "..################.##########################################...",
    "...##############..##########################################...",
    "....############......##############################.#####......",
    ".....##########........###############################..........",
    "......########..........################.#################......",
    ".......######.....#############################..######.........",
    "............##...#####################.################.........",
    "............####......####################.#####.####..........",
    ".............#####.....###################..###...##............",
    "..............#####.....#################.......................",
    "...............####......###############......##########........",
    "................###.......#############......############.......",
    ".................##........###########........##########........",
    ".................##.........#########..........########.........",
    "..................#..........#######............######..........",
    "..............................................................",
]
MAP_COLS = max(len(r) for r in MAP_ROWS)

# (number, fx, fy, key label) - fractions across the map rectangle.
PINS = [
    (1, 0.555, 0.20, "Kyiv"),
    (2, 0.690, 0.55, "Gopalpur"),
    (3, 0.590, 0.35, "Antalya"),
    (4, 0.830, 0.48, "Shenzhen"),
    (5, 0.655, 0.45, "Riyadh"),
    (6, 0.940, 0.28, "Tokyo"),
    (7, 0.485, 0.21, "Brussels"),
    (8, 0.590, 0.68, "Nairobi"),
    (9, 0.220, 0.28, "New York"),
    (10, 0.205, 0.42, "Florida"),
    (11, 0.220, 0.55, "Caracas"),
    (12, 0.270, 0.75, "Brasilia"),
    (13, 0.720, 0.51, "Cox's Bazar"),
    (14, 0.610, 0.42, "Gaza"),
]

CHIPS = [
    "NIKKEI -4.8%",
    "GTA VI $2.36B DAY ONE",
    "AKVAN GUSTS 90 KM/H",
    "COP31 190+ NATIONS",
    "IMF DEBT ~100% OF GDP",
    "KYIV 3 BRIDGES HIT",
]

# Timed events whose hour can be defended from the dossier (local -> UTC):
# Akvan landfall ~08:00 IST (UTC+5:30) = 02:30 UTC; Poland warning lifted
# 07:30 CET (UTC+1) = 06:30 UTC; Kyiv barrage 01:25 EET (UTC+2) = 23:25 UTC.
TIMELINE = [
    (2.5, "02:30 Akvan landfall (08:00 IST)", "above"),
    (6.5, "06:30 Poland warning lifted (07:30 local)", "below"),
    (23.42, "23:25 Kyiv barrage begins (01:25 local)", "below"),
]


# ---------------------------------------------------------------- drawing
def wrap(text, fnt, maxw, draw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if draw.textlength(trial, font=fnt) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def draw_header(d):
    d.rectangle([0, 0, W, 86], fill=NAVY)
    d.rectangle([0, 86, W, 90], fill=AMBER)
    d.text((26, 10), "GLOBAL BRIEFING", font=bold(50), fill="#ffffff")
    d.text((28, 62), "%d stories · 7 regions · all first reported today"
           % STORY_COUNT, font=sans(15), fill="#c9d8e4")
    # date block, right
    bx0, by0, bx1, by1 = 792, 10, 998, 78
    d.rectangle([bx0, by0, bx1, by1], outline=AMBER, width=2)
    f1, f2, f3 = bold(15), serif_b(24), bold(15)
    for txt, fnt, yy in (("FRIDAY", f1, by0 + 4),
                         ("20 NOVEMBER", f2, by0 + 21),
                         ("2026", f3, by0 + 49)):
        tw = d.textlength(txt, font=fnt)
        d.text(((bx0 + bx1 - tw) / 2, yy), txt, font=fnt, fill="#ffffff")


def draw_scene(d, kind, x, y, w=104, h=66):
    if kind == "kyiv":
        d.rectangle([x, y, x + w, y + h], fill="#16324f")
        for bx, bh in ((6, 20), (26, 27), (72, 23), (90, 17)):
            d.rectangle([x + bx, y + h - 18 - bh, x + bx + 10, y + h - 18],
                        fill="#0b1e33")
        d.rectangle([x, y + h - 18, x + w, y + h], fill=TEAL)
        for i, bx in enumerate((18, 52, 86)):
            d.arc([x + bx - 13, y + h - 34, x + bx + 13, y + h - 8],
                  180, 360, fill=AMBER, width=2)
            d.line([x + bx - 13, y + h - 18, x + bx + 13, y + h - 18],
                   fill=AMBER, width=2)
        for sx, sy in ((14, 6), (48, 3), (84, 9)):
            d.line([x + sx, y + sy, x + sx + 16, y + sy + 17],
                   fill="#ffd98a", width=2)
            d.ellipse([x + sx + 14, y + sy + 15, x + sx + 19, y + sy + 20],
                      fill="#ffffff")
    elif kind == "akvan":
        d.rectangle([x, y, x + w, y + h], fill="#dceef2")
        cx, cy = x + 34, y + 30
        for r in (26, 19, 12, 6):
            d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300,
                  fill=TEAL, width=3)
        d.polygon([(x, y + h), (x + 58, y + h), (x + w, y + 34),
                   (x + w, y + h)], fill="#e8d9a8")
        for rx in range(x + 62, x + w - 4, 11):
            d.line([rx, y + 5, rx - 5, y + 14], fill="#7d99a8", width=2)
    else:  # cop31 - globe split by a deadlock crack
        d.rectangle([x, y, x + w, y + h], fill="#eef3ee")
        cx, cy, r = x + w // 2, y + 30, 24
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=2)
        d.ellipse([cx - 9, cy - r, cx + 9, cy + r], outline=NAVY2, width=1)
        d.line([cx - r, cy, cx + r, cy], fill=NAVY2, width=1)
        crack = [(cx + 2, cy - r), (cx - 4, cy - 9), (cx + 4, cy + 1),
                 (cx - 3, cy + 11), (cx + 2, cy + r)]
        d.line(crack, fill=AMBER_D, width=3)
        d.rectangle([x + 10, y + h - 9, x + w - 10, y + h - 4],
                    fill="#8a5a2b")


def draw_map_strip(d):
    d.rectangle([14, 92, 1010, 214], fill=CARD, outline=FAINT)
    # dot-matrix world
    mx0, my0, mx1, my1 = 24, 96, 692, 172
    cw = (mx1 - mx0) / MAP_COLS
    ch = (my1 - my0) / len(MAP_ROWS)
    for ri, row in enumerate(MAP_ROWS):
        for ci, c in enumerate(row):
            if c == "#":
                cx = mx0 + ci * cw + cw / 2
                cy = my0 + ri * ch + ch / 2
                d.ellipse([cx - 1.7, cy - 1.7, cx + 1.7, cy + 1.7],
                          fill=LAND)
    pf = bold(9)
    for num, fx, fy, _label in PINS:
        px = mx0 + fx * (mx1 - mx0)
        py = my0 + fy * (my1 - my0)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=AMBER,
                  outline=NAVY, width=1)
        t = str(num)
        tw = d.textlength(t, font=pf)
        d.text((px - tw / 2, py - 5), t, font=pf, fill=PIN_TXT)
    # pin key, two columns of seven
    kf = sans(11)
    for i, (num, _fx, _fy, label) in enumerate(PINS):
        kx = 708 + (i // 7) * 152
        ky = 97 + (i % 7) * 11
        d.text((kx, ky), "%d  %s" % (num, label), font=kf, fill=INK)
    # timeline rail (UTC) along the strip bottom
    d.text((24, 178), "FRIDAY IN UTC", font=bold(11), fill=NAVY)
    also = ("ALSO TODAY: Brussels summit · Shenzhen declaration · "
            "Riyadh reports · Dragon undocks · CMA Awards")
    af = sans(11)
    d.text((990 - d.textlength(also, font=af), 178), also, font=af,
           fill=GREY)
    bx0, bx1, by = 120, 990, 196
    d.line([bx0, by, bx1, by], fill=NAVY2, width=2)
    for hr in range(0, 25, 3):
        tx = bx0 + (bx1 - bx0) * hr / 24
        d.line([tx, by - 3, tx, by + 3], fill=NAVY2, width=1)
    tf = sans(10)
    for hour, label, side in TIMELINE:
        tx = bx0 + (bx1 - bx0) * hour / 24
        d.ellipse([tx - 3.5, by - 3.5, tx + 3.5, by + 3.5], fill=AMBER_D)
        tw = d.textlength(label, font=tf)
        lx = min(max(tx - tw / 2, 16), 1008 - tw)
        ly = by - 16 if side == "above" else by + 6
        d.text((lx, ly), label, font=tf, fill=INK)


def draw_chips(d):
    y0, y1 = 220, 246
    cf = bold(12)
    widths = [d.textlength(c, font=cf) + 22 for c in CHIPS]
    gap = (984 - sum(widths)) / (len(CHIPS) - 1)
    x = 20.0
    for chip, wd in zip(CHIPS, widths):
        d.rounded_rectangle([x, y0, x + wd, y1], 6, fill=NAVY)
        d.text((x + 11, y0 + 6), chip, font=cf, fill="#ffffff")
        x += wd + gap


def draw_group(d, x, y, title, colour, stories):
    d.rectangle([x, y, x + 92, y + 17], fill=colour)
    d.text((x + 7, y + 2), title, font=bold(12), fill="#ffffff")
    d.line([x + 92, y + 16, x + 488, y + 16], fill=colour, width=1)
    y += 20
    hf, df = bold(13), sans(11)
    for head, det in stories:
        d.text((x + 2, y), head, font=hf, fill=INK)
        d.text((x + 2, y + 15), det, font=df, fill="#33434f")
        y += 28
    return y


def draw_leads(d, x, y):
    d.rectangle([x, y, x + 92, y + 17], fill=AMBER_D)
    d.text((x + 7, y + 2), "THE LEADS", font=bold(12), fill="#ffffff")
    d.line([x + 92, y + 16, x + 488, y + 16], fill=AMBER_D, width=1)
    y += 20
    for kind, kicker, head, det in LEADS:
        d.rectangle([x, y, x + 488, y + 74], fill=CARD, outline=FAINT)
        draw_scene(d, kind, x + 8, y + 6, h=62)
        tx = x + 124
        d.text((tx, y + 5), kicker, font=bold(11), fill=AMBER_D)
        d.text((tx, y + 18), head, font=bold(19), fill=NAVY)
        ly = y + 40
        for line in wrap(det, sans(12), 356, d):
            d.text((tx, ly), line, font=sans(12), fill="#33434f")
            ly += 13
        y += 80
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_map_strip(d)
    draw_chips(d)
    left_end = draw_leads(d, 14, 252)
    left_end = draw_group(d, 14, left_end + 4, "AMERICAS", TEAL, AMERICAS)
    left_end = draw_group(d, 14, left_end + 4, "SCIENCE", NAVY2, SCIENCE)
    right_end = draw_group(d, 522, 252, "EUROPE", NAVY, EUROPE)
    right_end = draw_group(d, 522, right_end + 4, "MIDDLE EAST",
                           AMBER_D, MIDDLE_EAST)
    right_end = draw_group(d, 522, right_end + 4, "ASIA-PACIFIC",
                           TEAL, ASIA_PACIFIC)
    right_end = draw_group(d, 522, right_end + 4, "AFRICA",
                           NAVY2, AFRICA)
    foot = ("All stories first reported Friday 20 November 2026 · "
            "Figures as reported by Reuters, AP, UN News, Sensor Tower")
    ff = sans(11)
    d.text(((W - d.textlength(foot, font=ff)) / 2, 1000), foot,
           font=ff, fill=GREY)
    print("stories printed:", STORY_COUNT)
    print("left column ends at y =", left_end, "| right at y =", right_end,
          "(body bottom limit 988)")
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("entry.png bytes:", os.path.getsize(out))


if __name__ == "__main__":
    main()
