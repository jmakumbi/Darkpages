# Darkpages

Source for **[billableonline.co](https://billableonline.co)** — a Hugo-based vault of standalone, unlinked pages deployed to GitHub Pages.

## Concept

This is not a website. It's a collection of self-contained pages that share a domain but have no navigation, no index, and no discoverability. If you don't have the URL, you don't find the page.

- **No homepage** — root URL shows a "Members only" gate
- **No navigation** — pages are islands, linked only by sharing the URL directly
- **No indexing** — `robots.txt` blocks all crawlers; every page has `noindex`
- **Minimal analytics** — GoatCounter pixel only, routed through `gc.billableonline.co` to avoid ad blocker interference; suppressed in local dev

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
├── hugo.yaml                          # Hugo config
├── assets/css/brand.css               # Brand tokens (colours, fonts, spacing)
├── layouts/
│   ├── _default/baseof.html           # Clean base layout (no navbar, no footer)
│   ├── index.html                     # "Members only" gate page
│   ├── partials/head.html             # Google Fonts, noindex meta, brand CSS
│   ├── pages/
│   │   ├── lab-log.html               # Image-heavy equipment/homelab pages
│   │   ├── article.html               # Long-form writing and product explainers
│   │   └── services.html              # Portfolio and consulting pages
│   └── shortcodes/
│       ├── labimg.html                # Image with Hugo processing + CSS lightbox
│       ├── gallery.html               # 2-column image grid wrapper
│       ├── screenshot-fig.html        # Full-width pipeline screenshot with caption
│       ├── screenshot.html            # Basic figure (no pipeline)
│       ├── hw-cards.html              # Hardware product card grid
│       ├── m365-screenshot.html       # M365 admin screenshot
│       ├── callout.html               # Highlighted callout block
│       ├── pullquote.html             # Pull quote
│       └── stamp.html                 # Status/label stamp
├── content/pages/                     # All pages as Hugo leaf bundles
│   ├── zimacube-2-pro-unboxing/
│   ├── viral-messages-qui-bono/
│   ├── legal-tech-portfolio/
│   ├── justiflow-adr/
│   ├── complyea/
│   ├── concordia-clm/
│   ├── convoy/
│   ├── opus-juris/
│   └── firewalla-homelab/
├── static/robots.txt                  # Disallow: /
├── scripts/strip-exif.py              # EXIF metadata stripping utility
├── .github/workflows/deploy.yml       # GitHub Actions deploy pipeline
├── prompt/                            # Active page briefs and source images
└── completed prompts/                 # Archived briefs for published pages
```

## Live Pages

| Page | URL |
|------|-----|
| Homepage (gate) | [billableonline.co](https://billableonline.co) |
| ZimaCube 2 Pro Unboxing | [/zimacube-2-pro-unboxing/](https://billableonline.co/zimacube-2-pro-unboxing/) |
| Viral Messages — Qui Bono? | [/viral-messages-qui-bono/](https://billableonline.co/viral-messages-qui-bono/) |
| Legal Tech Portfolio | [/legal-tech-portfolio/](https://billableonline.co/legal-tech-portfolio/) |
| JustiFlow ADR | [/justiflow-adr/](https://billableonline.co/justiflow-adr/) |
| ComplyEA | [/complyea/](https://billableonline.co/complyea/) |
| Concordia CLM | [/concordia-clm/](https://billableonline.co/concordia-clm/) |
| Convoy | [/convoy/](https://billableonline.co/convoy/) |
| Opus Juris | [/opus-juris/](https://billableonline.co/opus-juris/) |
| Firewalla Homelab | [/firewalla-homelab/](https://billableonline.co/firewalla-homelab/) |

## Page Layouts

| Layout | Purpose | Status |
|--------|---------|--------|
| `lab-log` | Homelab builds, equipment reviews, image-heavy documentation | Built |
| `article` | Long-form writing, product explainers, analysis | Built |
| `services` | Service offerings, consulting capabilities, portfolio | Built |
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
cd D:\Repositories\Darkpages
hugo server
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
   (Python path on this machine: `C:\Users\jmaku\AppData\Local\Programs\Python\Python312\python.exe`)
3. Build and verify: `hugo --minify` (zero errors, zero warnings)
4. Commit and push to `main`
5. Page goes live at `https://billableonline.co/[slug]/`
