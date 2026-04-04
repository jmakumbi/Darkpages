---
title: "ZimaBoard 832 — Unboxing & First Impressions"
date: 2023-12-14
draft: false
layout: "lab-log"
description: "Unboxing and first impressions of the ZimaBoard 832 single-board server from IceWhale Technology. Gift-wrap packaging, dual Gigabit Ethernet, passive cooling, and a Jellyfin server up in an afternoon."
slug: "zimaboard-832-unboxing"
url: "/zimaboard-832-unboxing/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "IceWhale Technology · Personal Purchase · December 2023"
series: "zimaboard"
toc: false
tags:
  - zimaboard
  - icewhale
  - homelab
  - single-board-server
  - jellyfin
  - casaos
---

## The Order

I ordered the ZimaBoard 832 on 30 November 2023. The decision traces back to a YouTube review of the Firewalla Gold SE — same reviewer, same week, also covered the ZimaBlade crowdfunding campaign. I looked at the ZimaBlade. I looked at the ZimaBoard. I chose the ZimaBoard. The ZimaBlade is fine. I stand by this entirely and without apology.

The order was three items: the ZimaBoard 832 (the 8GB RAM, 32GB eMMC model), a PCIe-to-NVMe & NGFF SSD adapter, and a SATA Y-Cable. All from IceWhale's store.

{{< labimg src="order-screenshot.png" caption="The order: ZimaBoard 832, SATA Y-Cable, and PCIe-to-NVMe adapter. Three items. One box. Efficient." id="order-receipt" >}}

## Arrival

It arrived five days later. IceWhale shipped from China via DHL — at my specific request. I love DHL. That is not a paid statement. They are simply the only courier that consistently delivers to Kampala without drama. IceWhale handles shipping and applicable taxes in advance, which means no surprise charges on collection. This detail is not small when you are importing hardware to East Africa.

Three beige boxes. Initially underwhelming. My love affair with IceWhale packaging was about to begin, and I had absolutely no idea.

{{< gallery >}}
{{< labimg src="shipping-boxes.jpg" caption="Three beige boxes. Appropriately unassuming. One of them will surprise you." id="shipping-boxes" >}}
{{< labimg src="outer-box-open.jpg" caption="The outer shipping box opened. ZimaBoard retail packaging left, power adapter box right, stickers top." id="outer-box-open" >}}
{{< /gallery >}}

## The Letter & Stickers

The largest box contains a personal letter from Lauren, founder of IceWhale Technology, and a sticker sheet. The letter is a genuine note about the vision behind IceWhale and ZimaBoard — not a boilerplate thank-you. Whether you read it or use it as a coaster is your business.

The sticker sheet has four stickers. "Home Is Where My Lab Is." I did not argue. There is a round ZimaBoard badge, an "If You Can't Open It, You Don't Own It" chip-shaped sticker (which I appreciate philosophically), and a warning-triangle-shaped "Oh My Root!" sticker that is either charming or a security notice, depending on how you read it.

{{< gallery >}}
{{< labimg src="outer-open-stickers.jpg" caption="The sticker sheet and Lauren's letter from IceWhale. \"Home is Where My Lab Is.\" I did not argue." id="outer-stickers" >}}
{{< labimg src="retail-box-desk.jpg" caption="The ZimaBoard retail box standing on the desk. The lab is always this tidy." id="retail-box-desk" >}}
{{< /gallery >}}

## Retail Packaging

The ZimaBoard retail box is shrink-wrapped. The back panel lists the specs with callout labels the way hardware packaging should — actual numbers, not marketing adjectives. Two Gigabit Ethernet ports, one Mini-DisplayPort at 4K@60Hz, two SATA at 6Gb/s, one PCIe 2.0 x4 slot. Everything you need to know before you open it.

The power adapter sits in its own separate beige box alongside the retail unit. IceWhale had just changed their packaging and SKU policy — the minimum required power adapter is now included with every device. Until this point, adapters were sold separately. This is the correct decision and I am glad they made it. The adapter is a 12V/3A unit with a UK plug already fitted and regional adapters in a small bag inside. CE, FCC, and UL certifications on the body. It is a proper adapter, not an afterthought.

{{< gallery >}}
{{< labimg src="retail-box-back.jpg" caption="Box rear with specs callouts. 2× GbE, 4K display, 2× SATA, 1× PCIe 2.0 x4. All the important numbers." id="retail-box-back" >}}
{{< labimg src="adapter-open.jpg" caption="The power adapter box: 12V/3A unit, UK plug fitted, regional adapters in the bag." id="adapter-open" >}}
{{< /gallery >}}

## The Gift Wrap

Remove the shrink wrap from the retail box and you find something unexpected. Instead of the usual slotted cardboard box — the kind that requires two hands and a mild oath — the ZimaBoard is packaged in a four-flap wrap that opens like gift wrapping. Touch the flaps and they fall open. No tape. No struggle. No cardboard dust landing on your desk. You feel, briefly, like the product warranted this level of care. At this price point, that feeling is not guaranteed and it is noticed.

{{< labimg src="gift-wrap-open.jpg" caption="Four flaps, no tape. The retail box opens like gift wrapping. This is not typical at this price point." id="gift-wrap" >}}

## The Inner Box

Under the gift wrap is a standard beige inner box. Eyeroll acknowledged — we are computer scientists, not Apple fanbois. It has "#SingleBoardServer" printed on the outside, which suggests someone in the copywriting department was enjoying themselves.

Inside the inner box: the user manual on top, and the ZimaBoard 832 in a properly sealed antistatic bag, with the single-drive SATA cable tucked alongside it.

{{< gallery >}}
{{< labimg src="inner-box-manual.jpg" caption="Inner beige box: manual on top, ZimaBoard below. \"#SingleBoardServer\" is printed on the outside." id="inner-box" >}}
{{< labimg src="antistatic-bag.jpg" caption="Still in the antistatic bag. SATA cable top left. The bag is properly sealed — not just folded over." id="antistatic-bag" >}}
{{< /gallery >}}

## The Board

The ZimaBoard 832 is a machined block of grey anodised aluminium. The orange accent lines — two of them, running the length of the top surface — are tasteful rather than gratuitous. The entire top surface is a passive fin array: no fan, no noise, no failure modes related to rotating parts. Under the aluminium block is a layered dark acrylic base that holds the motherboard assembly. The effect is industrial and deliberate. It would not look out of place in a server room. It does not look out of place on a desk.

I am not embarrassed to have it visible. For hardware in this category, that is a meaningful design achievement.

{{< gallery >}}
{{< labimg src="board-spread.jpg" caption="The full spread: ZimaBoard 832, 12V/3A adapter, SATA cable, and the manual nobody reads." id="board-spread" >}}
{{< labimg src="heatsink-upright.jpg" caption="Stood upright, the passive fin array covers the entire top surface. No fan. No noise. No excuses." id="heatsink-upright" >}}
{{< /gallery >}}

{{< gallery >}}
{{< labimg src="side-profile-left.jpg" caption="Left side profile. The dark acrylic layers under the aluminium block are visible. Deliberate engineering." id="side-left" >}}
{{< labimg src="side-profile-right.jpg" caption="Right side, showing the PCIe x4 slot. Standard x16 physical slot, four electrical lanes." id="side-right" >}}
{{< /gallery >}}

## Specifications

| Specification | Detail |
|---|---|
| Model | ZimaBoard 832 |
| CPU | Intel Celeron N3450, Quad-core, up to 2.2 GHz |
| RAM | 8GB LPDDR4 |
| Storage (onboard) | 32GB eMMC |
| Ethernet | 2× Gigabit Ethernet (RJ45) |
| Display | 1× Mini-DisplayPort 1.2, 4K@60Hz |
| USB | 2× USB-A 3.0 |
| SATA | 2× SATA 6.0 Gb/s (with integrated power headers) |
| PCIe | 1× PCIe 2.0 x4 (x16 physical slot) |
| Power input | 12V/3A barrel jack |
| Power adapter | 12V/3A, multi-region plugs included |
| OS support | Linux, Windows, OpenWrt, pfSense, Android |
| Cooling | Passive (aluminium fin array, no fan) |

## Ports

The ZimaBoard distributes its IO across three sides, which I find more sensible than everything on one face.

The front panel carries the two Gigabit Ethernet ports, two USB-A 3.0 ports, one Mini-DisplayPort (4K@60Hz), and the barrel jack for power. Everything you need to connect the board to a network, a display, and a power source is in one place.

One side carries the two SATA ports with integrated power headers. This detail matters: the power headers are built into the board, which means you do not need a separate power adapter for your drives. The SATA cable included in the box connects both the data and power lines for one drive. For two drives, the SATA Y-Cable splits the power header. More on that below.

The other side carries the PCIe 2.0 x4 slot — physical x16, electrical x4. This is where the NVMe adapter lives.

{{< gallery >}}
{{< labimg src="io-panel.jpg" caption="Front IO: 2× Gigabit Ethernet, 2× USB-A 3.0, 1× Mini-DisplayPort, 1× barrel jack. Everything needed, nothing else." id="io-panel" >}}
{{< labimg src="sata-ports.jpg" caption="The SATA side: two data ports with built-in power headers. No separate power adapter required for drives." id="sata-ports" >}}
{{< /gallery >}}

{{< labimg src="pcie-slot.jpg" caption="PCIe 2.0 x4 slot. Fits the NVMe adapter without modification. This is where the extra storage lives." id="pcie-slot" >}}

## Accessories

Two accessories in this order — both necessary, neither glamorous.

The SATA Y-Cable splits one of the board's SATA power headers into two connections, allowing both SATA data ports to be used simultaneously. If you are running two SATA drives, this cable is not optional. It comes in a small box and is, as advertised, a cable.

The PCIe-to-NVMe & NGFF SSD adapter came in a separate small box alongside a screwdriver, assorted screws, and several faceplates. I prefer to use it without faceplates. The adapter itself slots into the PCIe x4 slot and accepts an M.2 NVMe or SATA SSD.

{{< labimg src="sata-y-cable.jpg" caption="The SATA Y-Cable. Splits one power header into two — required if you're running two drives." id="sata-y-cable" >}}

## In Service

First boot: CasaOS. The ZimaBoard ships with CasaOS pre-installed on the eMMC, or you can flash it yourself. I used the pre-installed image. It booted cleanly.

From CasaOS, I installed Jellyfin from the app store. Local media — video, music, audiobooks — streaming to any device on the home network, without touching the internet. One 2.5" SATA SSD for the OS and app data, one NVMe via the PCIe adapter for media storage. The setup took an afternoon, including formatting the drives and populating the Jellyfin library.

Ten days after unboxing, it was running under a shelf in a red 3D-printed stand — one yellow Ethernet cable in use, second port empty, USB drive attached, keyboard connected, mini-DP adapter fitted. The keyboard and adapter suggest I had already flashed it to ZimaOS by this point, leaving the safe harbour of CasaOS for the wild seas. Blue LED lit. Has not moved since.

{{< labimg src="in-service.jpg" caption="Ten days later. Red 3D-printed stand, one yellow Ethernet cable, USB drive, keyboard, mini-DP adapter. Second port unused. Blue LED lit." id="in-service" >}}

{{< callout >}}
My adventures with CasaOS and later ZimaOS — the app store, Docker containers, service configuration — will be covered in later entries in this series. The ZimaBoard 832 is not the end of the story. It is the beginning of it.
{{< /callout >}}
