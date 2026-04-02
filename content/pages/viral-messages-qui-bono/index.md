---
title: "Viral Messages: Qui Bono?"
date: 2026-04-02
draft: false
layout: "article"
description: "A thought experiment examining a Kampala security alert through the lens of network analysis, surveillance architecture, and information operations."
slug: "viral-messages-qui-bono"
url: "/viral-messages-qui-bono/"
noindex: true
subtitle: "Who Benefits When Your WhatsApp Group Becomes a Research Instrument?"
series: ""
toc: true
tags: ["information-security", "surveillance", "metadata", "uganda", "thought-experiment"]
---

{{< callout >}}
DISCLAIMER: What follows is a thought experiment — a structured exercise in imaginative paranoia for those who enjoy overthinking mundane things. The author does not own a tinfoil hat, has never attended a conspiracy convention, and genuinely believes that sometimes a WhatsApp forward is just a WhatsApp forward. Probably. Most of the time. The conclusions herein should be treated with the same seriousness you would afford a fortune cookie — intriguing, mildly unsettling, and best not acted upon.
{{< /callout >}}

## I. The Message That Started It All

It began, as most digital panic does, on WhatsApp. Somewhere between a recipe for matoke and a video of a surprisingly talented goat, a security alert arrived with the breathless urgency of someone who had clearly been waiting their entire life for an emergency. It warned, in bold text and dramatic ellipses, that SECURITY THREATS had extended — extended, mind you, not started, as though these threats had been politely limiting themselves to a smaller area until now — to twenty-six areas of Kampala simultaneously.

{{< pullquote >}}
Kawempe, Nabweru, Nansana, Katooke, Mpererwe, Kyebando, Bwayise, Kawaala, Namungoona, Nateete, Kyengera, Bulenga, Mutundwe, Kabowa, Nkulabye, Najjanankumbi, Ndeeba, Makindye, Nakawa, Salaama Road, Kira, Bulindo, Kireka, Bweyogerere, Namugongo & Kampala Central. — Twenty-six areas. They were not being shy about scope.
{{< /pullquote >}}

The threat involved thugs wielding pangas who, with remarkable theatrical flair, would scream and make alarms pretending to be distressed neighbours — and then, when a kind-hearted resident opened their gate, hack them and steal their property. It is, one must admit, a diabolically effective scheme that doubles as a rather dark commentary on the cost of community spirit in modern Kampala.

The message concluded with twelve safety tips and police contact numbers spanning three KMP divisions, and ended: *Kindly share with others.*

So we did. Of course we did. But let us pause here and ask — with the calm analytical detachment of someone who has clearly been indoors too long — a simple Latin question:

{{< pullquote centered="true" >}}
*Qui bono? Who benefits?*
{{< /pullquote >}}

## II. First, Does The Threat Actually Exist?

In the spirit of fairness, let us establish whether panga-wielding gangs are real before accusing anyone of running network mapping exercises.

The Uganda Police Force's own website provides evidence. In late February 2026, two suspects were arrested in Kabuusu carrying a panga near a petrol station. In March 2026, three suspects were found hiding in the ceiling of a home in Kabaale B Ward after a panga-armed robbery. UPF conducted massive crackdowns across Kampala Metropolitan, arresting over 1,000 suspects in a single week.

So panga gangs: confirmed real. The screaming-neighbour deception tactic: not independently verified anywhere. The specific 26-area geographic scope: not corroborated by any official UPF communication.

UPF's own operations reports mention Kyengera, Nateete, and Bweyogerere — but in the context of narcotics crackdowns and general robbery, not the specific modus operandi described. It is a bit like someone warning about shark attacks in Lake Victoria — the lake is real, the danger is real, but the sharks are doing something imaginative.

## III. The Geographic Scope Problem

Those twenty-six areas collectively cover the entire Kampala Metropolitan footprint — north, south, east, west, and central. This is not a neighbourhood watch. This is not a community alert. The geographic scope spans the jurisdictions of three Regional Police Commanders, dozens of Division Police Commanders, and multiple district authorities.

No single community source has operational visibility across that entire geography. To compile this list with confidence requires either access to intelligence from all three KMP divisional commands simultaneously, a sufficiently elevated position in the security architecture, or the creative use of a map of Kampala and an afternoon with nothing better to do.

{{< screenshot src="fig2-kampala-scope.svg" caption="No single community actor has operational visibility across this complete footprint" fig="2" >}}

The phone numbers attached are not community contacts — they are Division-level and Regional Police Commander contacts drawn from official UPF directories. A community member compiling this message would have needed to cross-reference official directories, maintain metropolitan-level situational awareness, and format a document with precisely the institutional veneer needed to ensure unedited forwarding. That is, charitably, an unusual skill set for an organic WhatsApp alert.

## IV. The Curious Architecture of the Message Itself

Here is where our thought experiment takes a turn from the mildly suspicious toward the genuinely interesting.

A well-designed message intended to propagate widely and unedited would need specific properties.

| Design Property | How This Message Achieves It |
|---|---|
| High forward probability | Security content achieves this — almost nobody deletes a security alert unforwarded |
| Wide demographic reach | Fear is non-discriminatory; this crosses age, class, and neighbourhood lines |
| Edit resistance | Official tone, numbered tips, and institutional contact numbers discourage personalisation |
| Natural propagation instruction | "Kindly share with others" — buried in official language so it feels like civic duty |
| Geographic specificity | Named areas generate localised engagement and increase forward probability |

The edit resistance deserves particular attention. Organic community messages get annotated, shortened, personalised as they travel. This message was structured to feel authoritative enough that most forwarders would transmit it verbatim. The institutional tone, the numbered format, the official-sounding contact list — all serve the function of discouraging light editing that would corrupt a consistent payload hash.

It is engineered for hash consistency. Which is either a remarkable coincidence or a design requirement.

{{< screenshot src="fig1-propagation-graph.svg" caption="Each forwarding decision is a voluntary edge declaration in a social graph" fig="1" >}}

## V. The Technical Layer — What the Network Actually Sees

### What WhatsApp Actually Does

WhatsApp uses end-to-end encryption via the Signal Protocol. Even Meta cannot read your messages — a fact they market enthusiastically and which is, for the most part, accurate.

However. And this is a significant however.

WhatsApp's client computes a hash of message content **client-side** — on your device — for its viral content detection system. This is how the "forwarded many times" label is generated. Your device reports frequently-forwarded message hashes back to WhatsApp's servers. Meta therefore maintains a database of hashes of widely-circulated messages, contributed involuntarily by every client that processed them.

Your telecom — MTN Uganda — cannot read the encrypted payload. But it can see:

- That your device connected to WhatsApp's servers
- When it connected, for how long, and how much data was transferred
- The size of the payload transmitted — which is a function of message length
- Your MSISDN, IMEI, and through CGNAT translation tables, your precise identity

MTN uses Carrier-Grade Network Address Translation, meaning you share a public IP with potentially hundreds of other subscribers. From outside MTN's network, you are invisible. But MTN maintains internal NAT translation tables that map exactly which private subscriber was behind that public IP at any given moment. You are completely identifiable to MTN regardless of CGNAT.

### The Payload Size Fingerprint

{{< screenshot src="fig4-payload-fingerprint.svg" caption="Ciphertext length is a function of plaintext length and is observable at the network layer" fig="4" >}}

A message of specific character length produces a ciphertext of predictable, consistent size. The content is encrypted, but the size of the encrypted payload is visible at the network layer.

This specific security alert has a fixed character count. Every device that received and forwarded it transmitted a payload of near-identical size within a narrow byte range. At MTN's packet inspection layer — accessible under Uganda's interception framework without judicial process — that payload size signature is queryable across all traffic logs without ever contacting Meta or decrypting anything.

Combined with timestamp and source MSISDN, one could reconstruct a complete propagation map built entirely from domestic network infrastructure. No international legal process. No platform cooperation. No conventional warrant.

{{< callout >}}
To be absolutely clear: the author is not suggesting this has been done, is being done, or would be done in relation to this specific message. This is a thought experiment about technical capability, not an allegation about operational intent. The author remains cheerfully uncertain about which is more unsettling.
{{< /callout >}}

## VI. Uganda's Surveillance Architecture — The Context

### The Huawei Safe City Deployment

Uganda contracted Huawei in 2019 for a Safe City deployment covering the Kampala Metropolitan Area. The stated scope included a CCTV network, a command centre at Naguru housing UPF, ISO, CMI and other agencies with unified dashboard access, facial recognition integrated into the camera network, and ANPR across major corridors.

The Naguru Joint Operations Centre is not a passive recording system. It provides real-time video analytics, cross-camera tracking to follow an individual continuously, retrospective search capability, and alerting on watchlisted faces without requiring human monitoring.

### The SIM-NIN Linkage — The Keystone

Uganda's mandatory SIM-to-NIN registration requirement tied every active SIM to a verified National ID, with biometric confirmation at point of registration — fingerprint matched against NIRA's national biometric database.

NIRA's database contains against each NIN: full legal name, date and place of birth, photograph (face biometric), fingerprints, physical address, and all issued documents.

Here is why this matters. The integration of Safe City and SIM-NIN creates a closed identification loop.

{{< screenshot src="fig3-identification-loop.svg" caption="SIM-NIN mandate is the keystone that closes the loop between face and communication record" fig="3" >}}

A face on a Kampala camera can be resolved to a full legal identity, a phone number, a home address, all communication patterns, and real-time location — within domestically controlled systems, in near real-time, without international legal cooperation.

For completeness: camera density drops sharply at the urban periphery, Huawei's facial recognition has documented accuracy degradation on darker skin tones, and NIRA's database has coverage gaps. The system has the technical ambition of a science fiction novel and the ground-truth reliability of a government IT project — impressive in theory, inconsistent in practice.

## VII. Metadata: More Dangerous Than Content

Content tells you what someone said once. Metadata tells you who they are, always.

| Content Reveals | Metadata Reveals |
|---|---|
| What you wrote in one message | Every person you communicate with |
| Your opinion on a specific topic | Communication frequency patterns revealing intimacy levels |
| Information you chose to share | Your physical location history — continuously |
| What you wanted someone to know | Your sleep patterns, work schedule, daily routine |
| A moment of your thinking | Your complete social graph: family, colleagues, casual contacts |
| — | Anomalies: who you suddenly stopped contacting |
| — | Who initiates contact with you that you never reciprocate |

The former NSA General Counsel Stewart Baker stated on the record that metadata absolutely tells you everything about somebody's life. This was not a boast. It was an admission.

Applied to our viral security alert: the people you chose to forward it to are your highest-trust, highest-concern contacts. You have just voluntarily labelled your inner circle in a format queryable against a biometrically-anchored subscriber database.

And the people who received it and did not forward it? Those are the most interesting nodes of all — either unusually security-conscious individuals, or people who recognised the message for something other than what it claimed to be.

## VIII. The Qui Bono Analysis

### Hypothesis A: A Very Organised Concerned Citizen

Someone who genuinely cared about community safety, happened to have access to all three KMP divisional command contact directories, maintained metropolitan-level situational awareness across 26 areas simultaneously, and wrote with the natural authority of an internal police briefing document. This person exists, presumably, somewhere between a civic superhero and a retired intelligence officer with an active WhatsApp subscription.

*Plausibility: Possible. Probability: Optimistic.*

### Hypothesis B: A Criminal Enterprise Running Cover

A widespread fear alert drives communities indoors and discourages movement, removing witnesses from the streets. If communities are self-imposing curfews, actual organised crime operates more freely. The alert instructs people to do exactly what makes them easier targets for burglary: predictable routines, no movement, reduced community presence.

There is something darkly comedic about the possibility that a security alert about panga gangs was written by panga gangs.

*Plausibility: Clever. Probability: Uncertain.*

### Hypothesis C: An Insurgency Information Operation

Uganda's security landscape includes documented urban networks affiliated with the Allied Democratic Forces, which have historically operated with Kampala components alongside their primary DRC theatre. An insurgency information operation would need to establish that the state cannot protect citizens, create conditions where communities self-isolate, and generate distrust between neighbours.

This message accomplishes all three without firing a single shot. The specific modus operandi described — the screaming neighbour tactic — is particularly elegant, as it weaponises the instinct to help, which is arguably the most demoralising thing you can do to a community's social fabric.

*Plausibility: Technically coherent. Probability: Hopefully low.*

### Hypothesis D: State-Adjacent Network Measurement

UCC's regulatory functions explicitly include network quality monitoring, traffic pattern analysis for capacity planning, and national security cooperation under their licensing framework. Measuring how a viral message propagates across licensed networks is entirely within their statutory mandate — not even controversial.

MTN Uganda independently has strong commercial motivation to know which neighbourhoods have high WhatsApp engagement density, which nodes drive disproportionate data consumption, and how information cascades affect network load.

A message seeded to carefully chosen nodes by an actor with intelligence access to telecom metadata could map the complete social graph of Kampala's informal information network, identify high-propagation community influencers, measure propagation velocity by neighbourhood, and establish baseline population response patterns to security information.

Nobody breaks any law Uganda recognises. Nobody needs to talk to Meta. The population does all the work voluntarily and with considerable civic enthusiasm.

*Plausibility: Technically well-supported. Probability: The author declines to speculate, largely on grounds of professional self-preservation.*

## IX. The Synthesis Nobody Asked For

The viral security alert is architecturally consistent with a deliberate information instrument. Its geographic scope exceeds what any single community source could plausibly command. Its structural properties maximise unedited propagation and hash consistency. It seeds 26 distinct geographic areas simultaneously, each functioning as an independent network probe.

Uganda has assembled — through the combination of the Huawei Safe City deployment, the NIRA biometric database, the SIM-NIN registration mandate, and the UCC interception framework — a population-scale passive surveillance infrastructure that is: persistent, retrospectively queryable, domestically sovereign, operating on a low legal threshold, and biometrically anchored.

The SIM-NIN requirement was the keystone. Without it, the camera network could identify faces but not reliably resolve them to communication records. With it, the loop is closed.

Any person who forwarded this message on a Ugandan-registered SIM generated a record — a communication metadata event tied to a biometrically-verified national identity — that is domestically accessible without international legal cooperation, without a conventional judicial warrant, and without the knowledge of the person who generated it.

{{< callout >}}
At this point the author would like to remind the reader that this is a thought experiment. None of the above constitutes evidence of wrongdoing by any specific actor. The infrastructure described is real, the technical capabilities are accurate, the legal framework reflects published Ugandan law, and the analytical reasoning is internally consistent. But the specific conclusions about who designed this message and why are entirely speculative. The author may simply have too much RAM and not enough social life.
{{< /callout >}}

## X. What This Tells Us About the Information Age

We have entered an era in which the infrastructure of ordinary social communication is simultaneously the infrastructure of population monitoring. Every forwarded message is a voluntary edge declaration in a social graph. Every SIM-registered device is a biometrically-anchored sensor node in a passive location network. Every WhatsApp connection is a metadata event logged against a government-verified identity.

This is not dystopian speculation. It is a description of systems that exist and are operational today.

The question of whether these systems are used appropriately, proportionately, and with adequate judicial oversight is a legitimate and important question for civil society, legislators, and regulators. That question is not the subject of this thought experiment. It is homework for the reader.

The more immediate observation: the decision to forward a message is now, in a technically meaningful sense, a more intelligence-rich act than the content of the message itself. The content is what you chose to communicate. The forwarding behaviour is who you are.

{{< pullquote centered="true" >}}
*You are not the sender of messages. You are the message.*
{{< /pullquote >}}

On that cheerful note, please do lock your gates at a specific hour and keep your phone charged. The panga gangs may well be real.

---

### Final Disclaimer

This document is a thought experiment. It was written by a person who spends too much time thinking about network infrastructure and not enough time watching football. It is not an intelligence assessment, not a legal opinion, not a policy recommendation, and emphatically not a conspiracy theory.

It is the written equivalent of staring at a WhatsApp message for slightly too long and asking: *what if?*

The author encourages the reader to apply the same analytical scepticism to this document as the document applies to the original message. The most important analytical discipline is recursive.

Go lock your gate. Turn on your security light. And perhaps — just perhaps — think twice before you forward the next one.

*— J.S.K. Makumbi, Kampala, April 2026*

{{< stamp >}}*Kindly share with others. (Just kidding. Please don't.)*{{< /stamp >}}
