---
title: "JustiFlow ADR — Arbitration Case Management Platform"
date: 2026-04-03
draft: false
layout: "article"
description: "JustiFlow ADR manages the full arbitration lifecycle under ACA 2024 for CADER, ICAMEK and NCIA — including the ADRF cryptographic event chain for tamper-evident proceedings."
slug: "justiflow-adr"
url: "/justiflow-adr/"
noindex: true
subtitle: "ADRF/1.0 · ACA 2024 compliant · CADER · ICAMEK · NCIA"
toc: false
tags: [justiflow, arbitration, adr, legal-tech, uganda, adrf, aca-2024]
author: "James S. K. Makumbi"
---

JustiFlow ADR is a purpose-built arbitration case management platform for Uganda's ADR ecosystem, serving CADER, ICAMEK, and NCIA. It manages the full arbitration lifecycle under the Arbitration and Conciliation Act 2000 as revised in 2024, from pre-arbitration notice through to enforcement.

JustiFlow is also the reference implementation of ADRF — the Arbitration Digital Record Format — an open cryptographic event chain protocol designed for East African arbitration institutions.

## Platform at a Glance

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

## The ADRF Event Chain

Every action in an arbitration is recorded as a signed, linked event. Each event references the one before it, forming an append-only chain that no party can alter. Every participant — institution, arbitrator, counsel — holds their own verified copy of the proceedings they were part of.

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

**CaseFiled** — `sha256:a3f8c2d4…` · prev: — · Stage 2 · ACA 2024 s.6 · UNCITRAL ML Art.3

The registry formally receives and records the arbitration claim. This is the first event in the ADRF chain. A unique case reference is assigned in the format INST-ARB-YYYY-NNN. The six-month award deadline clock begins once the tribunal is constituted.

**TribunalConstituted** — `sha256:7d35f1c2…` · prev: a3f8c2d4… · Stage 3 · ACA 2024 s.10 · UNCITRAL ML Art.11

All arbitrators have confirmed acceptance of their appointment. This event starts the statutory award deadline — six months under ACA 2024 s.31. Each arbitrator's profile is recorded, including any disclosures required under the IBA Guidelines on Conflicts of Interest 2014.

**HearingScheduled** — `sha256:e9b4a7f3…` · prev: 7d35f1c2… · Stage 7 · ACA 2024 s.20 · UNCITRAL ML Art.24

A procedural order sets the hearing date, format (in-person or remote), and venue. This event is dispatched to all participant nodes — institution, arbitrators, counsel, and any co-institution — and the statutory deadline is tracked and displayed automatically.

**AwardIssued** — `sha256:f2c81d9e…` · prev: e9b4a7f3… · Stage 8 · ACA 2024 s.31 · UNCITRAL ML Art.31 · NYC 1958 Art.IV

The final award has been signed and formally issued. A cryptographic fingerprint of the award document is recorded in the chain, making it tamper-evident. The New York Convention 1958 enforcement pathway is now open — the award can be recognised and enforced in any of the 172 signatory states.

## The Platform Interface

{{< screenshot-fig src="justiflow-platform-screenshot.jpg" alt="JustiFlow ADR platform interface" caption="JustiFlow ADR — live platform view. Active matters, ADRF event chain, and ACA 2024 statutory deadline tracker." >}}

This is what arbitrators see when they log into JustiFlow — their active matters, the ADRF event chain tracking every proceeding action, and statutory deadlines automatically calculated under ACA 2024.

## User Roles

JustiFlow is arbitrator-centric, not institution-centric. An arbitrator may be appointed simultaneously across CADER, ICAMEK, and NCIA — the platform reflects this without forcing them to manage separate logins or views.

**Arbitrator** — An independent professional who may hold simultaneous appointments across institutions. Access covers all documents in their cases, the ability to upload and sign award documents, full ADRF event chain visibility, and a cross-institution case dashboard.

**Legal Counsel** — Represents a party in the proceedings. Access is automatically limited to the cases in which they appear as counsel of record: cases where they represent a party, public and parties-only documents, upload of pleadings and submissions. No access to confidential documents.

**Party Representative** — An authorised agent acting on behalf of a case party. Access is strictly limited to viewing publicly released case information: cases where their party is involved, public documents only, read-only throughout. No upload capability.

Additionally: Institution Registrar (full registry administration), Institution Administrator (configuration and user management), and ADRF Node Operator (infrastructure and federation management).

## 12-Stage Arbitration Lifecycle

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

All 12 stages are mapped to their applicable statutory authority. Ten stages are implemented in the current release; two (Settlement & Closure and Archival & Retention) are planned for a future release and shown accordingly.

## How the Platform is Delivered

**Online Access** — Web portal, external users. Arbitrators, legal counsel, and party representatives access their cases through a secure web portal from any browser. Document visibility is automatically enforced per role.

**Registry Administration** — Desktop, registry staff. Institution registrars use a dedicated desktop application to file cases, constitute tribunals, manage fees, process documents, and advance cases through workflow stages.

**Institutional Node** — Per institution, self-hosted. Each institution — CADER, ICAMEK, NCIA — operates its own independent JustiFlow node. Nodes communicate over the ADRF protocol and synchronise the event chain automatically.

## The ADRF Protocol

The Arbitration Digital Record Format (ADRF) records every proceeding action as a cryptographically signed, permanently linked event. No party can alter the history of a case. Each institution, arbitrator, and counsel holds their own verified copy of the proceedings they participated in — analogous to how email works, but for arbitration records.

ADRF is being developed as an open East African standard, initially under Uganda's Electronic Transactions Act 2011, with planned recognition across EAC and OHADA regions. More at adrf.africa.

<div class="adrf-tags">
  <span class="adrf-tag">Tamper-evident chain</span>
  <span class="adrf-tag">Cryptographically signed</span>
  <span class="adrf-tag">Federated nodes</span>
  <span class="adrf-tag">Cross-institution</span>
</div>

## Deploy JustiFlow at your institution

Deployment involves configuring the institutional node, integrating with your case registry, and a training session for registrar staff. The platform is already in operation at CADER. A demonstration can be arranged at your institution or remotely.

Email: james@billableonline.co

WhatsApp: +256783354036

Payment: Bank transfer, USD only.
