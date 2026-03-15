# Darkpages

Planning documents, templates, and page bundles for **billableonline.co** — a Hugo-based vault of standalone, unlinked pages deployed to GitHub Pages.

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
| Theme | `hugo-profile` (used as CSS/typography base only; all layouts overridden) |
| Hosting | GitHub Pages (`gh-pages` branch) |
| Domain | `billableonline.co` (CNAME + DNS A records, HTTPS enforced) |
| CI/CD | GitHub Actions — push to `main` triggers build and deploy |
| Styling | Vanilla CSS (Grid + Flexbox), no frameworks |
| JavaScript | None by design |

## Repository Contents

```
├── PROJECT-README.md              # Architecture overview & brand guide
├── hugo-darkpages-scaffold.md     # Instructions to build the Hugo skeleton
├── page-building-guide.md         # Reference for creating individual pages
├── github-pages-dns-setup.md      # DNS configuration & deployment guide
├── lablog-page-template.md        # Reusable template for lab-log page type
├── zimacube-page-bundle/          # Example page bundle (ZimaCube 2 Pro unboxing)
│   ├── zimacube-2-pro-unboxing.md
│   └── *.jpg
└── zimacube-page-bundle.zip       # Bundled copy of the above
```

## Page Types

| Layout | Purpose |
|--------|---------|
| `article` | Long-form writing, guides, analysis |
| `services` | Service offerings, consulting capabilities |
| `lab-log` | Homelab builds, equipment reviews, image-heavy documentation |
| `note` | Short observations, quick references |
| `profile` | Bio pages, credentials |

## Brand

| Token | Hex | Usage |
|-------|-----|-------|
| Deep Brown | `#450f00` | Dark surfaces, headers |
| Amber Orange | `#eb9130` | Accents, links, CTAs |
| Warm Cream | `#e8e1d1` | Page backgrounds, light text on dark |
| Near-Black | `#1a0800` | Body text |

**Fonts:** Playfair Display (headings) · Source Sans 3 (body) · JetBrains Mono (code)

## Workflow

1. Build the Hugo skeleton once using `hugo-darkpages-scaffold.md`
2. Create individual pages using `page-building-guide.md` as reference
3. Each page is a Hugo leaf bundle under `content/pages/[slug]/`
4. Push to `main` — GitHub Actions builds and deploys automatically
5. Page goes live at `https://billableonline.co/[slug]/`

## Deployment

Push to `main` triggers a GitHub Actions workflow that runs `hugo --minify` and deploys the `public/` directory to the `gh-pages` branch. GitHub Pages serves the site with automatic HTTPS via Let's Encrypt.
