---
title: "DeskPi RackMate T1 — Unboxing & First Assembly"
date: 2025-07-18
draft: false
layout: "lab-log"
description: "A personal purchase. The DeskPi RackMate T1 in black — an 8U, 10-inch open-frame rack that turned a pile of homelab hardware into something intentional."
slug: "deskpi-rackmate-t1"
url: "/deskpi-rackmate-t1/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "DeskPi · Personal Purchase"
series: "homelab"
toc: false
tags: ["deskpi", "homelab", "rack", "unboxing", "10-inch"]
---

The DeskPi RackMate T1 is a 10-inch, 8U open-frame rack. It costs about $60 on Amazon. It is, by any reasonable measure, a solution to a problem that did not need to exist as elegantly as it does.

## A Brief History of the Thing

DeskPi started out making Raspberry Pi enclosures that looked like miniature PCs — the kind of case that made a $35 board look like it belonged on a desk instead of taped to a wall. They acquired a following, because the homelab community will spend three times the cost of a device on the enclosure for it, and no one should be surprised by this.

The RackMate series — T0 (4U), T1 (8U), and the larger T2 — came out of a recognition that people with multiple Raspberry Pis and SBCs needed somewhere to put them that was not a cardboard box or a tangle of USB cables. The 10-inch form factor is a real standard — SOHO (Small Office/Home Office) equipment has been built to it for years — but DeskPi turned it into something hobbyists could buy, assemble at home, and photograph for the internet.

The T1 hit the sweet spot: eight rack units is enough space for a usable homelab stack without requiring you to dedicate an entire corner of a room to it. The aluminium frame and acrylic side panels make it look deliberate rather than improvised. The community has done everything with it — Proxmox nodes on Pi 4s, OPNsense on Mini-ITX, full networking stacks with patch panels, and 3D-printed mounts for hardware DeskPi never intended. It has become the quiet standard for the minilab movement.

I ordered the black colorway. The T1 ships in silver by default; the black variant is harder to find but worth the search if your homelab does not need to look like a kitchen appliance.

## What Arrived

{{< gallery >}}
{{< labimg src="amazon-shipping-box.jpg" caption="The outer Amazon packaging with DHL transit label. It arrived looking like it had opinions about the journey." id="shipping-box" >}}
{{< labimg src="retail-box.jpg" caption="The DeskPi RackMate T1 retail box — matte black, architectural line drawing, FRAGILE sticker. Someone takes their packaging seriously." id="retail-box" >}}
{{< /gallery >}}

An Amazon box with a DHL transit label and the kind of structural integrity that suggests the contents had been handled by exactly as many people as were necessary. The outer packaging was unremarkable, which is exactly what you want. Inside: the DeskPi retail box itself, matte black with an architectural line drawing of the rack printed in white. The FRAGILE sticker appeared to have been treated as a suggestion. The box was fine.

## What's In The Box

{{< labimg src="box-opened-manual.jpg" caption="First layer: dense foam padding with the User Manual (DP-0022) sitting on top. The foam is proper — not the cheap crumbly kind." id="box-opened" >}}

The packaging is layered — properly layered, not the kind where everything rattles around in a single foam tray. Each lift reveals another moulded section.

{{< gallery >}}
{{< labimg src="contents-layer1-accessories.jpg" caption="Layer one: a 1U vented shelf panel, brass standoffs, rubber feet, and two DeskPi KL-P24 Raspberry Pi shelf modules in anti-static bags." id="contents-layer1" >}}
{{< labimg src="contents-layer2-shelves.jpg" caption="Layer two: the black 1U vented shelf and the multi-SBC mounting tray — silkscreened with mounting positions for RPi 3B/4B, Jetson Nano, Rock Pi 5B, and 2.5-inch storage." id="contents-layer2" >}}
{{< /gallery >}}

{{< gallery >}}
{{< labimg src="contents-layer3-panels.jpg" caption="Layer three: the two acrylic side panels and additional frame hardware in custom-moulded foam." id="contents-layer3" >}}
{{< labimg src="contents-layer4-rails.jpg" caption="The rack uprights and horizontal rails — perforated steel, powder-coated flat black." id="contents-layer4" >}}
{{< /gallery >}}

The bundle includes two **DeskPi KL-P24** Raspberry Pi rack shelf modules — each mounts two Pi boards in 1U with front-panel breakout for USB and HDMI. The black multi-SBC mounting tray is silkscreened with mounting positions for Raspberry Pi 3B/3B+/4B, Jetson Nano, Rock Pi 5B, and 2.5-inch HDDs and SSDs. There is no guesswork about whether your board will fit; either the mounting holes match or they do not, and for the boards labelled, they do.

The User Manual (DP-0022) is a proper printed booklet, not a folded A4 sheet. This is a small thing, but it is the kind of small thing that tells you whether a company thought about the out-of-box experience.

## The Assembly

{{< gallery >}}
{{< labimg src="assembly-hardware-spread.jpg" caption="The mid-assembly evidence: two screwdrivers, several bags of hardware that DeskPi did not feel the need to label, and the manual." id="assembly-spread" >}}
{{< labimg src="assembled-rack.jpg" caption="Assembled. It took an evening, a stubborn hardware bag, and a surprising amount of floor space. The result is a proper open-frame 10-inch rack." id="assembled" >}}
{{< /gallery >}}

The manual is clear enough. The problem is not the instructions — it is the unlabelled hardware bags. DeskPi includes multiple screw sizes and types, sorted into separate bags, which is good. The bags are not labelled with the screw type or size, which is less good. You identify the right hardware by process of elimination and, eventually, by reading the manual carefully enough to match the diagram. A sticker reading "M3×6 — uprights" would solve this entirely.

I used two screwdrivers — both orange-handled, neither technically the right size for every fastener. This is a sentence that applies to most of my assembly experiences, and I have made peace with it.

The assembly itself is solid. The uprights are thick enough, the rails click into place with a satisfying absence of wobble, and the acrylic panels slot in cleanly. The finished rack is rigid. Nothing flexes. Nothing rattles. For approximately $60, this is not obvious.

Total assembly time: one evening. Most of that was sorting hardware.

## What Goes In It

The multi-SBC mounting tray will hold the VisionFive 2 — the RISC-V board I documented over at [VisionFive 2 — Unboxing](/visionfive2-unboxing/). The tray's mounting holes accommodate it without modification.

The rest of the rack is earmarked for network gear, the ZimaBlade, and possibly one of the ZimaBoards. I will cover that build in a later post once the MokerLink switch arrives and the VLAN plan stops being a plan.

For now, it stands against a wall looking more intentional than the pile of devices it is about to replace.
