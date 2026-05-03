---
title: "ZimaBlade 7700 — Unboxing"
date: 2024-03-09
draft: false
layout: "lab-log"
description: "Unboxing the ZimaBlade 7700, purchased via Crowd Supply crowdfunding. First boot, CasaOS, and a network flow log that confirmed my paranoia was well-founded."
slug: "zimablade-7700-unboxing"
url: "/zimablade-7700-unboxing/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "IceWhale Technology · Personal Purchase · March 2024"
series: "dark-gate-homelab"
toc: false
tags:
  - zimablade
  - icewhale
  - homelab
  - casaos
  - dark-gate
---

## Arrival & Shipping

This one came via courier, directly to my door. Not DHL — whatever IceWhale was using at the time got it through. The outer box was standard brown corrugated cardboard. Nothing ceremonial about it. East Africa received a small electronics package intact, which I note without irony.

{{< labimg src="zimablade-arrival-box.jpg" caption="The outer box. The ZimaBlade retail box on the right, a plain IceWhale accessory box alongside it." id="arrival-box" >}}

## The Packaging

The retail box is shrink-wrapped and printed in a dark anime aesthetic — black, purple, chip art. In the top-left corner: "zima blade," in case you had forgotten. The design signals that someone at IceWhale has opinions about aesthetics and has aimed them at a specific audience. I am, apparently, that audience.

{{< labimg src="zimablade-retail-box.jpg" caption="The retail box. Shrink-wrapped, purple-and-black chip art. It does not prepare you for what is inside — which is the point." id="retail-box" >}}

## In the Box

The ZimaBlade arrived alongside a plain white IceWhale box — a dual 3.5" hard disk tray stand (SKU ZBA039), free, no announcement. Tucked in beside it: a kraft cardboard box containing the 12V/3A power adapter. The adapter uses a USB-C connector. This is different from the ZimaBoard's barrel connector, and the spec is strict: the blade does not negotiate with adapters that cannot deliver exactly 12V/3A. It simply declines to power on. This failure mode has generated a remarkable volume of support tickets. Buy the adapter from IceWhale.

{{< gallery >}}
{{< labimg src="zimablade-icewhale-accessory-box.jpg" caption="The IceWhale accessory box. Free hard disk tray stand inside, no fanfare." id="icewhale-box" >}}
{{< labimg src="zimablade-sata-ycable.jpg" caption="SATA Y-Cable, also included. Paired with a 12V/3A adapter, it will power exactly zero 3.5&quot; drives." id="sata-ycable" >}}
{{< /gallery >}}

I had backed a Crowd Supply tier that included extras, which I chose deliberately: I suspected I would rather pay a little more upfront than receive a device I could not use. The tier included a Mini DisplayPort to HDMI 4K adapter (ZBA017), braided cable, genuinely useful for first-boot troubleshooting; and 16GB of DDR3L SODIMM RAM (ZBA045). The "L" is not decorative — it is a low-voltage specification, designed for the same class of device as a laptop SODIMM. The community forums around this period were essentially a catalogue of incorrect RAM purchases. Backing the right tier was probably the single smartest decision of the entire build.

{{< gallery >}}
{{< labimg src="zimablade-minidp-hdmi.jpg" caption="Mini DP to HDMI 4K adapter (ZBA017). Braided cable. One of the better accessories IceWhale sells." id="minidp-hdmi" >}}
{{< labimg src="zimablade-ram-sodimm.jpg" caption="16GB DDR3L SODIMM (ZBA045). The &quot;L&quot; matters. The community has many stories about forgetting it matters." id="ram-sodimm" >}}
{{< /gallery >}}

{{< gallery >}}
{{< labimg src="zimablade-adapter-box.jpg" caption="The 12V/3A adapter in its kraft box. USB-C connector, not barrel. Important." id="adapter-box" >}}
{{< labimg src="zimablade-manual-card.jpg" caption="User manual and the founder's card. Lauren. Mass-printed, but the founder is genuinely on Discord during China working hours." id="manual-card" >}}
{{< /gallery >}}

## The Device

Inside the retail box, the ZimaBlade sat in a moulded black tray, still in a translucent protective bag. You could see it through the bag. That was either a design decision or a packaging oversight, and I am fairly certain it was a design decision.

{{< gallery >}}
{{< labimg src="zimablade-in-tray-bagged.jpg" caption="In the tray, still bagged. &quot;RECLAIM YOUR CLOUD.&quot; on the box beneath." id="in-tray-bagged" >}}
{{< labimg src="zimablade-out-of-bag.jpg" caption="Out of the bag. Clear acrylic top, PCB visible. SATA ports at the front edge." id="out-of-bag" >}}
{{< /gallery >}}

The device looks exactly like a Sony Walkman. I do not say this as marketing copy. I say it because my friend Dr K — who is old enough to have owned one — would be extremely entertained by this object. Part clear acrylic cover exposing the PCB, flexible plastic edges concealing the mounting screws, and a black cast aluminium heatsink forming the entire base of the unit. The heatsink is also the motherboard's mounting platform. It is a very tidy piece of industrial design. I say that reluctantly.

{{< gallery >}}
{{< labimg src="zimablade-with-cables.jpg" caption="With cables: SATA+power ribbon and USB-C. The short braided USB-C cable came in the inner tray." id="with-cables" >}}
{{< labimg src="zimablade-side-view.jpg" caption="Side view. The clear acrylic edge and SATA port connectors. Compact is an understatement." id="side-view" >}}
{{< /gallery >}}

The inner tray also contained the stickers. If applied correctly, they complete the Walkman aesthetic. Mine are still in the bag.

{{< labimg src="zimablade-stickers.jpg" caption="The stickers. Two sheets. The Walkman visual identity, deferred indefinitely." id="stickers" >}}

## RAM Installation

To install the RAM, you remove the flexible plastic sleeve and lift off the clear acrylic cover. With the cover removed, you have a full, unobstructed view of the two SATA ports with the HDD power connector sitting between them, and the single SODIMM slot. The slot looks straightforward. It is not straightforward. Seating the RAM correctly and firmly — to the point where the retention clips engage properly — is apparently a non-trivial task, and the community posts confirm this is not an edge case. I include myself in that admission. I will revisit it in the 10-inch rack post if the memory holds.

{{< labimg src="zimablade-bare-pcb.jpg" caption="Cover off. Two SATA ports bottom-left, HDD power between them, SODIMM slot centre. The orange standoffs are not for decoration." id="bare-pcb" >}}

## The Adapter

The 12V/3A adapter ships in its own small kraft box. The cable ends in a USB-C connector. This is not the barrel connector on the ZimaBoard adapter. The blade's power circuit is not forgiving of substitutions — the wrong voltage or current rating, or an adapter that cannot cleanly negotiate the spec, and the device simply refuses to start. There are posts from users who received units without adapters. There are posts from users who sourced third-party adapters and then wondered why nothing happened. The safest path is to buy it from IceWhale when you order the unit.

{{< gallery >}}
{{< labimg src="zimablade-adapter-unboxed.jpg" caption="The adapter inside its box. USB-C cable. 12V, 3A." id="adapter-unboxed" >}}
{{< labimg src="zimablade-adapter-cable.jpg" caption="Adapter and cable together. The braided USB-C is included. Do not mistake this for the short USB-C that came in the inner tray." id="adapter-cable" >}}
{{< /gallery >}}

{{< callout >}}There are stories circulating of users running 12V/5A adapters on the ZimaBlade. Some of these stories have sequels. Not good sequels.{{< /callout >}}

## Specifications

<table class="spec-table">
  <thead>
    <tr><th>Component</th><th>Detail</th></tr>
  </thead>
  <tbody>
    <tr><td>CPU</td><td>Intel Celeron N3450, quad-core, 1.1GHz base / 2.2GHz burst</td></tr>
    <tr><td>RAM</td><td>DDR3L SODIMM, up to 16GB — order from IceWhale</td></tr>
    <tr><td>Storage interface</td><td>2× SATA III, 1× PCIe (M.2 slot)</td></tr>
    <tr><td>Ethernet</td><td>2× Gigabit Ethernet (1000Base-T)</td></tr>
    <tr><td>Display output</td><td>Mini DisplayPort (4K capable)</td></tr>
    <tr><td>USB</td><td>USB 3.0 Type-A, USB-C (power)</td></tr>
    <tr><td>Power</td><td>12V/3A via USB-C adapter</td></tr>
    <tr><td>OS (shipped)</td><td>CasaOS on Debian</td></tr>
    <tr><td>Form factor</td><td>3.5" HDD chassis (approximately)</td></tr>
  </tbody>
</table>

## First Boot

I connected via my Microsoft Surface Book 3. The Firewalla Gold SE had already assigned an IP without complaint. CasaOS loaded immediately — a dark-themed dashboard with system stats, app icons, and an invitation to sync files and "smarten up your home." The UI is polished for what it is. The device then attempted to update itself. The update failed: `FAILED to download package`. I found this encouraging. A device that reaches for updates on first boot is the right disposition. The update server was having a moment. These things happen.

{{< gallery >}}
{{< labimg src="zimablade-casaos-dashboard.jpg" caption="CasaOS on first boot. 18:42. 15.47GB RAM recognised. CPU at 35°C, idle." id="casaos-dashboard" >}}
{{< labimg src="zimablade-casaos-update-fail.jpg" caption="The update attempt, and its outcome. Architecture confirmed, package not delivered. We move on." id="casaos-update-fail" >}}
{{< /gallery >}}

## The Network Tells All

I finished the session by reviewing flow logs in the Firewalla app. Eight outbound connections in the first twenty minutes of operation. Of those, two went to `casaos.oss-cn-shanghai.aliyuncs.com` — an Alibaba Cloud storage endpoint in Shanghai. I made a note to review it. To be direct: this is about my security practice, not about IceWhale. They have exceptional customer service, responsive support, and genuinely good products that do not come with the bureaucratic overhead of getting hardware out of the continental United States — I am looking at you, Firewalla. The IceWhale team are people I am glad to know. But I am also the kind of person who checks flow logs immediately after a device's first boot, and a connection to a cloud storage endpoint I did not configure is something I want to understand before I let it run. The ZimaOS post will go into what I found, what I blocked, and what I concluded.

{{< labimg src="zimablade-firewalla-flows.jpg" caption="Firewalla flow history from the first twenty minutes. Eight connections. Two to Shanghai. One immediately earmarked for review." id="firewalla-flows" >}}
