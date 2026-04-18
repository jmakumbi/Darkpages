---
title: "One Machine, Two Network Positions, Zero Commercial Licences"
date: 2026-04-17
draft: false
layout: "lab-log"
description: "A ZimaBoard2 with dual Ethernet becomes a concurrent external/internal VAPT appliance. No commercial licences: Greenbone CE, Wazuh, DefectDojo, and Metasploit deliver a complete assessment platform."
slug: "vapt-appliance-zimaboard2"
url: "/vapt-appliance-zimaboard2/"
noindex: true
author: "James S. K. Makumbi"
kicker: "Security · ZimaOS · April 2026"
title_html: 'One Machine, Two Network Positions, <em>Zero Commercial Licences</em>'
standfirst: "A friend needed a vulnerability assessment and penetration test. Building the platform to deliver it sent me down a rabbit hole involving a commercial licensing trap, a hardware insight hiding in plain sight, and an open-source toolchain that delivers more than the industry benchmark at a fraction of the ongoing cost."
reading_time: "14 min"
toc: false
disclosure: false
tags:
  - zimaboard2
  - zimaos
  - docker
  - pentesting
  - greenbone
  - wazuh
  - open-source
---

A friend called. He needed a VAPT — vulnerability assessment and penetration test.
That is all you need to know about the client. The rest of this piece is about
what I built to deliver it.

---

## The Core Problem: Two Positions, Not Two Machines

A complete VAPT requires two fundamentally different network positions.
The external assessment must originate from outside the target network —
seeing what an attacker on the internet would see, unfiltered by any internal
knowledge or routing. The internal assessment must originate from inside —
reaching assets directly with credentials, performing local checks that a
network scanner cannot do from the outside.

These are not two machines. They are two positions. You could use the same laptop
for both by unplugging it from the external connection and plugging into the LAN
— and many practitioners do exactly that. The problem is that some tooling breaks
when you switch, network configurations cache, and the discipline of keeping
those positions cleanly separated starts to erode when the physical act of switching
is tedious. It is not a hard requirement for two devices. It is a strong
operational argument for one device that occupies both positions simultaneously.

<div class="insight">
  <div class="insight-bar"></div>
  <div class="insight-body">
    <div class="insight-label">The ZimaBoard2 Insight</div>
    <p>
      It has two Ethernet ports. <code>eth0</code> upstream of the client's perimeter,
      connected directly to the ISP side. <code>eth1</code> on the internal LAN.
      A single device with genuine, concurrent external and internal positioning.
      External assessment traffic originates from outside the network — because
      it physically does. No routing tricks, no NAT confusion, no switching cables.
    </p>
  </div>
</div>

This is not what the ZimaBoard2 is marketed for. The product pages talk about
NAS builds, home servers, Plex, and Docker labs. But an x86\_64 machine with
dual Ethernet, 16GB RAM, ZimaOS pre-installed, and two SATA ports is also an
entirely credible security assessment appliance — and at a price point that
does not require a purchase order conversation with anyone.

---

## ZimaOS and Docker: Why This Combination Works

ZimaOS treats Docker as a first-class citizen. Not a compatibility layer,
not an optional add-on — the platform is built around containerised workloads.
For an assessment platform that runs twelve or more containers simultaneously,
that is not a trivial property. Container restarts, volume mounts, inter-service
networking, and persistent data management all behave predictably because the
OS was designed with this in mind.

The web-based management interface handles container lifecycle without requiring
SSH access. For a client's IT staff who will be checking scan schedules and
restarting a container after an update, that matters. Under the hood it is a
standard Linux host — full Docker CLI available, standard volume mounts,
nothing proprietary that creates lock-in. The client can hand the device to
any Linux-literate administrator and they will know how it works within an hour.

The 256GB SATA SSD fitted into one of the two SATA slots holds the `data`
volume — everything that needs to survive a container update.
The NVT vulnerability feed database, the scan results, the finding register,
the endpoint monitoring indices. The eMMC handles the OS and container images.
Persistent data never touches it.

---

## The Case: Making It Deployable

A bare ZimaBoard2 is a circuit board with a heatsink. It will run indefinitely
on a shelf but it is not something you hand a client and expect to survive
a year in a comms cabinet. For a device that lives at a client site,
handling is a real consideration.

The enclosure is a 3D-printed wall-mount case designed specifically for the
ZimaBoard2 — [available on Printables](https://www.printables.com/model/1570677-zimaboard-2-wall-mount).
It holds the board securely, keeps the SATA drives accessible and protected,
leaves every port reachable, and can be screwed directly to a wall or the inside
of a cabinet. The whole assembly — board, two drives, case — becomes something
a client can mount once and forget about.

<div class="img-pair">
{{< labimg src="vapt-case-side-view.webp" caption="The assembled appliance. The ZimaBoard2's aluminium heatsink sits above the printed enclosure. The small blower fan is the only moving part — everything else is passive thermal dissipation through the fins." id="case-side-view" >}}
{{< labimg src="vapt-case-drive-bays.webp" caption="The case open, showing the two 2.5-inch drive bays in the lower section and the board ports above. The latticed infill keeps weight down without sacrificing rigidity. Two SSDs give separate volumes for OS and data — exactly what the architecture calls for." id="case-drive-bays" >}}
</div>

Printing in white PLA keeps costs low and the result looks intentional rather than improvised.
The total enclosure cost at Kampala print rates is roughly UGX 90,000 — approximately USD 24.
For a device that will be wall-mounted at a client site indefinitely, that is not a rounding error.
It is the difference between a professional installation and a circuit board on a shelf.

---

## The Container Stack

<div class="stack">
  <div class="stack-layer">
    <div class="stack-label">External · eth0</div>
    <div class="stack-items">
      <span class="stack-item">Metasploit</span>
      <span class="stack-item">nmap</span>
      <span class="stack-item">testssl.sh</span>
      <span class="stack-item">theHarvester</span>
      <span class="stack-item">subfinder</span>
      <span class="stack-item">gobuster</span>
      <span class="stack-item">nikto</span>
    </div>
  </div>
  <div class="stack-layer">
    <div class="stack-label">Internal · eth1</div>
    <div class="stack-items">
      <span class="stack-item">Greenbone CE ×8</span>
      <span class="stack-item">Wazuh manager</span>
      <span class="stack-item">Wazuh indexer</span>
      <span class="stack-item">Wazuh dashboard</span>
    </div>
  </div>
  <div class="stack-layer">
    <div class="stack-label">Both · eth1 mgmt</div>
    <div class="stack-items">
      <span class="stack-item">DefectDojo</span>
    </div>
  </div>
  <div class="stack-layer">
    <div class="stack-label">Platform</div>
    <div class="stack-items">
      <span class="stack-item">ZimaOS</span>
      <span class="stack-item">Docker</span>
      <span class="stack-item">256GB SSD → /data</span>
    </div>
  </div>
</div>

All management interfaces — Greenbone's web UI, the Wazuh dashboard,
DefectDojo — bind to `eth1` only. Nothing on `eth0` accepts inbound connections.
The external interface carries outbound scan traffic and nothing else.

---

## External Assessment: The Toolchain

The external assessment runs in sequence. Passive intelligence gathering first —
nothing touches the target network. Active reconnaissance second. Exploitation
of confirmed vulnerabilities last. Everything is logged. Evidence is captured
at each stage. Nothing moves forward without confirmation from the stage before it.

<div class="tool-grid">
  <div class="tool-card">
    <div class="tool-name">theHarvester + subfinder</div>
    <div class="tool-role">Open-source intelligence — emails, subdomains, hostnames, and DNS records from public sources. Zero contact with the target at this stage.</div>
    <div class="tool-net">↑ passive only</div>
  </div>
  <div class="tool-card">
    <div class="tool-name">nmap</div>
    <div class="tool-role">Port scanning with service version detection and OS fingerprinting. The output drives every subsequent decision. Run via eth0 — the results reflect what an external attacker actually sees.</div>
    <div class="tool-net">↑ eth0 external</div>
  </div>
  <div class="tool-card">
    <div class="tool-name">testssl.sh</div>
    <div class="tool-role">Comprehensive SSL/TLS audit — certificate validity, cipher suites, protocol support, BEAST, POODLE, Heartbleed, ROBOT. A dedicated tool does this better than any general scanner.</div>
    <div class="tool-net">↑ eth0 external</div>
  </div>
  <div class="tool-card">
    <div class="tool-name">nikto + gobuster</div>
    <div class="tool-role">Web surface enumeration — server misconfiguration, outdated components, exposed paths and directories on any HTTP or HTTPS services found by nmap.</div>
    <div class="tool-net">↑ eth0 external</div>
  </div>
  <div class="tool-card">
    <div class="tool-name">CISA KEV + NVD APIs</div>
    <div class="tool-role">Live threat intelligence. Service versions from nmap are correlated against the CISA Known Exploited Vulnerabilities catalogue before any exploitation attempt. This distinction matters — not every vulnerability deserves a Metasploit module.</div>
    <div class="tool-net">↑ live feeds</div>
  </div>
  <div class="tool-card">
    <div class="tool-name">Metasploit Framework</div>
    <div class="tool-role">Controlled exploitation of confirmed, intelligence-corroborated vulnerabilities. Every session logged. Evidence captured. The last tool in the sequence, not the first.</div>
    <div class="tool-net">↑ eth0 external</div>
  </div>
</div>

---

## The Internal Assessment Platform: And the Licensing Trap

Internal credentialed vulnerability assessment needs a scanner.
The market leader — the tool that appears in every pentesting course,
every security certification syllabus, every comparison article written
in the last decade — has a free tier. It used to cover 16 IP addresses
permanently. I had that figure in my planning notes, unverified,
from something I had read eighteen months prior.

Checking the current pricing page before committing anything to a deliverable
revealed that the permanent 16-IP free tier no longer exists.
The current free tier is a 30-day evaluation with a 5-IP limit and no data
retention after expiry. The full commercial licence is approximately
USD 4,790 per year.

<div class="callout-dark">
  <div class="callout-label">What almost went into the deliverable</div>
  <p>
    My planning notes said "free, permanent, 16 IPs." Every single word of that
    was wrong. Licensing models change without announcement.
    Review articles do not retroactively update when they do.
    Verify current pricing pages before any tool goes into client-facing documentation.
    Every time. Without exception.
  </p>
</div>

### Greenbone Community Edition

OpenVAS — the open-source scanner that forked from the original Nessus codebase
in 2005 when Tenable closed its licence — has been in continuous development since
then under Greenbone's stewardship. The Community Edition runs approximately 50,000
vulnerability tests updated daily via the free community feed.
It supports credentialed SMB and WMI scanning on Windows, which is what
a deep internal assessment of Windows systems requires.

The coverage gaps versus the commercial alternative are real and documented.
In particular, certain Microsoft enterprise products and some commercial networking
equipment have weaker community feed coverage. Whether those gaps matter depends
entirely on what is in scope. For the environment in question, they did not.

But the argument that won was not cost avoidance. It was the API.

<blockquote class="pullquote">
<p>Greenbone CE publishes GMP — the Greenbone Management Protocol, v22.7 —
a fully documented, open, programmatic interface to every scanning function.
Create targets, configure credentials, start scans, pull results, generate reports:
all scriptable. The commercial alternative is a closed system. The interface it
ships with is permanently the interface you get.</p>
<cite>— The architectural argument, not the cost argument</cite>
</blockquote>

For a consulting practice building recurring engagements, that distinction compounds
over time. A custom dashboard showing a specific client's assets, their vulnerability
trend, their compliance posture — built once, refined across every subsequent engagement.
With a closed proprietary system, you are on the vendor's roadmap permanently.

### Greenbone CE is eight containers

It is not one container with a scanner inside it.
The current architecture is a proper microservices decomposition:
`gvmd` (the central daemon and GMP API endpoint),
`gsad` (the web server), `gsa` (the React interface),
`openvas-scanner` (the NASL scan engine),
`ospd-openvas` (the OSP bridge between gvmd and the scanner),
`notus-scanner` (high-performance local security checks that
replace individual NASL scripts for installed software CVE detection),
`pg-gvm` (PostgreSQL — all scan configs and results),
and the NVT feed sync container that runs on a schedule and does nothing else.
All eight stay alive permanently on the ZimaBoard2. ZimaOS manages restarts.

---

## The Compliance Gap: And Wazuh

Network vulnerability scanning from the internal interface finds what is
exposed to the network. It does not find what is misconfigured inside the machine.
Verifying that Windows security configuration — audit policies, account controls,
service hardening, registry settings — matches established hardening benchmarks
requires something running on the endpoint with local access.

The commercial scanner includes over a thousand CIS and DISA compliance audit
templates as standard. Greenbone CE locks its compliance policies behind the
paid Enterprise feed. That looked like a gap that cost money to close,
until I looked at what Wazuh actually delivers.

Wazuh is a free, open-source security platform. Its agents are lightweight,
deploy silently to Windows via admin credentials — no physical access, no user
interruption, no software distributed by hand — and perform local security
configuration assessment against CIS benchmark policies that ship with the
platform by default. No paid feed. Its vulnerability detection pulls from
Microsoft's official security update database, NVD, and the CISA KEV catalogue.

<table class="spec-table">
  <thead>
    <tr>
      <th>Gap in Greenbone CE community</th>
      <th>Wazuh closes it?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CIS benchmark compliance templates</td>
      <td class="good">✓ built-in, no paid feed</td>
    </tr>
    <tr>
      <td>Microsoft security update CVE coverage</td>
      <td class="good">✓ MSU feed included</td>
    </tr>
    <tr>
      <td>Continuous monitoring between scans</td>
      <td class="good">✓ agents report in real time</td>
    </tr>
    <tr>
      <td>File integrity monitoring</td>
      <td class="good">✓ built-in FIM module</td>
    </tr>
    <tr>
      <td>Annual licence cost</td>
      <td class="good">USD 0</td>
    </tr>
  </tbody>
</table>

Wazuh runs as three containers on the same ZimaBoard2: manager, indexer
(OpenSearch), and dashboard. Greenbone CE and Wazuh are not running their
heavy workloads concurrently — the credentialed scan is scheduled for an
agreed quiet window, while Wazuh processes lightweight continuous agent
telemetry at a rate that does not pressure the available RAM.

---

## DefectDojo: One Register for Everything

Two tools, two output formats. Greenbone exports XML via the GMP API.
Wazuh surfaces findings through its REST API. Without a unified finding register,
you are comparing separate outputs and manually deduplicating findings that both
tools detected through different mechanisms — and there will be overlap.

DefectDojo runs as a fourth container stack and aggregates everything.
It has a native parser for Greenbone's OpenVAS XML format and accepts Wazuh output
via its generic findings API. One severity classification, one retest workflow,
one export for the final report. Not glamorous. Purpose-built for this workflow.
Free.

---

## Software Licensing: What the Stack Costs to Run

<table class="spec-table">
  <thead>
    <tr>
      <th>Tool</th>
      <th>Licence</th>
      <th>Annual cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Greenbone Community Edition</td>
      <td>GPL</td>
      <td class="good">USD 0</td>
    </tr>
    <tr>
      <td>Wazuh</td>
      <td>GPL / Apache 2.0</td>
      <td class="good">USD 0</td>
    </tr>
    <tr>
      <td>DefectDojo</td>
      <td>BSD</td>
      <td class="good">USD 0</td>
    </tr>
    <tr>
      <td>Metasploit Framework</td>
      <td>BSD / commercial</td>
      <td class="good">USD 0 (community)</td>
    </tr>
    <tr>
      <td>nmap, testssl.sh, nikto, gobuster, theHarvester, subfinder</td>
      <td>Various OSS</td>
      <td class="good">USD 0</td>
    </tr>
    <tr>
      <td>ZimaOS</td>
      <td>Proprietary / free</td>
      <td class="good">USD 0</td>
    </tr>
    <tr>
      <td><strong>Total</strong></td>
      <td></td>
      <td class="good"><strong>USD 0</strong></td>
    </tr>
    <tr>
      <td>Equivalent commercial VA scanner licence (for reference)</td>
      <td>Proprietary</td>
      <td class="bad">~USD 4,790 / year</td>
    </tr>
  </tbody>
</table>

The commercial scanner also does not include continuous endpoint monitoring,
CIS compliance checking, or a finding register. Those are separate procurement
conversations. This stack delivers all of it, on hardware the client owns outright,
running indefinitely without external dependency.

---

## The Next Layer: A Unified Control Plane

Three tools. Three web interfaces. Three different mental models for navigating
findings, triggering scans, and reading compliance results. Greenbone CE's
Security Assistant, the Wazuh dashboard, and DefectDojo are each adequate
for what they do individually. Switching between them to get a coherent picture
of one client's security posture is friction that accumulates into hours per engagement.

The GMP API, the Wazuh REST API, and the DefectDojo REST API mean you do not
have to live with that friction permanently. A single custom interface —
a Blazor Server application running as its own Docker container on the same
ZimaBoard2 — can consume all three and present a unified view: named assets,
current vulnerability status, CIS compliance scores, CISA KEV correlation,
open findings, scan controls, and report generation, all in one place accessible
on the client's LAN.

{{< labimg src="2026-04-18_12-21-36.png" caption="Mockup of the unified control plane. Asset status from Greenbone CE and Wazuh SCA in one grid. CISA KEV correlation live from the daily feed. Scan scheduling and agent status without opening three separate dashboards." id="control-plane" >}}

The Greenbone GMP API is the piece that makes this possible and the piece that
the commercial alternative cannot offer. A closed scanner gives you its interface
and nothing else — permanently. Greenbone CE's published protocol means the
interface is a variable, not a constant. Build it once for one client,
refine it across the next ten. The container sits alongside the others on the
same machine, binds to the same `eth1` management interface,
and adds roughly 256MB to the RAM footprint.

This is not in the current engagement. It is the next conversation —
the one that happens after the client has seen the three-tool stack running
and started to feel the switching cost themselves.

---

## Hardware Options: It Is Not Just the ZimaBoard2

The ZimaBoard2 1664 is the right platform for this engagement at this scale.
It is not the right platform for every engagement. The architecture —
ZimaOS, Docker, dual-NIC positioning — is hardware-agnostic.
Any x86\_64 machine with two Ethernet ports runs this stack identically.

<div class="hw-grid">
  <div class="hw-card">
    <div class="hw-name">ZimaBoard2 1664</div>
    <div class="hw-tier">Entry — small engagements</div>
    <div class="hw-body">
      Intel N150, 16GB LPDDR5, dual 2.5GbE, 2× SATA, PCIe 3.0 slot.
      Fanless, silent, under 15W. RAM is not expandable — 16GB is what you get.
      Enough for a focused engagement. Not enough for 50+ assets running both
      Greenbone CE and Wazuh simultaneously without careful scheduling.
    </div>
    <a class="hw-link" href="https://billableonline.co/zimaboard-832-unboxing/">→ My ZimaBoard 832 unboxing (the predecessor)</a>
  </div>
  <div class="hw-card">
    <div class="hw-name">ZimaCube 2 Pro</div>
    <div class="hw-tier">Mid-range — larger environments</div>
    <div class="hw-body">
      Intel Core Ultra, up to 64GB RAM, dual Thunderbolt 4, multiple drive bays,
      PCIe expansion. The RAM ceiling disappears. Multiple concurrent heavy workloads
      become routine rather than a scheduling exercise. Larger form factor, significantly
      more headroom for growing asset counts or running additional containers.
    </div>
    <a class="hw-link" href="https://billableonline.co/zimacube-2-pro-unboxing/">→ My ZimaCube 2 Pro unboxing</a>
  </div>
  <div class="hw-card">
    <div class="hw-name">Any dual-NIC x86_64</div>
    <div class="hw-tier">Flexible — scale to requirement</div>
    <div class="hw-body">
      A Topton or CWWK 4-NIC mini PC, a repurposed corporate small-form-factor desktop,
      or a purpose-built mini-ITX node with a dual-port PCIe NIC. ZimaOS installs on any
      x86_64 machine. The container stack does not care what the chassis looks like.
      For large-scale or long-term engagements, a machine with 32GB+ and NVMe storage
      removes every constraint this platform has at the small end.
    </div>
  </div>
</div>

<div class="callout-dark">
  <div class="callout-label">On the ZimaBoard2's PCIe slot</div>
  <p>
    The PCIe 3.0 x4 slot on the ZimaBoard2 1664 sits unused in this deployment.
    A dual-NVMe adapter would improve storage throughput considerably.
    A 10GbE NIC would make the external scanning interface faster than any target
    you are likely to encounter in Uganda. Neither is necessary at this scale,
    but the expansion headroom is there. The <a href="https://billableonline.co/zimaboard-832-unboxing/">ZimaBoard 832 review</a>
    covers the PCIe slot in detail — the 1664 is the same board with doubled RAM and storage.
  </p>
</div>

---

## What I Would Do Differently

Verify every tool's current licensing before it appears in any planning document.
The Nessus pricing assumption was a near-miss that cost two days of rework.
"I read somewhere that it's free" is not due diligence when you are about to put
a number on a deliverable.

Wazuh should have been part of the initial architecture, not an addition made
after the Greenbone stack was already settled. The two tools are designed to
complement each other — network scanner and endpoint agent, each covering what
the other cannot reach. Evaluating them together from the start would have
produced a cleaner design and avoided one round of replanning.

The hardware scale question should be resolved before the engagement starts,
not derived from what is sitting on the shelf. The ZimaBoard2 was the right call
here. For the next engagement it may not be. The ZimaCube 2 Pro exists for exactly
the scenarios where 16GB and two SATA slots are not enough, and the price difference
is easily absorbed into an engagement of any meaningful size.
