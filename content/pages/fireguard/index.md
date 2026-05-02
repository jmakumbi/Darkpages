---
title: "FireGuard — An AI Security Dashboard for the Paranoid Network Administrator"
date: 2026-05-01
draft: false
layout: "lab-log"
description: "How I built FireGuard: an Electron AI security dashboard for my Firewalla Gold SE homelab, with local Ollama inference, five threat intelligence sources, and a RAG pipeline grounded in CISA and SANS advisories."
slug: "fireguard"
url: "/fireguard/"
noindex: true
author: "James S. K. Makumbi"
subtitle: "Personal project · Electron / React / TypeScript"
series: "dark-gate-homelab"
toc: false
disclosure: false
tags:
  - fireguard
  - homelab
  - firewalla
  - dark-gate
---

If you have read the [Firewalla Gold SE homelab post](/firewalla-homelab/) or the [OS reflash story](/firewalla-reflash/), you already know I live inside the Firewalla dashboard more than is probably healthy. After two years of accumulated data — device fingerprints, traffic flows, blocked connections, firewall rules — I found myself wanting something the official app does not quite do: ask questions. Not browse data. Ask questions. What is this device really doing? Which of my connections are genuinely suspicious? What known security flaws exist in the specific hardware sitting on my network right now?

So I built it.

## A Word on When This Gets Built

The development log for FireGuard reads like the schedule of someone who codes in the gaps between everything else. The first session started at 8:21 AM on an April Saturday. By noon there was a power outage — I confirmed the project was intact and resumed at 12:21 PM. By 1:25 PM the context window was full and the session ended. A second afternoon run lasted until 3:33 PM. Then a long evening session from 8:05 PM to past midnight — the longest single stretch of the entire project, covering everything in the intelligence pipeline.

Three weeks later: a 41-minute session on a May evening to tighten up a settings bug and automate the release process. One full day, mostly. Then three weeks of nothing. Then forty-one minutes. That is about right for how personal projects work.

## The Technical Problem Nobody Warns You About

The Firewalla MSP portal — the cloud interface that lets you manage your Firewalla device remotely — exposes a channel that software can communicate with. You send a structured question ("give me all alarms from the last hour") and get a structured answer back. Every modern web service has something like this, and the Firewalla one is perfectly well-designed.

The problem is browsers. Web browsers have a built-in rule that prevents a page you are viewing from reaching out to a completely different service in the background — a protection against malicious websites acting on your behalf without your knowledge. Any browser-based dashboard I built would run immediately into this wall. The standard workaround is to run a middleman server that relays the requests, but that felt like unnecessary infrastructure for a personal tool running on my own machine.

Electron solved both problems at once. Electron is a framework for building desktop applications using web technologies, and its behind-the-scenes process runs as a full desktop application — not a browser — so it is exempt from that restriction entirely. The same background process also handles AI calls, which means credentials for paid AI services never touch the visible interface. No relay server. No exposed credentials.

## The Dashboard

The entry point is a risk score. Not a number I invented — the AI looks at live alarms, active threats, and the current state of the network and produces a score with a brief explanation. Alongside it: a live threat feed, an AI-generated action summary broken down by priority, a bandwidth chart for the last six hours, and an at-a-glance count of online devices, active alarms, block rules, and managed boxes.

{{< labimg src="fireguard-dashboard.png" caption="The dashboard on a moderately paranoid evening. Risk score: 65 / HIGH. Three immediate actions, one of them mentioning TikTok. The bandwidth spike at the -1h mark was me. Probably." id="fg-dashboard" >}}

The AI action items are expandable. Each carries a severity badge and a brief explanation. The point is not to scare you — it is to give you something actionable when you open the app at 10 PM and find 53 block rules and a risk score that has ticked upward since this morning.

## The AI Providers

I wanted options. The first is Ollama — software you install on your own machine that runs AI models entirely on your hardware, with no internet connection required and no usage fees. The second and third are Anthropic and OpenAI, both cloud-based services that charge based on how much text is processed. Google was not among the three. Three integrations was already more than I planned.

{{< labimg src="fireguard-settings-ai.png" caption="Ollama takes priority and the app is honest about it. Cloud options are there when the local model is not adequate. Sorry Google." id="fg-settings-ai" >}}

Local AI is auto-detected on startup. If it is running, the app defaults to it. The reason I prefer running AI locally is hardware: I am running an NVIDIA RTX 4080, a high-end graphics card with 16GB of dedicated memory. AI models that would normally require a data centre can run entirely in that memory at useful speeds — without paying per request, without sending network traffic data to a third party, and without the round-trip delay of a remote server. For a security tool, keeping the analysis on-premises is not just economical; it is appropriate.

One AI model required a specific fix before it became usable. Qwen3 — one of the model families Ollama supports — has an internal reasoning mode that produces lengthy deliberation before it gives an answer. For general conversation this is a feature. For structured security scoring it was a problem: risk scores were varying between 20 and 90 for identical input depending on how the model happened to reason through it. I disabled the reasoning mode and set the randomness as close to zero as the model supports. The fix is now permanent and invisible to the user.

## The Intelligence Pipeline: Where the Mad Scientist Came Out

A dashboard that only reads your own firewall data is a glorified log viewer. I wanted external context — what does the security community already know about the addresses and software appearing in my network traffic? Malicious software leaves a trail. Researchers catalogue it. Several of them publish their findings publicly, in real time, at no cost.

{{< labimg src="fireguard-settings-intelligence.png" caption="AbuseIPDB requires a free account to obtain a lookup credential. Everything else runs without one." id="fg-settings-int" >}}

| Source | What It Provides | Account Required | Cache |
|---|---|---|---|
| Shodan InternetDB | Open network ports, known vulnerabilities, service tags on public IPs | No | 24h |
| ThreatFox | Known malicious software families and their associated addresses | No | 6h |
| Feodo Tracker | Addresses used by attackers to remotely control compromised devices | No | 6h |
| URLhaus | Addresses actively distributing malicious software | No | 6h |
| AbuseIPDB | Community abuse reports, confidence score, ISP, country | Yes (free tier) | 12h |

All five sources run simultaneously for each address lookup. A failure in any one is silent — the others still return. The composite result, combined with an AI narrative, tells you whether a suspicious address belongs to an attacker control server, a Tor exit node (the final hop in the Tor anonymity network — often flagged because it can mask where traffic actually originates), an automated scanner probing the internet for vulnerable devices, or something the community has not yet catalogued.

## Security Best Practices on Tap

Catching active threats is one thing. Understanding whether the vulnerabilities appearing in your network are being actively exploited in the wild — and whether your setup aligns with current security guidance — requires knowledge that changes week to week. I did not want to maintain that knowledge myself.

There is a technique in AI applications where, instead of relying purely on what the AI learned during training, you retrieve relevant documents and include them in the question you ask. The AI's answer is grounded in those documents rather than potentially stale training data. FireGuard does this with five publicly available security feeds — from organisations like CISA (the US cybersecurity agency) and SANS (a well-regarded security research institute) — fetched, processed, and stored locally each night.

The processing step deserves a brief explanation. Before documents can be searched for relevance, they are converted into a mathematical representation that allows them to be compared to the question being asked. A small, specialised AI model reads each chunk of text and produces a set of numbers representing its meaning. When a question comes in, the same model converts the question into numbers, and the chunks with the closest match are retrieved and sent to the AI alongside the question. This conversion model runs locally through Ollama — the whole chain stays on-machine.

{{< labimg src="fireguard-settings-rag.png" caption="170 processed segments of current threat intelligence, refreshed nightly. The Known Exploited Vulnerabilities list alone contributes 100 segments." id="fg-settings-rag" >}}

{{< callout >}}**If this sounds complex:** the setup is one-time and the app manages it entirely. The nightly refresh runs at 3 AM without any intervention. If the local AI is not running, all analysis still works — it just responds without the additional security context. Nothing breaks; the knowledge layer is additive.{{< /callout >}}

## Alarms

The Alarms page pulls from Firewalla's cloud and presents them in a filterable table. Severity tabs across the top — Critical, High, Medium, Low, Resolved. Search by device or host. For each alarm: Resolve, Ignore, or Analyse with AI.

{{< labimg src="fireguard-alarms.png" caption="A typical evening. Several \"accessing malware site\" alarms from the same device, a couple of game-related connections. The AI analysis tells you whether these are worth acting on or whether the device is just a Samsung TV doing Samsung TV things." id="fg-alarms" >}}

The AI analysis generates a triage assessment and a remediation plan with specific rule recommendations. A separate detection layer analyses alarm history and upload volumes to flag devices that may be contacting attacker-controlled servers or sending unexpected data outbound — it works even without full traffic history, which matters on Firewalla tiers that do not expose it.

## Devices

Every device on the network gets a card: online or offline status, hardware manufacturer, IP address, traffic in and out, the protection rules applied to it, and a link to that device's connection history. The AI footprinting function classifies every device — what type it is, who made it, what operating system it likely runs, how risky it looks — and saves confirmed identities so they persist across sessions.

{{< labimg src="fireguard-devices.png" caption="My Dark-Gate network laid out. The naming convention is deliberately unhelpful to anyone who does not already know what each device is." id="fg-devices" >}}

The device deep-dive is where the intelligence pipeline earns its keep. You type a description — *"I know this is a Tapo C200 camera"* — and the AI returns a security profile specific to that exact product: confirmed type, operating system estimate, a table of known security vulnerabilities (each given a standardised reference ID so you can look up the details independently), known active exploits with links, a prioritised hardening checklist, and advice on how to isolate it from the rest of the network. The profile is saved and pre-loaded on the next session.

Similarity tagging extends this. Once one TP-Link camera is identified, every other device with the same manufacturer and AI classification gets an amber badge suggesting the same type — one click pre-fills the description. I have four cameras. Identifying the first one effectively identified all four.

{{< callout >}}**Missing feature I intend to add:** The ability to isolate a device from the rest of the network directly from this page. Right now I would need to create a firewall rule manually. It is the next obvious thing to build.{{< /callout >}}

## Flows

Every connection the network makes, timestamped. Device, destination host or address, country, data downloaded, data uploaded, category, and whether it was blocked. Time range selector: 1h, 6h, 24h, 7d. Filter by device. Export to a spreadsheet. Run an AI anomaly analysis across everything visible.

{{< labimg src="fireguard-flows.png" caption="Six hours of traffic from my network. The country column is the fastest way to spot anomalies." id="fg-flows" >}}

The first real finding from this dashboard came on the first successful flow analysis: a massive outbound data transfer from my main workstation. It turned out to be a sync job I had forgotten about — but it surfaced immediately, without me having to look for it. That is what I built this for.

## Rules and Target Lists

The Rules page surfaces everything the Firewalla Gold SE is enforcing: which domains and addresses are allowed or blocked, in which direction, and for which devices. Create new rules, pause or delete existing ones. The AI recommendation engine analyses active alarms and suggests specific new rules where gaps exist.

{{< gallery >}}
{{< labimg src="fireguard-rules.png" caption="The firewalla-test.com entries are Firewalla's own malware and phishing test targets — useful for confirming the protection stack actually works before something real comes along." id="fg-rules" >}}
{{< labimg src="fireguard-target-lists.png" caption="12 lists. None maintained by me. Security researchers publish and update these; I apply them." id="fg-target-lists" >}}
{{< /gallery >}}

Target lists — named collections of addresses and domains that can be applied as rules in bulk — are where the security community does the maintenance work I would otherwise have to do myself. Tor exit nodes, newly registered domains, known advertising trackers, attacker infrastructure. The curation happens continuously; I just apply the lists and get the benefit.

## Insights — The One Worth Its Own Pages

Insights is the section I am most interested in and the one I am still writing about. It is an on-demand AI analysis centre — five sections, each running independently, results not saved between sessions. Device Footprint classifies everything on the network. Phone-Home Detection looks for devices contacting suspicious external servers. Security Overview is the AI's assessment of the network's current posture. Traffic Intelligence is anomaly detection on the connection data. Rule Gap Analysis recommends new firewall rules based on active threats.

{{< labimg src="fireguard-insights.png" caption="Five accordion sections, each a distinct analysis mode. The collapsed view does not do it justice." id="fg-insights" >}}

<div class="upcoming"><strong>Coming Next</strong> I am writing dedicated pages on each Insights section. Each one runs a different kind of analysis, uses the intelligence pipeline differently, and produces output worth explaining properly rather than squeezing into a paragraph here. Those pages will follow this one.</div>

## Watchlist

Any device can be placed on a watchlist for closer monitoring. A background job checks watched devices every five minutes and sends a Windows notification on threat contact. Device security profiles persist across sessions. The check interval is configurable per device; a manual trigger is also available at any time.

{{< labimg src="fireguard-watchlist.png" caption="Eleven devices under watch. Every device on this list has a reason for being here that I will not explain on a public page." id="fg-watchlist" >}}

Every device on this list has a reason for being here that I will not explain on a public page.

## Debug Logs: The Accidental Feature That Stayed

There were errors I could not reproduce. The worst was the local AI repeatedly refusing requests — a retry loop was fighting itself, with two competing attempts hitting a limit simultaneously and each making the other worse. I added a log viewer to Settings purely to diagnose that specific problem. After I fixed it, I left the logs in.

{{< labimg src="fireguard-settings-debug.png" caption="The log viewer that started as a debugging tool and became a permanent fixture. The confirmation lines showing security knowledge being loaded are the most satisfying thing to see on startup." id="fg-settings-debug" >}}

The log file sits on disk. The viewer shows the last 200 lines, colour-coded by severity, with copy and clear controls. Not elegant. Useful. I am going to keep tinkering with this application, so I will need it.
