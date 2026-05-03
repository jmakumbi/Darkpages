---
title: "AI in Your Practice: What Every Legal Professional Needs to Know"
date: 2026-05-02
draft: false
layout: "article"
description: "A guide for legal practitioners in Uganda on using AI responsibly — covering what it is, where it fails, privacy obligations under the DPPA 2019, the 3-Check Rule, and the real opportunities in the practice."
slug: "ai-in-your-practice"
url: "/ai-in-your-practice/"
noindex: true
toc: true
author: "James S. K. Makumbi"
subtitle: "James S.K. Makumbi · May 2026"
tags:
  - ai
  - legal-practice
  - uganda
  - dppa
  - professional-development
---

In 2023, two lawyers in New York each paid $5,000 to learn a lesson that cost them nothing but their willingness to verify. They submitted a court brief citing six case precedents. ChatGPT had fabricated all six — names, docket numbers, and quotes attributed to real judges who had said nothing of the sort. The judge was not sympathetic. Their names went on public record.

The lesson was not that AI is dangerous. The lesson was that they used a tool they did not understand. That is a fixable problem. That is what this page is for.

## What AI Actually Is

AI — specifically the large language models behind ChatGPT, Claude, and Microsoft Copilot — is software that predicts the next most probable word. Repeatedly. Billions of times per second. That is the entire mechanism. It is not thinking. It is not reasoning. It is calculating probability against a vast amount of text it was trained on.

I find the most useful mental model is this: picture a very well-read intern who has consumed every book, journal, newspaper, and website ever published. They are available at 2am, never complain, and produce well-structured prose on demand. They have also never been to court, never signed their name to anything, and have no idea what is true versus what merely sounds plausible. Fast, available, and in desperate need of supervision.

The confusion between AI and search engines is where most professionals trip up. They are doing entirely different things.

| 🔍 Google / Search Engine | 🤖 AI (ChatGPT, Claude, Copilot) |
|---|---|
| Queries the live internet | Generates text from training data |
| Returns links to real sources | Produces answers that sound authoritative |
| You evaluate the sources | The sources may not exist |
| Updated in real time | Knowledge has a cutoff date |

{{< callout type="warning" label="Important distinction" >}}
**Google finds. AI generates.** Treating AI output as a verified fact is the most common professional error with this technology. One is pointing you to a source that exists. The other is constructing language that sounds like it could be true.
{{< /callout >}}

## The Knowledge Cutoff Problem

Every AI model has a training cutoff — a date after which it knows nothing. Not "is less informed about." Knows nothing. If something happened after that date, the model cannot tell you, and it will not tell you it cannot tell you. It will produce an answer anyway.

| Model | Training Cutoff | Notes |
|---|---|---|
| ChatGPT (GPT-4o) | August 2025 | General purpose — most widely used |
| Claude (Sonnet 4.6) | August 2025 | Strong for professional drafting |
| Gemini 2.5 | January 2025 | Google's model |
| DeepSeek V3 | July 2024 | Open-source, self-hostable |
| Llama 4 | August 2024 | Open-source, self-hostable |
| Google Search | Real-time | Indexes the live web right now — this is not AI |

For Ugandan legal practice, the cutoff gap is more acute than it looks. Ugandan legal content is underrepresented in the training data of every major AI model. They were trained predominantly on English-language material from the US and UK legal systems. An AI asked about Ugandan constitutional law is working from whatever fragments of Ugandan content made it into its training set — which may be limited and is certainly not current.

{{< callout type="warning" label="Uganda-specific" >}}
UPPC and URSB are not integrated into any major AI tool. ULII has recently added document-level AI — an "Ask AI" button that lets you query a specific judgment you are already reading. That is a useful development, and the document-scoped architecture is sensible: it keeps the model small and responses fast. What it is not is a legal research AI. You still have to find the right case first. When a general-purpose AI answers a question about Ugandan law unprompted, it is still drawing on whatever it absorbed during training. Verify on [ulii.org](https://ulii.org) and [uppc.go.ug](https://uppc.go.ug).
{{< /callout >}}

## The Hallucination Problem

Hallucination is the technical term for what happens when AI produces confident, fluent, entirely fabricated content. It is not a bug that will eventually be patched. It is a structural consequence of how these models work. They are predicting the most probable next word — and sometimes the most probable next word is wrong.

The model has no internal alarm that fires when it does not know something. It always answers. The two lawyers in *Mata v. Avianca* were not dealing with an experimental edge case. They were dealing with a model doing exactly what it was designed to do.

In the context of Ugandan legal practice, this means an AI can produce:

- Fully fabricated case citations — complete with plausible-sounding docket numbers, dates, and holdings from cases that were never decided
- References to legislation that was never enacted, or to the wrong version of legislation that was
- Legally incorrect interpretations delivered with the same confident tone as legally correct ones
- Analysis based on UK or US legal principles presented as if they apply without modification to Ugandan law

Try it after reading this. Ask an AI to describe a landmark Constitutional Court case from Uganda. Read what comes back. Then check ULII. That exercise will teach you more about hallucination than any explanation I can give.

## What It Can Actually Do For Your Practice

The answer to "AI hallucinates and has a knowledge cutoff" is not "therefore never use it." The answer is "use it for the right tasks with appropriate oversight." There is a meaningful distinction between tasks where AI's limitations are disqualifying and tasks where they are manageable.

AI is not a better Google. It is a different kind of tool entirely — a thinking partner that can work with documents and ideas rather than a search index. Where it genuinely adds value:

| Task | What This Looks Like |
|---|---|
| First drafts | A demand letter at 10pm. A service agreement from bullet points. NDA recitals from a brief. The structure is usually sound — local law nuances need your eye. |
| Document analysis | Give it two contracts, ask what the material differences are. That analysis takes hours manually. Minutes with AI. |
| Summarisation | A 40-page government procurement tender condensed to the key obligations and deadlines. Verify the summary, then use it. |
| Plain English explanations | A client does not understand the indemnity clause. Ask AI to explain the implications in ordinary language — not just the definition. Check the explanation. Then use it. |
| Research framing | Use AI to identify what questions to ask and what areas of law are relevant. Use ULII to find the actual law. |
| Meeting notes | Microsoft 365 Copilot in Teams transcribes and summarises automatically — if your firm has Business Premium, this is available now. |

The compound advantage is worth understanding. Week one: you save two to three hours per document on first drafts. By month one, you have learned to prompt effectively and output quality has improved substantially. By quarter one, you can offer services that were not commercially viable before — comprehensive contract reviews, compliance assessments at scale. That progression is real, and it is available to any practitioner who starts now with appropriate safeguards.

## The Tools Available

| Category | Tool | Best For | Privacy Level |
|---|---|---|---|
| General purpose | ChatGPT · Claude · Gemini | Drafting, research, summarising | Free = significant risk · Pro = materially safer |
| Microsoft integrated | Copilot (Word, Outlook, Teams) | Office documents, meeting notes | High — stays within your M365 tenant |
| Specialist legal | Harvey AI · Clio Duo | Legal drafting | High — not yet East Africa-localised |
| Private / self-hosted | Ollama (local server) | Confidential matters, offline use | Maximum — data never leaves the device |

{{< callout type="tip" label="Recommended starting point" >}}
For most practitioners, [Claude.ai](https://claude.ai) free tier is the cleanest place to start. No client data. No case facts. Use it for internal drafts and to understand the technology. If your firm is on Microsoft 365 Business Premium, M365 Copilot is one administrator toggle away and is the most appropriate tool for firm work.
{{< /callout >}}

## Privacy — The Non-Negotiable

The privacy question is not a technicality. The Uganda Data Protection and Privacy Act 2019 applies to every query you send to a foreign-hosted AI platform if that query contains personal data. A client's name is personal data. Their case facts are personal data. Their financial situation is personal data. Pasting any of that into a free consumer AI tool is a potential breach of client confidentiality.

On the Microsoft Copilot distinction — this matters and most people get it wrong. There are two products with "Copilot" in the name that behave differently:

- **M365 Copilot in Word, Outlook, and Teams** is included in Microsoft 365 Business Premium. Your data stays within your company's Microsoft tenant. Microsoft is contractually prohibited from using it for training. This is a meaningfully different privacy posture.
- **The Copilot button on your Windows 11 taskbar** is a different product. If you are logged into Windows with your work Microsoft account — which most people in a firm environment are — that Copilot routes through your company's Microsoft tenant. Your IT administrator can see those queries. Personal matters go on personal devices.

### The Three Zones

This framework governs all AI use. The risk is not the technology — it is mixing contexts.

<div class="zones-table">

| | 🟢 Personal | 🔵 Professional Development | 🔴 Work |
|---|---|---|---|
| Device | Personal device | Work or personal | Work device |
| Account | Personal account | Work account — learning only | Work account |
| Employer visibility | None | Possible | Full |
| Rule | Your data, your risk | No personal content | Client governance applies |

</div>

{{< callout type="warning" label="Zone mixing creates real risk" >}}
Using your work M365 account on a personal device means Copilot sessions may route through your company tenant. Using M365 Copilot for personal matters means that content enters your employer's data environment. These are not hypothetical — they are the scenarios that generate professional disciplinary complaints. Keep the zones clean.
{{< /callout >}}

## The Uganda Context

There is no AI-specific law in Uganda yet. The DPPA 2019 is the current framework. The Uganda Law Society has not issued formal guidance for practitioners. NITA-U is the regulatory body. None of this means you have no obligations — it means you currently set your own standard of care.

| Area | Where We Stand |
|---|---|
| DPPA 2019 | Applies to all data shared with AI tools — including queries sent to consumer platforms hosted abroad. Penalties: up to UGX 4.8 million or 10 years imprisonment for unlawful obtaining or disclosure of personal data. |
| ULII AI (new) | ULII has added document-level AI — an "Ask AI" feature on individual judgment pages. The architecture is document-scoped RAG, likely to keep the model small and responses fast. Useful for interrogating a case you have already found. It does not replace finding the right case yourself, and UPPC and URSB remain unintegrated. Every AI output touching Ugandan law must still be independently verified. |
| ULS guidance | The Uganda Law Society has not yet issued formal AI guidance for practitioners. The standard of care is currently self-defined. |
| Laws.Africa | South African NPO that has digitised 98 Uganda Acts and 8 Statutory Instruments in partnership with ULII. Adding an AI Knowledge Base API in 2026. Approach with architecture awareness — see below. |
| First-mover position | Firms that adopt AI responsibly now will lead. The question is not whether AI will change legal practice in Uganda — it is who gets there first with proper safeguards. |

On Laws.Africa specifically: the risk is not the legislation data — legislation is public law. The risk is what you do with it. If their AI chat feature launches and you type a client's name into that query, that personal data has just crossed into South Africa. The correct architecture: use their API as a one-way legislation feed into a local database on your own server. All AI reasoning happens on your hardware. Laws.Africa never sees a client query. *Laws.Africa supplies the law. Your hardware does the thinking. Client data never leaves.*

## The 3-Check Rule

Memorise these three words before you use AI professionally. They are not a bureaucratic procedure. They are the professional standard you are applying when you put your name on anything AI-assisted.

{{< three-check-rule >}}

{{< rule-box >}}
If you cannot answer *yes* to all three — do not use it.
{{< /rule-box >}}

## The Bigger Opportunity: In-House AI

Everything above is about using other people's tools safely. There is a more interesting conversation about what you can own.

Running AI on your own hardware eliminates the entire class of privacy concerns above by design. Not by policy — by architecture. Client data never crosses a border because there is no border to cross. The models are open-source (Llama, Gemma, DeepSeek, Phi) and free. One hardware investment. No per-seat billing. Load-shedding and MTN outages do not disable your AI.

| Scenario | DPPA Position | Recommended Action |
|---|---|---|
| ✅ AI runs locally — all processing on-premises | Compliant by architecture — no cross-border transfer | Preferred for all client work |
| ⚠ Enterprise cloud AI — no client PII in queries | Manageable — document your firm policy | Enterprise accounts only; written policy required |
| ❌ Free AI tools with client names or case facts | Potential breach — personal data transferred abroad | Stop immediately. Switch to enterprise or self-hosted. |

I have built a working implementation of the architecture described above. DocuRef is a local AI document search and Q&A system — point it at a folder of PDFs and Word files, ask questions in plain English, and every answer cites the exact document and page it came from. Runs entirely on Ollama. No cloud. No internet required. The 3-Check Rule is built into the output — every answer comes with its source.

The same architecture applied to Laws.Africa's Uganda legislation API is in development: a Uganda legal AI research system where Laws.Africa supplies the legislation and local hardware does the reasoning. DPPA-compliant by design, not by policy.

## Your First Week

Do not start with client work. Start where a mistake costs you time, not your reputation.

1. **Tonight:** Create a free [Claude.ai](https://claude.ai) account. No client data. Ask it to explain a legal concept you know well — see how it performs. The gaps will be instructive.
2. **Days 2–3:** Use AI to draft one internal document. Not client-facing. Compare it to what you would have written. Note where it is useful and where you had to correct it.
3. **Week 2:** Apply the 3-Check Rule to an AI research task. Cross-reference on ULII. Build your own view on what it can and cannot do for your practice area.
4. **Week 3+:** If your firm is on Microsoft 365 Business Premium, evaluate M365 Copilot. Ask your IT administrator whether it is enabled.

{{< callout type="tip" label="Suggested resources" >}}
[ULII](https://ulii.org) — Uganda Legal Information Institute · [UPPC](https://uppc.go.ug) — Uganda Printing & Publishing Corporation · [Laws.Africa](https://laws.africa) — Uganda Acts digitised with ULII · [Claude.ai](https://claude.ai) — recommended starting tool
{{< /callout >}}

{{< rule-box >}}
AI drafts. You decide. *Always.*
{{< /rule-box >}}

{{< callout type="reference" label="Available on request" >}}
This material is also available as a structured 45-minute in-person session with a slide deck and participant workbook. The session is designed for legal teams and professional associations. Contact me if you want to bring it to your firm or organisation.
{{< /callout >}}

Questions on any of this — self-hosted setups, M365 Copilot deployment, or the document AI system — reach me on WhatsApp at **+256 783 354036** or email [james@billableonline.co](mailto:james@billableonline.co).
