# Legal Technology Portfolio — Services Page Build
## billableonline.co Dark Pages Vault

---

## How to Use This Prompt

Drop this file into a Claude Code session. Fill in nothing — the content below is
complete. Build the page, verify locally, then push.

---

## Page Brief

**Page type:** services
**Slug:** `legal-tech-portfolio`
**Title:** Legal Technology & IT Services — James S. K. Makumbi
**Subtitle:** Custom software · Hardware · Managed IT · East Africa
**Purpose:** Portfolio and credentials page for James as a freelance IT consultant —
showing the full scope of his legal technology software, hardware deployments, and
managed IT services. Shared with law firm decision-makers and procurement contacts
who want to see the full picture before a conversation.
**Audience:** Managing partners, IT directors, and operations managers at East African
law firms and corporate organisations evaluating a technology partner.
**Date:** 2026-04-02
**Tags:** portfolio, legal-tech, managed-it, hardware, east-africa, uganda
**Tone:** Authoritative and specific. This is a credentials page, not a sales deck.
First person where natural. Lists of real products and real deployments, not category
descriptions. The reader should finish the page knowing exactly what this person
builds and what he has already built.

---

## Content

### Intro (before any headings)

A single experienced partner for law firms and growing organisations across East
Africa — from custom software development through to the infrastructure it runs on
and the people who manage it day to day.

Twenty-plus years in enterprise IT. National policy advisory work. A product portfolio
built entirely for East African legal and regulatory practice. All of it available
to the same client, through the same conversation.

### Section 1: Legal Technology Software

Six enterprise platforms designed from the ground up for East African legal practice.
Self-hosted, data-sovereign, no cloud subscription required.

All platforms run on your own infrastructure — no SaaS model. Built on DevExpress XAF
enterprise architecture. Designed specifically for Uganda and EAC regulatory frameworks.
AI inference runs locally where applicable — client data does not leave your servers.

**JustiFlow ADR**
Full arbitration case management built for the Arbitration and Conciliation Act 2000
(revised 2024). Manages the complete case lifecycle, implements the ADRF cryptographic
event chain for tamper-evident record keeping, and supports multi-institution
federation for arbitration centres operating across jurisdictions.

**ComplyEA**
Statutory compliance management for Ugandan companies. Automates the full compliance
lifecycle — from tracking obligations under the Companies Act 2012 to delivering tiered
reminders at 30, 14, 7, 3, and 1 day to the right person at the right company.
Multi-client dashboard, role-based access, URSB-ready audit reporting.

**ConcordiaCLM**
Contract lifecycle management from draft to renewal. Version history with full approval
trail, milestone and deadline alerts, CGI and ICSA governance compliance. Designed
for the governance standards applicable to Ugandan legal practice.

**ARIA (HR Automation)**
HR automation for law firms. Leave management, IT onboarding checklists, firm
calendar, automated Microsoft 365 email notifications. Reduces the administrative
overhead of managing a professional services workforce.

**Opus Juris**
On-premise AI legal research and document intelligence. Hybrid search across your
entire document archive, AI-powered conversations with contracts and case files,
contract management, smart mailroom routing, precedent vault, and first-draft
generation. All AI inference runs locally — designed for compliance with Uganda's
Data Protection and Privacy Act 2019.

**NewsLens**
Legal and regulatory news intelligence. Monitors sources relevant to East African
legal practice and surfaces developments that affect your clients before your clients
ask about them.

### Section 2: Hardware and Network Security

IceWhale Zima single-board servers and Firewalla Gold Series network security
appliances — in use since launch across homelab and client deployments.

**ZimaBoard 832** — First-generation single-board server. In production use since
initial availability.

**ZimaBoard2 1664** — Second-generation, increased compute. Current homelab backbone.

**ZimaBlade 7700** — Compact NAS and compute blade. Client-site deployments.

**ZimaCube 2 Pro** — Received directly from IceWhale Technology. Lab-tested and
documented. Eight-bay NAS with internal compute — the platform that runs self-hosted
services at the level a small firm would need.

**Firewalla Gold SE** and **Firewalla Gold Plus** — Network security and monitoring
at the gateway layer. Deployed at client sites and in homelab.

These are not products on a brochure — they are devices that have been running
continuously, broken, repaired, upgraded, and documented.

### Section 3: Managed IT Services

On-call IT management and infrastructure services for organisations without in-house
IT capability. Current scope: 120-plus users under management.

**Microsoft 365 Deployment and Administration** — Tenant setup, Intune and Autopilot
device management, Exchange configuration, SharePoint and Teams governance, conditional
access and security policy administration.

**On-Call IT Management** — A named IT manager who knows your infrastructure, answers
on WhatsApp, and shows up when something breaks. For firms that cannot justify a
full-time IT headcount but need the same level of service.

**Network Design and Infrastructure** — Structured cabling, wireless access point
deployment, firewall and router configuration, VLAN segmentation, remote access setup.

**Security Audits and Business Continuity** — Penetration testing, security policy
review, backup and recovery architecture, business continuity planning. Documented
to investment-grade standards.

### Credentials

- 20+ years enterprise IT, Uganda and East Africa
- National policy leadership and government advisory roles
- Design patents in technology solutions
- Award-winning innovator
- Health and Safety certified
- Human-centred design methodology practitioner

### Contact

All enquiries by email or WhatsApp. No voice calls — WhatsApp is easier to track and
creates a record of the conversation.

---

## Image Manifest

Seven product images extracted from the source file. Copy all of these into
`content/pages/legal-tech-portfolio/` (the leaf bundle directory) before running
the build — Hugo can only process them as page resources if they are in the bundle.

```
filename: zimaboard-832.jpg
caption: ZimaBoard 832 — First-generation single-board server. In production use since initial availability.
section: Hardware and Network Security
status: In Use

filename: zimaboard2-1664.jpg
caption: ZimaBoard2 1664 — Second-generation, increased compute. Current homelab backbone.
section: Hardware and Network Security
status: In Use

filename: zimablade-7700.jpg
caption: ZimaBlade 7700 — Compact NAS and compute blade. Client-site deployments.
section: Hardware and Network Security
status: In Use

filename: zimacube-2-pro.jpg
caption: ZimaCube 2 Pro — Eight-bay NAS with internal compute. Received from IceWhale Technology. Lab-tested and documented.
section: Hardware and Network Security
status: In Use

filename: firewalla-gold-se.jpg
caption: Firewalla Gold SE — Network security and monitoring at the gateway layer. Homelab deployment.
section: Hardware and Network Security
status: In Use · Homelab

filename: firewalla-gold-plus.jpg
caption: Firewalla Gold Plus — Client-site gateway security deployment.
section: Hardware and Network Security
status: Client · Managed

filename: m365-admin-screenshot.jpg
caption: Microsoft 365 Admin Center — Service Health & Updates panel. Typical view from tenant management.
section: Managed IT Services
status: screenshot
```

**Image display:** Hardware images appear as product cards in the Hardware section.
Each card shows: product image (full width of card), status badge (amber pill,
monospace), product name (Playfair, dark brown), description (body text, small).
Use the `.hw-grid` and `.hw-card` classes defined below.

For the M365 screenshot, display it inline in the Managed IT Services section as a
full-width screenshot figure with caption.

Use Hugo image processing for all images:
```
{{ $img := .Page.Resources.GetMatch "filename.jpg" }}
{{ $webp := $img.Resize "800x webp q82" }}
{{ $jpeg := $img.Resize "800x jpg q76" }}
```

## Specific Layout Requests

This page uses the **services** layout, which does not yet exist in the project.
Build `layouts/pages/services.html` fresh.

**Additional CSS classes needed for hardware cards:**

```css
/* ── Hardware Product Cards ── */
.hw-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
}
@media (min-width: 768px) {
  .hw-grid { grid-template-columns: repeat(3, 1fr); }
}
.hw-card {
  background: var(--color-card);
  border: 1px solid rgba(69,15,0,0.1);
  border-radius: 4px;
  overflow: hidden;
}
.hw-card img {
  width: 100%; display: block;
  background: #f0ece4;
}
.hw-card-body { padding: 0.75rem 1rem; }
.hw-status {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.6rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--color-accent);
  background: var(--color-bg-dark);
  padding: 2px 6px; border-radius: 2px;
  margin-bottom: 0.4rem;
}
.hw-name {
  font-family: var(--font-heading);
  font-size: 0.9rem; font-weight: 700;
  color: var(--color-bg-dark);
  margin-bottom: 0.3rem;
  display: block;
}
.hw-desc {
  font-size: 0.78rem;
  line-height: 1.5;
  color: rgba(26,8,0,0.6);
}
/* ── M365 Screenshot ── */
.screenshot-fig {
  margin: 1.5rem 0;
  border: 1px solid rgba(69,15,0,0.12);
  border-radius: 4px;
  overflow: hidden;
}
.screenshot-fig img { width: 100%; display: block; }
.screenshot-fig figcaption {
  padding: 0.5rem 0.75rem;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: rgba(26,8,0,0.5);
  font-style: italic;
  background: var(--color-card);
}
```

**Hardware cards in the Markdown body** — write them as raw HTML in the content:
```html
<div class="hw-grid">
  <div class="hw-card">
    <picture>
      <source srcset="[webp url]" type="image/webp">
      <img src="[jpeg url]" alt="ZimaBoard 832" width="[w]" height="[h]" loading="lazy">
    </picture>
    <div class="hw-card-body">
      <span class="hw-status">In Use</span>
      <span class="hw-name">ZimaBoard 832</span>
      <p class="hw-desc">First-generation single-board server. In production use since initial availability.</p>
    </div>
  </div>
  <!-- repeat for each device -->
</div>
```

Instruct Claude Code to generate the full hardware grid with all 6 device cards
using Hugo's image pipeline from the page bundle resources.

**Layout structure:**

**Header band** — full-width dark brown band:
- Name / title: Playfair Display, cream, large (`clamp(1.8rem, 3vw, 2.6rem)`)
- Subtitle: monospace, amber, 60% opacity, small
- A single amber rule (28×2px) below the subtitle

**Reading column** — max width `var(--max-width-wide)` (1100px), centred, horizontal
padding `2rem`.

**Section headings (`h2`)** — Playfair Display, dark brown, preceded by amber rule.
Each section is a visual block — add `margin-top: 3rem` before each `h2`.

**Service card grid** (`.service-grid` class):
- `display: grid`
- `grid-template-columns: 1fr` mobile, `repeat(2, 1fr)` at 640px,
  `repeat(3, 1fr)` at 1024px
- `gap: 1.25rem`
- `margin: 1.5rem 0`

Each card (`.service-card` class):
- `background: var(--color-card)`
- `border: 1px solid rgba(69,15,0,0.12)`
- `border-radius: 4px`
- `padding: 1.25rem 1.5rem`
- Top amber rule: `display: block; width: 28px; height: 2px; background: var(--color-accent); margin-bottom: 1rem`
- Card title: Source Sans 3, 600, dark brown, `1rem`, `margin-bottom: 0.4rem`
- Card body: Source Sans 3, `0.9rem`, `1.6` line-height, muted dark

**Credentials strip** (`.credentials` class):
- A horizontal wrapped row of credential pills
- Each pill (`.credential-pill`): monospace, 0.72rem, amber text, dark brown background,
  `padding: 0.25rem 0.6rem`, `border-radius: 2px`, `letter-spacing: 0.06em`
- `display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0`

**CTA / contact block** (`.cta-block`) — same spec as article layout:
- Dark brown background, padding `2rem`, border-radius `4px`
- Heading: Playfair Display, cream, `1.4rem`
- Body: cream, 90% opacity
- Contact links: amber, monospace
- Payment note: cream, 70% opacity, italic, small

**Meta footer:**
- Top border, monospace date left, tags right (amber)

The services layout does not render `.Content` directly — the Markdown body is
rendered through `.Content` as usual, but the layout wraps it with the services grid
CSS context so that raw HTML in the Markdown (service card divs) renders correctly.
Hugo renders raw HTML in Markdown by default when `unsafe: true` is set in the
goldmark config. Add this to `config.yaml` if not already present:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

Write the index.md content so that the service cards, credentials pills, and CTA
block are written as raw HTML divs inside the Markdown body, using the CSS classes
defined in the layout. This is the correct pattern for the services layout.

- `toc: false`

---
---

## ↓ DO NOT EDIT BELOW THIS LINE — PROJECT CONTEXT ↓

---
---

## Project: billableonline.co Dark Pages Vault

This page is part of the `billableonline.co` dark pages vault — Hugo static site on
GitHub Pages. Scaffold already built and deployed. Adding ONE new services page.
The services layout does not yet exist — create it fresh.

### Site Architecture Summary

- **Generator:** Hugo (extended, latest version)
- **Theme:** `hugo-profile` submodule, all nav/homepage overridden
- **Host:** GitHub Pages, `gh-pages` branch
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → GitHub Actions → ~60s

### Content Structure

Hugo leaf bundles:

```
content/pages/legal-tech-portfolio/
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

Do not add `<link>` font tags:
- Playfair Display (700)
- Source Sans 3 (400, 600)
- JetBrains Mono (400)

### Global Behaviours Already in Place

- `noindex, nofollow` via `layouts/partials/head.html`
- `robots.txt` — `Disallow: /`
- No analytics, no tracking, no third-party embeds
- Nav/footer suppressed via `brand.css`

---

## What to Build

### 1. `content/pages/legal-tech-portfolio/index.md`

Frontmatter:

```yaml
---
title: "Legal Technology & IT Services — James S. K. Makumbi"
date: 2026-04-02
draft: false
layout: "services"
description: "Full-stack IT consultancy for East African law firms — custom legal technology software, hardware deployment, and managed IT services."
slug: "legal-tech-portfolio"
noindex: true
subtitle: "Custom software · Hardware · Managed IT · East Africa"
toc: false
tags: [portfolio, legal-tech, managed-it, hardware, east-africa, uganda]
---
```

Write the body using the Content section above. Use raw HTML divs inside the Markdown
for service card grids, credential pills, and the CTA block. The layout provides the
CSS — the Markdown provides the structure.

### 2. `layouts/pages/services.html`

Build fresh — this layout does not yet exist. Follow the layout specification in the
Specific Layout Requests section above.

Must satisfy:
- `{{ define "main" }}` extending `layouts/_default/baseof.html`
- No global navigation, no footer links
- Renders `.Content` in the services column layout context
- All CSS in a `<style>` block at the top of the `{{ define "main" }}` block

### 3. Check `config.yaml` for goldmark unsafe setting

If `markup.goldmark.renderer.unsafe: true` is not already present, add it. This
is required for raw HTML divs inside Markdown to render correctly.

### 4. No new shortcodes required for this page.

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

---

## Verification Checklist

```bash
hugo server
```

Navigate to `http://localhost:1313/legal-tech-portfolio/` and verify:

- [ ] Header band: name and subtitle correct
- [ ] Service cards: grid renders, 3 columns desktop / 1 column mobile
- [ ] Credential pills: dark brown, amber monospace text
- [ ] CTA block: dark brown, amber contact links
- [ ] All three sections visible and distinct
- [ ] Clean at 375px
- [ ] `hugo --minify` — zero errors, zero warnings

---

## Deployment

```bash
git add content/pages/legal-tech-portfolio/ layouts/pages/services.html config.yaml
git commit -m "Add services: legal technology portfolio page"
git push origin main
```

Page live at: `https://billableonline.co/legal-tech-portfolio/`
