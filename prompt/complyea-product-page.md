# ComplyEA — Product Page Build
## billableonline.co Dark Pages Vault

---

## How to Use This Prompt

Drop this file into a Claude Code session. Fill in nothing — the content below is
complete. Build the page, verify locally, then push.

---

## Page Brief

**Page type:** article
**Slug:** `complyea`
**Title:** ComplyEA — Regulatory Compliance for East African Law Firms
**Subtitle:** Purpose-built compliance management · Uganda & East Africa
**Purpose:** Product explainer page for ComplyEA — shared directly with law firm
prospects who have been given the URL.
**Audience:** Managing partners, compliance directors, and company secretaries at
East African law firms evaluating ComplyEA.
**Date:** 2026-04-02
**Tags:** complyea, compliance, legal-tech, uganda, east-africa
**Tone:** Confident and direct. First person where appropriate. Specific about what
the product does and doesn't do. No startup-speak. Treats the reader as a
professional who has heard too many software pitches.

---

## Content

### Opening (before any headings)

ComplyEA automates the regulatory compliance lifecycle for East African law firms —
from tracking statutory obligations to delivering the right reminder to the right
person, on time, without anyone chasing anyone.

It was built because a shared compliance spreadsheet is a productivity tool for one
person and a consumption tool for everyone else.

### The Problem

Compliance officers at Ugandan law firms are skilled legal professionals. They
should not be spending their afternoons calculating due dates, composing reminder
emails by hand, and chasing company secretaries for confirmation. That work is
mechanical. ComplyEA handles it.

The specific failure modes this replaces:

- Deadlines tracked in a spreadsheet owned by one person, invisible to everyone else
- Reminder emails sent manually, with no audit trail of who was notified when
- New client onboarding multiplies the manual burden with no parallel efficiency gain
- When a deadline is missed, nobody can prove who was responsible for the reminder
- No visibility into portfolio-wide compliance status without producing a manual report

### How It Works

Four steps from obligation to completion:

**Load Your Regulations** — ComplyEA comes pre-loaded with Uganda's Companies Act
2012 and applicable East African legislation. You apply relevant acts to each client
company once, during setup.

**Generate Obligations** — With one action, the system generates every compliance
obligation for the period: Annual Returns, AGMs, quarterly filings, director change
notifications — with precise due dates calculated per client.

**Automated Reminders** — Tiered reminders go out automatically at 30, 14, 7, 3,
and 1 day before each deadline, to the right contact at the client company, via email.
If a reminder is not acknowledged, it escalates to a senior contact automatically.
No one picks up the phone.

**Track and Close** — Compliance officers update obligation status as work progresses.
The dashboard shows exactly what is overdue, what is upcoming, and what is completed
across all clients — at a glance, not after producing a report.

### What It Does

Full feature set:

**Automated Reminders and Escalations** — Tiered at 30, 14, 7, 3, and 1 day.
Unacknowledged reminders escalate automatically.

**Multi-Client Portfolio Management** — All client companies from one dashboard.
Filter by company, regulation, status, or deadline. Assign obligations to named
contacts.

**Obligation Lifecycle Tracking** — Every obligation moves through a defined workflow:
Pending → In Progress → Submitted → Completed. Overdue items surface automatically.

**Role-Based Access** — Compliance officers get full access. Client representatives
get a read-only view of their own obligations only. No cross-client data exposure.

**Calendar and Email Integration** — Reminders send via existing Gmail or Outlook
accounts. Deadlines push to Google Calendar or Outlook Calendar.

**Uganda Regulatory Framework Built In** — Uganda Companies Act 2012 pre-loaded,
including Annual Returns, AGMs, director changes, and beneficial ownership reporting.
Additional acts can be added.

### Deployment Options

ComplyEA is available in three configurations depending on firm size and infrastructure:

**Hosted** — Deployed on your own Windows Server or virtual machine. Your data,
your infrastructure. No cloud subscription.

**Shared** — Multi-firm deployment managed by the provider, with full data isolation
between firms.

**Standalone** — Single-firm, single-machine deployment for smaller practices.

### Who It's For

Law firms managing compliance for multiple corporate clients, from boutique practices
to multi-partner firms. In-house legal departments at corporate and government
organisations managing a high volume of obligations internally. Compliance and
governance officers who need an auditable record for board reporting and regulatory
submissions.

If you are managing compliance for more than three client companies and still using
a spreadsheet, you have already outgrown the spreadsheet.

### Contact and Next Steps

ComplyEA is not available for self-service sign-up. Deployment involves a setup
session to configure your regulatory framework, import your client list, and brief
your compliance officers. It takes less than a day.

To arrange a demonstration or discuss deployment, reach out directly.

---

## Image Manifest

No raster images. The dashboard mockup below serves as the visual element.

## Dashboard Mockup

Embed the following raw HTML block in the Markdown body, immediately after the
"How It Works" section and before "What It Does". This is a CSS-drawn app window
showing the compliance dashboard. All styles use inline CSS and brand variables —
no external dependencies, no JavaScript.

```html
<div class="complyea-mock">
  <div class="mock-bar">
    <span class="mock-dot" style="background:#e05050"></span>
    <span class="mock-dot" style="background:#e0b030"></span>
    <span class="mock-dot" style="background:#50b050"></span>
    <span class="mock-label">ComplyEA — Compliance Dashboard</span>
  </div>
  <div class="mock-body">
    <nav class="mock-nav">
      <span class="mock-nav-group">Organisation</span>
      <span class="mock-nav-item">Legal Firms</span>
      <span class="mock-nav-item">Companies</span>
      <span class="mock-nav-group">Compliance</span>
      <span class="mock-nav-item mock-nav-active">Obligations</span>
      <span class="mock-nav-item">Reminders</span>
      <span class="mock-nav-item">Documents</span>
      <span class="mock-nav-group">Regulatory</span>
      <span class="mock-nav-item">Acts</span>
      <span class="mock-nav-item">Requirements</span>
    </nav>
    <div class="mock-main">
      <div class="mock-header">
        <span class="mock-title">Overdue Obligations — All Clients</span>
        <span class="mock-btn">Generate Reminders</span>
      </div>
      <div class="mock-grid">
        <div class="mock-row mock-row-head">
          <span>Obligation</span><span>Company</span>
          <span>Due Date</span><span>Status</span>
        </div>
        <div class="mock-row">
          <span>Annual Return Filing</span>
          <span>ACME Corporation</span>
          <span class="mock-date-over">31 Dec 2024</span>
          <span class="mock-pill mock-over">● Overdue</span>
        </div>
        <div class="mock-row">
          <span>AGM — Q4</span>
          <span>Beta Finance Ltd</span>
          <span class="mock-date-soon">28 Feb 2025</span>
          <span class="mock-pill mock-soon">● Due Soon</span>
        </div>
        <div class="mock-row">
          <span>Director Change Notice</span>
          <span>ACME Corporation</span>
          <span>15 Mar 2025</span>
          <span class="mock-pill mock-prog">● In Progress</span>
        </div>
        <div class="mock-row">
          <span>Quarterly Board Meeting</span>
          <span>Beta Finance Ltd</span>
          <span>31 Mar 2025</span>
          <span class="mock-pill mock-done">● Completed</span>
        </div>
      </div>
    </div>
  </div>
</div>
```

Add the following CSS classes to the article layout's `<style>` block:

```css
/* ── ComplyEA Dashboard Mockup ── */
.complyea-mock {
  background: var(--color-bg-dark);
  border-radius: 8px 8px 0 0;
  overflow: hidden;
  margin: 2rem 0;
  box-shadow: 0 16px 48px rgba(0,0,0,0.35);
  font-family: var(--font-mono);
  font-size: 0.78rem;
}
.mock-bar {
  background: rgba(255,255,255,0.06);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 6px;
  border-bottom: 1px solid rgba(196,122,34,0.2);
}
.mock-dot {
  width: 10px; height: 10px;
  border-radius: 50%; display: inline-block;
}
.mock-label {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: rgba(214,205,184,0.45);
  letter-spacing: 0.04em;
  margin-left: 8px;
}
.mock-body { display: flex; min-height: 230px; }
.mock-nav {
  width: 160px; flex-shrink: 0;
  background: rgba(0,0,0,0.2);
  padding: 14px 0;
  border-right: 1px solid rgba(196,122,34,0.12);
  display: flex; flex-direction: column;
}
.mock-nav-group {
  padding: 8px 14px 3px;
  font-size: 0.62rem; letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(196,122,34,0.5);
}
.mock-nav-item {
  padding: 5px 18px;
  font-size: 0.72rem;
  color: rgba(214,205,184,0.5);
  border-left: 2px solid transparent;
}
.mock-nav-active {
  color: var(--color-text-inv);
  background: rgba(196,122,34,0.1);
  border-left-color: var(--color-accent);
}
.mock-main { flex: 1; background: var(--color-card); }
.mock-header {
  background: var(--color-bg);
  padding: 10px 16px;
  border-bottom: 1px solid rgba(69,15,0,0.12);
  display: flex; align-items: center;
  justify-content: space-between;
}
.mock-title {
  font-size: 0.78rem; font-weight: 600;
  color: var(--color-bg-dark);
  font-family: var(--font-body);
}
.mock-btn {
  background: var(--color-accent);
  color: var(--color-text-inv);
  font-family: var(--font-mono);
  font-size: 0.65rem; font-weight: 700;
  padding: 4px 10px; border-radius: 3px;
  letter-spacing: 0.04em;
}
.mock-grid { padding: 8px 16px; }
.mock-row {
  display: grid;
  grid-template-columns: 2fr 1.5fr 1fr 1fr;
  gap: 10px; padding: 7px 0;
  border-bottom: 1px solid rgba(69,15,0,0.08);
  font-size: 0.72rem; align-items: center;
  font-family: var(--font-body);
  color: var(--color-text);
}
.mock-row-head {
  font-family: var(--font-mono);
  font-size: 0.62rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: rgba(69,15,0,0.45);
  border-bottom-color: rgba(69,15,0,0.15);
}
.mock-date-over { color: #c0392b; font-weight: 600; }
.mock-date-soon { color: #e07000; font-weight: 600; }
.mock-pill {
  font-family: var(--font-mono); font-size: 0.62rem;
  font-weight: 700; padding: 2px 6px; border-radius: 3px;
  display: inline-block; white-space: nowrap;
}
.mock-over { background: rgba(192,57,43,0.12); color: #c0392b; }
.mock-soon { background: rgba(224,112,0,0.12); color: #e07000; }
.mock-prog { background: rgba(41,128,185,0.12); color: #2980b9; }
.mock-done { background: rgba(39,174,96,0.12); color: #27ae60; }
@media (max-width: 640px) {
  .mock-nav { display: none; }
  .mock-row { grid-template-columns: 1fr 1fr; font-size: 0.68rem; }
  .mock-row-head span:nth-child(n+3),
  .mock-row span:nth-child(n+3) { display: none; }
}
```

## Specific Layout Requests

- Include a product feature table after the "What It Does" section — two columns:
  Feature (left) and Description (right). Dark brown header row, alternating rows.
- Include a CTA block at the end of the page:
  - Dark brown background
  - Heading: "Arrange a demonstration"
  - Body: "ComplyEA is deployed, not purchased off a shelf. A 60-minute session covers
    your regulatory framework, your client list, and what the system will do for you
    from day one."
  - Contact line: james@billableonline.co
  - WhatsApp: +256783354036
  - Note below: WhatsApp preferred — easier to track than calls.
  - Payment note: Bank transfer, USD only.
- `toc: false` — no floating table of contents on this page.

---
---

## ↓ DO NOT EDIT BELOW THIS LINE — PROJECT CONTEXT ↓

---
---

## Project: billableonline.co Dark Pages Vault

This page is part of the `billableonline.co` dark pages vault — a Hugo static site
hosted on GitHub Pages. The scaffold is already built and deployed. You are adding
ONE new article page. Do not touch any existing file unless you are adding CSS classes
to an existing layout's `<style>` block.

### Site Architecture Summary

- **Generator:** Hugo (extended, latest version)
- **Theme:** `hugo-profile` — loaded as a git submodule but all homepage, nav, and
  layout templates are overridden by files in `layouts/`
- **Host:** GitHub Pages, branch `gh-pages`, auto-deployed via GitHub Actions
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → GitHub Actions builds → deploys in ~60s
- **Philosophy:** No navigation. No sitemap. No RSS. No discoverability. Pages are
  shared by URL only.

### Content Structure

Pages are Hugo leaf bundles:

```
content/pages/[slug]/
├── index.md        ← page content + frontmatter
└── (images if any, as page resources)
```

### Brand Tokens

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

Google Fonts loaded globally — do not add `<link>` tags inside layout files:
- Playfair Display (700)
- Source Sans 3 (400, 600)
- JetBrains Mono (400)

### Global Behaviours Already in Place

- `noindex, nofollow` injected on every page via `layouts/partials/head.html`
- `robots.txt` has `Disallow: /`
- No analytics, no tracking scripts, no third-party embeds
- Navbar and footer suppressed via CSS in `brand.css`

---

## What to Build

### 1. `content/pages/complyea/index.md`

Frontmatter:

```yaml
---
title: "ComplyEA — Regulatory Compliance for East African Law Firms"
date: 2026-04-02
draft: false
layout: "article"
description: "ComplyEA automates statutory compliance for East African law firms — automated reminders, multi-client tracking, Uganda regulatory framework built in."
slug: "complyea"
noindex: true
subtitle: "Purpose-built compliance management · Uganda & East Africa"
toc: false
tags: [complyea, compliance, legal-tech, uganda, east-africa]
---
```

Write the full article body in Markdown using the Content section above.
Voice: direct, professional, no hyperbole. Treat the reader as a sceptical buyer
who has seen too many software demos.

### 2. `layouts/pages/article.html`

Check if this file already exists in the project. **If it exists, do not recreate it.**
Only add CSS classes needed for this page (feature table, CTA block) to the existing
`<style>` block.

If creating fresh, it must satisfy:

**Structure:**
- `{{ define "main" }}` extending `layouts/_default/baseof.html`
- No navigation, no footer links, no links back to homepage
- Renders `.Content` in reading column

**Header band:**
- Dark brown full-width band
- Page title: Playfair Display, cream, large
- Subtitle: monospace, amber, 60% opacity, small

**Reading column:**
- Max width `var(--max-width)` (760px), centred
- `h2`: Playfair Display, dark brown, preceded by 28×2px amber rule
- `h3`: Source Sans 3, semibold, small uppercase monospace
- Body: Source Sans 3, 1.05rem, line-height 1.75
- `a`: `var(--color-accent)`, underline on hover only
- `code`/`pre`: JetBrains Mono, dark brown background, cream text

**Feature table** (`.feature-table` class):
- `width: 100%`, `border-collapse: collapse`
- Header row: dark brown background, cream text, monospace, uppercase, 0.78rem
- `tbody tr:nth-child(odd)`: `var(--color-bg)`
- `tbody tr:nth-child(even)`: `var(--color-card)`
- `td`: `padding: 0.5rem 0.85rem`, `font-size: 0.9rem`, `vertical-align: top`
- `td:first-child`: semibold, dark brown, `width: 35%`
- Mobile: wrap in `overflow-x: auto` div

**CTA block** (`.cta-block` class):
- Background: `var(--color-bg-dark)`
- Padding: `2rem`
- Border-radius: `4px`
- Heading: Playfair Display, cream, `1.4rem`
- Body text: cream, 90% opacity, `0.95rem`, line-height 1.7
- Contact links: `var(--color-accent)`, monospace
- Bottom note (payment/preference): cream, 70% opacity, 0.8rem, italic

**Meta footer:**
- After `.Content`, top border `2px solid rgba(69,15,0,0.15)`
- Date left (monospace, 0.78rem, muted) · Tags right (monospace, 0.78rem, amber)
- Tags rendered from `.Params.tags`, joined with ` · `

### 3. No shortcodes required for this page.

---

## Constraints (Non-Negotiable)

- No external CSS frameworks
- No JavaScript
- No analytics, tracking, or third-party scripts
- No links to homepage
- No `<form>` elements
- Vanilla CSS only — Grid and Flexbox
- All colours via CSS variables — never hardcode hex in layout files
- `noindex: true` in frontmatter always
- Check layout file before creating — do not overwrite if it exists

---

## Verification Checklist

```bash
hugo server
```

Navigate to `http://localhost:1313/complyea/` and verify:

- [ ] Header band: title and subtitle render correctly
- [ ] Feature table: dark header row, alternating rows
- [ ] CTA block: dark brown, amber contact links
- [ ] Meta footer: date left, tags right
- [ ] Page reads cleanly on 375px viewport
- [ ] `hugo --minify` — zero errors, zero warnings

---

## Deployment

```bash
git add content/pages/complyea/ layouts/
git commit -m "Add article: ComplyEA product page"
git push origin main
```

Page live at: `https://billableonline.co/complyea/`
