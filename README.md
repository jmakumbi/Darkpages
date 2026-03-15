# Darkpages

Source for **[billableonline.co](https://billableonline.co)** — a Hugo-based vault of standalone, unlinked pages deployed to GitHub Pages.

## Concept

This is not a website. It's a collection of self-contained pages that share a domain but have no navigation, no index, and no discoverability. If you don't have the URL, you don't find the page.

- **No homepage** — root URL shows a "Members only" gate
- **No navigation** — pages are islands, linked only by sharing the URL directly
- **No indexing** — `robots.txt` blocks all crawlers; every page has `noindex`
- **No analytics** — no tracking, no third-party scripts

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Generator | [Hugo](https://gohugo.io/) (extended) |
| Theme | `hugo-profile` (git submodule — used as CSS/typography base only; all layouts overridden) |
| Hosting | GitHub Pages via `actions/deploy-pages` |
| Domain | `billableonline.co` (CNAME + DNS A records, HTTPS enforced) |
| CI/CD | GitHub Actions — push to `main` triggers build and deploy |
| Styling | Vanilla CSS (Grid + Flexbox), no frameworks |
| JavaScript | None by design |

## Project Structure

```
├── hugo.yaml                          # Hugo config — theme loaded, all sections disabled
├── assets/css/brand.css               # Brand tokens (colours, fonts, spacing)
├── layouts/
│   ├── _default/baseof.html           # Clean base layout (no navbar, no footer)
│   ├── index.html                     # "Members only" gate page
│   ├── partials/head.html             # Google Fonts, noindex meta, brand CSS
│   ├── pages/lab-log.html             # Lab-log page layout
│   └── shortcodes/
│       ├── labimg.html                # Image with Hugo processing + lightbox
│       └── gallery.html               # 2-column image grid wrapper
├── content/pages/                     # All pages as Hugo leaf bundles
│   └── zimacube-2-pro-unboxing/       # Live page with images
├── static/
│   ├── robots.txt                     # Disallow: /
│   └── CNAME                          # billableonline.co
├── scripts/strip-exif.py              # EXIF metadata stripping utility
├── .github/workflows/deploy.yml       # GitHub Actions deploy pipeline
└── docs/                              # Planning documents
    ├── PROJECT-README.md              # Architecture overview & brand guide
    ├── hugo-darkpages-scaffold.md     # Hugo skeleton build instructions
    ├── page-building-guide.md         # Reference for creating pages
    ├── github-pages-dns-setup.md      # DNS & deployment guide
    └── lablog-page-template.md        # Reusable lab-log prompt template
```

## Live Pages

| Page | URL |
|------|-----|
| Homepage (gate) | [billableonline.co](https://billableonline.co) |
| ZimaCube 2 Pro Unboxing | [billableonline.co/zimacube-2-pro-unboxing/](https://billableonline.co/zimacube-2-pro-unboxing/) |

## Page Types

| Layout | Purpose | Status |
|--------|---------|--------|
| `lab-log` | Homelab builds, equipment reviews, image-heavy documentation | Built |
| `article` | Long-form writing, guides, analysis | Spec only |
| `services` | Service offerings, consulting capabilities | Spec only |
| `note` | Short observations, quick references | Spec only |
| `profile` | Bio pages, credentials | Spec only |

## Brand

| Token | Hex | Usage |
|-------|-----|-------|
| Deep Brown | `#450f00` | Dark surfaces, headers |
| Muted Amber | `#c47a22` | Accents, links, CTAs |
| Warm Cream | `#d6cdb8` | Page backgrounds, light text on dark |
| Near-Black | `#1a0800` | Body text |
| Card | `#e8e2d4` | Card backgrounds, alt table rows |

**Fonts:** Playfair Display (headings) · Source Sans 3 (body) · JetBrains Mono (code)

## Local Development

```bash
hugo server -D
# http://localhost:1313/
```

## Deployment

Push to `main` triggers the GitHub Actions workflow:
1. Hugo builds with `--minify`
2. `actions/upload-pages-artifact` packages the output
3. `actions/deploy-pages` deploys to GitHub Pages

Site is live with HTTPS at `billableonline.co` within ~60 seconds.

## Adding a New Page

1. Create a leaf bundle at `content/pages/[slug]/` with `index.md` and images
2. Strip EXIF from images: `python scripts/strip-exif.py content/pages/[slug]/`
3. Build and verify: `hugo --minify` (zero errors)
4. Commit and push to `main`
5. Page goes live at `https://billableonline.co/[slug]/`
