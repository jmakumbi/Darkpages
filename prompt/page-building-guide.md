# Page Building Guide — billableonline.co Dark Pages

## How This Works

Each page gets its own Claude Code chat session. This file is your reference
for how to brief those sessions consistently.

The scaffold (`hugo-darkpages-scaffold.md`) must be run first. Every page
prompt assumes the base project already exists.

---

## Page Types Available

| Layout Name | Use For | Feel |
|-------------|---------|------|
| `article` | Long-form writing, analysis, guides | Editorial, text-heavy, readable |
| `services` | Consulting capabilities, what you offer | Professional, structured, conversion-focused |
| `lab-log` | Homelab builds, project documentation | Technical, visual, pictorial |
| `note` | Short observations, quick references | Minimal, fast, knowledge-base |
| `profile` | Bio page, credentials, speaking | Personal, authoritative |

New layout types can be added anytime — just name them and build a matching
`layouts/pages/<name>.html` in the same session.

---

## Frontmatter Reference

Every page `.md` file should have this frontmatter block. Fill in all fields.

```yaml
---
title: "Your Page Title"
date: 2026-03-13
draft: false
layout: "article"             # Pick from the table above
description: "One sentence. Used in Open Graph if sharing is enabled."
slug: "your-url-slug"         # becomes billableonline.co/your-url-slug/
noindex: true                 # Always true. Never index.

# Optional fields depending on page type:
subtitle: ""                  # Secondary heading shown under title
cover_image: ""               # Path to hero image e.g. /images/pages/slug/hero.jpg
tags: []                      # Internal organisation only — never rendered as links
series: ""                    # For multi-part content e.g. "homelab-build"
toc: true                     # Show floating table of contents (article/lab-log only)
---
```

---

## How to Structure a Page Prompt

When starting a new page chat, open with this block and fill it in:

```
## Page Brief

**Page type:** [article | services | lab-log | note | profile]
**Slug:** [url-slug]
**Title:** [Full page title]
**Purpose:** [One sentence — what does this page do?]
**Audience:** [Who gets this URL?]
**Tone:** [e.g. technical and direct | warm and persuasive | dry and confident]

## Content Notes

[Bullet points of what should be on the page — key sections, key messages,
specific facts to include. Be as detailed or as brief as you want here.
The prompt will expand this into full content.]

## Layout Notes

[Any specific layout preferences — e.g. "two-column for services",
"image gallery halfway through", "pull quote on the right side"]
```

Then append the standard boilerplate below.

---

## Standard Boilerplate (append to every page prompt)

```
## Project Context

This page is part of the billableonline.co dark pages vault.
The scaffold is already built. You are adding ONE new page to it.

## What to Build

1. `content/pages/<slug>.md` — Full page content in Markdown with complete frontmatter
2. `layouts/pages/<layout>.html` — The HTML layout for this page type

   The layout must:
   - Extend `layouts/_default/baseof.html` using `{{ define "main" }}`
   - Use only brand CSS variables (no hardcoded colours)
   - Be fully self-contained — no global nav, no footer links
   - Be responsive (mobile-first, single breakpoint at 768px is fine)
   - Include an optional `<head>` block override for page-specific meta tags
   - Respect the `noindex` frontmatter param:
     `{{ if .Params.noindex }}<meta name="robots" content="noindex,nofollow">{{ end }}`

3. Any static assets (images, icons) → reference paths only, note where files go

## Brand Reference

--color-bg:       #e8e1d1   (Warm Cream — page background)
--color-bg-dark:  #450f00   (Deep Brown — dark surfaces, headers)
--color-accent:   #eb9130   (Amber Orange — accents, links, CTAs)
--color-text:     #1a0800   (Near-black warm — body copy)
--color-text-inv: #e8e1d1   (Cream — text on dark backgrounds)

Font stack already loaded globally:
--font-heading: 'Playfair Display', Georgia, serif
--font-body:    'Source Sans 3', system-ui, sans-serif
--font-mono:    'JetBrains Mono', 'Courier New', monospace

## Constraints

- No external CSS frameworks
- No JavaScript unless it genuinely improves the page (note what it does)
- No analytics, tracking, or third-party scripts
- No links back to a homepage (there is none)
- Vanilla CSS only — use CSS Grid and Flexbox
- Content should feel written, not generated — real voice, real context
```

---

## Layout Design Principles

**article** — Max width 720px, centered. Large Playfair Display headline.
Drop cap optional. Subheadings in amber. Code blocks in dark brown with
cream text. Floating TOC on desktop (right sidebar, sticky).

**services** — Max width 1100px. Two or three column grid for service cards.
Each card: icon/symbol, short title, 2-3 sentence description, optional CTA.
Dark header band at top with title in cream. Amber accent rules.

**lab-log** — Full width for image galleries. Gear/spec tables with alternating
row shading using cream/brown tones. Series navigation (prev/next) at bottom.
Image captions in small italic.

**note** — Extremely minimal. Max width 600px. No images. Date shown small.
One level of headings maximum. Fast to read. Monospace accent for code.

**profile** — Optional hero band. Two columns on desktop: portrait left,
bio right. Credentials as a clean list. Amber rules as section dividers.

---

## Adding Images to Pages

Static images go in: `static/images/pages/<slug>/`

Reference in Markdown as: `![Alt text](/images/pages/slug/filename.jpg)`

For lab-log pages, use a Hugo shortcode for gallery grids. The page prompt
should request a `gallery` shortcode be created in `layouts/shortcodes/gallery.html`.

---

## URL Structure

Pages deploy to: `https://billableonline.co/<slug>/`

Keep slugs:
- Lowercase, hyphenated
- Descriptive but short (3–5 words max)
- Stable — once shared, never change

---

## Checklist Before Sharing a Page URL

- [ ] `noindex: true` in frontmatter
- [ ] `robots.txt` still has `Disallow: /`
- [ ] No links to other pages unless deliberate
- [ ] Page renders correctly on mobile
- [ ] Hugo builds with zero errors (`hugo --minify`)
- [ ] Deployed to `gh-pages` branch via GitHub Actions
- [ ] HTTPS working on `billableonline.co/<slug>/`
