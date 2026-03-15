# Darkpages — billableonline.co

## What This Is

A Hugo static site vault — standalone, unlinked pages deployed to GitHub Pages under `billableonline.co`. No navigation, no sitemap, no discoverability. Pages are shared by URL only.

## Quick Reference

- **Hugo extended** is required. Binary path (if not on PATH): `C:/Users/jmaku/AppData/Local/Microsoft/WinGet/Packages/Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe/hugo.exe`
- **Python 3.12** for EXIF stripping: `C:/Users/jmaku/AppData/Local/Programs/Python/Python312/python.exe`
- **GitHub CLI**: `D:/Program Files/GitHub CLI/gh.exe`
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
- `article` — long-form writing (spec in `page-building-guide.md`, build when first needed)
- `services` — consulting/offerings (spec in `page-building-guide.md`, build when first needed)
- `note` — short observations (spec in `page-building-guide.md`, build when first needed)
- `profile` — bio pages (spec in `page-building-guide.md`, build when first needed)

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
- Use `{{</* labimg src="filename.jpg" caption="Caption" id="unique-id" */>}}` for all images
- Use `{{</* gallery */>}}...{{</* /gallery */>}}` to wrap images in a 2-column grid
- Hugo processes images automatically: `Fill 1400x1050 Smart` crop for thumbnails, `Resize 1400x` for lightbox
- All images get WebP (q82) + JPEG fallback (q76)
- Thumbnail and lightbox use separate processed images — thumbnails are cropped 4:3, lightbox shows full image

### 6. Build and verify
```bash
hugo --minify    # must be zero errors
```

### 7. Commit and push
```bash
git add content/pages/[slug]/ layouts/  # only add layouts/ if a new layout was created
git commit -m "Add [page-type]: [brief description]"
git push origin main
```

Page goes live at: `https://billableonline.co/[slug]/`

## Planning Documents

Planning docs and page brief templates are in the repo root:
- `PROJECT-README.md` — original architecture overview and brand guide
- `hugo-darkpages-scaffold.md` — Hugo skeleton build instructions (already executed)
- `page-building-guide.md` — reference for page creation across all layout types
- `lablog-page-template.md` — reusable prompt template for lab-log pages
- `github-pages-dns-setup.md` — DNS A records and GitHub Pages configuration
- `zimacube-page-bundle/` — source brief and images for the ZimaCube post

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

- `labimg` — single image with Hugo processing + CSS lightbox (`src`, `caption`, `id` params)
- `gallery` — wraps `labimg` calls in a 2-column CSS grid (1-column on mobile)

## Constraints (always enforce)

- No JavaScript — CSS `:target` only for interactivity
- No analytics, tracking, or third-party scripts
- No links to a homepage
- All colours via CSS variables — never hardcode hex in layouts
- All images through Hugo's processing pipeline — never reference raw files
- `noindex: true` on every page, always
- Strip EXIF from every image before commit
- All source images must have EXIF stripped using `scripts/strip-exif.py`
