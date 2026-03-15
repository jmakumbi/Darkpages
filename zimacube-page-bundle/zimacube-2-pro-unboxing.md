# Page Build — ZimaCube 2 Pro Unboxing & First Impressions

## Page Brief

**Page type:** lab-log
**Slug:** zimacube-2-pro-unboxing
**Title:** ZimaCube 2 Pro — Unboxing & First Impressions
**Purpose:** Document the arrival, unboxing experience, and physical first impressions of the
ZimaCube 2 Pro personal cloud NAS, received for review from IceWhale Technology.
**Audience:** Prospective ZimaCube buyers; homelab enthusiasts; technically-minded readers
who received this URL directly.
**Tone:** Brutally honest with whimsical asides. First person. Written, not generated.
Light barbs welcome. Allegorical humour encouraged. Think: a seasoned IT consultant who
has seen everything, is mildly suspicious of anything that calls itself a "personal cloud",
but is genuinely charmed when the thing deserves it. Real praise reads like reluctant concession.
Criticism is specific and constructive, never mean-spirited.

---

## Disclosure Notice

Display as a styled banner immediately before the article body (not a modal, not a popup):

> I received this device for review and testing from IceWhale Technology.
> They have not read this post and have no influence on its content.

---

## Content Notes

### Narrative Voice Notes

The author's humour runs to light barbs and allegory. Work in jokes naturally — don't label
them as jokes. A few tonal examples to calibrate:

- On DHL reliability in Uganda: something to the effect that in a country where the phrase
  "the package is with the courier" can mean anything from "it's ten minutes away" to
  "it exists, somewhere", DHL is the exception that proves the rule.
- On the Phillips screwdriver inclusion: gently comic observation about receiving a
  Phillips screwdriver with a device aimed at homelab builders — the technological equivalent
  of a hotel putting a single teabag in the room and calling it "hospitality".
- On the sharp corners: the ZimaCube has angles that suggest it was designed by someone
  who has never stubbed a toe or moved house.
- On the weight: something referential — perhaps to Ugandan import duty being charged by
  the kilogram, or the feeling of lifting it like lifting a small relative who has had
  one too many.
- On the packaging design: treat the orange-and-black retail box the way you would a
  well-dressed person arriving at a chaotic office — it creates expectations the product
  then has to work hard to meet.

Do NOT force all jokes into every section. Let them appear naturally. Two or three well-placed
lines across the whole piece are better than a relentless stream of wit.

---

### Section 1 — What is the ZimaCube 2?

Write a factual but voice-driven introduction covering:

- [IceWhale Technology](https://zimaspace.com) (link the text "IceWhale Technology" to
  `https://zimaspace.com`) — a Shenzhen-based hardware company best known for making
  personal cloud and homelab devices. Previously produced the ZimaBoard (a single-board
  server) and ZimaBlade (its smaller sibling) before shipping the original ZimaCube via
  crowdfunding.
- The [original ZimaCube](https://www.zimaspace.com/products/cube-personal-cloud) (link
  to `https://www.zimaspace.com/products/cube-personal-cloud`) was a 6-bay personal NAS
  that launched on Kickstarter. It was well-received but the Intel N100 CPU proved to be
  a bottleneck for the feature set — only 9 PCIe lanes for 6 drives, 4 M.2 slots, dual
  NIC and multiple USB. The follow-on was inevitable.
- The ZimaCube 2 comes in three variants. All share the same chassis (240 × 221 × 220 mm)
  and power supply (19V 13A, 247W rated):
  - **ZimaCube 2** (standard): Intel Core i3-N215U (6 cores, up to 4.40 GHz), 8GB DDR5,
    256GB onboard NVMe, 2× 2.5GbE, Silver
  - **ZimaCube 2 Pro**: Intel Core i5-1235U (10 cores, up to 4.40 GHz), 16GB DDR5 4800
    MT/s (2×8GB, upgradeable to 64GB), 256GB onboard NVMe, 10GbE + 2× 2.5GbE, Black
  - **ZimaCube 2 Creator Pack**: Same i5-1235U, but 64GB DDR5 (2×32GB), 1TB onboard NVMe,
    adds NVIDIA RTX PRO 2000 GPU, Black

  All three variants share: 6× SATA3 bays (3.5" & 2.5" HDD), the "7th Bay" with 4×
  M.2 NVMe slots (3200 MB/s R/W on Pro), Thunderbolt 4 (2× rear USB-C), DP 1.4, HDMI
  2.0, 3.5mm audio, 4× USB-A 3.0, 1× USB-C 3.0, PCIe expansion (x16 + x8 slots),
  13× RGB LEDs, and ZimaOS pre-installed.

- The author received the **ZimaCube 2 Pro** for review.
- Do NOT invent any specs not listed above or in the attached specification screenshot.
  All figures come from the official ZimaCube 2 spec sheet (attached as image).

---

### Section 2 — Arrival: A Box, a Sofa, and Five Days

**Use the image `box_arrived_couch.jpg` in this section.**

- The outer shipping container is a brown corrugated cardboard box printed directly with
  "ZimaCube Personal cloud\_" in clean sans-serif — no branding tape, no stickers, the
  brand is just... printed on the box. This is a flex.
- Shipped from China to Kampala, Uganda via DHL. Transit time: approximately 5 days.
- Shipped weight: approximately 5.5 kg (we will discuss why shortly).
- Add a short aside on DHL in Uganda — reliable, no hidden charges on arrival, no mystery
  disappearances. The author's preferred courier. Use the recommended voice note above
  about Ugandan courier roulette.
- The box arrived at the DHL office with what appeared to be a dedicated attendant —
  which, in context, makes sense.

**Use the image `dhl_arrival_redacted.jpg` in this section.**
Caption: *"Collected from the DHL office. The box is fine. The suspense was not."*

---

### Section 3 — What's in the Box

Two distinct inner boxes inside the outer shipping carton, plus a loose accessories layer.

**Inner box 1 — The "ZimaCube Parts\_" box:**
- A small, flat black box labelled "ZimaCube Parts\_" in the same typeface as the
  outer carton. Sits in a custom die-cut dense foam insert.
- Contains: a very large external AC adapter (KPTEC branded, UL/CE/GS/UK CA certified),
  multiple zip-lock bags of assorted replacement screws and fasteners, and a power cord.
- The PSU is the reason the package weighs 5.5 kg. It is a large, slab-like brick —
  the kind that makes you briefly question whether you ordered hardware or portable
  heating equipment. 19V 13A, 247W rated. No complaints — it's properly specced for
  six spinning drives and a Core i5.

**Loose accessories layer:**
- 1× CAT6 UTP Patch Cord, 1M, Black (Model WV-E651)
- 1× IceWhale custom screwdriver — a proprietary magnetic-head driver with an IW-stamped
  grip. Thoughtful inclusion; this is the tool you actually need for drive installation.
- 1× Standard Phillips head screwdriver — included, apparently, in case you have never
  encountered a screw before. Any tech-savvy user has three of these already. The
  Phillips screwdriver is the technological equivalent of a hotel putting a single
  teabag in the room and calling it "hospitality". It should be a free add-on option on
  the product page, not a standard inclusion — it adds weight, cost, and mild existential
  confusion to the unboxing experience.
- 4× M.2 NVMe heat sinks with pre-applied thermal pads. These are for drives installed
  in the 7th Bay — a thoughtful inclusion given how compressed the thermal environment
  will be with four M.2 cards stacked in that module.

**Inner box 2 — The main event:**
- The ZimaCube 2 Pro retail box. Black exterior, single orange accent band at the
  equator, "ZimaCube Personal cloud\_" in white. No foam insert inside the retail box
  itself — the device sits directly in the shell, wrapped in protective plastic. The
  design aesthetic lands somewhere between a corporate gift and a director's cut Blu-ray.
  It creates expectations. The product then has to meet them.
- On the packaging design philosophy: IceWhale appears to have studied the Dieter Rams
  school of "less but better" for this. It works. A NAS device this large has no business
  arriving this tastefully.

---

### Section 4 — Physical First Impressions

**Use images: `front_panel.jpg`, `rear_panel.jpg`, `side_vent.jpg`, `unit_unwrapped.jpg`**
(mapped to filenames from the image sequence table at the end of this document)

**Chassis:**
- Four sides of matte black aluminium plate. No branding on the sides. No ventilation.
  No fingerprint magnet effect. The aluminium is the mass you feel when you pick it up.
- Dimensions: 240 × 221 × 220 mm — roughly the size of a shoebox for someone with
  unusually square feet.
- Front and rear panels are black plastic mesh grilles. The front covers the 6 drive
  bays; the rear covers the two 80mm fans. Both grilles are noticeably thinner and
  flexier than the aluminium panels they're flanked by. This is a minor but real
  criticism: the flat panel format gives nothing structural to grip when lifting, and
  an uninitiated user's natural handhold is exactly where the grille lives. A dropped
  grille won't destroy the device, but it will feel bad.
- The machined edges and corners are sharp. Not "slightly uncomfortable" sharp —
  genuinely sharp. This device was designed by someone who has never moved house.
  Wrap your forearms accordingly.
- At this weight and corner geometry, dropping it on a foot crosses from accident into
  incident report territory.

**Cooling design note (observation, no testing yet):**
- Two 80mm fans at the rear eject hot air from the drive bay section. The side panels
  feature two bands of circular perforations — top and bottom — for passive supplemental
  airflow. The upper section (CPU and PCIe) and lower section (drives) are thermally
  separated inside — a good design decision that means drive heat doesn't cook the
  motherboard and vice versa.
- 13 RGB LEDs are included. Their purpose is presumably to let you know the device is
  alive in a dark room, or to satisfy the demographic who believes blinking lights
  improve throughput.

**Front panel I/O (left to right):**
- 2× USB-A 3.0
- 1× USB-C 3.0
- 1× 3.5mm audio jack
- 1× Power button

**Rear panel I/O:**
- 1× DC barrel jack (power input)
- 2× Thunderbolt 4 / USB-C (rear)
- 1× 10GbE RJ45 (Marvell AQC113)
- 2× 2.5GbE RJ45 (Intel i226)
- 2× USB-A
- 1× HDMI 2.0
- 1× DisplayPort 1.4

**PCIe expansion:**
- Two slots accessible via the top panel: 1× PCIe x16 (Gen 4.0, 8GB/s) and 1× PCIe x8
  (Gen 3.0, 2GB/s). Supports SFF GPU cards, AI cards, U.2, additional SSD expansion.
  The i5-1235U brings 20 PCIe lanes to the table, which is exactly why the Pro version
  exists — the standard ZimaCube 2's i3-N215U shares the N100's lane constraints.

---

### Spec Table

Render as a styled table with the brand's alternating row colours. Use these exact values
from the official spec sheet — do not invent or approximate any figures:

| Specification | ZimaCube 2 Pro |
|---|---|
| Pre-installed OS | ZimaOS Plus |
| Compatible OS | CasaOS, Linux, OMV, Unraid, Home Assistant OS, TrueNAS, OpenWrt, pfSense, LibreELEC, Windows, Android |
| Processor | Intel® Core™ i5-1235U — 10 cores up to 4.40 GHz |
| GPU | — |
| Memory (default) | 16GB DDR5 4800 MT/s (2× 8GB) |
| Max Memory | 64GB SODIMM DDR5 (2× 32GB) |
| System Storage | 256GB NVMe SSD (onboard) |
| PCIe Expansion | Gen4.0 8GB/s × 1 (PCIe x16) + Gen3.0 2GB/s × 1 (PCIe x8) |
| 7th Bay | 4× M.2, 3200 MB/s R/W |
| M.2 Slots | 1× M.2 onboard (OS), 4× M.2 on 7th Bay |
| Drive Bays | 6× SATA3, supports 3.5" & 2.5" HDD/SSD |
| Network | 2× Intel i226 2.5GbE + 1× Marvell AQC113 10GbE |
| Thunderbolt 4 | 2× Rear USB-C (Mac or PC direct connection) |
| USB | 4× USB-A 3.0, 1× USB-C 3.0 |
| Display | DP 1.4 × 1, HDMI 2.0 × 1 |
| Audio | 3.5mm audio jack × 1 |
| RGB | 13 RGB LEDs |
| Colour | Black |
| Dimensions (W×D×H) | 240 × 221 × 220 mm |
| Power | 19V 13A, 247W |

---

### Section 5 — First Impressions Summary

3–5 short paragraphs:

1. The packaging and presentation set a high bar. The device largely meets it physically.
   For a piece of homelab equipment that could have shipped in a plain brown box with
   a warranty card, IceWhale have done something that most enterprise NAS vendors have
   never bothered with: they made the object feel worth owning before you've turned it on.

2. The hardware spec is genuinely capable. An i5-1235U with 10GbE, Thunderbolt 4, and a
   PCIe x16 slot in a 240mm cube is not something you can easily replicate with off-the-shelf
   components in this form factor. The compromises (sharp corners, flexible grilles,
   a Phillips screwdriver nobody needed) are real but minor.

3. One honest note on the RAM: the ZC2 Pro ships with 16GB DDR5 as standard, which is
   adequate but not generous given the ambition of the platform. With six drives, a
   10GbE NIC, and a PCIe card potentially in play, the upgrade path to 64GB is real and
   worth budgeting for from day one.

4. What comes next: drive installation, ZimaOS initial setup, and some baseline
   performance numbers. This is an unboxing post — the device hasn't been turned on yet.
   Conclusions will have to wait. The box was very nice, though.

---

## Image Sequence & File Map

Place all image files in `content/pages/zimacube-2-pro-unboxing/` (the leaf bundle folder).
All images are included in the zip alongside this prompt file.

Process all images using Hugo's built-in image pipeline:
- Resize to max 1400px wide
- Convert to WebP, quality 82
- JPEG fallback, quality 76
- `loading="lazy"` on all `<img>` tags
- Explicit `width` and `height` from processed image dimensions (prevents CLS)

| Reference name in prompt | Filename in bundle | Caption |
|---|---|---|
| retail_box | `20260313_210418.jpg` | The retail box. Black cube, orange band. IceWhale knows what they're doing here. |
| parts_box | `20260313_205521.jpg` | The "ZimaCube Parts\_" inner box seated in die-cut foam |
| accessories_layer | `20260313_205620.jpg` | The accessories layer — bags of hardware, the power cord, and optimism |
| psu_closeup | `20260313_205714.jpg` | The KPTEC power supply. 19V 13A. This is why the box weighed 5.5 kg. |
| accessories_spread | `20260313_210138.jpg` | Full spread: CAT6, IW custom screwdriver, standard Phillips (sigh), 4× NVMe heat sinks |
| unit_unwrapped | `20260313_210504.jpg` | The main unit in factory wrap, seated on the retail box |
| unit_foam_sandwich | `20260313_210257.jpg` | Side panel sandwiched in dense grey foam. CE / RoHS certified. |
| front_panel | `20260313_210641.jpg` | Front panel: USB-A ×2, USB-C, 3.5mm audio, power button |
| rear_panel | `20260313_210657.jpg` | Rear panel: 10GbE, 2×2.5GbE, Thunderbolt 4 ×2, HDMI, DisplayPort, USB-A ×2 |
| side_vent | `20260313_211053.jpg` | Side panel ventilation — two bands of circular perforations, top and bottom |
| box_arrived_couch | `box_arrived_couch.jpg` | It arrived. On the sofa. As things do. |
| dhl_arrival | `dhl_arrival_redacted.jpg` | Collected from the DHL office. The box is fine. The suspense was not. |

---

## Layout Requirements

**Layout name:** `lab-log`
**File to create/update:** `layouts/pages/lab-log.html`

### Responsive Design Requirements
- **Mobile-first** — all layout decisions start at 375px and scale up
- Single breakpoint at 768px for two-column gallery grid
- Navigation-free, footer-free (this is the dark pages vault)
- No JavaScript — use CSS `:target` for lightbox

### Header Band
- Full-width dark brown background (`var(--color-bg-dark)`)
- Series tag in monospace amber at top: `SERIES: zimacube-2-pro`
- Title in Playfair Display, cream, large (clamp 1.8rem to 2.8rem)
- Subtitle in monospace, small, amber, 60% opacity: `IceWhale Technology · Review Unit`
- On mobile: reduce padding, title drops to 1.6rem minimum

### Disclosure Banner
- Directly below header, full content width
- Left border: 3px solid `var(--color-accent)`
- Background: slightly darker than page bg (use rgba overlay on `--color-bg-dark`)
- Text: small, italic, cream-on-dark, 90% opacity
- Not dismissable — it stays.

### Body
- Max width: 760px, centered with auto margins
- Horizontal padding: 1.5rem on mobile, 2rem on desktop
- Section headings (`h2`): Playfair Display, `--color-bg-dark`, preceded by a 28px wide
  amber rule (`display: block; width: 28px; height: 2px; background: var(--color-accent)`)
- Body text: Source Sans 3, 1.1rem, line-height 1.7
- Links: `var(--color-accent)`, no underline by default, underline on hover

### Image Gallery Grid
- 2-column CSS Grid on desktop (768px+), 1-column on mobile
- `gap: 1rem`
- Each item: card container with `background: var(--color-card)`, 1px border
  `rgba(69,15,0,0.15)`, `border-radius: 4px`
- Image: full width of container, `aspect-ratio: 4/3`, `object-fit: cover`
- Caption: `padding: 0.5rem 0.75rem`, `font-size: 0.8rem`, `font-style: italic`,
  `color: var(--color-text)`, `opacity: 0.7`
- Lightbox: clicking the image opens a full-screen overlay via CSS `:target`.
  The overlay should darken the page and show the full image centred.
  Include `<a href="#">` close link at top right.

### Spec Table
- Full width within reading column
- `border-collapse: collapse`
- Header row: `background: var(--color-bg-dark)`, cream text, small caps, 0.85rem
- Odd rows: `background: var(--color-bg)`
- Even rows: `background: var(--color-card)`
- Cell padding: `0.5rem 0.85rem`
- First column: bold, 38% width, `color: var(--color-bg-dark)`
- On mobile: reduce font to 0.8rem, allow horizontal scroll on table wrapper

### Meta Footer
- Sticky to bottom of content (not viewport)
- Background: `var(--color-card)`, top border `2px solid rgba(69,15,0,0.15)`
- Date: monospace, small, muted
- Tags: monospace, amber — `homelab · zimacube · icewhale · nas`

---

## Brand Tokens

All CSS variables are already defined globally in `assets/css/brand.css`.
Use only these — do not hardcode any colours in the layout file:

```
--color-bg:       #d6cdb8   Warm Cream — page background
--color-bg-dark:  #450f00   Deep Brown — dark surfaces, headers
--color-accent:   #c47a22   Muted Amber — links, rules, accents
--color-text:     #1a0800   Near-black warm — body copy
--color-text-inv: #d6cdb8   Cream — text on dark backgrounds
--color-card:     #e8e2d4   Slightly off-white — card backgrounds, alt table rows

--font-heading: 'Playfair Display', Georgia, serif
--font-body:    'Source Sans 3', system-ui, sans-serif
--font-mono:    'JetBrains Mono', 'Courier New', monospace
```

---

## Files to Create

### 1. `content/pages/zimacube-2-pro-unboxing/index.md`

Frontmatter:
```yaml
---
title: "ZimaCube 2 Pro — Unboxing & First Impressions"
date: 2026-03-13
draft: false
layout: "lab-log"
description: "Unboxing and first physical impressions of the ZimaCube 2 Pro personal cloud
  NAS, received for review and shipped to Kampala, Uganda from IceWhale Technology."
slug: "zimacube-2-pro-unboxing"
noindex: true
subtitle: "IceWhale Technology · Review Unit"
series: "zimacube-2-pro"
toc: false
---
```

Write full page content in Markdown. Use the `labimg` shortcode for all images.
Use the `gallery` shortcode to group images into the 2-column grid.
The disclosure notice is the first element in the body, before any headings.
All links to IceWhale and the original ZimaCube must be present and correctly targetted.

### 2. `layouts/pages/lab-log.html`

Full layout per the specifications above. Must:
- Use `{{ define "main" }}` to extend baseof
- Include Hugo image processing for all page resources
- Implement CSS-only lightbox using `:target`
- Be fully responsive (mobile-first)
- Reference only CSS variables for all colours
- Have zero JavaScript

### 3. `layouts/shortcodes/labimg.html`

Usage: `{{< labimg src="filename.jpg" caption="Caption text" id="img01" >}}`

- Look up image as page resource via `.Page.Resources.GetMatch`
- Generate WebP (1400px, q82) and JPEG fallback (1400px, q76)
- Render as `<figure>` with `<picture>`, `<figcaption>`, and lightbox anchor/target
- Lightbox: wrap image in `<a href="#id">`, render `<div id="id" class="lightbox">` with
  the full-size processed image and `<a href="#" class="lb-close">✕</a>`

### 4. `layouts/shortcodes/gallery.html`

Usage:
```
{{< gallery >}}
{{< labimg src="img1.jpg" caption="Caption" id="g01" >}}
{{< labimg src="img2.jpg" caption="Caption" id="g02" >}}
{{< /gallery >}}
```

Renders a `<div class="gallery-grid">` wrapper. CSS grid is defined in the lab-log layout.

---

## Project Context

This page is part of the `billableonline.co` dark pages vault.
The scaffold is already built. You are adding ONE new page to it.

Key reminders:
- The scaffold uses `hugo-profile` as a theme but all layouts are overridden
- `layouts/_default/baseof.html` exists from the scaffold — extend it
- Brand CSS variables are already globally available via `assets/css/brand.css`
- Google Fonts (Playfair Display, Source Sans 3, JetBrains Mono) are already loaded in
  `layouts/partials/head.html`
- All pages have `noindex, nofollow` injected globally — the `noindex: true` frontmatter
  param is belt-and-suspenders

---

## After Build — User Instructions

Tell the user at the end of the Claude Code session:

1. Copy all image files from the zip into:
   `content/pages/zimacube-2-pro-unboxing/`
   (Filenames must match exactly as listed in the image table above)

2. Run locally to verify:
   ```bash
   hugo server
   # Visit: http://localhost:1313/zimacube-2-pro-unboxing/
   ```

3. Check:
   - [ ] Images render in 2-column grid on desktop, single column on mobile
   - [ ] Click on any image opens lightbox overlay
   - [ ] Lightbox closes on clicking ✕ or navigating away
   - [ ] Spec table renders with alternating row shading
   - [ ] Disclosure banner appears above first heading
   - [ ] All links (IceWhale, original ZimaCube) are live
   - [ ] `hugo --minify` produces zero errors

4. Deploy:
   ```bash
   git add .
   git commit -m "Add lab-log: ZimaCube 2 Pro unboxing"
   git push origin main
   # GitHub Actions deploys in ~60 seconds
   ```

5. Page will be live at:
   `https://billableonline.co/zimacube-2-pro-unboxing/`
