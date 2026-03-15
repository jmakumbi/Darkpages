# Hugo Dark Pages — Skeleton Scaffold

## What to Build

A minimal Hugo project using the **hugo-profile** theme as a CSS/typography foundation,
with all theme navigation and homepage layouts **completely overridden** by custom files.

The result is a dark pages vault — a collection of standalone, unlinked pages deployed
to GitHub Pages under a custom domain. No navigation. No sitemap. No RSS.
No discoverability by design.

This is the scaffold only. Individual pages are added in separate sessions.

---

## Step 1 — Initialise Hugo

```bash
hugo new site billableonline --format yaml
cd billableonline
git init
git submodule add https://github.com/gurusabarish/hugo-profile.git themes/hugo-profile
```

---

## Step 2 — `config.yaml`

Generate this exact `config.yaml`. The theme is loaded but its homepage and menus
are neutralised via config and layout overrides.

```yaml
baseURL: "https://billableonline.co/"
title: "billableonline.co"
languageCode: "en-gb"
theme: "hugo-profile"

enableRobotsTXT: false          # robots.txt managed manually in /static/

disableKinds:
  - taxonomy
  - term
  - RSS
  - sitemap

outputs:
  home:
    - HTML
  page:
    - HTML
  section:
    - HTML

# Neutralise all theme menus — empty arrays, not omitted
menu:
  main: []

params:
  title: "billableonline.co"
  description: ""
  favicon: ""
  useBootstrapCDN: false
  animate: false
  theme:
    defaultTheme: "light"
    disableThemeToggle: true
  color:
    primaryColor: "#eb9130"

  # Disable every theme section that would render on a homepage
  hero:
    enable: false
  about:
    enable: false
  skills:
    enable: false
  experience:
    enable: false
  education:
    enable: false
  achievements:
    enable: false
  projects:
    enable: false
  contact:
    enable: false

  navbar:
    disableSearch: true
    stickyNavBar:
      enable: false
    menus:
      disableAbout: true
      disableExperience: true
      disableEducation: true
      disableProjects: true
      disableAchievements: true
      disableContact: true
```

---

## Step 3 — Brand CSS Override (`assets/css/brand.css`)

Create `assets/css/brand.css` to inject brand tokens and override the theme's
colour defaults.

```css
:root {
  --color-bg:       #e8e1d1;
  --color-bg-dark:  #450f00;
  --color-accent:   #eb9130;
  --color-text:     #1a0800;
  --color-text-inv: #e8e1d1;
  --font-heading:   'Playfair Display', Georgia, serif;
  --font-body:      'Source Sans 3', system-ui, sans-serif;
  --font-mono:      'JetBrains Mono', 'Courier New', monospace;
  --max-width:      720px;
  --max-width-wide: 1100px;
}

body {
  background-color: var(--color-bg) !important;
  color: var(--color-text) !important;
  font-family: var(--font-body) !important;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading) !important;
  color: var(--color-bg-dark) !important;
}

a { color: var(--color-accent) !important; }
a:hover { color: var(--color-bg-dark) !important; }
code, pre { font-family: var(--font-mono) !important; }

/* Suppress the theme navbar and footer completely */
#navbar, nav.navbar, .navbar { display: none !important; }
footer.footer, #footer { display: none !important; }
```

---

## Step 4 — Head Partial Override (`layouts/partials/head.html`)

This overrides the theme's head partial. Include Google Fonts and force noindex
on every page — this is a vault, nothing gets indexed, ever.

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} — {{ .Site.Title }}{{ end }}</title>
<meta name="robots" content="noindex, nofollow">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400&family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">

{{- template "_default/head.html" . }}
```

---

## Step 5 — Homepage Override (`layouts/index.html`)

Completely replaces the theme's homepage. Must NOT call any theme homepage partials.

```html
{{ define "main" }}
<style>
  .gate-wrapper {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--color-bg-dark);
    padding: 2rem;
    text-align: center;
  }
  .gate-rule {
    display: block;
    width: 48px;
    height: 3px;
    background: var(--color-accent);
    margin: 0 auto 2rem;
  }
  .gate-headline {
    font-family: var(--font-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
    color: var(--color-text-inv);
    line-height: 1.2;
    margin-bottom: 1.5rem;
    font-weight: 700;
  }
  .gate-sub {
    font-family: var(--font-body);
    font-size: clamp(1rem, 2.5vw, 1.25rem);
    color: var(--color-text-inv);
    opacity: 0.75;
    max-width: 420px;
    line-height: 1.6;
    margin-bottom: 3rem;
  }
  .gate-domain {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    color: var(--color-accent);
    opacity: 0.6;
    letter-spacing: 0.08em;
    position: fixed;
    bottom: 1.5rem;
    left: 50%;
    transform: translateX(-50%);
  }
</style>

<div class="gate-wrapper">
  <span class="gate-rule"></span>
  <h1 class="gate-headline">Members only.</h1>
  <p class="gate-sub">
    If you're looking for something,<br>
    you already have the link.
  </p>
  <span class="gate-domain">billableonline.co</span>
</div>
{{ end }}
```

---

## Step 6 — `static/robots.txt`

```
User-agent: *
Disallow: /
```

---

## Step 7 — `static/CNAME`

```
billableonline.co
```

---

## Step 8 — Pages Folder and Archetype

```bash
mkdir -p content/pages
touch content/pages/.gitkeep
mkdir -p layouts/pages
```

Create `archetypes/pages.md`:

```yaml
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
layout: "article"
description: ""
slug: ""
noindex: true
---
```

---

## Step 9 — GitHub Actions (`.github/workflows/deploy.yml`)

Generate a complete workflow that:
- Triggers on push to `main`
- Uses `actions/checkout@v4` with `submodules: true` and `fetch-depth: 0`
  (`submodules: true` is required — the hugo-profile theme is a git submodule)
- Uses `peaceiris/actions-hugo@v3` with `hugo-version: 'latest'` and `extended: true`
- Runs `hugo --minify`
- Deploys `./public` to the `gh-pages` branch via `peaceiris/actions-gh-pages@v4`
- Sets `cname: billableonline.co` in the deploy step

---

## Step 10 — README (`README.md`)

Generate a technical README covering:
- What this is: dark pages vault, no navigation, no discoverability
- The hugo-profile theme is present as a submodule but all homepage/nav layouts are overridden
- Hugo version: extended required (for CSS pipeline)
- Local dev: `hugo server -D`
- Deployment: push to `main`, GitHub Actions handles the rest
- Custom domain: CNAME in static/, DNS A records:
  185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153
- Adding pages: `hugo new pages/your-slug.md` → add layout to `layouts/pages/`

---

## Step 11 — Verify

```bash
hugo server
```

Expected:
- `http://localhost:1313/` → Dark brown Members Only gate, no navbar
- No other routes exist yet
- Zero build errors, zero warnings

---

## Deliverables Summary

| Path | Description |
|------|-------------|
| `config.yaml` | Theme loaded, all sections + menus disabled |
| `assets/css/brand.css` | Brand tokens, nav/footer suppression |
| `layouts/partials/head.html` | Google Fonts, hard noindex on all pages |
| `layouts/index.html` | Members Only gate — replaces theme homepage |
| `static/robots.txt` | `Disallow: /` |
| `static/CNAME` | `billableonline.co` |
| `archetypes/pages.md` | Page archetype |
| `content/pages/.gitkeep` | Placeholder |
| `layouts/pages/` | Empty — page layouts added per session |
| `.github/workflows/deploy.yml` | GitHub Actions with `submodules: true` |
| `README.md` | Project documentation |
