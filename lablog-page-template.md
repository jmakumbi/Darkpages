# Lab-Log Page Build — billableonline.co Dark Pages Vault

---

## How to Use This Prompt

This is a reusable template. Before running it in Claude Code, fill in every section
marked with `[ ]`. Everything else is pre-configured project context — do not change
it unless the scaffold itself has changed.

Sections you fill in:
- `## Page Brief` — slug, title, purpose, audience, tone notes
- `## Author's Impressions` — your raw notes, observations, opinions
- `## Image Manifest` — filenames, captions, which section each image belongs to
- `## Specific Layout Requests` — any one-off layout decisions for this page

Everything else is standard. Claude Code handles the rest.

---

## Page Brief

**Page type:** lab-log
**Slug:** `[ your-url-slug ]`
**Title:** `[ Full Page Title ]`
**Series slug (if part of a series):** `[ series-name | leave blank if standalone ]`
**Subtitle (shown under title in header band):** `[ e.g. "Manufacturer Name · Review Unit" ]`
**Purpose:** `[ One sentence — what does this page document? ]`
**Audience:** `[ Who gets this URL? e.g. "Prospective buyers, homelab enthusiasts" ]`
**Date:** `[ YYYY-MM-DD ]`
**Tags (internal only, never rendered as links):** `[ tag1, tag2, tag3 ]`

**Tone:**
`[ Describe the voice. Example: "Brutally honest with dry wit. First person. Written,
not generated. Specific technical observations paired with light allegorical humour." ]`

---

## Author's Impressions

`[ Paste your raw notes here. Bullet points, fragments, half-formed thoughts — all fine.
Claude Code will expand these into full prose matching the tone above. Be as detailed or
as brief as you like. The more specific your observations, the more accurate the result.

Do NOT worry about structure or completeness here. Just write what you noticed,
what you liked, what annoyed you, what surprised you. Claude Code will organise it. ]`

---

## Image Manifest

List every image file for this page. All images must be placed in the leaf bundle folder
(`content/pages/[slug]/`) before building.

For each image, provide:
- `filename` — exact filename as it will appear in the bundle folder
- `id` — a short unique string for the lightbox anchor (no spaces, no special chars)
- `caption` — the caption shown below the image
- `section` — which section of the article this image appears in
- `processing` — optional override; defaults to `resize 1400px webp q82 / jpeg q76`

```
[ EXAMPLE — replace with your actual images:

filename: 20260313_210418.jpg
id: retail-box
caption: The retail packaging. Black cube, orange band.
section: Packaging & Unboxing
processing: default

filename: dhl_arrival_redacted.jpg
id: dhl-arrival
caption: Collected from the DHL office. The box is fine. The suspense was not.
section: Arrival & Shipping
processing: default

]
```

**Gallery groupings** — list which image IDs should appear side by side in a 2-column
grid. Images not listed here will render full-width inline.

```
[ EXAMPLE:

Gallery 1 (Packaging): retail-box, parts-box
Gallery 2 (Accessories): accessories-spread, psu-closeup
Gallery 3 (Unit): front-panel, rear-panel

]
```

---

## Specific Layout Requests

`[ List any one-off layout decisions for this page only. Examples:
- "The teardown section should use a single-column full-width image layout"
- "Add a warning callout box before the disassembly section"
- "The spec table should appear after Section 2, not at the end"
- Leave blank if you have no special requests — the standard lab-log layout will be used.
]`

---

---
---

## ↓ DO NOT EDIT BELOW THIS LINE — PROJECT CONTEXT ↓

---
---

## Project: billableonline.co Dark Pages Vault

This page is part of the `billableonline.co` dark pages vault — a Hugo static site
hosted on GitHub Pages. The scaffold is already built and deployed. You are adding
ONE new lab-log page. You do not touch any other existing file unless a layout file
for this page type does not yet exist, in which case you create it.

### Site Architecture Summary

- **Generator:** Hugo (extended, latest version)
- **Theme:** `hugo-profile` — loaded as a git submodule but all homepage, nav, and
  layout templates are overridden by files in `layouts/`
- **Host:** GitHub Pages, branch `gh-pages`, auto-deployed via GitHub Actions
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → GitHub Actions builds → deploys to `gh-pages` in ~60s
- **Philosophy:** No navigation. No sitemap. No RSS. No discoverability. Pages are
  shared by URL only. If you don't have the link, you don't find the page.

### Content Structure

Pages are Hugo **leaf bundles**:

```
content/pages/[slug]/
├── index.md        ← page content + frontmatter
├── image1.jpg      ← all images live here as page resources
├── image2.jpg
└── ...
```

This means Hugo's image processing pipeline can access images as `.Resources.GetMatch`
calls inside layouts and shortcodes. Do NOT reference images from `static/` for pages
that use image processing — only from the leaf bundle.

### Brand Tokens

These CSS variables are already defined globally in `assets/css/brand.css`.
Use ONLY these in all layout files — never hardcode colours.

```css
--color-bg:       #d6cdb8;   /* Warm Cream — page background */
--color-bg-dark:  #450f00;   /* Deep Brown — dark surfaces, header bands */
--color-accent:   #c47a22;   /* Muted Amber — links, rules, CTAs, accents */
--color-text:     #1a0800;   /* Near-black warm — body copy */
--color-text-inv: #d6cdb8;   /* Cream — text on dark backgrounds */
--color-card:     #e8e2d4;   /* Off-white — card backgrounds, alt table rows */

--font-heading: 'Playfair Display', Georgia, serif;
--font-body:    'Source Sans 3', system-ui, sans-serif;
--font-mono:    'JetBrains Mono', 'Courier New', monospace;

--max-width:      760px;
--max-width-wide: 1100px;
```

### Typography Already Loaded

Google Fonts are loaded globally in `layouts/partials/head.html`:
- Playfair Display (700)
- Source Sans 3 (400, 600)
- JetBrains Mono (400)

Do not re-add `<link>` tags for fonts inside the layout file.

### Global Behaviours Already in Place

- `noindex, nofollow` is injected on every page via `layouts/partials/head.html`
- `robots.txt` has `Disallow: /` — no crawlers, ever
- No analytics, no tracking scripts, no third-party embeds
- The navbar and footer from `hugo-profile` are suppressed via CSS in `brand.css`

---

## What to Build

### 1. `content/pages/[slug]/index.md`

Use this exact frontmatter block (substitute values from the Page Brief above):

```yaml
---
title: "[Title]"
date: [YYYY-MM-DD]
draft: false
layout: "lab-log"
description: "[One sentence for Open Graph / sharing.]"
slug: "[slug]"
noindex: true
subtitle: "[Subtitle]"
series: "[series-slug or omit if blank]"
toc: false
---
```

Write the full article body in Markdown, expanding the Author's Impressions into
well-structured prose. Voice and tone must match what's specified in the Page Brief.

Rules for the content:
- First-person throughout
- Disclosure notice (if a review unit) is the first element before any headings
- Do not invent specifications — use only what's in the Author's Impressions or
  what you can verify from official manufacturer documentation
- If manufacturer URLs are mentioned, link them; use descriptive anchor text
- All images are inserted via the `labimg` shortcode (see below)
- Images grouped into galleries via the `gallery` shortcode (see below)
- Spec data (if any) renders as a spec table using standard Markdown table syntax
  (the layout handles the styling)

---

### 2. `layouts/pages/lab-log.html`

Check if this file already exists in the project. If it does, do not recreate it —
use it as-is. Only create it if it does not exist.

If creating it fresh, it must satisfy all of the following:

**Structure:**
- `{{ define "main" }}` extending `layouts/_default/baseof.html`
- No global navigation, no footer links, no "back to home"
- Renders `.Content` (the Markdown body) in the reading column

**Header band:**
```
[ Dark brown full-width band ]
[ Series tag — monospace amber, small, top ]
[ Page title — Playfair Display, cream, large ]
[ Subtitle — monospace, amber, 60% opacity, small ]
```

**Disclosure banner** (rendered only if page content contains the disclosure shortcode
or if `.Params.disclosure` is set to true in frontmatter — implement both):
- Left border 3px solid `var(--color-accent)`
- Background: `rgba(69,15,0,0.85)`
- Text: small, italic, cream, 90% opacity
- Full width of reading column

**Reading column:**
- Max width `var(--max-width)` (760px), centred
- Horizontal padding: `1.5rem` mobile, `2rem` desktop
- `h2` elements: Playfair Display, `--color-bg-dark`, preceded by the amber rule
  `(display:block; width:28px; height:2px; background:var(--color-accent); margin-bottom:0.5rem)`
- `h3` elements: Source Sans 3, semibold, `--color-bg-dark`
- Body text: Source Sans 3, `1.05rem`, line-height `1.75`
- `a`: `var(--color-accent)`, no underline default, underline on hover
- `code` / `pre`: JetBrains Mono, background `var(--color-bg-dark)`, text `var(--color-text-inv)`,
  `padding: 0.15em 0.4em`, `border-radius: 3px`

**Gallery grid** (`.gallery-grid` class):
- `display: grid`
- `grid-template-columns: 1fr` on mobile (< 768px)
- `grid-template-columns: 1fr 1fr` on desktop (≥ 768px)
- `gap: 1rem`

**Gallery item** (`.gallery-item` class):
- `background: var(--color-card)`
- `border: 1px solid rgba(69,15,0,0.15)`
- `border-radius: 4px`
- `overflow: hidden`
- Image inside: `width: 100%`, `aspect-ratio: 4/3`, `object-fit: cover`, `display: block`
- Caption: `padding: 0.45rem 0.75rem`, `font-size: 0.8rem`, `font-style: italic`,
  `color: var(--color-text)`, `opacity: 0.7`, `line-height: 1.45`

**Spec table** (standard `<table>` rendered from Markdown):
- `width: 100%`
- `border-collapse: collapse`
- Header row: `background: var(--color-bg-dark)`, text `var(--color-text-inv)`,
  `font-family: var(--font-mono)`, `font-size: 0.78rem`, letter-spacing `0.06em`,
  padding `0.5rem 0.85rem`, text-transform uppercase
- `tbody tr:nth-child(odd)`: `background: var(--color-bg)`
- `tbody tr:nth-child(even)`: `background: var(--color-card)`
- `td`: `padding: 0.45rem 0.85rem`, `vertical-align: top`, `font-size: 0.9rem`
- `td:first-child`: `font-weight: 600`, `color: var(--color-bg-dark)`, `width: 38%`
- Mobile: wrap table in a `div` with `overflow-x: auto`, reduce font to `0.8rem`

**Callout / warning block** (`.callout` class — for safety notices, important notes):
- Left border `3px solid var(--color-accent)`
- Background `var(--color-card)`
- Padding `0.75rem 1rem`
- `border-radius: 0 4px 4px 0`
- Font size `0.9rem`
- Use in Markdown via: `<div class="callout">Your note here</div>`

**CSS-only lightbox:**
- Trigger: `<a href="#[id]">` wraps the gallery item image
- Target: `<div id="[id]" class="lightbox">` rendered immediately after the gallery grid
- `.lightbox`: `display: none`, full viewport fixed overlay when `:target`
  ```css
  .lightbox:target {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.88);
    z-index: 999;
  }
  ```
- Image inside: `max-width: 92vw`, `max-height: 90vh`, `object-fit: contain`
- Close button: `<a href="#" class="lb-close">` — positioned top-right,
  `color: var(--color-text-inv)`, `font-size: 1.5rem`, `text-decoration: none`

**Meta footer:**
- After `.Content`, full-width of reading column
- Top border `2px solid rgba(69,15,0,0.15)`
- Padding `0.75rem 0`
- Date on left: `font-family: var(--font-mono)`, `font-size: 0.78rem`, muted
- Tags on right: `font-family: var(--font-mono)`, `font-size: 0.78rem`,
  `color: var(--color-accent)` — rendered from `.Params.tags`, joined with ` · `

**Image processing** — all images are page resources. Use this pattern in shortcodes:
```html
{{ $img := .Page.Resources.GetMatch (.Get "src") }}
{{ if $img }}
  {{ $webp := $img.Resize "1400x webp q82" }}
  {{ $jpeg := $img.Resize "1400x jpg q76" }}
  <picture>
    <source srcset="{{ $webp.RelPermalink }}" type="image/webp">
    <img src="{{ $jpeg.RelPermalink }}"
         alt="{{ .Get "caption" }}"
         width="{{ $jpeg.Width }}"
         height="{{ $jpeg.Height }}"
         loading="lazy">
  </picture>
{{ end }}
```

---

### 3. `layouts/shortcodes/labimg.html`

Check if this file already exists. If it does, use it as-is.

If creating fresh:

**Usage in Markdown:**
```
{{< labimg src="filename.jpg" caption="Caption text" id="img01" >}}
```

**Logic:**
1. Get image as page resource: `.Page.Resources.GetMatch (.Get "src")`
2. Generate WebP: `.Resize "1400x webp q82"`
3. Generate JPEG fallback: `.Resize "1400x jpg q76"`
4. Render:
   ```html
   <figure class="gallery-item">
     <a href="#[id]">
       <picture>
         <source srcset="[webp url]" type="image/webp">
         <img src="[jpeg url]" alt="[caption]" width="[w]" height="[h]" loading="lazy">
       </picture>
     </a>
     <figcaption>[caption]</figcaption>
   </figure>
   <!-- lightbox target -->
   <div id="[id]" class="lightbox">
     <a href="#" class="lb-close">✕</a>
     <picture>
       <source srcset="[webp url]" type="image/webp">
       <img src="[jpeg url]" alt="[caption]">
     </picture>
   </div>
   ```

---

### 4. `layouts/shortcodes/gallery.html`

Check if this file already exists. If it does, use it as-is.

If creating fresh:

**Usage in Markdown:**
```
{{< gallery >}}
{{< labimg src="img1.jpg" caption="Caption" id="g01" >}}
{{< labimg src="img2.jpg" caption="Caption" id="g02" >}}
{{< /gallery >}}
```

**Renders:**
```html
<div class="gallery-grid">
  [inner content]
</div>
```

The CSS grid behaviour is defined in the layout's `<style>` block — the shortcode
only provides the wrapper `<div>`.

---

## Constraints (Non-Negotiable)

- No external CSS frameworks
- No JavaScript — CSS `:target` only for lightbox
- No analytics, tracking, or third-party scripts
- No links to a homepage (there is none)
- No `<form>` elements
- Vanilla CSS only — Grid and Flexbox
- All images must go through Hugo's image processing pipeline — never reference
  raw uploaded files directly
- All images must have `loading="lazy"` and explicit `width`/`height` attributes
  to prevent cumulative layout shift
- All colours must reference CSS variables — never hardcode hex values in layout files
- `noindex: true` in frontmatter at all times

---

## Verification Checklist

After generating all files, confirm:

```bash
hugo server
```

Navigate to `http://localhost:1313/[slug]/` and verify:

- [ ] Header band renders correctly — series tag, title, subtitle
- [ ] Disclosure banner appears (if review unit)
- [ ] Images render in correct positions per Image Manifest
- [ ] Gallery grids show 2 columns on desktop, 1 column on mobile
- [ ] Clicking any gallery image opens lightbox overlay
- [ ] Lightbox closes on ✕ click
- [ ] Spec table renders with correct alternating row shading
- [ ] All external links open correctly
- [ ] Page is fully readable on a 375px viewport
- [ ] `hugo --minify` completes with zero errors and zero warnings

---

## Deployment

Once verified locally:

```bash
git add content/pages/[slug]/ layouts/
git commit -m "Add lab-log: [brief description]"
git push origin main
```

GitHub Actions will build and deploy to `gh-pages` in approximately 60 seconds.

Monitor at: `https://github.com/[YOUR-USERNAME]/billableonline/actions`

Page will be live at: `https://billableonline.co/[slug]/`
