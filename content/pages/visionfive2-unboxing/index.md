---
title: "StarFive VisionFive 2 — First Impressions and Unboxing"
date: 2024-01-11
draft: false
layout: "lab-log"
description: "Unboxing and first impressions of the StarFive VisionFive 2, the first high-performance RISC-V SBC with integrated 3D GPU and dual Gigabit Ethernet."
slug: "visionfive2-unboxing"
url: "/visionfive2-unboxing/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "StarFive Technology · Personal Purchase"
series: "riscv-lab"
toc: false
tags:
  - riscv
  - sbc
  - starfive
  - visionfive2
  - homelab
  - linux
---

By the end of 2023, the lab was feeling reasonably coherent. The Firewalla Gold SE had the network under control, the ZimaBoard 832 was handling local services — Jellyfin, Plex, Immich — and somewhere in a shipping container, my crowdfunded ZimaBlade 7700 was making its way toward me. I had no pressing need for more hardware.

And yet.

The RISC-V coverage had been building for months, and there's a particular itch that comes from reading about an architecture described as "the Linux of hardware." The comparison is apt: open-standard, royalty-free, theoretically transparent down to the silicon. No 40 years of x86 legacy bolted on top like load-bearing scaffolding that nobody can remove because something, somewhere, still depends on it.

On January 3rd, 2024, the curiosity won. I ordered the StarFive VisionFive 2 from Amazon. It arrived about five days later.

## Why RISC-V

The short version: RISC-V is an open instruction set architecture. Anyone can implement it. Nobody owns it. Intel and AMD own x86; ARM Holdings owns ARM — meaning every chip manufacturer building on those architectures pays a licensing fee that eventually finds its way into the price of your hardware. RISC-V removes that layer entirely.

Beyond economics, the architecture is lean by design. "Reduced Instruction Set" is the name, and unlike x86, which has been accumulating instructions since the 1970s, RISC-V starts clean. The base integer instruction set is 47 instructions. Extensions are additive and optional. The result is a chip that runs cooler, consumes less power, and does exactly what you ask it to do without dragging decades of compatibility baggage along for the ride.

Whether that matters to your homelab in 2024 is a different question. But it mattered enough to make me curious.

## The Field in Early 2024

Before committing to the VisionFive 2, the obvious alternatives were sitting right there.

The **Raspberry Pi 5** had just launched. Broadcom BCM2712, four ARM Cortex-A76 cores at 2.4 GHz, software ecosystem that just works. If you want a media player, a desktop replacement, or a board where you spend time on your project rather than on getting the OS to boot, the Pi 5 is the answer. The software is the most polished in the category. It is also ARM, which is proprietary, and at the time it shipped without a built-in NVMe slot — you needed a HAT to add one.

The **ZimaBoard 832** was already on my bench. Intel Celeron N3450, x86-64, dual Gigabit Ethernet, dual SATA, PCIe 2.0 × 4 slot, 8GB RAM soldered on. The single most practical SBC in a homelab context because it runs anything built for standard x86: Docker containers, Windows, Linux, without any of the architectural hunting that ARM and RISC-V require. It is what it is: a mini-server in a credit-card-with-ambitions form factor.

The VisionFive 2 was the third option. Slower than the Pi 5, less software-compatible than the ZimaBoard, more complex to get running than either. It was also the only one on the list built on an open architecture with real expansion — NVMe built in, dual Gigabit on the B variant, and a GPU that could theoretically do useful work once the drivers matured.

| | VisionFive 2 | Raspberry Pi 5 | ZimaBoard 832 |
|---|---|---|---|
| Architecture | RISC-V (open ISA) | ARM Cortex-A76 (proprietary) | x86-64 Intel (proprietary) |
| SoC | StarFive JH7110 | Broadcom BCM2712 | Intel Celeron N3450 |
| Cores / Clock | 4 × 1.5 GHz | 4 × 2.4 GHz | 4 × 1.1–2.2 GHz |
| RAM | 2 / 4 / 8 GB LPDDR4 | 4 / 8 GB | 8 GB (soldered) |
| Ethernet | Dual Gigabit (B version) | Single Gigabit | Dual Gigabit |
| Storage expansion | M.2 M-Key NVMe | PCIe 2.0 via HAT | PCIe 2.0 × 4 + 2× SATA |
| Software state (Jan 2024) | Experimental | Consumer-ready | Universal |
| Best fit | RISC-V development, exploration | General projects, media, desktop | Homelab, NAS, virtualisation |

The Pi 5 wins on raw speed and polish. The ZimaBoard wins on compatibility and practicality. The VisionFive 2 was the only one that offered the chance to work with an open instruction set on hardware that could actually do something useful in a network context. That framing is what justified the purchase. Whether it held up is a different question.

## The VisionFive 2

The StarFive VisionFive 2 was notable — at the time of its release — for being the first high-performance RISC-V SBC with a real integrated 3D GPU and dual Gigabit Ethernet. Previous RISC-V boards existed but were largely development tools: useful if you were compiling kernels, less useful if you wanted to run a network service or stream a video.

The JH7110 SoC drives it: a 64-bit quad-core RISC-V implementation using SiFive U74 cores, running at up to 1.5 GHz. The GPU is an Imagination IMG BXE-4-32 MC1, supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.2. My unit is the 8GB LPDDR4 variant.

For connectivity: four USB 3.0 Type-A ports, dual Gigabit Ethernet, HDMI 2.0 (4K@30fps), a 40-pin GPIO header, a microSD slot, an M.2 M-Key NVMe slot, and a USB-C port for power at up to 30W via QC/PD 2.0. The board measures 100mm × 74mm — slightly larger than a Raspberry Pi 4, and the extra real estate is visible in the port density.

| Spec | Detail |
|---|---|
| SoC | StarFive JH7110 (SiFive U74, 64-bit quad-core RISC-V) |
| CPU speed | Up to 1.5 GHz |
| GPU | Imagination IMG BXE-4-32 MC1 |
| GPU APIs | OpenCL 3.0, OpenGL ES 3.2, Vulkan 1.2 |
| RAM | 8GB LPDDR4 (also available in 2GB, 4GB) |
| Storage | microSD, eMMC socket, M.2 M-Key (NVMe), QSPI Flash |
| Ethernet | Dual Gigabit RJ45 (model VF202080-B0, B version) |
| USB | 4× USB 3.0 Type-A, 1× USB-C (power + device) |
| Display | HDMI 2.0 (4K@30fps), MIPI DSI (1× 2-lane, 1× 4-lane) |
| Camera | 1× 2-lane MIPI CSI |
| GPIO | 40-pin header (Raspberry Pi-compatible layout) |
| Audio | 3.5mm 4-pole stereo jack |
| Power | USB-C, QC/PD 2.0, up to 30W |
| Dimensions | 100mm × 74mm |

## Packaging

It arrived in a blue-and-black shrinkwrapped box. The StarFive branding is on the front panel; the product information is on the side label — model VF202080-B0, the "B version" Gigabit variant, sourced through a youyeetoo reseller. A youyeetoo label was affixed over part of the barcode, which tells you immediately this unit traveled through a middleman before reaching Amazon.

{{< gallery >}}
{{< labimg src="retail-box-side.jpg" caption="The retail box. Blue-black with circuit-trace aesthetics and StarFive branding." id="retail-box-side" >}}
{{< labimg src="retail-box-label.jpg" caption="Side label: model VF202080-B0, the B version Gigabit variant. youyeetoo reseller sticker present." id="retail-box-label" >}}
{{< /gallery >}}

Inside the shrinkwrap: a clear plastic hinged case, roughly the size of a small lunchbox. Inside the case: an ESD bag containing the board, seated on grey anti-static foam. No power adapter. No cable. No getting started card beyond a printed URL pointing to the wiki.

{{< gallery >}}
{{< labimg src="unbox-contents.jpg" caption="The contents: clear plastic case with ESD-bagged board inside, and the retail sleeve." id="unbox-contents" >}}
{{< labimg src="board-io-panel.jpg" caption="Board seated in the plastic tray, IO panel visible: four USB 3.0 ports, HDMI, dual Ethernet." id="board-io-panel" >}}
{{< /gallery >}}

Underwhelming? A little. But you're not buying a consumer product. You're buying a development board, and the people buying development boards already know what they need.

## The Board

Out of the ESD bag, the VisionFive 2 presents itself clearly. The JH7110 SoC dominates the top surface — StarFive branding on the package, LPDDR4 memory stacks flanking it. The four USB 3.0 ports and dual Ethernet jacks line one edge; HDMI sits between them. The 40-pin GPIO header runs along the opposite edge.

{{< gallery >}}
{{< labimg src="board-top-overview.jpg" caption="Top view of the board in its ESD bag. JH7110 SoC centre-left, GPIO header along the right edge." id="board-top-overview" >}}
{{< labimg src="board-top-alt.jpg" caption="Alternate top angle. The LPDDR4 package and SiFive SoC branding are visible." id="board-top-alt" >}}
{{< /gallery >}}

{{< gallery >}}
{{< labimg src="board-bottom.jpg" caption="Bottom of the board: microSD card slot lower-left, M.2 M-Key connector exposed." id="board-bottom" >}}
{{< labimg src="board-edge-connectors.jpg" caption="Edge view showing the MIPI DSI and MIPI CSI FPC connectors on opposing sides." id="board-edge-connectors" >}}
{{< /gallery >}}

The build quality is competent. Nowhere near the industrial-grade finish of the ZimaBoard 832's machined aluminium body, but appropriate for a development board in this category and price range.

## In the Case

Eight days later, I assembled the clear acrylic case I had ordered alongside the board. It is designed specifically for the VisionFive 2, requires no tools, and took about ten minutes. Four threaded standoffs, a snap-fit top panel, and a 30mm brushless fan — a SHCHV LD3007MS running at 5V DC, 0.20A — that mounts directly over the SoC and plugs into the board's 2-pin fan header.

{{< gallery >}}
{{< labimg src="case-io-panel.jpg" caption="Assembled case, IO panel facing out. USB 3.0 ports, HDMI, and dual Ethernet all accessible." id="case-io-panel" >}}
{{< labimg src="case-fan-top.jpg" caption="Top panel with fan installed. SHCHV LD3007MS, 30mm, 5V brushless. Moves adequate air." id="case-fan-top" >}}
{{< /gallery >}}

{{< gallery >}}
{{< labimg src="case-bottom.jpg" caption="Bottom side of the case. The microSD slot and USB-C power port are exposed through cutouts." id="case-bottom" >}}
{{< labimg src="case-power-gpio.jpg" caption="Opposite side: USB-C power port and GPIO header visible through the clear acrylic." id="case-power-gpio" >}}
{{< /gallery >}}

{{< labimg src="case-vents-bottom.jpg" caption="Ventilation slots on the underside. PCB traces visible through the clear base panel." id="case-vents-bottom" >}}

The case does what it needs to do: keeps the board off the desk, keeps fingers off the components, and moves enough air to keep thermals manageable. Acrylic scratches if you look at it wrong and has a limited service life under continuous use, but as a working enclosure in a lab context, it is adequate.

The fan speed is fixed at full until you configure a thermal profile in software. Out of the box: audible, not silent.

## Software Landscape, January 2024

The hardware was capable. What you could do with it in January 2024 depended heavily on your tolerance for a terminal and your definition of "ready."

The most stable path was StarFive's own Debian engineering release — pre-built images for SD, eMMC, and NVMe boot, with curated repositories covering Firefox, LibreOffice, and VLC. Ubuntu Server ran cleanly at 23.10 and in early 24.04 builds, though GPU acceleration was not functional at that stage. openSUSE Tumbleweed had RISC-V images available by mid-January. Fedora supported the board but wanted its own firmware builds to unlock the full feature set.

Desktop environments existed — GNOME, XFCE — but with caveats. Wayland fared better than X11 because the community was betting on Vulkan rendering via the Imagination GPU rather than the legacy X11 pathway. You could run a desktop. Calling it smooth would be generous.

Where the board was genuinely ready: development. A native RISC-V environment for compiling C, C++, or Rust without cross-compiling from an x86 machine — the VisionFive 2 delivered that cleanly. The dual Gigabit Ethernet and M.2 NVMe slot made it credible as a low-power file server or network gateway. The 40-pin GPIO and MIPI CSI port opened paths toward industrial IoT and camera work.

The bottom line: powerful sandbox, January 2024 edition. Server tasks and development were production-ready. The polished desktop experience was being assembled by the community in real time. Whether you found that exciting or frustrating depended entirely on why you bought it.

I found it exciting. More on what I actually did with it in a future entry.
