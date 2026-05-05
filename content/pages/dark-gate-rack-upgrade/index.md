---
title: "Dark-Gate Rack Upgrade: Ports, Power, and the Slow Creep of Scope Creep"
date: 2025-07-19
draft: false
layout: "lab-log"
description: "Adding a MokerLink 2.5G backbone switch, a second patch panel, EAP720 APs, and a sober look at what 604W of peak load does to a UPS budget."
slug: "dark-gate-rack-upgrade"
url: "/dark-gate-rack-upgrade/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Dark-Gate Homelab · Personal Build"
series: "dark-gate"
toc: false
tags: ["homelab", "networking", "rack", "mokerlink", "firewalla", "vlans", "power", "ups", "3d-printing"]
---

The rack has always been more of a suggestion than a plan. Four units, three active,
one patch panel with twelve ports serving a homelab that long ago stopped having twelve
devices. I added things. I removed things. I moved the Lenovo M900 out — I needed its
RAM and storage for something else, and eventually gave it away, which is a sentence
that sounds more calculated than it was. The VisionFive2s went out for an upgrade and
never came back. The slot they left behind has been staring at me for months.

What remained was the TL-SG108E in 1U, a 12-port patch panel in 2U, the Firewalla
Gold SE in 3U, and the ZimaBlade 7700 in 4U. Lean, yes. Also completely out of ports.

{{< gallery >}}
{{< labimg src="rack-diagram-before.png" caption="The rack as it stood — eight ports, one patch panel, one Firewalla, one ZimaBlade. Cosy." id="rack-before" >}}
{{< labimg src="rack-photo.jpg" caption="Physical rack, mid-transition. The Lenovo M900 and VisionFive2s are already gone." id="rack-photo" >}}
{{< /gallery >}}

## The Port Problem

Thirteen devices require direct Ethernet connections. That number does not count the
trunk between the Firewalla and the switch, or the two WAN uplinks, or the access point
connections. Thirteen devices, eight ports on the TL-SG108E, and a patch panel that
stopped being useful around the time I ran out of places to plug things in.

The solution, obviously, was more ports. The less obvious part was doing it without
turning the rack into a cable management catastrophe or spending money I would rather
keep. The MokerLink 8-port 2.5G managed switch was the answer. Eight 2.5GbE ports and
an SFP+ slot — the latter currently reserved, which is a polite way of saying I have
no SFP modules yet but I wanted the option. It replaces the TL-SG108E as the backbone
switch. The TL-SG108E moves down to become an expansion switch, feeding off the
MokerLink via trunk on P7. Combined, that is sixteen access ports before you count the
trunk link, which is enough room to breathe.

A second 12-port patch panel comes in at 5U. The ZimaBlade drops to 6U. The rack is
now six units tall and actually organised.

{{< gallery >}}
{{< labimg src="rack-diagram-after.png" caption="The planned layout. MokerLink at 1U, second patch panel at 5U, ZimaBlade at 6U." id="rack-after" >}}
{{< labimg src="outside-rack-devices.png" caption="The outside-rack layer. The IoT population is growing." id="outside-rack" >}}
{{< /gallery >}}

## What Moved Outside the Rack

The Archer C6 is staying for now, joined by a TP-Link AC750 as the second access
point. Not the wifi upgrade I eventually intend to make — that post is a separate
conversation — but sufficient for the current phase. The outside-rack diagram shows
the planned EAP720 layout for reference; what is actually running is the Archer C6
and the AC750.

The ESP32 CYD is a small touch-screen display mounted on the rack panel. It connects
to Home Assistant over WiFi and displays whatever HA knows — Firewalla WAN status,
Frigate camera events, MQTT device states, and anything else the homelab throws at it
over time. It is a read-only dashboard on glass; it does not push data anywhere.
Power is currently from a wall adapter until a portable rechargeable solution gets
rigged. The full write-up is its own future post. Here is a preview.

{{< labimg src="esp32-cyd-wan-status.jpg" caption="WAN STATUS on the ESP32 CYD — WAN1 GPON fibre online, WAN2 MTN 4G/5G on standby, 100.7 Mbps on the primary line. The full story is a future post." id="esp32-cyd-wan" >}}

## Port Assignments and Topology

The Firewalla Gold SE has four ports. P3 and P4 are the only WAN-capable ports — P1
and P2 are LAN-only, which is worth remembering if you ever try to repurpose one of
them. P4 connects to the Huawei HG8245H5 GPON modem: primary fibre. P3 goes to the
ZTE G5TS for MTN 4G/5G failover. P1 trunks to the MokerLink. P2 goes to the
Archer C6 — root AP, no switch in the path.

{{< gallery >}}
{{< labimg src="port-assignment-table.png" caption="Full port assignments across all three switches. Thirteen direct connections, two trunk links, two WAN ports." id="port-table" >}}
{{< labimg src="network-topology.png" caption="The topology. Dashed lines are wireless. Everything else is copper." id="topology" >}}
{{< /gallery >}}

The MokerLink backbone: P1 to Firewalla P1 (trunk, gateway uplink), P2 to ZimaCube2
Pro on VLAN 20, P3 to ZimaBlade 7700 on VLAN 20, P4 to ZimaBoard2 1664 on VLAN 20,
P5 to ZimaBoard 832 on VLAN 20, P6 to the desktop PC on VLAN 10, P7 trunk to
TL-SG108E, P8 to the laptop on VLAN 10. SFP+ reserved.

The TL-SG108E expansion switch: P1 to MokerLink P7 (trunk), P2 to Google TV Streamer
on VLAN 30, P4 to the AC750 (wired AP), P3 and P5–P8 spare. Five spare ports on the
expansion switch alone. That has not happened in this rack before.

IoT devices — SONOFF MINIR4 ×4, Tapo C200 ×3, Google TV Streamer — all on VLAN 30.
The SONOFF units run Tasmota for local MQTT. The Tapos push RTSP streams to Frigate
on the ZimaCube2 Pro. The Streamer is wired.

Thirteen direct connections. Two trunk links. Two WAN connections. As I noted to
myself while drawing this: a crazy topology. It is also the topology that works, so
I am not complaining.

## The Power Situation

The numbers are not entirely comfortable to look at.

Rack networking alone — Firewalla at 10W typical, MokerLink at an estimated 15W,
TL-SG108E at 4W — comes to 29W typical, 45W at rated maximum. Add the WAN modems:
Huawei at 8W, ZTE at 12W. Add current WiFi hardware. Rack and all network equipment:
75W typical, 125W at rated maximum.

{{< gallery >}}
{{< labimg src="power-breakdown.png" caption="Power consumption by device group. The RTX 4080 dominates at inference load." id="power-breakdown" >}}
{{< labimg src="ups-capacity.png" caption="UPS capacity analysis. The APC 650 caps out at the rack networking layer." id="ups-capacity" >}}
{{< /gallery >}}

The Zima compute fleet: ZimaCube2 Pro base system at 51W idle, ZimaBlade 7700 at 10W,
ZimaBoard2 1664 at 10W, ZimaBoard 832 at 8W. Zima subtotal: 79W. The desktop PC with
its RTX 4080 is a separate machine on a separate circuit — that accounting comes in
another post.

System total at current idle load: 154W. That is the honest number to plan around.

## The Power Backup Situation

I have an Eaton 5E 1500i and an APC 650, both upgraded from the stock 12V 7Ah to 12V
9Ah sealed lead-acid batteries. The Eaton gives approximately 45 minutes at rack-only
load. The APC gives two microseconds. I counted. Honestly.

The path forward is an inverter system first, then solar on top of it. Chloride Exide
Uganda have already specced something: a 200Ah 25.6V LiFePO4 battery bank with 4kWh
of usable capacity. At 90% inverter efficiency, that is 3,600Wh available at the wall.

The runtime numbers at that capacity:

| Load | Draw | Runtime |
|---|---|---|
| Rack networking only | 75W | 48 hours |
| Rack + Zima fleet idle | 154W | 23.4 hours |

The rack networking layer runs for two days on a single charge. The full homelab at
idle runs for almost a full day. Those are numbers worth having in Kampala.

Solar top-up comes in a later phase. The inverter system is the first step — get the
capacity in place, then point panels at it. That post will come when the hardware does,
probably around my birthday.

## The 3D Printing Detour

Before the MokerLink goes into the rack, there is a conversation to have with my
friends at [paulettedecorarts.com](https://paulettedecorarts.com). I need a rack
mount for the MokerLink and a carry case for the ZimaBoard2 — something I can take
out when the ZimaBoard needs to travel. The slicers are already running. The cable
management tray for the MokerLink prints flat with supports on a textured PEI plate.
The ZimaBoard2 rack mount case stands upright at 140mm and takes considerably longer.
Patience is a virtue I am still developing.

{{< gallery >}}
{{< labimg src="3dprint-cable-tray.png" caption="MokerLink cable management tray in the slicer. Creality Ender-3 V3 Plus, textured PEI plate." id="3d-tray" >}}
{{< labimg src="3dprint-rack-mount.png" caption="ZimaBoard2 rack mount case. 140mm tall — this one requires patience." id="3d-mount" >}}
{{< /gallery >}}

## What's Next

Three things, in order.

First, the rack upgrade gets completed — MokerLink installed, second patch panel
patched in, VLANs properly segmented. This post covers the planning; a follow-up
will cover the implementation.

Second, the wifi upgrade gets its own post when the time comes. There is also some
new Home Assistant hardware in the pipeline that deserves coverage.

Third, the power situation gets addressed. The inverter system from Chloride Exide
Uganda comes first, then solar on top of it. Probably both in the same post,
probably around my birthday.

In the meantime: thirteen devices, sixteen available ports, and a rack that finally
makes sense on paper. Progress.
