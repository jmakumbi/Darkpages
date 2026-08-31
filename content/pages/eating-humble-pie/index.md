---
title: "Eating Humble Pie"
date: 2026-08-31
draft: false
layout: "lab-log"
description: "A retraction: ZeroTier wasn't the vulnerability in ZimaOS's remote-access feature. Two other things were, and Engagement 7 found them."
slug: "eating-humble-pie"
url: "/eating-humble-pie/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "I was wrong about ZeroTier, and Engagement 7 is why"
toc: false
disclosure: false
tags:
  - zerotier
  - zimaos
  - icewhale
  - security
  - homelab
  - vulnerability-assessment
---

I was wrong about ZeroTier, and Engagement 7 is why

For a while now I've held a strong opinion about ZimaOS: it's a great product, but the ZeroTier remote-access feature baked into it — ZimaNet — was a massive vulnerability. Enough of an opinion that I wrote and maintained zima-harden, a set of host-hardening scripts for ZimaOS boxes. One of its three flagship jobs (alongside restoring SSH access and running a configurable firewall) was making that remote-access overlay opt-in instead of opt-out: disable and mask the ZeroTier services, blackhole the vendor's phone-home endpoints, and hand the decision back to the operator.

Today I'm reversing that call. Not the hardening itself — but the framing of ZeroTier as "the" vulnerability. It isn't. It's safe. The actual problems are two specific things sitting next to it, and I only found that out because I finally ran the numbers.

{{< labimg src="overlay-from-outside.svg" caption="Anyone with the network ID crosses this line automatically — no approval step, no notice." id="overlay-from-outside" width="1600" height="700" >}}

## How I got here

About a month ago IceWhale's Discord community was asked to test the latest client build, and I wanted in. But my own boxes were locked down hard enough — a specific UDP port and a public IP I'm not going to publish, because it's mine — that unwinding my own hardening to participate was going to take real effort. That friction is what finally pushed me to stop assuming and actually go measure the thing I'd been warning people about.

So I ran a proper internal vulnerability assessment (Engagement 7) across my home lab estate, including a dedicated investigation into exactly how the ZimaOS / IceWhale ZeroTier implementation behaves. I want to be precise about scope: what I tested was IceWhale's specific implementation of remote access on top of ZeroTier — how ZimaOS configures it, what it defaults to, what the shipped binary actually does. I was not testing ZeroTier the protocol or ZeroTier Inc.'s infrastructure. That's a much bigger job, and better-resourced people than me test it continuously. My question was narrower and vendor-specific: given that IceWhale chose to build on ZeroTier, did they build on it safely? I wanted a definitive answer to three questions: does IceWhale see your traffic, does IceWhale see your ZeroTier membership, and is IceWhale's specific implementation the flaw.

{{< labimg src="engagement7-process.svg" caption="A month of assuming, settled by one engagement of actually checking." id="engagement7-process" width="900" height="900" >}}

## What I actually found

{{< labimg src="public-by-default.svg" caption="Public by default — three of four devices carried unidentified peers, one for roughly five months." id="public-by-default" width="900" height="900" >}}

The overlay is public and joinable by anyone who has the network ID. Each ZimaOS device self-hosts its own ZeroTier network as PUBLIC, meaning anyone who obtains the 16-hex network ID can auto-join it and get an address that can reach the host. Three of my four ZimaOS devices had unidentified devices sitting on them — one for roughly five months. I want to be careful here: "unidentified" is the honest word, not "unauthorised." I can't actually attribute who or what joined — it could have been me testing something and forgetting, my Windows PC, my phone, or IceWhale support helping me with an earlier issue, since the ID had at some point been shared with them during a troubleshooting exchange. ZeroTier identities are self-minted with no real-world binding, so proving who connected — or ruling out that it was perfectly innocent — isn't something the tooling lets you do after the fact. That ambiguity is itself part of the finding.

But ZeroTier itself isn't the exposure. I checked this three separate ways:

- IceWhale doesn't see your traffic. The devices ride ZeroTier Inc.'s own public root servers, not IceWhale's. IceWhale runs neither the controller (that's self-hosted per device) nor the relays, so at the transport layer it never brokers or observes what crosses the overlay.
- IceWhale doesn't exfiltrate your membership list either. I pulled apart the ZimaOS binary that handles ZeroTier and every relevant function talks only to the local daemon on the box itself — there's no code path that uploads who's connected to any IceWhale server. The only outbound calls that binary makes are OS update downloads and reading forum announcements.
- The reason a stranger could reach in wasn't a ZeroTier flaw — it was that the join door was propped open and reachable services sat right behind it. Because the unauthenticated web terminal (ttyd) binds to all interfaces, an unidentified device joining the overlay wasn't just "on the network" — it had a real path to a root shell on the box holding my engagement data, whoever or whatever it actually was.

{{< labimg src="real-attack-path.svg" caption="ZeroTier was the road. It wasn't the open door." id="real-attack-path" width="900" height="1000" >}}

So the actual finding isn't "ZeroTier is dangerous." It's: a public auto-join overlay, sitting in front of a handful of services that don't ask for a password, is dangerous. ZeroTier was the transport. It wasn't the vulnerability.

{{< labimg src="icewhale-visibility.svg" caption="Two independent checks. Both came back clean." id="icewhale-visibility" width="900" height="900" >}}

And I want to be direct about the other half of this: I'm not just clearing ZeroTier-the-protocol. I'm clearing IceWhale. I went in with a suspicion that a vendor-run remote-access feature, enabled by default, probably meant the vendor was in the loop somehow — watching traffic, or at least collecting who's connected. I checked both, independently, rather than taking anyone's word for it, and both came back clean. That's not "benefit of the doubt." That's a verified result. IceWhale doesn't broker your traffic, doesn't see it, and doesn't harvest your membership list. There's no hidden agenda here — just a default I disagreed with.

## What's actually broken, and what isn't

### Fixed / not a real problem:

- Cloud brokering — confirmed absent, by static analysis of the binary, not by taking anyone's word for it.
- Membership exfiltration — confirmed absent, same way.

### Still genuinely wrong, and unrelated to the "is ZeroTier evil" question:

- The device ID has effectively very little real secrecy. It's discoverable on the wire, the vendor cloud holds it by design, and it leaks through logs and the CasaOS interface. "Just don't share it" was never real access control — mine got out through completely ordinary vendor support contact.
- The network is public by default. Anyone with the ID auto-joins with no approval step. Resetting the network ID evicts current members, but the freshly generated network comes back public too — so a reset buys you a clean slate, not a closed door.

{{< labimg src="subnet-mechanics.svg" caption="The protocol offers a private, approval-gated mode. IceWhale never wires it in." id="subnet-mechanics" width="900" height="1000" >}}

Both of those are real. But notice what they are: a default-configuration choice, not evidence of anything adversarial. "Public network, auto-join" is a decision you can disagree with — I do — without it implying IceWhale is trying to get at your data. Every path I could check for actual bad intent (traffic visibility, membership collection) came back negative. What's left is a defaults argument, not a trust argument.

## What I'm doing about it

Two changes, both direct results of the engagement:

1. Removing the ZeroTier-lockdown behavior from zima-harden, and probably renaming the project. Masking `znet.service` on principle no longer holds up once you've actually verified the thing you were defending against doesn't happen. The other two pillars of the script — SSH restoration and the configurable firewall — still stand on their own merits and aren't going anywhere.

{{< labimg src="three-pillars-retired.svg" caption="Project is being renamed to reflect what's left." id="three-pillars-retired" width="900" height="900" >}}

2. Actually closing the two things that are real: rotating credentials that were reachable over those public overlays for months, clearing the unidentified devices from the affected controllers' member lists so a stale entry can't quietly persist, and binding the unauthenticated services to loopback or behind auth instead of leaving them open on every interface. On top of that, my longer-term plan is LAN-direct access at home with self-hosted WireGuard for anything remote — which sidesteps the public-join problem entirely rather than trying to keep patching around it.

One honest caveat on point 1: SSH restoration — the part of zima-harden that puts network root SSH back after ZimaOS locks it down — is itself a real exposure, and I'm not pretending otherwise. But the fix for that isn't "keep root SSH disabled forever" any more than the fix for ZeroTier was "keep it masked forever." The fix is ordinary operational discipline: don't expose the device directly to the internet, keep the host firewall locked down to a trusted subnet, and never hand out credentials that carry root access. Restoring the capability and running it recklessly are two different decisions, and I'd been treating them as one.

## The humble pie part

I built a whole tool around an assumption I never actually tested against the vendor's real behavior. Not because the instinct was crazy — "vendor-run remote-access overlay, enabled by default" is a completely reasonable thing to be suspicious of — but because I let a plausible worry stand in for a verified one, for a long time, without going and checking. The Discord beta test is what created enough friction that I finally did.

Turns out the feature was fine, and so is the vendor. My threat model was pointed at the wrong layer — I was suspicious of IceWhale when I should have been looking at how the defaults and a couple of unauthenticated services combined. IceWhale isn't operating a backdoor, isn't watching my traffic, and isn't quietly collecting who's on my network. That was never true, and I should have checked sooner instead of building a whole tool on the assumption that it might be.
