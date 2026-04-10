---
title: "Firewalla Gold SE — The Night the OS Ate Itself"
date: 2026-04-09
draft: false
layout: "lab-log"
description: "A power outage corrupted the Firewalla OS. This is the midnight reflash and rebuild."
slug: "firewalla-reflash"
url: "/firewalla-reflash/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Firewalla · Self-owned"
series: "firewalla"
toc: false
tags:
  - firewalla
  - homelab
  - network
  - reflash
  - power-outage
  - uganda
---

*I own this Firewalla Gold SE. Nobody sent it to me. This is purely self-inflicted.*

---

## The Blinkenlights

{{< labimg src="blinkenlights.jpg" caption="The original Blinkenlights notice. Computing culture's longest-running in-joke, circa 1950s IBM mainframe era. Still accurate." id="blinkenlights" >}}

For those not versed in computing folklore: *blinkenlights* is the affectionate term for
the status LEDs on network hardware — the lights that blink when things are working,
and blink differently when they are not. The word comes from a parody notice that
circulated in early computing facilities, written in a deliberately mangled pidgin German.
It warned users not to touch the machine. The lights on my Firewalla were blinking.
Just not in any way I wanted them to.

---

## The Setup

{{< labimg src="rack-overview.jpg" caption="The setup. MTN 5G on standby, Huawei ONT on fibre, TP-Link TL-SG108E with all 12 ports doing their job. Before." id="rack-overview" >}}

Power had been off for most of the night. About four hours in total, with a 45-minute
reprieve somewhere in the middle — long enough to remember what electricity felt like,
brief enough to accomplish nothing useful. When it finally came back for good, the UPSes
stopped their collective complaint and the network stack came back to life.

Or most of it did.

Standing in my home office at 11pm, I ran the mental checklist. MTN fibre: check.
MTN WiMax: check. Network switch: check. Wi-Fi router: check.

Firewalla Gold SE: blinking blue.

Not the reassuring white-to-blue startup pulse. A steady, repetitive blink. The kind
that means the device is alive but has nothing to run.

I grabbed the spare HDMI cable. The rear panel has an HDMI port — I documented it,
when I [first wrote about this hardware](/firewalla-homelab/), as being for console
access. It is, in fact, for console access. What I got was every Linux user's specific
nightmare: a blinking cursor. Top-left corner of a black screen. Nothing else.

I restarted. Blinking cursor.
I reset the device. Blinking cursor.

The OS was gone.

---

## The Maths of a Bad Night

To be precise about what this was: the first incident in thirty months of continuous
operation. The [Firewalla had run without complaint](/firewalla-homelab/) since October
2023 — firmware updates happening silently, dual-WAN failover triggering and recovering
without my intervention, status LED solid green throughout. This was not a reliability
failure. This was a power event meeting an unlucky moment in the write cycle.
The distinction matters, though it was not especially comforting at 11:30pm.

The Firewalla [sits between my network and everything else](/firewalla-homelab/),
which means without it, I had a functioning LAN and absolutely no path to the outside
world. The only solution was to reflash the firmware from scratch. Not reconfigure —
start over. Four years of firewall rules, device groups, content policies, VPN
configuration, and carefully assembled allow/block lists. All of it gone.

I did what any reasonable person does at this point: performed a silent, internal,
Khan-grade scream — the *Wrath of Khan* variety, not the *Into Darkness* one — and
got to work. It was late. The neighbours were innocent bystanders in all of this.

---

## The Flash

Firewalla's documentation deserves acknowledgement: it is genuinely good. I found the
firmware download page quickly. Two options: stable and beta.

I downloaded the beta.

The stable version is for people who have something to lose at midnight. I didn't
feel that I qualified anymore.

My laptop was tethered to my phone. I bought 10,000 UGX of MTN Freedom data —
17GB, valid for 365 days. The cost of the evening's entertainment. I opened
[Balena Etcher](https://etcher.balena.io), a tool I trust unreservedly because
it has never once lied to me about what it was doing.

I needed an 8GB microSD. The smallest I had was 64GB. It works.
Nobody panic.

The flash process ran exactly as documented. I want to be clear about how rare that is.
Hardware installation processes that work exactly as advertised, the first time, without
a single missing step or outdated screenshot, deserve specific praise. The Firewalla
documentation earned it. The installation began, and I watched it run.

Then the first real setback.

---

## The QR Code Problem

{{< gallery >}}
{{< labimg src="firewalla-in-rack.jpg" caption="The Firewalla Gold SE in its custom rack panel. Four ports lit, HDMI and USB broken out to the front. This is what rack-mounting looks like until you need to scan the underside." id="firewalla-in-rack" >}}
{{< labimg src="the-screwdriver.jpg" caption="Two rack screws and a Jakemy ratchet. 12:30am. Necessary." id="the-screwdriver" >}}
{{< /gallery >}}

To connect to a freshly flashed Firewalla, you open the app and scan the QR code on
the underside of the unit.

The underside.

Of the unit I had spent considerable time and energy [mounting in a 10-inch 8U rack](/firewalla-homelab/).

There is a specific kind of frustration reserved for undoing work you were proud of.
Out came the screwdriver. I disassembled enough of the rack to extract the Firewalla,
found the QR code, scanned it with the app, and watched it pick up the MTN fibre link
almost immediately.

Small mercy. One small mercy in an otherwise unremarkable night.

---

## Naked

The device was online. I was not protected.

*Naked* in this context means exactly what it implies for a network: the firewall was
factory fresh and had no idea who I was or what I cared about. Four years of rules —
every device group, every content policy, every allow and block list — gone.
The Firewalla was completely indifferent to this.

I rebuilt what mattered first. Static IPs are the only reason this wasn't worse —
every critical device came back to its address without negotiation. Then the
essentials in order: ad blocking on, quarantine mode on, content policy on.

My method is block-first: block everything, permit selectively. So I unblocked
Netflix, YouTube, WhatsApp, and LinkedIn. That last one I continue to permit out
of some professional obligation I have not yet fully examined. Porn, gambling,
violence, alcohol, social media beyond the permitted list — all blocked.

It was 1:49am. The network was functional. Ugly, but functional.

---

## What Comes Next

The CCTV cameras are still in device jail. The household's personal devices are
still in device jail. The Wi-Fi extenders are offline. None of this has been
noticed yet, which is a small miracle I intend to ride for as long as possible.

The allow list needs retraining. My block-first policy means that every site that
matters but doesn't appear in the default permitted list will surface over the
next few days as someone tries to load something and looks at me. I know this
process. I've been through it before.

The logs are empty. Four years of network pattern data — what connects, when, to
what — gone. It comes back. It just takes time.

The rack goes back together this weekend.

---

## What I Would Have Done Differently

Not much, honestly. The reflash worked. The documentation was accurate. The process
was sound.

I would have made a configuration backup before the power outage. Firewalla supports
this. I had not done it in some time. I will be doing it now on a schedule.

The red security dongle — the component the original documentation singles out as the
one thing not to lose — stayed plugged into the rear USB port throughout the entire
process and was picked up immediately after the flash. The thing they told me to worry
about was the one thing that required no attention whatsoever. Everything else needed
rebuilding from scratch.

The QR code placement on a rack-mounted device is a design decision I will charitably
describe as *optimistic*. It assumes the device is sitting on a flat surface in front
of you, not in a rack. I understand why — it's where the serial number lives, it's
a manufacturing default. It's still irksome. A printed QR code card in the box,
or a QR code displayed on the app itself during first-time setup, would have been
appreciated at 12:30am.

Everything else was exactly as hard as a midnight OS reflash deserves to be.
No harder. That's a reasonable outcome.

---

*Last updated: April 2026*
