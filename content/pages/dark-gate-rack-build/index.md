---
title: "Dark-Gate Gets Dressed: Custom 3D-Printed Shelves for the Rackmate T1"
date: 2025-07-21
draft: false
layout: "lab-log"
description: "How I populated the DeskPi Rackmate T1 with custom 3D-printed shelves from a Kampala fabrication studio, and ended up with a rack that looks intentional from the front."
slug: "dark-gate-rack-build"
url: "/dark-gate-rack-build/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Personal Purchase · Series: Dark-Gate"
series: "dark-gate"
toc: false
tags: ["homelab", "3d-printing", "rack", "firewalla", "zimablade", "dark-gate", "deskpi", "rackmate"]
---

{{< callout >}}
This is a follow-up to the [DeskPi Rackmate T1 unboxing and first impressions](/deskpi-rackmate-t1/). That page covers the rack itself. This one covers filling it with things that were never designed to go into a 10-inch frame.
{{< /callout >}}

## The Problem With 10-Inch Racks

The Rackmate T1 arrived, got unboxed, and sat there looking expectant. The problem with a 10-inch rack is that the standard 19-inch world wants nothing to do with it. You are not buying anything off-the-shelf. If you want to mount a [Firewalla Gold SE](/firewalla-gold-se/), a TP-Link SG108E, a GeeekPi 12-port patch panel, a [ZimaBlade 7700](/zimablade-7700-unboxing/), a Lenovo ThinkCentre M900, and a [ZimaBoard 2 1664](/zimaboard-2-unboxing/) in a frame that was designed for dental X-ray equipment, you are going to be making things.

The obvious answer was 3D printing. I went to <a href="https://yeggi.com/" target="_blank" rel="noopener">Yeggi</a> — effectively a Google but only for 3D models — found the shelf designs I needed, and then had a more interesting problem: who prints them? I will not bore you with the search process.

## Finding Paula at Paulette Decor Arts

That search led me to Paula at <a href="https://paulettedecorarts.com/about-pda/" target="_blank" rel="noopener">Paulette Decor Arts</a> — and I am glad it did.

{{< pda-card >}}

Paula was patient with my spec sheet, direct about timelines, and had the parts ready ahead of schedule. The kind of professional discipline that makes "local artisan" feel like an understatement. She also does considerably more interesting work than rack shelves — the 3D printing portfolio is worth a look.

{{< gallery >}}
{{< labimg src="paulette-work-1.png" caption="3D printing work from the Paulette Decor Arts portfolio." id="pda-work-1" >}}
{{< labimg src="paulette-work-2.png" caption="More from the studio's 3D printing output. The rack shelves were in good company." id="pda-work-2" >}}
{{< /gallery >}}

My only genuine gripe: two filament colour options — white and black. I chose both. The Firewalla shelf model came in white; the rest in black. No further decisions were necessary.

## The Prints Arrive

The pieces arrived in a satisfying heap. The Firewalla shelf — white, honeycomb-vented, properly rigid — looked like it had been designed by someone who actually uses the internet. The ZimaBlade and ZimaBoard trays came with dual 2.5-inch drive bays each: mount SSDs or spinning drives, hot-swap without disassembling anything. A thoughtful touch.

The mounting brackets for the ThinkCentre M900 and the switch tier were black, open-frame, no-nonsense. Everything fit the model dimensions without adjustment.

What nobody tells you about 3D-printed rack hardware: the tolerances are fine, the finish is fine, but you will spend an irritating amount of time with M4 screws and a screwdriver that is not quite the right length.

{{< gallery >}}
{{< labimg src="3d-prints-unboxed-1.jpg" caption="The Firewalla shelf (white, honeycomb), ZimaBlade trays, and ThinkCentre brackets laid out before assembly." id="prints-1" >}}
{{< labimg src="3d-prints-unboxed-2.jpg" caption="A second angle of the full print set. The black drive-bay trays are visible centre-right." id="prints-2" >}}
{{< labimg src="3d-prints-unboxed-3.jpg" caption="The bracket stack in detail. Open-frame construction, tight tolerances, minimal flex." id="prints-3" >}}
{{< /gallery >}}

## Mounting the Firewalla Gold SE

The shelf is designed for the entire Firewalla Gold series, which means it fits the Gold SE the way a suit fits someone who has recently lost weight. The device sits with room to rattle. Velcro solved this — three cable tie loops across the top.

With the Firewalla in its shelf and the cables routed, my cabling philosophy became official policy: all long cables go out the back. The front gets short patch cables only. Six-inch patch cables. The kind of decision that takes thirty seconds and saves you from staring at a rat's nest every time you glance at your network.

{{< gallery >}}
{{< labimg src="firewalla-mounted-front.jpg" caption="Firewalla Gold SE installed in the white shelf, velcroed in, front panel facing forward. Four Ethernet ports visible." id="fw-front" >}}
{{< labimg src="firewalla-mounted-angle.jpg" caption="Three-quarter view of the Firewalla shelf with cables routed. The red power button on the blanking panel is visible right." id="fw-angle" >}}
{{< /gallery >}}

{{< labimg src="firewalla-mounted-rear.jpg" caption="Rear of the Firewalla shelf. Short Ethernet cables routed neatly through the honeycomb panel." id="fw-rear" >}}

## Assembly

Everything went into the rack in order. TP-Link SG108E at the top — the weight logic was sound; the execution was not. The Firewalla panel below it, looking unreasonably professional for a device that is technically velcroed to a plastic shelf. The [ZimaBlade 7700](/zimablade-7700-unboxing/) next, then the ThinkCentre M900, and at the bottom — the open-frame tray holding two VF2 SBCs. Yes, two VF2s. The second was purchased voluntarily. This requires no further explanation.

The [ZimaBoard 2](/zimaboard-2-unboxing/) did not make it in. The reason was rational at the time and is no longer remembered. It remains in its original 3D-printed rack from a different vendor. The Dark-Gate rack is complete without it.

{{< labimg src="rack-assembly-progress.jpg" caption="Mid-assembly. TP-Link SG108E at top, Firewalla panel below, ZimaBlade and ThinkCentre slots taking shape." id="rack-progress" >}}

{{< labimg src="rack-complete-front.jpg" caption="The completed Dark-Gate rack, front view. Top to bottom: TP-Link SG108E, Firewalla Gold SE panel, ZimaBlade 7700, Lenovo ThinkCentre M900, VF2 open tray." id="rack-front" >}}

## Final State — Dark-Gate

The rack lives in the corner now. A Huawei ONT modem sits on top — not by design, but because it fits and space is finite. The ZimaBoard has its own setup beside the rack, connected by a short cable. Also not by design. Also now permanent.

The front of the rack looks exactly as I intended. The back looks like a network. That is the correct distribution of chaos.

{{< labimg src="dark-gate-final.jpg" caption="Dark-Gate in its corner. Huawei ONT on top. ZimaBoard 832 parked to the left, outside the rack, where it will remain indefinitely." id="darkgate-home" >}}
