---
title: "ZimaCube 2 Pro — Unboxing & First Impressions"
date: 2026-03-13
draft: false
layout: "lab-log"
description: "Unboxing and first physical impressions of the ZimaCube 2 Pro personal cloud NAS, received for review and shipped to Kampala, Uganda from IceWhale Technology."
slug: "zimacube-2-pro-unboxing"
url: "/zimacube-2-pro-unboxing/"
noindex: true
subtitle: "IceWhale Technology · Review Unit"
series: "zimacube-2-pro"
author: "James S. K. Makumbi"
toc: false
disclosure: true
disclosure_text: "I received this device for review and testing from IceWhale Technology. They have not read this post and have no influence on its content."
tags:
  - homelab
  - zimacube
  - icewhale
  - nas
---

## What Is the ZimaCube 2?

[IceWhale Technology](https://zimaspace.com) is a Shenzhen-based hardware company best known for making personal cloud and homelab devices. They produced the ZimaBoard — a single-board server that quietly found its audience — and the ZimaBlade, its smaller sibling, before shipping the [original ZimaCube](https://www.zimaspace.com/products/cube-personal-cloud) via crowdfunding. That first ZimaCube was a 6-bay personal NAS that earned genuine goodwill, but the Intel N100 at its core proved to be a bottleneck for the ambition around it: only 9 PCIe lanes to feed 6 drives, 4 M.2 slots, dual NIC, and multiple USB ports. Something had to give, and what gave was the CPU. A follow-on was inevitable.

The ZimaCube 2 comes in three variants. All share the same chassis (240 × 221 × 220 mm) and power supply (19V 13A, 247W rated):

- **ZimaCube 2** (standard): Intel Core i3-1215U (6 cores, up to 4.40 GHz), 8GB DDR5, 256GB onboard NVMe, 2× 2.5GbE. Silver.
- **ZimaCube 2 Pro**: Intel Core i5-1235U (10 cores, up to 4.40 GHz), 16GB DDR5 4800 MT/s (2×8GB, upgradeable to 64GB), 256GB onboard NVMe, 10GbE + 2× 2.5GbE. Black.
- **ZimaCube 2 Creator Pack**: Same i5-1235U, 64GB DDR5 (2×32GB), 1TB onboard NVMe, adds NVIDIA RTX PRO 2000 GPU. Black.

All three share: 6× SATA3 bays (3.5″ & 2.5″ HDD), the "7th Bay" with 4× M.2 NVMe slots, Thunderbolt 4 (2× rear USB-C), DP 1.4, HDMI 2.0, 3.5mm audio, 4× USB-A 3.0, 1× USB-C 3.0, PCIe expansion (x16 + x8 slots), 13× RGB LEDs, and ZimaOS pre-installed.

I received the **ZimaCube 2 Pro** for review.

## Arrival: A Box, a Sofa, and Five Days

The outer shipping container is a brown corrugated cardboard box printed directly with "ZimaCube Personal cloud_" in clean sans-serif — no branding tape, no stickers. The brand identity is just... printed on the box. This is a flex, and a deliberate one.

Shipped from China to Kampala, Uganda via DHL. Transit time: approximately five days. In a country where the phrase "the package is with the courier" can mean anything from "it's ten minutes away" to "it exists, somewhere, probably", DHL is the exception that proves the rule. No hidden charges on arrival, no mystery disappearances, no philosophical debates about what "delivered" means. Collected from the DHL office with what appeared to be a dedicated attendant — which, given what was inside, makes sense.

Shipped weight: approximately 5.5 kg. We will discuss why shortly.

{{< labimg src="box_arrived_couch.jpg" caption="It arrived. On the sofa. As things do." id="box-couch" >}}

{{< labimg src="dhl_arrival_redacted.jpg" caption="Collected from the DHL office. The box is fine. The suspense was not." id="dhl-arrival" >}}

## What's in the Box

Two distinct inner boxes inside the outer shipping carton, plus a loose accessories layer.

### The "ZimaCube Parts_" Box

A small, flat black box labelled "ZimaCube Parts_" in the same typeface as the outer carton. Sits in a custom die-cut dense foam insert. Contains: a very large external AC adapter (KPTEC branded, UL/CE/GS/UK CA certified), multiple zip-lock bags of assorted replacement screws and fasteners, and a power cord.

The PSU is the reason the package weighs 5.5 kg. It is a large, slab-like brick — the kind that makes you briefly question whether you ordered hardware or portable heating equipment. 19V 13A, 247W rated. No complaints — it is properly specced for six spinning drives and a Core i5.

{{< gallery >}}
{{< labimg src="20260313_205521.jpg" caption="The \"ZimaCube Parts_\" inner box seated in die-cut foam" id="parts-box" >}}
{{< labimg src="20260313_205714.jpg" caption="The KPTEC power supply. 19V 13A. This is why the box weighed 5.5 kg." id="psu-closeup" >}}
{{< /gallery >}}

### Loose Accessories

{{< gallery >}}
{{< labimg src="20260313_205620.jpg" caption="The accessories layer — bags of hardware, the power cord, and optimism" id="accessories-layer" >}}
{{< labimg src="20260313_210138.jpg" caption="Full spread: CAT6, IW custom screwdriver, standard Phillips (sigh), 4× NVMe heat sinks" id="accessories-spread" >}}
{{< /gallery >}}

- **1× CAT6 UTP Patch Cord** — 1M, black (Model WV-E651)
- **1× IceWhale custom screwdriver** — a proprietary magnetic-head driver with an IW-stamped grip. Thoughtful inclusion; this is the tool you actually need for drive installation.
- **1× Standard Phillips head screwdriver** — included, apparently, in case you have never encountered a screw before. Any tech-savvy user already has three of these. The Phillips screwdriver is the technological equivalent of a hotel putting a single teabag in the room and calling it "hospitality". It should be a free add-on option on the product page, not a standard inclusion — it adds weight, cost, and mild existential confusion to the unboxing experience.
- **4× M.2 NVMe heat sinks** with pre-applied thermal pads. These are for drives installed in the 7th Bay — a thoughtful inclusion given how compressed the thermal environment will be with four M.2 cards stacked in that module.

### The Main Event

The ZimaCube 2 Pro retail box. Black exterior, single orange accent band at the equator, "ZimaCube Personal cloud_" in white. No foam insert inside the retail box itself — the device sits directly in the shell, wrapped in protective plastic. The design aesthetic lands somewhere between a corporate gift and a director's cut Blu-ray. It creates expectations. The product then has to meet them.

IceWhale appears to have studied the Dieter Rams school of "less but better" for this. It works. A NAS device this large has no business arriving this tastefully.

{{< gallery >}}
{{< labimg src="20260313_210418.jpg" caption="The retail box. Black cube, orange band. IceWhale knows what they're doing here." id="retail-box" >}}
{{< labimg src="20260313_210504.jpg" caption="The main unit in factory wrap, seated on the retail box" id="unit-unwrapped" >}}
{{< labimg src="20260313_210257.jpg" caption="The ZimaCube 2 Pro in its packing foam. CE / RoHS certified." id="unit-foam" >}}
{{< /gallery >}}

## Physical First Impressions

### Chassis

Four sides of matte black aluminium plate. No branding on the sides. No ventilation. No fingerprint magnet effect. The aluminium is the mass you feel when you pick it up — and you feel it. Lifting this thing is like lifting a small relative who has had one too many at Christmas dinner.

Dimensions: 240 × 221 × 220 mm — roughly the size of a shoebox for someone with unusually square feet.

Front and rear panels are black plastic mesh grilles. The front covers the 6 drive bays; the rear covers the two 80mm fans. Both grilles are noticeably thinner and flexier than the aluminium panels they flank. This is a minor but real criticism: the flat panel format gives nothing structural to grip when lifting, and an uninitiated user's natural handhold is exactly where the grille lives. A dropped grille won't destroy the device, but it will feel bad.

The machined edges and corners are sharp. Not "slightly uncomfortable" sharp — genuinely sharp. This device was designed by someone who has never stubbed a toe or moved house. Wrap your forearms accordingly. At this weight and corner geometry, dropping it on a foot crosses from accident into incident report territory.

{{< gallery >}}
{{< labimg src="20260313_210641.jpg" caption="Front panel: USB-A ×2, USB-C, 3.5mm audio, power button" id="front-panel" >}}
{{< labimg src="20260313_210657.jpg" caption="Rear panel: 10GbE, 2×2.5GbE, Thunderbolt 4 ×2, HDMI, DisplayPort, USB-A ×2" id="rear-panel" >}}
{{< labimg src="20260313_211053.jpg" caption="Side panel ventilation — two bands of circular perforations, top and bottom" id="side-vent" >}}
{{< /gallery >}}

### Cooling

Two 80mm fans at the rear eject hot air from the drive bay section. The side panels feature two bands of circular perforations — top and bottom — for passive supplemental airflow. The upper section (CPU and PCIe) and lower section (drives) are thermally separated inside — a good design decision that means drive heat doesn't cook the motherboard and vice versa.

13 RGB LEDs are included. Their purpose is presumably to let you know the device is alive in a dark room, or to satisfy the demographic who believes blinking lights improve throughput.

### I/O

**Front panel (left to right):** 2× USB-A 3.0, 1× USB-C 3.0, 1× 3.5mm audio jack, 1× Power button

**Rear panel:** 1× DC barrel jack (power input), 2× Thunderbolt 4 / USB-C, 1× 10GbE RJ45 (Marvell AQC113), 2× 2.5GbE RJ45 (Intel i226), 2× USB-A, 1× HDMI 2.0, 1× DisplayPort 1.4

### PCIe Expansion

Two slots accessible via the top panel: 1× PCIe x16 (Gen 4.0, 8GB/s) and 1× PCIe x8 (Gen 3.0, 2GB/s). Supports SFF GPU cards, AI accelerators, U.2 adapters, and additional SSD expansion. The i5-1235U brings 20 PCIe lanes to the table, which is exactly why the Pro version exists — the standard ZimaCube 2's i3-1215U shares the N100's lane constraints.

## Specifications

| Specification | ZimaCube 2 Pro |
|---|---|
| Pre-installed OS | ZimaOS Plus |
| Compatible OS | CasaOS, Linux, OMV, Unraid, Home Assistant OS, TrueNAS, OpenWrt, pfSense, LibreELEC, Windows, Android |
| Processor | Intel® Core™ i5-1235U — 10 cores up to 4.40 GHz |
| GPU | — |
| Memory (default) | 16GB DDR5 4800 MT/s (2× 8GB) |
| Max Memory | 64GB SODIMM DDR5 (2× 32GB) |
| System Storage | 256GB NVMe SSD (onboard) |
| PCIe Expansion | Gen4.0 8GB/s × 1 (PCIe x16) + Gen3.0 2GB/s × 1 (PCIe x8) |
| 7th Bay | 4× M.2, 3200 MB/s R/W |
| M.2 Slots | 1× M.2 onboard (OS), 4× M.2 on 7th Bay |
| Drive Bays | 6× SATA3, supports 3.5″ & 2.5″ HDD/SSD |
| Network | 2× Intel i226 2.5GbE + 1× Marvell AQC113 10GbE |
| Thunderbolt 4 | 2× Rear USB-C (Mac or PC direct connection) |
| USB | 4× USB-A 3.0, 1× USB-C 3.0 |
| Display | DP 1.4 × 1, HDMI 2.0 × 1 |
| Audio | 3.5mm audio jack × 1 |
| RGB | 13 RGB LEDs |
| Colour | Black |
| Dimensions (W×D×H) | 240 × 221 × 220 mm |
| Power | 19V 13A, 247W |

## First Impressions

The packaging and presentation set a high bar. The device largely meets it physically. For a piece of homelab equipment that could have shipped in a plain brown box with a warranty card, IceWhale have done something that most enterprise NAS vendors have never bothered with: they made the object feel worth owning before you have turned it on.

The hardware spec is genuinely capable. An i5-1235U with 10GbE, Thunderbolt 4, and a PCIe x16 slot in a 240mm cube is not something you can easily replicate with off-the-shelf components in this form factor. The compromises — sharp corners, flexible grilles, a Phillips screwdriver nobody needed — are real but minor.

One honest note on the RAM: the ZimaCube 2 Pro ships with 16GB DDR5 as standard, which is adequate but not generous given the ambition of the platform. With six drives, a 10GbE NIC, and a PCIe card potentially in play, the upgrade path to 64GB is real and worth budgeting for from day one.

What comes next: drive installation, ZimaOS initial setup, and some baseline performance numbers. This is an unboxing post — the device has not been turned on yet. Conclusions will have to wait.

The box was very nice, though.
