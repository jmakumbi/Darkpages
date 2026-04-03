# JustiFlow ADR — Product Page Build
## billableonline.co Dark Pages Vault

---

## How to Use This Prompt

Drop this file into a Claude Code session. Copy `justiflow-platform-screenshot.jpg`
into `content/pages/justiflow-adr/` before running the build. Fill in nothing else —
the content below is complete.

---

## Page Brief

**Page type:** article
**Slug:** `justiflow-adr`
**Title:** JustiFlow ADR — Arbitration Case Management Platform
**Subtitle:** ADRF/1.0 · ACA 2024 compliant · CADER · ICAMEK · NCIA
**Purpose:** Product explainer for JustiFlow ADR — shared with arbitration institutions,
legal counsel, and ADR ecosystem stakeholders evaluating the platform.
**Audience:** Registrars and administrators at CADER, ICAMEK, and NCIA; arbitration
practitioners; legal counsel active in Uganda's ADR ecosystem; institutional investors
and development partners evaluating arbitration infrastructure.
**Date:** 2026-04-03
**Tags:** justiflow, arbitration, adr, legal-tech, uganda, adrf, aca-2024
**Tone:** Precise and institutional. The reader is a legal professional or institutional
administrator — they expect correct use of statutory references, proper legal
terminology, and specificity about what the platform does at each stage. Dry and
authoritative. First person is appropriate for the builder's perspective but this
is primarily a platform description, not a personal essay.

---

## Content

### Opening (before any headings)

JustiFlow ADR is a purpose-built arbitration case management platform for Uganda's
ADR ecosystem, serving CADER, ICAMEK, and NCIA. It manages the full arbitration
lifecycle under the Arbitration and Conciliation Act 2000 as revised in 2024, from
pre-arbitration notice through to enforcement.

JustiFlow is also the reference implementation of ADRF — the Arbitration Digital
Record Format — an open cryptographic event chain protocol designed for East African
arbitration institutions.

### Platform at a Glance

Four headline figures:

- **3 institutions** — CADER, ICAMEK, NCIA
- **12 lifecycle stages** — ACA 2024 compliant
- **7 user roles** — with role-based access controls
- **NYC 1958** — New York Convention enforcement pathway built in

### The ADRF Event Chain

Every action in an arbitration is recorded as a signed, linked event. Each event
references the one before it, forming an append-only chain that no party can alter.
Every participant — institution, arbitrator, counsel — holds their own verified copy
of the proceedings they were part of.

[INSERT ADRF CHAIN SVG HERE — see SVG Graphic section below]

Four events are shown in the chain illustration:

**CaseFiled** — `sha256:a3f8c2d4…` · prev: — · Stage 2 · ACA 2024 s.6 · UNCITRAL ML Art.3

The registry formally receives and records the arbitration claim. This is the first
event in the ADRF chain. A unique case reference is assigned in the format
INST-ARB-YYYY-NNN. The six-month award deadline clock begins once the tribunal is
constituted.

**TribunalConstituted** — `sha256:7d35f1c2…` · prev: a3f8c2d4… · Stage 3 · ACA 2024 s.10 · UNCITRAL ML Art.11

All arbitrators have confirmed acceptance of their appointment. This event starts
the statutory award deadline — six months under ACA 2024 s.31. Each arbitrator's
profile is recorded, including any disclosures required under the IBA Guidelines on
Conflicts of Interest 2014.

**HearingScheduled** — `sha256:e9b4a7f3…` · prev: 7d35f1c2… · Stage 7 · ACA 2024 s.20 · UNCITRAL ML Art.24

A procedural order sets the hearing date, format (in-person or remote), and venue.
This event is dispatched to all participant nodes — institution, arbitrators, counsel,
and any co-institution — and the statutory deadline is tracked and displayed
automatically.

**AwardIssued** — `sha256:f2c81d9e…` · prev: e9b4a7f3… · Stage 8 · ACA 2024 s.31 · UNCITRAL ML Art.31 · NYC 1958 Art.IV

The final award has been signed and formally issued. A cryptographic fingerprint of
the award document is recorded in the chain, making it tamper-evident. The New York
Convention 1958 enforcement pathway is now open — the award can be recognised and
enforced in any of the 172 signatory states.

### The Platform Interface

[INSERT PLATFORM SCREENSHOT HERE — see Image Manifest below]

This is what arbitrators see when they log into JustiFlow — their active matters,
the ADRF event chain tracking every proceeding action, and statutory deadlines
automatically calculated under ACA 2024.

### User Roles

JustiFlow is arbitrator-centric, not institution-centric. An arbitrator may be
appointed simultaneously across CADER, ICAMEK, and NCIA — the platform reflects
this without forcing them to manage separate logins or views.

**Arbitrator** — An independent professional who may hold simultaneous appointments
across institutions. Access covers all documents in their cases, the ability to
upload and sign award documents, full ADRF event chain visibility, and a
cross-institution case dashboard.

**Legal Counsel** — Represents a party in the proceedings. Access is automatically
limited to the cases in which they appear as counsel of record: cases where they
represent a party, public and parties-only documents, upload of pleadings and
submissions. No access to confidential documents.

**Party Representative** — An authorised agent acting on behalf of a case party.
Access is strictly limited to viewing publicly released case information: cases where
their party is involved, public documents only, read-only throughout. No upload
capability.

Additionally: Institution Registrar (full registry administration), Institution
Administrator (configuration and user management), and ADRF Node Operator
(infrastructure and federation management).

### 12-Stage Arbitration Lifecycle

[INSERT LIFECYCLE TABLE HERE — see Lifecycle Table section below]

All 12 stages are mapped to their applicable statutory authority. Ten stages are
implemented in the current release; two (Settlement & Closure and Archival &
Retention) are planned for a future release and shown accordingly.

### How the Platform is Delivered

**Online Access** — Web portal, external users. Arbitrators, legal counsel, and
party representatives access their cases through a secure web portal from any browser.
Document visibility is automatically enforced per role.

**Registry Administration** — Desktop, registry staff. Institution registrars use
a dedicated desktop application to file cases, constitute tribunals, manage fees,
process documents, and advance cases through workflow stages.

**Institutional Node** — Per institution, self-hosted. Each institution — CADER,
ICAMEK, NCIA — operates its own independent JustiFlow node. Nodes communicate over
the ADRF protocol and synchronise the event chain automatically.

### The ADRF Protocol

The Arbitration Digital Record Format (ADRF) records every proceeding action as a
cryptographically signed, permanently linked event. No party can alter the history
of a case. Each institution, arbitrator, and counsel holds their own verified copy
of the proceedings they participated in — analogous to how email works, but for
arbitration records.

ADRF is being developed as an open East African standard, initially under Uganda's
Electronic Transactions Act 2011, with planned recognition across EAC and OHADA
regions. More at adrf.africa.

Key properties: tamper-evident chain · cryptographically signed · federated nodes ·
cross-institution.

### Contact

JustiFlow ADR is deployed to institutions, not licensed individually. Deployment
involves configuring the institutional node, integrating with the existing case
registry, and training registrar staff. To discuss a deployment for your institution:

---

## Image Manifest

One raster image. Copy into `content/pages/justiflow-adr/` before building.

```
filename: justiflow-platform-screenshot.jpg
caption: JustiFlow ADR — live platform view. Active matters, ADRF event chain, and ACA 2024 statutory deadline tracker (43 days remaining shown for CADER-ARB-2025-014).
section: The Platform Interface
processing: resize 1400x webp q82 / jpeg q76
```

Render using Hugo image pipeline as a full-width screenshot figure with caption
and subtle border. Use the `.screenshot-fig` class.

---

## ADRF Chain SVG Graphic

Embed this SVG directly in the Markdown body (using raw HTML, which requires
`markup.goldmark.renderer.unsafe: true` in `config.yaml` — check before adding).
Place it immediately after the "The ADRF Event Chain" section intro paragraph,
before the four event descriptions.

The SVG uses CSS variables for colours — replace the original theme vars with brand
vars as follows when embedding:

- `var(--bg)` → `var(--color-card)`
- `var(--text)` → `var(--color-text)`
- `var(--text3)` → `rgba(26,8,0,0.4)`
- `var(--bg2)` → `rgba(214,205,184,0.4)`
- `var(--border2)` → `rgba(26,8,0,0.2)`
- `var(--font-sans)` → `'Source Sans 3', system-ui, sans-serif`
- `var(--font-mono)` → `'JetBrains Mono', monospace`
- Arrow colours `#1a6b6b` → `var(--color-accent)` (amber suits the brand better
  than teal; adjust node stroke colours accordingly)
- Amber `#c9962a` → `var(--color-accent)`

```html
<div class="adrf-chain-wrap">
<svg class="adrf-chain-svg" viewBox="0 0 680 98" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="var(--color-accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="ahd" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="rgba(26,8,0,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <line x1="108" y1="49" x2="148" y2="49" stroke="var(--color-accent)" stroke-width="1" stroke-opacity=".5" marker-end="url(#ah)"/>
  <line x1="250" y1="49" x2="290" y2="49" stroke="var(--color-accent)" stroke-width="1" stroke-opacity=".5" marker-end="url(#ah)"/>
  <line x1="392" y1="49" x2="432" y2="49" stroke="var(--color-accent)" stroke-width="1" stroke-opacity=".6" marker-end="url(#ah)"/>
  <line x1="534" y1="49" x2="570" y2="49" stroke="rgba(26,8,0,0.2)" stroke-width="1" stroke-opacity=".35" stroke-dasharray="4 3" marker-end="url(#ahd)"/>
  <g>
    <rect x="10" y="18" width="98" height="62" rx="7" fill="var(--color-card)" stroke="var(--color-accent)" stroke-width="1"/>
    <text x="59" y="40" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">CaseFiled</text>
    <text x="59" y="57" text-anchor="middle" font-size="9" fill="var(--color-accent)" font-family="'JetBrains Mono',monospace">a3f8c2d4…</text>
    <text x="59" y="70" text-anchor="middle" font-size="9" fill="rgba(26,8,0,0.4)" font-family="'JetBrains Mono',monospace">prev: —</text>
  </g>
  <g>
    <rect x="150" y="18" width="100" height="62" rx="7" fill="var(--color-card)" stroke="var(--color-accent)" stroke-width="1"/>
    <text x="200" y="37" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Tribunal</text>
    <text x="200" y="51" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Constituted</text>
    <text x="200" y="66" text-anchor="middle" font-size="9" fill="var(--color-accent)" font-family="'JetBrains Mono',monospace">7d35f1c2…</text>
  </g>
  <g>
    <rect x="292" y="18" width="100" height="62" rx="7" fill="var(--color-card)" stroke="var(--color-accent)" stroke-width="1"/>
    <text x="342" y="37" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Hearing</text>
    <text x="342" y="51" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Scheduled</text>
    <text x="342" y="66" text-anchor="middle" font-size="9" fill="var(--color-accent)" font-family="'JetBrains Mono',monospace">e9b4a7f3…</text>
  </g>
  <g>
    <rect x="434" y="18" width="100" height="62" rx="7" fill="var(--color-card)" stroke="var(--color-accent)" stroke-width="1.5"/>
    <text x="484" y="37" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Award</text>
    <text x="484" y="51" text-anchor="middle" font-size="11" font-weight="500" fill="var(--color-text)" font-family="'Source Sans 3',sans-serif">Issued</text>
    <text x="484" y="66" text-anchor="middle" font-size="9" fill="var(--color-accent)" font-family="'JetBrains Mono',monospace">f2c81d9e…</text>
  </g>
  <rect x="572" y="18" width="96" height="62" rx="7" fill="rgba(214,205,184,0.4)" stroke="rgba(26,8,0,0.2)" stroke-width="0.5" stroke-dasharray="4 3"/>
  <text x="620" y="40" text-anchor="middle" font-size="11" font-weight="500" fill="rgba(26,8,0,0.4)" font-family="'Source Sans 3',sans-serif">Case</text>
  <text x="620" y="54" text-anchor="middle" font-size="11" font-weight="500" fill="rgba(26,8,0,0.4)" font-family="'Source Sans 3',sans-serif">Closed</text>
  <text x="620" y="70" text-anchor="middle" font-size="9" fill="rgba(26,8,0,0.25)" font-family="'JetBrains Mono',monospace" opacity=".5">pending…</text>
</svg>
<p class="adrf-chain-note">Four events shown — full chain continues through all 12 lifecycle stages. Each event fingerprint links cryptographically to its predecessor.</p>
</div>
```

---

## Lifecycle Table

Render the 12 stages as a structured table in the Markdown body using raw HTML.
Place it immediately after the "12-Stage Arbitration Lifecycle" heading.

```html
<div class="lifecycle-table">
  <div class="lc-row lc-head">
    <span>Stage</span><span>Name</span><span>Legal Basis</span><span>Status</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">01</span>
    <span class="lc-name">Pre-arbitration notice</span>
    <span class="lc-law">ML Art.3 · ACA s.3</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">02</span>
    <span class="lc-name">Case filing &amp; registration</span>
    <span class="lc-law">ACA s.6</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">03</span>
    <span class="lc-name">Arbitrator appointment</span>
    <span class="lc-law">ACA s.10 · ML Art.11</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">04</span>
    <span class="lc-name">Terms of reference</span>
    <span class="lc-law">ICC Art.23</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">05</span>
    <span class="lc-name">Pleadings exchange</span>
    <span class="lc-law">ML Art.23 · ACA s.18</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">06</span>
    <span class="lc-name">Interim measures</span>
    <span class="lc-law">ML Art.17 · ACA s.14</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">07</span>
    <span class="lc-name">Hearings</span>
    <span class="lc-law">ACA s.20 · ML Art.24</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">08</span>
    <span class="lc-name">Award issuance</span>
    <span class="lc-law">ACA s.31 · ML Art.31</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">09</span>
    <span class="lc-name">Post-award applications</span>
    <span class="lc-law">ACA s.32–33</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row">
    <span class="lc-num">10</span>
    <span class="lc-name">Enforcement</span>
    <span class="lc-law">NYC 1958 · ACA Part IV</span>
    <span class="lc-done">Live</span>
  </div>
  <div class="lc-row lc-plan-row">
    <span class="lc-num">11</span>
    <span class="lc-name">Settlement &amp; closure</span>
    <span class="lc-law">ACA s.35</span>
    <span class="lc-plan">Planned</span>
  </div>
  <div class="lc-row lc-plan-row">
    <span class="lc-num">12</span>
    <span class="lc-name">Archival &amp; retention</span>
    <span class="lc-law">10yr minimum</span>
    <span class="lc-plan">Planned</span>
  </div>
</div>
```

---

## Specific Layout Requests

### config.yaml

Check `config.yaml` for `markup.goldmark.renderer.unsafe: true`. If absent, add it —
required for the SVG and lifecycle table raw HTML to render in Markdown.

### New CSS classes (add to `layouts/pages/article.html` `<style>` block)

```css
/* ── JustiFlow ADRF Chain ── */
.adrf-chain-wrap {
  margin: 1.75rem 0;
  background: var(--color-bg-dark);
  border-radius: 6px;
  padding: 1.25rem 1rem 0.75rem;
  overflow-x: auto;
}
.adrf-chain-svg {
  display: block;
  width: 100%;
  max-width: 680px;
  height: auto;
  margin: 0 auto;
  min-width: 420px;
}
.adrf-chain-note {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: rgba(214,205,184,0.4);
  text-align: center;
  margin: 0.6rem 0 0;
  letter-spacing: 0.03em;
}

/* ── Platform Screenshot ── */
.screenshot-fig {
  margin: 1.75rem 0;
  border: 1px solid rgba(69,15,0,0.12);
  border-radius: 4px;
  overflow: hidden;
}
.screenshot-fig img {
  width: 100%; display: block;
}
.screenshot-fig figcaption {
  padding: 0.5rem 0.85rem;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: rgba(26,8,0,0.5);
  font-style: italic;
  background: var(--color-card);
  border-top: 1px solid rgba(69,15,0,0.08);
}

/* ── Stat Strip ── */
.jf-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
  margin: 1.5rem 0;
}
@media (min-width: 600px) {
  .jf-stats { grid-template-columns: repeat(4, 1fr); }
}
.jf-stat {
  background: var(--color-bg-dark);
  border-radius: 4px;
  padding: 0.85rem 1rem;
  text-align: center;
}
.jf-stat-n {
  display: block;
  font-family: var(--font-mono);
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--color-accent);
  line-height: 1.1;
}
.jf-stat-l {
  display: block;
  font-family: var(--font-body);
  font-size: 0.72rem;
  color: var(--color-text-inv);
  opacity: 0.6;
  margin-top: 0.2rem;
}

/* ── Lifecycle Table ── */
.lifecycle-table {
  margin: 1.5rem 0;
  border: 1px solid rgba(69,15,0,0.1);
  border-radius: 4px;
  overflow: hidden;
  font-size: 0.82rem;
}
.lc-row {
  display: grid;
  grid-template-columns: 2.5rem 1fr 1fr 4rem;
  gap: 0;
  border-bottom: 1px solid rgba(69,15,0,0.07);
  align-items: center;
}
.lc-row:last-child { border-bottom: none; }
.lc-row > span {
  padding: 0.5rem 0.75rem;
}
.lc-head {
  background: var(--color-bg-dark);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: rgba(214,205,184,0.55);
}
.lc-row:not(.lc-head):not(.lc-plan-row):nth-child(odd) {
  background: var(--color-bg);
}
.lc-row:not(.lc-head):not(.lc-plan-row):nth-child(even) {
  background: var(--color-card);
}
.lc-plan-row { background: rgba(214,205,184,0.3); opacity: 0.65; }
.lc-num {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--color-accent);
}
.lc-name { font-weight: 500; color: var(--color-text); }
.lc-law {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: rgba(26,8,0,0.5);
}
.lc-done {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  color: #2d7a3a;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.lc-plan {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  color: rgba(26,8,0,0.35);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
@media (max-width: 600px) {
  .lc-row { grid-template-columns: 2rem 1fr 3.5rem; }
  .lc-law { display: none; }
  .lifecycle-table { font-size: 0.78rem; }
}

/* ── ADRF Protocol Tags ── */
.adrf-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin: 1rem 0;
}
.adrf-tag {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--color-accent);
  background: var(--color-bg-dark);
  padding: 0.25rem 0.6rem;
  border-radius: 2px;
  border: 1px solid rgba(196,122,34,0.3);
}
```

### Stat strip in Markdown body

Place this raw HTML block immediately after the "Platform at a Glance" heading,
before the bullet list (or instead of it):

```html
<div class="jf-stats">
  <div class="jf-stat">
    <span class="jf-stat-n">3</span>
    <span class="jf-stat-l">Institutions<br>CADER · ICAMEK · NCIA</span>
  </div>
  <div class="jf-stat">
    <span class="jf-stat-n">12</span>
    <span class="jf-stat-l">Lifecycle stages<br>ACA 2024 compliant</span>
  </div>
  <div class="jf-stat">
    <span class="jf-stat-n">7</span>
    <span class="jf-stat-l">User roles<br>with access controls</span>
  </div>
  <div class="jf-stat">
    <span class="jf-stat-n">NYC<br>1958</span>
    <span class="jf-stat-l">Enforcement pathway<br>built in</span>
  </div>
</div>
```

### ADRF protocol tag strip

Place this immediately before the Contact section:

```html
<div class="adrf-tags">
  <span class="adrf-tag">Tamper-evident chain</span>
  <span class="adrf-tag">Cryptographically signed</span>
  <span class="adrf-tag">Federated nodes</span>
  <span class="adrf-tag">Cross-institution</span>
</div>
```

### CTA block at end

```
- Heading: "Deploy JustiFlow at your institution"
- Body: "Deployment involves configuring the institutional node, integrating with
  your case registry, and a training session for registrar staff. The platform is
  already in operation at CADER. A demonstration can be arranged at your institution
  or remotely."
- Contact: james@billableonline.co
- WhatsApp: +256783354036 (preferred — trackable)
- Payment: Bank transfer, USD only.
```

- `toc: false`

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
- **Theme:** `hugo-profile` — loaded as a git submodule, all nav/homepage overridden
- **Host:** GitHub Pages, branch `gh-pages`, auto-deployed via GitHub Actions
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → GitHub Actions builds → deploys in ~60s
- **Philosophy:** No navigation. No sitemap. No RSS. URL-only access.

### Content Structure

Hugo leaf bundles:

```
content/pages/justiflow-adr/
├── index.md
└── justiflow-platform-screenshot.jpg   ← place this here before building
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

Do not add `<link>` font tags — loaded globally in `layouts/partials/head.html`:
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

### 1. `content/pages/justiflow-adr/index.md`

Frontmatter:

```yaml
---
title: "JustiFlow ADR — Arbitration Case Management Platform"
date: 2026-04-03
draft: false
layout: "article"
description: "JustiFlow ADR manages the full arbitration lifecycle under ACA 2024 for CADER, ICAMEK and NCIA — including the ADRF cryptographic event chain for tamper-evident proceedings."
slug: "justiflow-adr"
noindex: true
subtitle: "ADRF/1.0 · ACA 2024 compliant · CADER · ICAMEK · NCIA"
toc: false
tags: [justiflow, arbitration, adr, legal-tech, uganda, adrf, aca-2024]
---
```

Write the full article body using the Content section above. Include all raw HTML
blocks (stat strip, ADRF SVG, platform screenshot figure, lifecycle table, ADRF
tag strip, CTA block) at the positions specified.

For the platform screenshot, render using Hugo image pipeline:

```go
{{ $img := .Page.Resources.GetMatch "justiflow-platform-screenshot.jpg" }}
{{ if $img }}
  {{ $webp := $img.Resize "1400x webp q82" }}
  {{ $jpeg := $img.Resize "1400x jpg q76" }}
  <figure class="screenshot-fig">
    <picture>
      <source srcset="{{ $webp.RelPermalink }}" type="image/webp">
      <img src="{{ $jpeg.RelPermalink }}"
           alt="JustiFlow ADR platform interface"
           width="{{ $jpeg.Width }}" height="{{ $jpeg.Height }}"
           loading="lazy">
    </picture>
    <figcaption>JustiFlow ADR — live platform view. Active matters, ADRF event chain, and ACA 2024 statutory deadline tracker.</figcaption>
  </figure>
{{ end }}
```

Note: Hugo template syntax cannot go inside Markdown body directly. Put the
screenshot in a shortcode or write it as a raw Go template partial in the layout.
The cleanest approach is to add a `screenshot-fig` shortcode that takes the
filename and caption as parameters. Check if `layouts/shortcodes/screenshot.html`
already exists — if so, adapt; if not, create it for this purpose.

### 2. `layouts/pages/article.html`

Check if this file already exists. **Do not recreate if it exists.**
Add only the new CSS classes from the Specific Layout Requests section above to the
existing `<style>` block.

### 3. `config.yaml`

Check for `markup.goldmark.renderer.unsafe: true`. Add if absent.

---

## Constraints (Non-Negotiable)

- No external CSS frameworks
- No JavaScript (the SVG is static — remove all `onclick` handlers from original)
- No analytics, tracking, or third-party scripts
- No homepage links
- No `<form>` elements
- Vanilla CSS only
- CSS variables only — no hardcoded hex in layout files
- `noindex: true` always
- Do not overwrite existing layout files

---

## Verification Checklist

```bash
hugo server
```

Navigate to `http://localhost:1313/justiflow-adr/` and verify:

- [ ] Header band: title and subtitle correct
- [ ] Stat strip: 4 tiles render (2-col mobile, 4-col desktop)
- [ ] ADRF chain SVG: renders with brand colours, no JS errors
- [ ] Platform screenshot: loads via Hugo pipeline, lazy-loaded
- [ ] Lifecycle table: 12 rows, legal basis column, Live/Planned status
- [ ] ADRF tag strip: dark brown pills, amber text
- [ ] CTA block: dark brown, amber contact links
- [ ] Clean at 375px viewport
- [ ] `hugo --minify` — zero errors, zero warnings

---

## Deployment

```bash
git add content/pages/justiflow-adr/ layouts/
git commit -m "Add article: JustiFlow ADR product page"
git push origin main
```

Page live at: `https://billableonline.co/justiflow-adr/`
