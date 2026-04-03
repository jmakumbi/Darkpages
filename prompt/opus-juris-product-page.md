# Opus Juris — Product Page Build
## billableonline.co Dark Pages Vault

---

## How to Use This Prompt

Drop this file into a Claude Code session. Fill in nothing — the content below is
complete. Build the page, verify locally, then push.

---

## Page Brief

**Page type:** article
**Slug:** `opus-juris`
**Title:** Opus Juris — Legal Intelligence Platform
**Subtitle:** AI-powered document search and contract intelligence · On-premise · Uganda & East Africa
**Purpose:** Product explainer for Opus Juris — the on-premise AI legal research and
document intelligence platform. Shared with law firm partners and legal directors
evaluating AI tools that comply with Uganda's data protection requirements.
**Audience:** Managing partners, legal directors, senior associates, and IT managers
at East African law firms who are curious about AI but concerned about data
sovereignty.
**Date:** 2026-04-02
**Tags:** opus-juris, legal-ai, document-intelligence, uganda, data-sovereignty
**Tone:** Precise and credible. The reader is a lawyer — they will notice vagueness
and punish it. Be specific about what the AI does, where the data goes (nowhere),
and what problems it actually solves. No AI buzzwords without explanation.

---

## Content

### Opening (before any headings)

Opus Juris lets legal teams search, analyse, and have conversations with their
documents and contracts using AI — with everything processed on their own infrastructure,
not on someone else's servers.

It was built specifically because Uganda's Data Protection and Privacy Act 2019
makes sending confidential client data to overseas cloud services a legal liability,
not just a privacy concern.

### The Problem

Ugandan law firms and corporate legal departments carry a specific burden that
international legal AI tools make worse, not better.

**Documents you cannot find** — Locating a specific clause across hundreds of files
takes hours. Searches through shared drives and email chains yield incomplete results
and wasted billable time. You know the contract exists. You cannot find the paragraph.

**Contracts that expire unnoticed** — Key renewal dates, milestone obligations, and
compliance deadlines get missed when contract management is done through calendar
reminders and personal memory. The contract was signed. Nobody set the renewal alert.

**Demand letters demanding hours** — Every demand letter requires either drafting
from scratch or spending time locating a relevant precedent. Associate time consumed
on mechanical work that should take minutes.

**Cloud tools you cannot legally use** — International legal AI software sends your
confidential client data to servers in jurisdictions your clients have not consented
to. Under Uganda's Data Protection and Privacy Act 2019, and under your professional
duty of confidentiality, this is not a philosophical concern — it is a compliance
exposure.

Opus Juris is built for this specific situation: the benefit of AI document
intelligence, without the data sovereignty problem.

### Platform Capabilities

Six modules. Each works independently and becomes more powerful in combination.

**Document Search** — Hybrid search combining traditional keyword matching with AI
semantic understanding. Ask in plain English or search for exact text across your
entire document library simultaneously. The search understands Ugandan legal
terminology and East African contract conventions. "Termination for cause" finds
relevant clauses even when those exact words are not used.

- Instant results across PDFs, Word documents, and scanned files
- Filter by document type, date range, matter, or client
- Relevance scoring surfaces the most applicable results first

**AI Conversations** — Ask questions about your documents in plain English and
receive answers with citations to the specific clauses and files they come from.
"What are the termination clauses in our lease agreements?" returns a synthesised
answer with source references — not a list of files for you to open yourself.

**Contract Management** — Track renewal dates, milestone obligations, and key terms
across your contract portfolio. The system flags upcoming deadlines without anyone
having to maintain a separate spreadsheet.

**Smart Mailroom** — Incoming documents — letters before action, court filings,
regulatory notices — are classified, dated, and routed automatically. Nothing gets
buried.

**Precedent Vault** — Your firm's approved precedents, organised and searchable.
A new associate finds the right template in two minutes instead of asking a partner.

**First Draft Engine** — Generate first-draft demand letters, standard agreements,
and routine correspondence from document context and a short instruction. Not a
finished product — a working draft that needs a lawyer's eye, not a blank page.

### How the AI Works

All AI inference runs locally on your server. Your documents are indexed on your
hardware, processed by models running on your hardware, and never transmitted
externally.

The system uses a hybrid retrieval approach:

1. Your documents are indexed when uploaded — text extracted, meaning encoded
2. A query triggers both keyword and semantic search simultaneously
3. Results are ranked by relevance and returned with source citations
4. For AI conversations, the model reads the retrieved passages and synthesises
   an answer — it does not hallucinate unsourced claims

The AI is a research and drafting assistant. Every output cites its sources. A lawyer
reviews the output. That is the intended workflow.

### Data Sovereignty

Opus Juris is explicitly designed for the legal environment in Uganda and East Africa:

**On-premise processing** — All AI models run on your own server. No document content,
no query, no result is transmitted to any external service.

**Uganda Data Protection and Privacy Act 2019** — On-premise deployment means you
are not transferring personal data outside your control. Compliance is architectural,
not contractual.

**Duty of confidentiality** — Client documents do not leave your infrastructure.
You can answer a client who asks where their data goes: it stays on your servers.

**No vendor access** — The vendor does not have access to your documents, your
queries, or your results. There is nothing to request and nothing to breach.

### Technical Requirements

Opus Juris runs on Windows Server. Minimum hardware depends on document library size
and concurrent user load. Typical law firm deployments run on a mid-range server
already used for other workloads. A full hardware specification is provided during
the scoping conversation.

### Who It's For

**Law firms** where associates spend significant time on document search, contract
review, and routine drafting — and where partners have concerns about where AI
systems send client data.

**In-house legal teams** at large corporates and government organisations with
substantial document archives and an interest in making them searchable and usable.

**Legal departments under regulatory scrutiny** who need to demonstrate that their
document handling practices comply with Uganda's data protection framework.

---

## Image Manifest

No raster images. The document search mockup below serves as the visual element.

## Document Search Mockup

Embed the following raw HTML block in the Markdown body, immediately after the
opening paragraph (before "The Problem"). This is a CSS-only app window showing
the Opus Juris document intelligence interface. No JavaScript.

```html
<div class="oj-window">
  <div class="oj-titlebar">
    <span class="oj-dot" style="background:#e05050"></span>
    <span class="oj-dot" style="background:#e0b030"></span>
    <span class="oj-dot" style="background:#50b050"></span>
    <span class="oj-title">Opus Juris — Document Intelligence</span>
  </div>
  <div class="oj-body">
    <div class="oj-search">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
      <span class="oj-query">What are the <mark class="oj-mark">termination clauses</mark> in our lease agreements?</span>
    </div>
    <div class="oj-result oj-result-top">
      <div class="oj-result-header">
        <span class="oj-doc">AF Mpanga — Lease Agreement 2024.pdf</span>
        <span class="oj-score">97% match</span>
      </div>
      <p class="oj-excerpt">…either party may terminate this agreement with <mark class="oj-mark">90 days written notice</mark> provided that the grounds for termination are specified in the notice and include material breach…</p>
    </div>
    <div class="oj-result">
      <div class="oj-result-header">
        <span class="oj-doc">Commercial Lease — Kampala Rd 2023.pdf</span>
        <span class="oj-score">88% match</span>
      </div>
      <p class="oj-excerpt">…<mark class="oj-mark">immediate termination</mark> is permitted where a party is adjudged bankrupt or enters into receivership under Ugandan insolvency law Section 14(2)…</p>
    </div>
    <div class="oj-ai">
      <div class="oj-ai-label">✦ AI Summary</div>
      <p class="oj-ai-text">Across your lease agreements, two termination mechanisms appear: standard notice (90 days) and immediate termination for insolvency events. Your 2024 agreement requires written grounds; the 2023 agreement does not.</p>
      <p class="oj-ai-cite">↳ Sources cited: 2 documents · 4 clauses referenced</p>
    </div>
  </div>
</div>
```

Add the following CSS classes to the article layout's `<style>` block:

```css
/* ── Opus Juris Document Search Mockup ── */
.oj-window {
  background: var(--color-bg-dark);
  border: 1px solid rgba(196,122,34,0.2);
  border-radius: 8px;
  overflow: hidden;
  margin: 2rem 0;
  box-shadow: 0 20px 56px rgba(0,0,0,0.4);
}
.oj-titlebar {
  background: rgba(0,0,0,0.25);
  padding: 10px 14px;
  display: flex; align-items: center; gap: 6px;
  border-bottom: 1px solid rgba(196,122,34,0.12);
}
.oj-dot {
  width: 10px; height: 10px;
  border-radius: 50%; display: inline-block;
}
.oj-title {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: rgba(214,205,184,0.4);
  margin-left: 8px; letter-spacing: 0.04em;
}
.oj-body { padding: 16px; display: flex; flex-direction: column; gap: 10px; }
.oj-search {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(196,122,34,0.2);
  border-radius: 6px;
  padding: 9px 12px;
  display: flex; align-items: center; gap: 10px;
  color: rgba(214,205,184,0.45);
}
.oj-query {
  font-family: var(--font-body);
  font-size: 0.82rem;
  color: rgba(214,205,184,0.75);
}
.oj-mark {
  background: transparent;
  color: var(--color-accent);
  font-weight: 600; font-style: normal;
}
.oj-result {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 6px; padding: 10px 12px;
}
.oj-result-top { border-color: rgba(196,122,34,0.25); }
.oj-result-header {
  display: flex; justify-content: space-between;
  align-items: center; margin-bottom: 5px;
}
.oj-doc {
  font-family: var(--font-mono);
  font-size: 0.68rem; font-weight: 700;
  color: var(--color-text-inv); opacity: 0.8;
}
.oj-score {
  font-family: var(--font-mono);
  font-size: 0.65rem; font-weight: 700;
  color: var(--color-accent);
}
.oj-excerpt {
  font-size: 0.78rem; line-height: 1.55;
  color: rgba(214,205,184,0.55);
  margin: 0;
  font-style: italic;
}
.oj-ai {
  background: rgba(196,122,34,0.07);
  border: 1px solid rgba(196,122,34,0.18);
  border-radius: 6px; padding: 10px 12px;
}
.oj-ai-label {
  font-family: var(--font-mono);
  font-size: 0.68rem; font-weight: 700;
  color: var(--color-accent);
  letter-spacing: 0.06em;
  margin-bottom: 6px;
}
.oj-ai-text {
  font-size: 0.8rem; line-height: 1.55;
  color: rgba(214,205,184,0.8); margin: 0 0 5px;
}
.oj-ai-cite {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: rgba(196,122,34,0.6); margin: 0;
}
```

## Specific Layout Requests

- Include a data sovereignty callout block after the "Data Sovereignty" section using
  the `.callout` class:
  "Opus Juris processes all data locally. No document content is transmitted to any
  external server, cloud service, or AI provider. This is not a privacy policy
  statement — it is an architectural fact."
  Style this as a slightly more prominent callout: amber left border, but also a
  subtle amber tint to the background (e.g. `rgba(196,122,34,0.07)` rather than
  `--color-card`). Add a class `.callout-highlight` for this variant.

- Include a module summary table after "Platform Capabilities": Module (left),
  What It Does (right).

- Include a CTA block at the end:
  - Heading: "Arrange a technical demonstration"
  - Body: "The demonstration covers live document search, AI conversations with actual
    sample contracts, and the on-premise architecture. Bring your own documents if
    you want to see how the system handles your specific content."
  - Contact: james@billableonline.co
  - WhatsApp: +256783354036 (preferred)
  - Payment: Bank transfer, USD only.

- `toc: false`

---
---

## ↓ DO NOT EDIT BELOW THIS LINE — PROJECT CONTEXT ↓

---
---

## Project: billableonline.co Dark Pages Vault

This page is part of the `billableonline.co` dark pages vault — Hugo static site on
GitHub Pages. Scaffold already built and deployed. Adding ONE new article page.
Do not touch existing files unless adding CSS to an existing layout's `<style>` block.

### Site Architecture Summary

- **Generator:** Hugo (extended, latest version)
- **Theme:** `hugo-profile` submodule, all nav/homepage overridden
- **Host:** GitHub Pages, `gh-pages` branch
- **Domain:** `billableonline.co`
- **Deployment:** Push to `main` → GitHub Actions → ~60s

### Content Structure

Hugo leaf bundles:

```
content/pages/opus-juris/
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

Do not add `<link>` font tags — loaded in `layouts/partials/head.html`:
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

### 1. `content/pages/opus-juris/index.md`

Frontmatter:

```yaml
---
title: "Opus Juris — Legal Intelligence Platform"
date: 2026-04-02
draft: false
layout: "article"
description: "Opus Juris brings AI document search, contract intelligence, and legal drafting assistance to East African law firms — fully on-premise, no cloud dependency."
slug: "opus-juris"
noindex: true
subtitle: "AI-powered document search and contract intelligence · On-premise · Uganda & East Africa"
toc: false
tags: [opus-juris, legal-ai, document-intelligence, uganda, data-sovereignty]
---
```

### 2. `layouts/pages/article.html`

Check if this file already exists. **Do not recreate if it exists.**
Add only the new CSS classes below to the existing `<style>` block.

New CSS classes needed:

**Highlighted callout** (`.callout-highlight`):
- Same structure as `.callout` (amber left border, border-radius `0 4px 4px 0`)
- Background: `rgba(196,122,34,0.07)` instead of `var(--color-card)`
- `border-left-width: 4px` (slightly thicker than standard callout)
- `font-style: italic`
- `font-size: 0.95rem`

**Feature table** (`.feature-table`) — if not already present.
**CTA block** (`.cta-block`) — if not already present.

### 3. No shortcodes required for this page.

---

## Constraints (Non-Negotiable)

- No external CSS frameworks
- No JavaScript
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

Navigate to `http://localhost:1313/opus-juris/` and verify:

- [ ] Header band: title and subtitle correct
- [ ] Callout highlight: amber background tint, italic text
- [ ] Module table: dark header, alternating rows
- [ ] CTA block: dark brown, amber contact links
- [ ] Clean at 375px
- [ ] `hugo --minify` — zero errors, zero warnings

---

## Deployment

```bash
git add content/pages/opus-juris/ layouts/
git commit -m "Add article: Opus Juris product page"
git push origin main
```

Page live at: `https://billableonline.co/opus-juris/`
