# billableonline.co — Dark Pages Architecture

## What This Is

A collection of standalone Hugo pages deployed to GitHub Pages under a custom domain.
No homepage. No navigation. No index. If you don't have the URL, you don't find the page.

This is not a website. It's a vault of pages that happen to share a domain.

---

## The Approach

Each page is:
- **Self-contained** — its own layout, its own purpose, its own feel
- **Unlinked by default** — no global nav, no footer links, no sitemap
- **Unsearchable** — `robots.txt` blocks all crawlers
- **Brandable** — shares the billableonline.co colour palette and typography
- **Shareable** — the URL is the key

Pages can link to each other deliberately (inline, in body copy) but never automatically.

---

## Root URL Behaviour

`https://billableonline.co` → A single, styled page in brand colours.  
Cheeky message. No links. No nav. Nothing to click.  
Something like: *"Members only. If you're looking for something, you already have the link."*

---

## Brand Palette

| Token        | HEX       | Usage                                     |
|--------------|-----------|-------------------------------------------|
| Deep Brown   | `#450f00` | Backgrounds, headers, dark surfaces       |
| Amber Orange | `#eb9130` | Accents, highlights, calls to action      |
| Warm Cream   | `#e8e1d1` | Body backgrounds, light text on dark      |
| Near-Black   | `#1a0800` | Body text                                 |

Typography: **Playfair Display** (headings) · **Source Sans 3** (body) · **JetBrains Mono** (code)

---

## File Structure

```
billableonline/
├── config.yaml                  # Hugo config — no menus, no RSS, no sitemap
├── static/
│   ├── robots.txt               # Disallow: /  (block all crawlers)
│   └── CNAME                    # billableonline.co
├── layouts/
│   ├── _default/
│   │   └── baseof.html          # Shared base: fonts, CSS vars, nothing else
│   ├── index.html               # The cheeky members-only root page
│   └── partials/
│       ├── head.html            # Meta, fonts, CSS
│       └── brand.css.html       # CSS custom properties (injected into <head>)
├── content/
│   └── _index.md                # Homepage frontmatter only
└── .github/
    └── workflows/
        └── deploy.yml           # GitHub Actions → GitHub Pages
```

Pages live at:
```
content/pages/
├── your-slug.md                 # → billableonline.co/your-slug/
├── another-slug.md
└── ...
```

Each page uses its own `layout` param in frontmatter to select a custom layout template.

---

## How Pages Are Built

Each page is built in **its own Claude Code chat session** using a page-specific prompt.

The page prompt will:
1. Define the page's purpose and content
2. Specify its layout type (article, services, lab-log, etc.)
3. Reference the shared brand vars
4. Generate the `.md` content file + matching `layouts/pages/<layout>.html`

The scaffold (built once, from `hugo-darkpages-scaffold.md`) provides the base.
Individual page prompts build on top of that base.

---

## Prompt Files

| File | Purpose | Status |
|------|---------|--------|
| `hugo-darkpages-scaffold.md` | Build the Hugo skeleton once — GitHub Actions, domain, root page | **Run first in Claude Code** |
| `page-building-guide.md` | Reference for building individual pages in their own chats | **Read before each page chat** |

---

## Deployment

- **Host:** GitHub Pages
- **Branch:** `gh-pages` (auto-deployed via GitHub Actions)
- **Domain:** `billableonline.co` (CNAME + DNS A records)
- **HTTPS:** Enforced automatically by GitHub Pages
- **Trigger:** Push to `main` → build → deploy

---

## What the Old Prompts Were

Previous prompts (`hugo-portfolio-gh-pages.md`, `hugo-portfolio-brand-colors.md`, `hugo-full-site-build.md`) were for a full three-section website with homepage, hub architecture, and global navigation.

**That direction has been abandoned.** Those files are archived only.  
Do not run them. Use only the files listed in this README.
