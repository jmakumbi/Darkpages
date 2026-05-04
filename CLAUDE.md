# Darkpages — billableonline.co

## What This Is

A Hugo static site vault — standalone, unlinked pages deployed to GitHub Pages under `billableonline.co`. No navigation, no sitemap, no discoverability. Pages are shared by URL only.

## Quick Reference

- **Hugo extended** is required (install via `winget install Hugo.Hugo.Extended` or equivalent)
- **Python 3.12+** with **Pillow** for EXIF stripping (`pip install Pillow`)
  - Python path on this machine: `C:\Users\jmaku\AppData\Local\Programs\Python\Python312\python.exe`
- **GitHub CLI** (`gh`)
- **Dev server**: `hugo server` → http://localhost:1313/
- **Build**: `hugo --minify` (must produce zero errors, zero warnings)
- **Deploy**: push to `main` → GitHub Actions builds with `actions/deploy-pages` in ~60s

## Deployment Architecture

The workflow (`.github/workflows/deploy.yml`) uses the official GitHub Pages deployment:
1. `peaceiris/actions-hugo@v3` builds with Hugo extended
2. `actions/upload-pages-artifact@v3` packages `./public`
3. `actions/deploy-pages@v4` deploys to GitHub Pages

GitHub Pages source is set to **"GitHub Actions"** (not "Deploy from a branch"). Do NOT change this — using branch-based deployment causes the raw `main` content to overwrite the Hugo output.

## Adding a New Post

When the user asks to create a new page, follow this workflow:

### 1. Create the leaf bundle
```
content/pages/[slug]/
├── index.md        ← frontmatter + content
├── image1.jpg      ← all images as page resources
└── ...
```

### 2. Strip EXIF from ALL images before building
```bash
python scripts/strip-exif.py content/pages/[slug]/
```
This is **mandatory** for every post. Never skip. Never commit images with EXIF data.

### 3. Write the content
Use existing layouts — do NOT create new layouts unless the user explicitly requests a new page type.

Available layouts:
- `lab-log` — equipment reviews, homelab builds, image-heavy technical docs (BUILT)
- `article` — long-form writing, product explainers (BUILT)
- `services` — consulting/offerings, portfolio pages (BUILT)
- `note` — short observations (spec in `prompt/page-building-guide.md`, build when first needed)
- `profile` — bio pages (spec in `prompt/page-building-guide.md`, build when first needed)

### 4. Frontmatter template
```yaml
---
title: "Page Title"
date: YYYY-MM-DD
draft: false
layout: "lab-log"
description: "One sentence for Open Graph."
slug: "url-slug"
url: "/url-slug/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Optional subtitle"
series: "optional-series-slug"
toc: false
disclosure: true  # set to true if review unit
disclosure_text: "Disclosure text here."
tags:
  - tag1
  - tag2
---
```

### 5. Images
- Use `{{</* labimg src="filename.jpg" caption="Caption" id="unique-id" */>}}` for all images in `lab-log` pages
- Use `{{</* screenshot-fig src="filename.jpg" alt="Alt text" caption="Caption" */>}}` for full-width pipeline screenshots in `article` pages
- Use `{{</* gallery */>}}...{{</* /gallery */>}}` to wrap `labimg` calls in a 2-column grid
- Hugo processes images automatically: `Resize 800x` for thumbnails (preserves natural aspect ratio), `Resize 1400x` for lightbox
- All images get WebP (q82) + JPEG fallback (q76)
- Thumbnail and lightbox use separate processed images — thumbnails maintain original ratio, lightbox shows full image
- For portrait galleries (mobile app screenshots), wrap `labimg` calls in `<div class="gallery-grid gallery-portrait">` raw HTML instead of the `gallery` shortcode — this triggers the portrait CSS override (400px fixed height, object-position: top)

### 6. Build and verify
```bash
hugo --minify    # must be zero errors
```

### 7. Commit and push
```bash
git add content/pages/[slug]/ layouts/  # only add layouts/ if a new layout was created or modified
git commit -m "Add [page-type]: [brief description]"
git push origin main
```

Page goes live at: `https://billableonline.co/[slug]/`

## Planning Documents

New page briefs go in `prompt/`. Completed briefs are archived in `completed prompts/`. Both folders are gitignored — local only, never pushed to GitHub.

- `completed prompts/PROJECT-README.md` — original architecture overview and brand guide
- `completed prompts/hugo-darkpages-scaffold.md` — Hugo skeleton build instructions (already executed)
- `completed prompts/page-building-guide.md` — reference for page creation across all layout types
- `completed prompts/lablog-page-template.md` — reusable prompt template for lab-log pages
- `completed prompts/github-pages-dns-setup.md` — DNS A records and GitHub Pages configuration

## Live Pages

| Slug | URL | Layout |
|------|-----|--------|
| zimacube-2-pro-unboxing | /zimacube-2-pro-unboxing/ | lab-log |
| viral-messages-qui-bono | /viral-messages-qui-bono/ | article |
| legal-tech-portfolio | /legal-tech-portfolio/ | services |
| justiflow-adr | /justiflow-adr/ | article |
| complyea | /complyea/ | article |
| concordia-clm | /concordia-clm/ | article |
| convoy | /convoy/ | article |
| opus-juris | /opus-juris/ | article |
| firewalla-homelab | /firewalla-homelab/ | lab-log |
| zimaboard-832-unboxing | /zimaboard-832-unboxing/ | lab-log |
| firewalla-reflash | /firewalla-reflash/ | lab-log |
| vapt-appliance-zimaboard2 | /vapt-appliance-zimaboard2/ | lab-log |
| fireguard | /fireguard/ | lab-log |
| firewalla-gold-se | /firewalla-gold-se/ | lab-log |
| zimablade-7700-unboxing | /zimablade-7700-unboxing/ | lab-log |
| zimaboard-2-unboxing | /zimaboard-2-unboxing/ | lab-log |
| visionfive2-unboxing | /visionfive2-unboxing/ | lab-log |
| ai-in-your-practice | /ai-in-your-practice/ | article |
| deskpi-rackmate-t1 | /deskpi-rackmate-t1/ | lab-log |
| dark-gate-rack-build | /dark-gate-rack-build/ | lab-log |

## Brand Tokens (DO NOT change without user request)

```css
--color-bg:       #d6cdb8   /* Warm Cream */
--color-bg-dark:  #450f00   /* Deep Brown */
--color-accent:   #c47a22   /* Muted Amber */
--color-text:     #1a0800   /* Near-black */
--color-text-inv: #d6cdb8   /* Cream on dark */
--color-card:     #e8e2d4   /* Card backgrounds */

--font-heading: 'Playfair Display'
--font-body:    'Source Sans 3'
--font-mono:    'JetBrains Mono'
```

## Shortcodes

- `labimg` — single image with Hugo processing + CSS lightbox (`src`, `caption`, `id` params) — for `lab-log` pages
- `gallery` — wraps `labimg` calls in a 2-column CSS grid (1-column on mobile); for portrait screenshots use raw `<div class="gallery-grid gallery-portrait">` instead
- `screenshot-fig` — full-width pipeline screenshot with caption, uses `.screenshot-fig` CSS class (`src`, `alt`, `caption` params)
- `hw-cards` — hardware product card grid, reads images from page resources, hardcoded to legal-tech-portfolio devices
- `m365-screenshot` — Microsoft 365 admin screenshot, hardcoded to legal-tech-portfolio
- `screenshot` — basic image figure without pipeline processing (`src`, `caption`, `fig` params)
- `callout` — highlighted callout block
- `pullquote` — pull quote styling
- `stamp` — status/label stamp
- `rule-box` — bordered content block for key rules or highlighted principles (`inner` content)
- `three-check-rule` — 3-card Verify/Review/Own It checklist (no params; hardcoded to AI-in-legal-practice context)
- `pda-card` — Paulette Decor Arts feature card with logo, description, and external link (no params; reads `paulette-logo.png` from page resources)

## Constraints (always enforce)

- No JavaScript — CSS `:target` only for interactivity
- No analytics beyond GoatCounter pixel — tracking via `gc.billableonline.co/count` (custom domain), suppressed during `hugo server`, configured via `params.goatcounter` in `hugo.yaml`
- Favicon is `static/favicon.svg` — referenced in `layouts/partials/head.html` as `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`
- No links to a homepage
- All colours via CSS variables — never hardcode hex in layouts
- All images through Hugo's processing pipeline — never reference raw files
- `noindex: true` on every page, always
- `url: "/slug/"` must be set explicitly in every page's frontmatter
- Strip EXIF from every image before commit
- All source images must have EXIF stripped using `scripts/strip-exif.py`
