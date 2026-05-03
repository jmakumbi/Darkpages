---
title: "ZimaBoard 2 1664 — Unboxing & First Impressions"
date: 2026-05-02
draft: false
layout: "lab-log"
description: "Unboxing the ZimaBoard 2 1664 — IceWhale Technology's successor to the ZimaBoard 832, purchased via Kickstarter. First impressions, fan installation, and a full port and processor comparison."
slug: "zimaboard-2-unboxing"
url: "/zimaboard-2-unboxing/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "IceWhale Technology · Personal Purchase via Kickstarter"
series: "zimaboard"
toc: false
tags:
  - zimaboard
  - icewhale
  - homelab
  - single-board-server
  - unboxing
  - sbc
---

The ZimaBoard 2 arrived in September last year. Birthday month — so I'm choosing to take the timing as a sign of good things to come, or at least of DHL's uncanny sense of occasion.

DHL delivered it exactly as one would expect: intact, on time, and with the sort of matter-of-fact professionalism that makes every other courier look like they're running a relay race blindfolded. I collected it from the DHL office and the box was there, exactly as it should be. No drama. That's DHL's superpower and I will not apologise for my affection.

## Arrival

{{< gallery >}}
{{< labimg src="outer-shipping-box.jpg" caption="The outer shipping box as received. Plain cardboard, DHL label, no branding. Doing exactly what a box should do." id="outer-shipping-box" >}}
{{< labimg src="outer-box-opened.jpg" caption="Outer box opened. Bubble wrap, two inner ZIMA boxes, nothing wasted." id="outer-box-opened" >}}
{{< /gallery >}}

The outer box was plain cardboard. Scuffed, taped at the seams, with a DHL sticker for identification and nothing else. No marketing. No branding. Just a box doing box things. Inside, cushioned in bubble wrap, were two ZIMA-branded boxes: one larger, one smaller, both printed with the spare Zima aesthetic and no unnecessary words.

## Packaging & Unboxing

{{< gallery >}}
{{< labimg src="zima-branded-boxes.jpg" caption="The two ZIMA boxes. The smaller one — ZBA069 — is the cooling fan. First time IceWhale has shipped active cooling in the box." id="zima-branded-boxes" >}}
{{< labimg src="cooling-fan-bag-on-box.jpg" caption="Cooling fan bag sitting on the main ZIMA box before opening. The fan accessory ships separately labelled." id="cooling-fan-bag-on-box" >}}
{{< /gallery >}}

The smaller box was labelled ZBA069 — ZimaBoard 2 Cooling Fan. This matters because the original ZimaBoard shipped with no active cooling at all, relying entirely on the finned aluminium heatsink chassis. The ZimaBoard 2 still has the passive fins, but now includes an optional active fan. Optional because you have to install it yourself — and I did, immediately.

{{< gallery >}}
{{< labimg src="welcome-zimaspace-lid.jpg" caption="Inside the lid of the outer ZIMA box: 'Welcome 2 ZimaSpace'. A small bit of levity in an otherwise deliberately minimal package." id="welcome-zimaspace-lid" >}}
{{< labimg src="inner-box-two-compartments.jpg" caption="Box ① — ZimaBoard 2 Single Board Server, held shut with the most gloriously orange elastic band I have seen on a product box. Box ② — Accessories. Everything numbered, nothing improvised." id="inner-box-two-compartments" >}}
{{< /gallery >}}

The main ZIMA box had "Welcome 2 ZimaSpace" printed on the inside of the lid — a small bit of levity in an otherwise deliberately minimal package. Inside that, two numbered compartments: Box ① — ZimaBoard 2, Single Board Server — secured with what I can only describe as the most gloriously orange elastic band I have seen on a product box. Box ② — Accessories: Power Adapter and Interchangeable Plugs.

IceWhale has been quietly iterating on their packaging for years. The ZimaCube 2 Pro had its own theatre of presentation. The ZimaBoard 2 goes the other way: functional minimalism, and then one orange elastic band. The contrast works.

{{< gallery >}}
{{< labimg src="lauren-letter-and-unit.jpg" caption="Box ① open. The letter from Lauren, the ZimaBoard 2 in its tray still wrapped in plastic. The board ships well-protected." id="lauren-letter-and-unit" >}}
{{< labimg src="box-layout-labels.jpg" caption="The Box ① lid shows die-cut slots labelled for two 2.5 inch SSDs and the ZimaBoard 2 itself. Tear it off along the perforations and it becomes a standing tray." id="box-layout-labels" >}}
{{< /gallery >}}

There is a practical twist to the packaging. The lid of Box ① has die-cut slots labelled for two 2.5 inch SSDs and the ZimaBoard 2 itself. Tear off the lid along the perforations and it becomes a standing tray — a portable desk stand for the board. I didn't use this during the [VAPT engagement last week](/vapt-appliance-zimaboard2/) because I was running an NVMe drive at the time, but the intent is obvious and reasonably clever.

## What's In The Box

{{< gallery >}}
{{< labimg src="accessories-box-with-booklet.jpg" caption="The accessories box alongside the 'ZimaBoard 2 / Hack Out New Rules' booklet. Minimal documentation by design — the assumption is you'll find the rest online." id="accessories-box-with-booklet" >}}
{{< labimg src="accessories-box-opened.jpg" caption="Accessories box opened. Cables bundled in plastic bags, PSU and plugs stacked beneath. Orderly." id="accessories-box-opened" >}}
{{< /gallery >}}

Box ① holds the board itself plus the "ZimaBoard 2 / Hack Out New Rules" booklet — styled with Zima's clean typographic language. No thick manual. The assumption is that you'll find the documentation online, which is fine by me.

{{< gallery >}}
{{< labimg src="full-spread-eu-plug.jpg" caption="Everything laid out: PSU with EU plug head, SATA-Y cable fanned from the unit, accessory bags. The EU and UK plug heads swap freely." id="full-spread-eu-plug" >}}
{{< labimg src="sata-y-cable-uk-plug.jpg" caption="The PSU with UK plug attached — the interchangeable heads cover the main markets without shipping different adapters. The SATA-Y cable unfurls into a surprisingly organised harness." id="sata-y-cable-uk-plug" >}}
{{< /gallery >}}

Box ② contains the power adapter and its interchangeable plug heads. The original ZimaBoard came with a 12V 3A adapter, which was the meaningful constraint on storage — two 2.5 inch spinning drives at that wattage is about as far as you could safely push it. The ZimaBoard 2 ships with a higher-rated adapter <!-- TODO: verify PSU amperage from label -->, which opens the door for heavier storage configurations and the 3.5 inch HDD expansion bracket that I have not yet explored.

The box also includes the SATA-Y cable — the breakout cable that splits from the board's single SATA connector into the two SATA data and power connections needed to run a pair of 2.5 inch drives. You unfurl it and it looks like a very organised wiring harness, which it is.

## The Board Itself

{{< gallery >}}
{{< labimg src="unit-top-and-rear-io.jpg" caption="The ZimaBoard 2 1664 sitting on its cardboard packaging. The finned aluminium top runs the full length of the board. Rear I/O visible on the right: two Ethernet, two USB, mini-DisplayPort, power." id="unit-top-and-rear-io" >}}
{{< labimg src="unit-rear-io-scale.jpg" caption="Rear I/O panel with a 1-litre water bottle for scale. The board is genuinely compact — the Ethernet ports are the visual anchor." id="unit-rear-io-scale" >}}
{{< /gallery >}}

The ZimaBoard 2 1664 — 16GB RAM, 64GB eMMC — is finished in plain brushed aluminium throughout. Top, sides, bottom: all metal, no gaps. The original ZimaBoard had an opaque perspex base that gave the unit a distinctive look — not translucent, just a clean dark panel that made the thing feel purposefully designed. The ZimaBoard 2 replaces that with a full aluminium enclosure. More enclosed, more industrial, more finished. Depending on your taste, this is either progress or the removal of something that had character.

I lean toward the original's look, if I'm honest. The ZimaBoard felt like a piece of enthusiast hardware. The ZimaBoard 2 feels like a product. A good product — desktop-friendly in the way a MacBook Pro is desktop-friendly — but a product nonetheless.

The port selection is meaningfully better across the board, and the processor has had a genuine generational upgrade:

<table class="spec-table">
  <thead>
    <tr><th>Feature</th><th>ZimaBoard 832</th><th>ZimaBoard 2 1664</th></tr>
  </thead>
  <tbody>
    <tr><td>Processor</td><td>Intel Celeron N3450 (Apollo Lake)</td><td>Intel N150 (Alder Lake-N)</td></tr>
    <tr><td>CPU Speed</td><td>1.1 GHz base / 2.2 GHz burst</td><td>0.8 GHz base / 3.6 GHz turbo</td></tr>
    <tr><td>Cores / Threads</td><td>4C / 4T</td><td>4C / 4T</td></tr>
    <tr><td>L3 Cache</td><td>2MB (L2 only)</td><td>6MB (Intel Smart Cache)</td></tr>
    <tr><td>TDP</td><td>6W</td><td>10W</td></tr>
    <tr><td>RAM</td><td>8GB LPDDR4</td><td>16GB LPDDR5 (4800MHz)</td></tr>
    <tr><td>Onboard Storage</td><td>32GB eMMC 5.1</td><td>64GB eMMC 5.1</td></tr>
    <tr><td>Ethernet</td><td>2× 1GbE</td><td>2× 2.5GbE</td></tr>
    <tr><td>USB</td><td>2× USB 3.0 (Type-A)</td><td>2× USB 3.1 (Type-A)</td></tr>
    <tr><td>Display</td><td>Mini-DisplayPort 1.2 (4K@60Hz)</td><td>Mini-DisplayPort 1.4 (4K@60Hz)</td></tr>
    <tr><td>PCIe</td><td>x4 Gen 2</td><td>x4 Gen 3</td></tr>
    <tr><td>SATA</td><td>2× SATA 6.0 Gb/s</td><td>2× SATA 6.0 Gb/s</td></tr>
  </tbody>
</table>

The 2.5GbE is the headline upgrade for a homelab context. If your switch supports it — and increasingly more do — you're looking at a meaningful bandwidth improvement on local transfers without touching a single cable. The PCIe slot is the same physical form factor as the original ZimaBoard's x4 Gen 2 slot; accessories built for the original should work here at Gen 3 speeds. That kind of upgrade continuity builds loyalty.

## Opening the Case

The fan doesn't install from the outside. You remove the aluminium cover, fit the fan onto the bracket that IceWhale provides in the accessories bag, and screw it down. The cover is held by four Torx screws.

{{< labimg src="pcb-exposed.jpg" caption="Cover off, PCB exposed. The SATA connector sits at the edge for cable routing, the eMMC module is visible near centre, and the fan header is already waiting. Dense, organised, no wasted space." id="pcb-exposed" >}}

{{< gallery >}}
{{< labimg src="fan-bracket-detail.jpg" caption="The fan bracket mounted at the corner of the heatsink chassis. The wire routes neatly alongside the aluminium edge." id="fan-bracket-detail" >}}
{{< labimg src="skil-screwdriver-kit.jpg" caption="The SKIL power screwdriver and bit kit that actually got the job done. IceWhale includes a tool in the accessories bag — patience was not included." id="skil-screwdriver-kit" >}}
{{< /gallery >}}

IceWhale includes a tool in the accessories bag, and in theory you use that. In practice, I ran out of patience before I got anywhere useful and switched to my SKIL power screwdriver. Early Kickstarter backers reported the screws stripping — a problem that appears to have been resolved since, because I encountered no such issue. What I did find is that the first opening benefits enormously from the right bit size and a driver with enough torque to seat properly. The manual approach is technically possible. It's also more frustrating than it needs to be.

{{< gallery >}}
{{< labimg src="screwdriver-on-unit-angle1.jpg" caption="The SKIL on the first screw. The angle matters — the bit needs to seat squarely before you apply torque." id="screwdriver-angle1" >}}
{{< labimg src="screwdriver-on-unit-angle2.jpg" caption="Second screw on the side panel. The fan bracket is now visible, secured at the top-left corner of the heatsink." id="screwdriver-angle2" >}}
{{< /gallery >}}

## The Cooling Fan

{{< labimg src="fan-installed.jpg" caption="Fan installed and bracket secured. Small fan, big difference in sustained thermal performance compared to the original ZimaBoard running fully passive." id="fan-installed" >}}

The fan itself is very small. Smaller than you'd expect given the surface area it's cooling. IceWhale's choice here is pragmatic: passive cooling handles steady-state loads, and the fan assists with sustained compute tasks. The ZimaBoard 2 is more manageable in terms of surface temperature during extended use than the original — the first ZimaBoard ran warm enough that you'd notice. The ZimaBoard 2 with the fan attached stays well within comfortable range.

## What's Next

The ZimaBoard 2 has already had eight months of productive use. I ran it through a VAPT engagement last week at [/vapt-appliance-zimaboard2/](/vapt-appliance-zimaboard2/) — headless, off an NVMe via the PCIe slot, with the aluminium case still cool to the touch three hours in. That was the 832's job for the two years before it. Now it's the 2's.

The 3.5 inch HDD expansion bracket is on the list. So is a dedicated teardown page once I've spent more time with the board. The ZimaBoard 832 review is at [/zimaboard-832-unboxing/](/zimaboard-832-unboxing/) if you want the comparison from the other side.

The ZimaBlade 7700 unboxing post is coming soon — a cyberpunk trip into tech nostalgia and modern technology.
