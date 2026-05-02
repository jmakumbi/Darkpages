---
title: "Firewalla Gold SE: A Firewall That Actually Does What It Says"
date: 2023-10-20
draft: false
layout: "lab-log"
description: "Two years with the Firewalla Gold SE in a Kampala homelab. Dual-WAN, child profiles, 46% of all traffic blocked. It works."
slug: "firewalla-gold-se"
url: "/firewalla-gold-se/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Firewalla · Personal Purchase · Kampala, Uganda"
series: "homelab"
toc: false
disclosure: false
tags:
  - firewalla
  - networking
  - firewall
  - homelab
  - security
  - kampala
  - uganda
  - routing
---

<div class="opening-aside">This was written on the 5th of April 2026. It is being published on the 2nd of May. Twenty-seven days in a folder is not a record, but it is an achievement. In my defence, the Firewalla was working fine the whole time — which is, on reflection, precisely the problem.</div>

## The Box

I ordered the Firewalla Gold SE on the 2nd of August 2023. I received it in October. That gap — eleven weeks — is not a DHL problem. DHL is excellent. The problem was that Firewalla had no shipping arrangement to Uganda. They could ship to Nairobi. Nairobi is a fine city but it is not Kampala, and getting a package across that particular border involves a sequence of phone calls, a cooperative third party, and a certain tolerance for logistical improvisation that you either already have or you acquire quickly. Anyone importing hardware into East Africa knows the sequence. Everyone else should factor it into their delivery expectations before checking out.

The box, when it finally arrived, was plain off-white with "Firewalla" printed in dark type on the lid. No product photography. No tagline. No rendering of the device at a flattering angle with soft light and a blurred background. Either the packaging team had tremendous confidence or they simply ran out of ideas and nobody pushed back. I choose to read it as the former.

{{< gallery >}}
{{< labimg src="box-closed.jpg" caption="The retail packaging. Plain off-white, brand name in dark type. Nothing else. Confident or lazy — I chose confident." id="box-closed" >}}
{{< labimg src="box-open.jpg" caption="First look inside. Quick-start card on top, unit in the grey foam tray beneath." id="box-open" >}}
{{< /gallery >}}

Inside: the unit, a power adapter, a USB cable, a sticker sheet, and a small quick-start card. No printed manual. The manual is the internet. This is fine.

{{< labimg src="contents-spread.jpg" caption="Everything it ships with. Box (upside down, because I was photographing the contents), sticker sheet, USB cable, power adapter. No printed manual." id="contents-spread" >}}

## Hardware

The enclosure is black anodised aluminium with yellow plastic end-caps. It looks like something a safety inspector would carry. Whether that is good design language for a security device I leave to the reader.

Front panel: four RJ45 ports. Port 1 and port 4 are 2.5Gb. Ports 2 and 3 are 1Gb. There is a status LED on the far left and a USB-C power port on the far right. That is everything on this side. The restraint is either deliberate or they ran out of panel.

The rear panel is the less photogenic face. It has a recessed reset button, a microSD card slot, an HDMI port, and two USB-A ports. The HDMI port is for console access. It is not a media centre. The USB ports accept storage for local network shares or VPN configuration files, which is more useful than it sounds.

{{< gallery >}}
{{< labimg src="ports-front.jpg" caption="Front panel. Ports 1–4 left to right. Status LED far left, USB-C power far right. Ports 1 and 4 are 2.5Gb; 2 and 3 are 1Gb." id="ports-front" >}}
{{< labimg src="ports-rear.jpg" caption="Rear panel. Reset, microSD, HDMI, two USB-A ports. The HDMI is for console access. It is not a television." id="ports-rear" >}}
{{< /gallery >}}

The red dongle deserves its own mention. It ships plugged into one of the rear USB ports. This is Firewalla's hardware security key — it stores the encrypted keys for VPN tunnels and secure device communications. You do not technically interact with it directly. You just leave it there. The instruction is simple: do not lose it. Firewalla will replace it if you do, but it is an unnecessary exercise in patience and shipping logistics. It glows red, which is either a threat or an aesthetic choice. Possibly both.

{{< gallery >}}
{{< labimg src="dongle-installed.jpg" caption="The red security dongle installed. This is the hardware security key for encrypted communications. Do not lose it." id="dongle-installed" >}}
{{< labimg src="unit-top.jpg" caption="The unit as it sits. Black aluminium, yellow end-caps. Looks like a safety inspector's lunch box. Means it every bit." id="unit-top" >}}
{{< /gallery >}}

The specification that justified the purchase is not visible from the outside. Ports 3 and 4 are dual-function: they can act as standard LAN ports or as WAN uplinks. This means two internet connections, simultaneously, with the device managing them. You can bond them for combined throughput, load-balance across them, or configure one as automatic failover for the other. In Uganda, where ISP reliability ranges from "mostly fine" to "maybe tomorrow," that last option is not a luxury.

Under the casing, this is a small Linux PC — Ubuntu 22.04.2 LTS, kernel 5.10.110. That is more significant than the spec sheet implies. There is a community at [community.firewalla.com](https://community.firewalla.com) running Docker-based extensions, custom configurations, and deeper packet inspection setups on top of the base OS. Future posts will cover what is possible at the software layer. The hardware layer, however, is a closed door: the Gold SE does not support RAM or storage upgrades. I was genuinely looking forward to opening it up. I was genuinely disappointed. I will live with it and do something interesting with the software stack instead.

| Spec | Detail |
|------|--------|
| Processor | Quad-core ARM Cortex-A55, 1.8GHz |
| RAM | 4GB DDR4 |
| Storage | 32GB eMMC |
| Ports | 2× 2.5GbE (ports 1 & 4), 2× 1GbE (ports 2 & 3) |
| WAN capable | Ports 3 and 4 (dual-WAN, failover or load balance) |
| USB | 2× USB-A (rear) |
| Display | HDMI (console access) |
| Storage expansion | microSD |
| Power | USB-C (included adapter) |
| Security | Hardware security dongle (USB) |
| Dimensions | 120 × 90 × 30 mm |
| Weight | ~380g |
| Management | Mobile app (iOS/Android), my.firewalla.com, firewalla.net |
| Firmware updates | Over-the-air, automatic |

## The Setup

I had four connections to route. Port 1 goes into a TP-Link TL-SG108E managed switch for the wired LAN. Port 2 feeds a TP-Link Archer C6 for wireless. Port 3 was the Airtel WiMAX uplink. Port 4 carries MTN Fibre as the primary WAN. Wired and wireless are on separate subnets, which is less paranoid than it sounds — it was a practical necessity. I needed IoT devices and cameras on the wired side to be network-isolated from the wireless client devices. The Firewalla handles subnet-to-subnet rules without requiring complex VLAN configuration, which is why I did not bother with either.

{{< labimg src="installed-lab.jpg" caption="In production. Sitting on the router, cables going in all four ports. This is what organised chaos looks like when it actually works." id="installed-lab" >}}

The Airtel WiMAX connection lasted about two months. Airtel sells data bundles with a hard expiry at the end of each calendar month, used or not. Buy 100GB on the 29th and you have 48 hours. MTN's Freedom Bundle takes a different position: the data does not expire. Minimum validity is 365 days from the purchase date. That is not a rollover policy — that is data you bought, that you keep. The difference is significant enough to choose one ISP over another, which is exactly what I did.

## Software & Management

There are three ways to reach a Firewalla dashboard. [my.firewalla.com](https://my.firewalla.com) is the free web portal. [firewalla.net](https://firewalla.net) — now branded as Firewalla MSP — is the paid tier for managing multiple networks from a single interface. The mobile app (iOS and Android, free) is the interface Firewalla actually intends you to use, and it earns that role.

A clarification before the screenshots: the my.firewalla.com dashboard below is a client network I manage remotely — 174 devices, their alarms, their rules. That client opted out of cloud management for their own unit, which is a reasonable position; the phone app handles everything they need. The firewalla.net MSP dashboard is my own homelab. I pay for the MSP tier because my principle is straightforward: I will not recommend something to a client that I have not run myself first.

The mobile app is where you will spend most of your time. Rules, device grouping, family profiles, VPN configuration, and the real-time alarm feed are all accessible without wanting to close the app and phone someone. The web dashboards are better for reading telemetry at scale and for bulk rule management. The web portal was read-only when I first deployed this in 2023 — it has since gained the ability to configure firewall rules, release quarantined devices, and investigate specific access blockages. Still not as capable as the app, but no longer just a display.

One feature worth mentioning explicitly: the device is manageable via Bluetooth through the mobile app when you are physically nearby. If your internet connection goes down and you need to switch WAN ports or reconfigure an ISP, Bluetooth is sufficient. You do not need working internet to manage the device that manages your internet. In Uganda, this is a practical feature, not a marketing checkbox.

{{< labimg src="app-screenshot.png" caption="The mobile app dashboard for the Dark-Gate network. 144GB Fibre usage with 26 days remaining, MTN backup barely touched. The child profile blocks are visible on the bottom carousel." id="app-dark-gate" portrait="true" >}}

Live throughput is only visible when you are on the same local network as the Firewalla — this is not a cloud view. The screenshot below was taken during a working afternoon: Fibre running at 9.43 Mb/s, with GTVS — the TV — consuming 9.06 Mb/s of that. Netflix was on the TV, not the desktop. DarkZen, my desktop, was at 55 kb/s doing work traffic. MTN Backup at 1 kb/s, which is exactly what a standby connection should look like when the primary is functioning.

{{< labimg src="live-throughput.png" caption="Live throughput on a working afternoon. Fibre at 9.43 Mb/s, the TV (GTVS) consuming almost all of it at 9.06 Mb/s. MTN backup at 1 kb/s, doing nothing useful, exactly as intended." id="live-throughput" portrait="true" >}}

Family controls are built into the management layer, not bolted on. The child profile named "zimas" has TikTok and Roblox on global block, a category-level adult content block, and a scheduled internet-off window. Configured in under five minutes from the app. The blocking works at the network layer — not an app filter that a browser workaround defeats, not a DNS trick that a VPN bypasses. Network-level means network-level.

The blocked flows numbers are the ones that get attention. On the client network: 43,903 flows blocked out of 94,433 total in the last 24 hours. That is 46.5% of all outbound connections stopped. If your current router is not showing you this data, it is not because nothing is happening. It is because your router does not know, or does not consider it your business to know.

{{< gallery >}}
{{< labimg src="dashboard-myfirewalla.png" caption="my.firewalla.com — the free web portal. 174 devices, 108 alarms, 47 rules, 46.5% of all flows blocked in the last 24 hours. A quiet day." id="dashboard-myfirewalla" >}}
{{< labimg src="dashboard-msp.png" caption="The Firewalla MSP portal — the paid tier for managing multiple networks. More telemetry, more detail. The daily blocked flows chart alone justifies the subscription." id="dashboard-msp" >}}
{{< /gallery >}}

## Terminal Access

SSH is always on. It cannot be disabled. This is a design decision, not an oversight, and it is the correct one — a device you cannot access when the management interface is unavailable is a device you do not fully control. The tradeoff Firewalla makes is that the SSH password is randomly generated on the device, changes periodically, and is only visible inside the Firewalla app linked to that specific unit. It is not stored on a server. It is not transmitted anywhere. It is, by any reasonable measure, actually secure.

Access is configurable per interface from the app. The WAN interfaces — Fibre, MTN Backup — are off by default, and the app notes plainly that opening SSH to WAN interfaces is not recommended from a security perspective. This is correct and should be left as-is. Wired LAN access is on by default. OpenVPN, WireGuard, and Wireless are individual toggles depending on what your setup uses.

{{< labimg src="ssh-console.png" caption="SSH access settings in the app. WAN interfaces (Fibre, MTN Backup) are off by default — correctly so. Wired LAN access is on. The password is randomly generated and lives only in the app." id="ssh-console" portrait="true" >}}

The MOTD on login is the kind of thing that either means something to you or it does not. FIREWALLA GOLD SE in ASCII across the top. Ubuntu 22.04.2 LTS, kernel 5.10.110. System load 1.2, memory at 42%, swap at zero, temperature 55.6°C, 270 processes running. A well-behaved box, doing its work quietly.

{{< labimg src="ssh-terminal.png" caption="The MOTD on login. Ubuntu 22.04.2 LTS, kernel 5.10.110. System load 1.2, memory at 42%, temperature 55.6°C, 270 processes. Everything running, nothing alarming." id="ssh-terminal" >}}

I am a terminal person. Given the choice between a dashboard and a shell prompt, I will take the shell. This is a Linux machine sitting at the edge of my network, and the fact that I can SSH into it and work directly — inspect processes, examine traffic, run custom scripts, or extend the stack with Docker — is not a minor feature. It is the feature that separates this from a consumer router for someone with my particular inclinations. The UI is well designed. The terminal is better. Future posts in this series will get into what is actually possible from inside the machine.

## Two Years In

No hardware failures. No unexpected reboots. The status LED on the front panel has been solid green since October 2023. Firmware updates happen automatically and silently — I have never had to think about them, which is the correct way for firmware updates to work.

The dual-WAN failover has triggered several times during MTN outages. Each time, it switched to the backup connection without me noticing until I checked the logs afterward. That is what failover is supposed to do. It is supposed to be invisible. It was.

One legitimate complaint: the mobile app requires a Firewalla account and active cloud connectivity to function normally. If the Firewalla cloud infrastructure is unavailable, remote management via app is unavailable. The Bluetooth management option exists precisely for this scenario — you can still reach the device locally when cloud is down — but it is worth knowing the dependency exists before you commit. I understand the security rationale. I still note the constraint.

The web portal at my.firewalla.com works around this to some degree, and the MSP portal adds enough additional telemetry and cross-network visibility to be worth the subscription cost if you are managing more than one Firewalla. For a single-device home network, the free tier is sufficient. For a homelab with multiple VLANs, monitored connections, and devices you are actually trying to understand rather than just connect, the MSP tier is worth considering.

The TL-SG108E is on its way out. In practice, I cannot get it to transfer at 1Gbps regardless of what the specification says. The replacement is a MokerLink 8 Port 2.5 Gigabit Managed Switch — partly because 2.5G per port matches what port 1 on the Firewalla is actually capable of, and partly because I am done leaving throughput on the table by accident.

The larger consequence of this device is harder to quantify in a single post. Managing a Linux machine sitting at the edge of my network — SSH access, real traffic data, granular control — made me think seriously about what else could run at the network edge. That line of thinking led directly into single-board computers: a Lenovo M900s Tiny, RISC-V development boards, and eventually the ZimaCube and ZimaBoard ecosystem. Each of those is its own lab-log. The TP-Link Archer C6 on port 2 has since been flashed to OpenWRT, which is also its own story. The Firewalla did not cause any of this directly. It just made the question feel worth asking.

Would I buy it again. Yes, with the caveat that getting it to Uganda is its own project. The device is competent hardware running software that takes network visibility seriously. In a market where most consumer routers consider their job done once you have an IP address and a blinking light, the Firewalla disagrees — in a way that turns out to matter.
