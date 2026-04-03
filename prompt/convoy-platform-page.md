# CONVOY — Platform Showcase Page Build
## billableonline.co Dark Pages Vault

---

## How to Use This Prompt

Drop this file into a Claude Code session. Fill in nothing — the content below is
complete. Build the page, verify locally, then push.

---

## Page Brief

**Page type:** article
**Slug:** `convoy`
**Title:** CONVOY — Collaborative Freight Intelligence for East Africa
**Subtitle:** Multi-party shipment coordination · Built for the Kampala–Mombasa corridor
**Purpose:** Platform showcase page for CONVOY — the collaborative freight forwarding
system. Shared with freight forwarders, transport operators, and logistics investors
evaluating the platform.
**Audience:** Freight forwarding business owners, logistics operations managers,
transport operators, and clearing agents across Uganda and East Africa.
**Date:** 2026-04-02
**Tags:** convoy, freight, logistics, east-africa, uganda, transport
**Tone:** Operational and direct. The reader moves cargo for a living — they know what
the coordination problem costs them. No startup mythology. Specific about what the
platform does and how multi-party workflows actually function.

---

## Content

### Opening (before any headings)

CONVOY connects freight forwarders, transport operators, clearing agents, and warehouse
providers on one coordinated platform — without forcing any party to surrender their
independence or their existing client relationships.

A single Kampala–Mombasa shipment touches four to six independent operators. Today,
they coordinate by WhatsApp, phone calls, and spreadsheets. CONVOY replaces that.

### The Problem

Freight in East Africa is fragmented by design — multiple specialist operators, each
excellent at their piece of the chain. The coordination layer is the weak point.

Specific failures that happen every week on East African freight corridors:

- **No shared visibility** — each party operates in isolation. Delays surface only
  when it is too late to act.
- **Billing disputes** — without centralised records, multi-party cost reconciliation
  becomes a post-trip argument over WhatsApp screenshots.
- **Compliance gaps** — URA customs requirements and FIATA documentation are managed
  manually, creating audit exposure and costly errors.
- **No P&L intelligence** — profit visibility per shipment is impossible when expenses
  and revenues sit in separate systems at separate companies.

### How CONVOY Coordinates a Shipment

A CONVOY shipment has one hub and multiple parties. Each party sees only their tasks
and their data. The hub — typically the freight forwarder — has full visibility.

Example: a Kampala–Mombasa export shipment:

- **Freight Forwarder** — coordinates the full shipment, bills the client, owns the
  P&L
- **Transport Operator** — trucks, drivers, trip tracking
- **Clearing Agent** — URA declarations, HS codes, duty calculation
- **Warehouse Provider** — storage, handling, cargo release

Each party operates independently. CONVOY gives the freight forwarder visibility
across all four without any party having to report to another.

### Platform Modules

Seven modules in one coordinated system:

**Party Management** — Onboarding, contacts, service capabilities, TIN and compliance
tracking for all six party types: Forwarder, Transport, Clearing, Warehouse,
Individual, Company. Thirty-plus profile fields across contact, capabilities, fleet,
and financial regions. TIN indexed for URA compliance.

**Shipment Management** — Multi-party workflows, task assignment, lifecycle tracking
from booking to delivery. Every party gets their task view; the forwarder gets the
full picture.

**Fleet Management** — Vehicles, drivers, trip planning, GPS waypoint tracking,
journey management for transport operators.

**Customs** — URA integration, HS code management, automated calculation of duty,
VAT, and infrastructure levy. Reduces manual customs errors.

**Document Management** — File upload, classification, and optional AI-powered data
extraction from cargo documents such as bills of lading and packing lists.

**Financial** — Multi-currency expense tracking, invoicing, and real-time profit and
loss per shipment. Supports UGX, USD, KES, TZS, and EUR.

**Reporting** — Standard operational and financial reports across all modules.

### What CONVOY Tracks

Platform scope by the numbers:

- Six party types supported
- Seven core modules
- Thirty-plus party profile fields
- Five currencies: UGX, USD, KES, TZS, EUR
- Standard reports across all modules
- URA customs integration for Uganda-origin shipments

### Current Status

Phase 1 is complete. The core shipment coordination, party management, financial, and
customs modules are built and tested. Phase 2 covers additional corridor coverage,
mobile client views for transport operators, and expanded document intelligence.

### Who It's For

**Freight forwarders** who coordinate multi-party shipments and need end-to-end
visibility without managing four separate WhatsApp groups.

**Transport operators** who want a proper job management and trip tracking system
rather than verbal handoffs.

**Clearing agents** who need a structured way to manage URA declarations across
multiple forwarder clients.

**Warehouse providers** whose current role in a shipment is invisible to everyone
until something goes wrong.

### Contact

CONVOY is deployed, not licensed off a shelf. Deployment involves configuring your
party structure, your corridor coverage, and integrating with your existing billing
workflow. To discuss a deployment or request a walkthrough of the platform:

---

## Image Manifest

No raster images. The coordination diagram below serves as the visual element.

## Multi-Party Coordination Diagram

Embed the following raw HTML block in the Markdown body, immediately after the
"How CONVOY Coordinates a Shipment" section (before "Platform Modules"). This is a
CSS-only diagram showing the CONVOY hub and four party types. No JavaScript.

```html
<div class="convoy-diagram">
  <div class="convoy-hub">
    <div class="convoy-hub-label">CONVOY</div>
    <div class="convoy-hub-sub">SHIPMENT HUB</div>
    <div class="convoy-hub-ref">CNV/EXP-202601001</div>
  </div>
  <div class="convoy-parties">
    <div class="convoy-party">
      <div class="convoy-party-role">Freight Forwarder</div>
      <div class="convoy-party-name">ABC Freight Ltd</div>
      <div class="convoy-party-desc">Coordinates · Bills client · P&L owner</div>
    </div>
    <div class="convoy-party">
      <div class="convoy-party-role">Transport Operator</div>
      <div class="convoy-party-name">XYZ Transport</div>
      <div class="convoy-party-desc">Trucks · Drivers · Trip tracking</div>
    </div>
    <div class="convoy-party">
      <div class="convoy-party-role">Clearing Agent</div>
      <div class="convoy-party-name">Quick Clear Agents</div>
      <div class="convoy-party-desc">URA declarations · HS codes · Duty</div>
    </div>
    <div class="convoy-party">
      <div class="convoy-party-role">Warehouse Provider</div>
      <div class="convoy-party-name">SafeStore Uganda</div>
      <div class="convoy-party-desc">Storage · Handling · Release</div>
    </div>
  </div>
  <p class="convoy-note">Each party sees only their tasks. Independent. Collaborative.</p>
</div>
```

Add the following CSS classes to the article layout's `<style>` block:

```css
/* ── CONVOY Coordination Diagram ── */
.convoy-diagram {
  margin: 2rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
.convoy-hub {
  background: var(--color-bg-dark);
  border: 2px solid var(--color-accent);
  border-radius: 4px;
  padding: 1rem 2rem;
  text-align: center;
  min-width: 200px;
}
.convoy-hub-label {
  font-family: var(--font-mono);
  font-size: 1rem; font-weight: 700;
  color: var(--color-accent);
  letter-spacing: 0.15em;
}
.convoy-hub-sub {
  font-family: var(--font-mono);
  font-size: 0.62rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.12em;
  color: rgba(214,205,184,0.5);
  margin-top: 0.15rem;
}
.convoy-hub-ref {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: rgba(214,205,184,0.35);
  margin-top: 0.4rem;
}
.convoy-parties {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
  width: 100%;
  max-width: 560px;
}
.convoy-party {
  background: var(--color-card);
  border: 1px solid rgba(69,15,0,0.12);
  border-left: 3px solid var(--color-accent);
  border-radius: 0 4px 4px 0;
  padding: 0.75rem 1rem;
}
.convoy-party-role {
  font-family: var(--font-mono);
  font-size: 0.62rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--color-accent);
  margin-bottom: 0.2rem;
}
.convoy-party-name {
  font-family: var(--font-body);
  font-size: 0.85rem; font-weight: 600;
  color: var(--color-bg-dark);
  margin-bottom: 0.2rem;
}
.convoy-party-desc {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: rgba(26,8,0,0.5);
}
.convoy-note {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: rgba(26,8,0,0.45);
  text-align: center;
  letter-spacing: 0.04em;
  margin: 0;
}
@media (max-width: 480px) {
  .convoy-parties { grid-template-columns: 1fr; }
}
```

## Specific Layout Requests

- Include a platform metrics row after the "What CONVOY Tracks" section — a simple
  horizontal strip of four stat tiles:
  - 6 Party Types
  - 7 Core Modules
  - 5 Currencies
  - URA Customs Integration
  Style: dark brown background tiles, amber number, cream label. Monospace numbers.
  On mobile, 2×2 grid. On desktop, single row.
  Use class `.stat-strip` for the container and `.stat-tile` for each item.

- Include the feature table after the "Platform Modules" section — Module (left),
  What It Does (right).

- Include a CTA block at the end:
  - Heading: "Request a platform walkthrough"
  - Body: "A 90-minute session covers the full shipment lifecycle, party coordination,
    and financial reconciliation. Bring a recent shipment docket — it makes the
    demonstration concrete."
  - Contact: james@billableonline.co
  - WhatsApp: +256783354036 (preferred — easier to track than calls)
  - Payment note: Bank transfer, USD only.
- `toc: false`

---
---

## ↓ DO NOT EDIT BELOW THIS LINE — PROJECT CONTEXT ↓

---
---

## Project: billableonline.co Dark Pages Vault

This page is part of the `billableonline.co` dark pages vault — a Hugo static site
hosted on GitHub Pages. The scaffold is already built and deployed. You are adding
ONE new article page. Do not touch any existing file unless adding CSS classes to an
existing layout's `<style>` block.

### Site Architecture Summary

- **Generator:** Hugo (extended, latest version)
- **Theme:** `hugo-profile` — submodule, all nav/homepage overridden
- **Host:** GitHub Pages, `gh-pages` branch, GitHub Actions deployment
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → Actions → ~60s

### Content Structure

Hugo leaf bundles:

```
content/pages/convoy/
├── index.md
```

### Brand Tokens

```css
--color-bg:       #d6cdb8;
--color-bg-dark:  #450f00;
--color-accent:   #c47a22;
--color-text:     #1a0800;
--color-text-inv: #d6cdb8;
--color-card:     #e8e2d4;

--font-heading: 'Playfair Display', Georgia, serif;
--font-body:    'Source Sans 3', system-ui, sans-serif;
--font-mono:    'JetBrains Mono', 'Courier New', monospace;

--max-width:      760px;
--max-width-wide: 1100px;
```

### Typography Already Loaded

Fonts in `layouts/partials/head.html` — do not add `<link>` tags:
- Playfair Display (700)
- Source Sans 3 (400, 600)
- JetBrains Mono (400)

### Global Behaviours Already in Place

- `noindex, nofollow` via `layouts/partials/head.html`
- `robots.txt` — `Disallow: /`
- No analytics, tracking, or third-party embeds
- Nav/footer suppressed via `brand.css`

---

## What to Build

### 1. `content/pages/convoy/index.md`

Frontmatter:

```yaml
---
title: "CONVOY — Collaborative Freight Intelligence for East Africa"
date: 2026-04-02
draft: false
layout: "article"
description: "CONVOY coordinates multi-party freight shipments across East Africa — forwarders, transport operators, clearing agents, and warehouse providers on one platform."
slug: "convoy"
noindex: true
subtitle: "Multi-party shipment coordination · Built for the Kampala–Mombasa corridor"
toc: false
tags: [convoy, freight, logistics, east-africa, uganda, transport]
---
```

### 2. `layouts/pages/article.html`

Check if this file already exists. **If it exists, do not recreate it.**
Only add new CSS classes to the existing `<style>` block.

New CSS classes needed:

**Stat strip** (`.stat-strip`):
- `display: grid`
- `grid-template-columns: repeat(2, 1fr)` mobile, `repeat(4, 1fr)` at 768px+
- `gap: 1rem`
- `margin: 1.5rem 0`

Each tile (`.stat-tile`):
- `background: var(--color-bg-dark)`
- `padding: 1rem 1.25rem`
- `border-radius: 4px`
- `text-align: center`

Stat number (`.stat-tile .stat-num`):
- `font-family: var(--font-mono)`
- `font-size: 1.6rem`
- `color: var(--color-accent)`
- `display: block`
- `line-height: 1.2`

Stat label (`.stat-tile .stat-label`):
- `font-family: var(--font-body)`
- `font-size: 0.78rem`
- `color: var(--color-text-inv)`
- `opacity: 0.75`
- `display: block`
- `margin-top: 0.25rem`

**Feature table** (`.feature-table`) — if not already in the layout.
**CTA block** (`.cta-block`) — if not already in the layout.

### 3. No shortcodes required for this page.

---

## Constraints (Non-Negotiable)

- No external CSS frameworks
- No JavaScript
- No analytics, tracking, or third-party scripts
- No homepage links
- No `<form>` elements
- Vanilla CSS only
- CSS variables only — no hardcoded hex
- `noindex: true` always
- Do not overwrite existing layout files

---

## Verification Checklist

```bash
hugo server
```

Navigate to `http://localhost:1313/convoy/` and verify:

- [ ] Header band: title and subtitle correct
- [ ] Stat strip: 4 tiles, 2-column mobile / 4-column desktop
- [ ] Feature table: dark header, alternating rows
- [ ] CTA block: dark brown, amber contact links
- [ ] Clean at 375px
- [ ] `hugo --minify` — zero errors, zero warnings

---

## Deployment

```bash
git add content/pages/convoy/ layouts/
git commit -m "Add article: CONVOY platform page"
git push origin main
```

Page live at: `https://billableonline.co/convoy/`
