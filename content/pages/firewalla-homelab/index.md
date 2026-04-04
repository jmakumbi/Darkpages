---
title: "Firewalla: Nine Features, One Obsessive Configuration"
date: 2026-04-04
draft: false
layout: "lab-log"
description: "How I've configured every significant Firewalla Gold SE feature — dual WAN failover, 53 rules, 57.5 million blocked flows, and what I still haven't touched. Hands-on before a client recommendation."
slug: "firewalla-homelab"
url: "/firewalla-homelab/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Firewalla Gold SE · Homelab · Kampala"
series: "homelab-build"
toc: false
tags:
  - firewalla
  - homelab
  - network-security
  - kampala
  - dual-wan
  - ips-ids
---

I had a client I was going to recommend Firewalla to. An important one. Before I recommend anything I expect someone else to run, I run it myself first. This is a rule without exceptions — I've been burned enough times by recommending things I'd only read about to know the value of having actual skin in the game.

So I bought the Gold SE. Mid-range of the Gold line. Sufficient for the client's likely use case. Replaced the ISP-supplied router over an afternoon that included several reboots and one genuine moment of uncertainty about whether the MTN backup SIM was going to cooperate. Everything is fine now. This page is a follow-up to the Firewalla devices and apps overview — that one covers the product range and what the spec sheet says; this one covers what it does when it's been running your network for months and you've had time to make decisions you'll have to live with.

## The Network

<div class="gallery-grid gallery-portrait">
{{< labimg src="network-manager.png" caption="Network Manager showing dual WAN — Fibre active, MTN Backup on standby." id="network-manager" >}}
{{< labimg src="device-list.png" caption="The full device list with groups. Cameras, Quarantine, RiscV, zimas — all deliberate." id="device-list" >}}
</div>

Dual WAN: 200Mbps fibre as primary (DHCP, always active) and an MTN 4G SIM as standby. Multi-WAN Failover mode. The handoff is clean enough that when the MTN link cycled at 21:12 one evening and came back at 21:15, I only knew about it from the alarms log. Not from anything stopping.

The device list shows green dots for devices live at time of writing, white for offline. Not everything is always on — this is a homelab, not a data centre. 27 wired devices in total.

On wireless: I have a separate router running in bridge mode, which keeps wireless and wired devices on the same subnet. This is why Firewalla shows zero registered wireless devices — the access point is bridged through rather than managed directly by Firewalla. It works. It is also architecturally sloppy, and I'm aware.

Device groups: Cameras (3 devices — IP cameras, ring-fenced), Quarantine (3 devices), RiscV (1 device — single-board cluster experiment), zimas (3 devices — ZimaCube 2 Pro and associated storage nodes). Quarantine is a trip-wire, not a staging area. Any device that joins the network without prior approval — wired or wireless — gets automatically placed in Quarantine: no internet, no LAN access, nothing. My phone gets an alert. No traffic flows until I make a deliberate decision about that device. Someone plugging into a wall port gets nothing, and I know about it immediately.

**The outstanding issue:** everything wired and wireless is currently on a flat subnet, with Firewalla groups doing rule-based isolation. That is not network segmentation. The cameras are in a group with block rules — they are not on a dedicated VLAN that is physically incapable of talking to the main network. Quarantine devices are rule-blocked, not airgapped at the network layer. This needs to change. The Gold SE supports VLANs. My current wireless router in bridge mode complicates implementation. This is the work item that matters most and that I keep deferring.

<div class="stats-band">
  <div class="stat-item">
    <div class="stat-number">27</div>
    <div class="stat-label">Devices</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">53</div>
    <div class="stat-label">Rules</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">57.5M</div>
    <div class="stat-label">Blocked</div>
  </div>
</div>

## Overview

<div class="gallery-grid gallery-portrait">
{{< labimg src="features-list.png" caption="The full Firewalla features list. Enabled and disabled. Everything visible at once." id="features-list" >}}
{{< labimg src="feature-grid.png" caption="The icon grid view. Every feature visible, notification dots where there's activity." id="feature-grid" >}}
</div>

The features list view is the honest audit. Everything the device can do, on or off, in one place. Most home routers hide their capabilities behind menus that assume you don't want to know. Firewalla puts them in a list and tells you which ones you're not using. I find this arrangement useful — it makes decisions visible rather than buried.

## The Rules Engine

<div class="gallery-grid gallery-portrait">
{{< labimg src="rules-overview.png" caption="Rules overview. 53 rules. 59.2 million hits. 57.5 million blocked." id="rules-overview" >}}
{{< labimg src="new-rule.png" caption="Rule creation UI. Action, target, device scope, schedule. Four fields, significant power." id="new-rule" >}}
</div>

<div class="gallery-grid gallery-portrait">
{{< labimg src="rule-matching.png" caption="Rule matching options — the full target type list." id="rule-matching" >}}
{{< labimg src="target-list.png" caption="Target lists managed via MSP portal. Curated blocklists, centrally controlled." id="target-list" >}}
</div>

<div class="gallery-grid gallery-portrait">
{{< labimg src="app-blocking.png" caption="App-level blocking. TikTok. Instagram. The usual suspects." id="app-blocking" >}}
{{< labimg src="rule-schedule.png" caption="Rule scheduling options. Simple, useful, underused." id="rule-schedule" >}}
</div>

53 rules. 59.2 million total hits since January 2024. 57.5 million blocked. That's a 97% block rate. The bulk of it is ad network telemetry, tracker pings, and smart devices attempting to phone home to manufacturer servers for reasons that are rarely in the user's interest.

Rule anatomy: Action (Allow / Block / Time Limit / Disturb) → Target (IP, domain, app, category, region) → Device or group scope → Schedule (Always, Every Day, Every Week, One-Time). Four fields. The combinations are wide enough that I haven't found something I wanted to express that the rule engine couldn't handle.

**Social media policy:** I'm not a social media person. On my network, almost everything is blocked by default. The allow list is short: LinkedIn, YouTube, WhatsApp, Spotify, Netflix. That's it. TikTok, Instagram, Facebook, Twitter/X, Snapchat, Discord — blocked, not scheduled, permanently blocked. Joining my network as a guest and expecting the usual feed experience is going to be disappointing. I consider this a feature.

**Traffic flows:** I don't read them except for diagnostics. I'm not interested in what people on my network are doing online. The content filtering, ad blocking, and target list enforcement mean the worst of what could be happening already isn't. Beyond that, I don't pry.

**Smart device telemetry:** IoT devices send usage data back to their manufacturers by default — sometimes diagnostics, sometimes more. I block all outbound traffic from smart and IoT devices unless there's a specific functional reason for it to exist. Software updates happen on my schedule. Everything else is closed.

Target Lists are managed via the MSP portal (My Portal), meaning they're centrally controlled and not touchable from the local app — this is intentional, not a limitation. Active lists: DShield Block List, HaGeZi's Pro Blocklist, Newly Registered Domains, NSFW AI List, Tor Exit and Full Nodes, Crypto List, DoH Services. Apple Private Relay gets a pass. OISD is a pending decision.

## Protect and Scan

<div class="gallery-grid gallery-portrait">
{{< labimg src="protect-settings.png" caption="Protect dashboard — DAP, Active Protect, Firewalla AI." id="protect-settings" >}}
{{< labimg src="scan-results.png" caption="Scan results. No external ports, no vulnerabilities, no port forwarding." id="scan-results" >}}
</div>

Device Active Protect is set to Strict mode. Seven devices in Learning (traffic baseline being built), two Active, zero Optimizing. Last DAP action at 01:43. The dual-engine IPS/IDS has caught nothing noteworthy. I prefer to read that as the network being clean, not as the sensors being inadequate — but I note both interpretations exist.

Firewalla AI is enabled and earns its keep when something starts phoning home unexpectedly. Unknown domains become identifiable quickly enough that you can make a rule decision before the traffic has been flowing for long.

External port scan: no open ports found (last scanned 14 March). System vulnerability scan: nothing found (last scanned 30 March, automatic scans on). Port forwarding: none configured. No ports forwarded. No exceptions. This is a deliberate posture, not a gap I haven't gotten to.

## DNS and Services

<div class="gallery-grid gallery-portrait">
{{< labimg src="services-dns.png" caption="Services — DNS over HTTPS on, Unbound off, NTP Intercept on." id="services-dns" >}}
{{< labimg src="smart-queue.png" caption="Smart Queue — Adaptive mode, CAKE algorithm selected." id="smart-queue" >}}
</div>

DNS over HTTPS is on for all devices. This matters specifically on Ugandan ISP connections, where DNS hijacking to inject redirect pages is a documented and recurring occurrence — not a theoretical concern. DoH sidesteps this cleanly.

Unbound is off. I considered it. The latency penalty on 4G failover didn't justify local recursive resolution for a mixed-use network where most of the benefit would be invisible in practice.

NTP Intercept is on for all networks. Intercepts external NTP requests and handles them locally. Most home setups skip this; it creates subtle problems for log correlation and certificate validation that appear entirely unrelated to their actual cause.

RADIUS Server is off. No enterprise Wi-Fi auth use case currently. Will revisit when the AP situation is resolved.

**Smart Queue:** Adaptive mode, CAKE algorithm. On 200Mbps fibre, largely invisible — things just work. On MTN 4G backup at 20Mbps, CAKE's per-flow fairness and active queue management are the difference between video calls that degrade gracefully and video calls that simply stop. Not a debatable choice on a dual-WAN setup where the backup link is asymmetric.

## Ad Block and Family

<div class="gallery-grid gallery-portrait">
{{< labimg src="adblock-settings.png" caption="Ad Block configuration. Strict mode. All devices. No exceptions." id="adblock-settings" >}}
{{< labimg src="family-settings.png" caption="Family features — Family Protect native mode, Safe Search on, Social Hour off." id="family-settings" >}}
</div>

Ad Block is Strict mode, all devices. No blanket exceptions — domain-level Allow rules where strict blocking breaks a legitimate service. The performance angle is worth stating plainly: blocking ads and tracking scripts is also a bandwidth optimisation. Every blocked tracker request is a round trip that doesn't happen. On a connection where every megabit counts — and on MTN 4G backup, it does — this is not a minor consideration.

Family Protect is on in Native mode, all devices. DNS-level filtering for violent and pornographic content. Native mode is harder to circumvent than proxy-based approaches, and occasionally broad in what it catches. I have yet to encounter a catch that was a genuine inconvenience.

Safe Search is on across all major platforms. Social Hour is off — the social media situation is handled permanently at the rule level, and a scheduled block on top of a permanent block would be redundant.

## VPN

<div class="gallery-grid gallery-portrait">
{{< labimg src="vpn-client.png" caption="VPN Client options. All modes available, none currently active." id="vpn-client" >}}
{{< labimg src="vpn-server.png" caption="VPN Server. OpenVPN, WireGuard, AmneziaWG. All off for now." id="vpn-server" >}}
</div>

None of the VPN options are active. This is not an oversight. There are three compounding problems, all specific to Uganda.

**CGNAT.** MTN and most Ugandan ISPs use Carrier-Grade NAT. You don't get a routable public IP address. Running a VPN server from behind CGNAT without additional infrastructure — a VPS with a public IP to tunnel through, or a service like Cloudflare Tunnel — is effectively impossible. The Firewalla VPN Server options assume you have a real public IP. Most residential connections in Uganda don't have one.

**ISP/UCC protocol blocking.** VPN protocols are being blocked or throttled by Ugandan ISPs, possibly at the direction of UCC (Uganda Communications Commission), though this isn't officially confirmed. OpenVPN and WireGuard traffic can be fingerprinted at the packet level and suppressed — MTN in particular. Standard VPN Client options are unreliable in this environment.

**AmneziaWG.** Specifically interesting because it's designed to evade protocol-level blocking — it disguises VPN traffic to look like normal HTTPS. On a network where the ISP is actively suppressing VPN connections, AmneziaWG isn't a nice-to-have, it's the only option worth attempting. It's on the list. Fix the link stability first, then address the CGNAT and blocking problems. AmneziaWG when the infrastructure is ready.

The MTN backup link keeps cycling (hence 13,503 alarms) because the Freedom Bundle isn't loaded on that SIM and because MTN's 5G requirements haven't been fully met. Building VPN infrastructure on an unstable backup link would be premature regardless of the other constraints.

## Alarms

{{< labimg src="alarms-overview.png" caption="Alarms log — 13,503 entries, mostly failover connectivity updates." id="alarms-overview" >}}

13,503 total alarms. The overwhelming majority are Internet Connectivity Updates — the failover system faithfully documenting each MTN connect and disconnect cycle.

The root cause of the cycling is two fixable things I haven't fixed yet. First, the MTN backup SIM doesn't have a Freedom Bundle loaded — without it, MTN's handling of the connection is less stable. Second, MTN has specific requirements for reliable 5G connectivity that I haven't fully cleared. The result is a backup WAN that reconnects frequently and generates alarms that are technically correct and operationally annoying.

The Security, Abnormal Upload, and Open Port filter tabs are where the useful signal lives. The full count is infrastructure noise.

## What I Haven't Done

<div class="postscript-card">

{{< labimg src="wifi-setup.png" caption="The Wi-Fi access point setup screen I haven't acted on yet. I know." id="wifi-setup" >}}

**VLANs.** This is the real priority. Everything wired and wireless is on a flat subnet — Firewalla groups doing rule-based isolation, which is not network segmentation. The cameras need a VLAN that is physically incapable of talking to the main network. The Quarantine group needs to be airgapped at the network layer, not just rule-blocked. The Gold SE supports all of this. My wireless router in bridge mode is the current obstacle — an AP with proper VLAN tagging support would resolve it. The Firewalla AP7 is the obvious candidate. This will not be deferred much longer.

**Freedom Bundle on the MTN SIM.** Needs to happen before the backup WAN alarm noise becomes acceptable.

**MTN 5G requirements.** A set of hoops I haven't finished jumping through. Related to the above.

**Wi-Fi AP.** Still on the "Add Your First Access Point" screen. See VLANs, above.

**RADIUS.** Off. Staying off until there's an AP that makes it relevant.

**VPN.** Blocked by CGNAT and ISP-level protocol suppression. AmneziaWG when the infrastructure supports it.

</div>
