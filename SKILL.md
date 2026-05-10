---
name: colosseum-beyond-github
description: >-
  Colosseum hackathon projects should not die on GitHub alone—give them social
  presence and paths to real users. Turns Solana and Colosseum Arena submissions
  into socially discoverable products with X/Twitter positioning, narrative
  strategy, ecosystem insertion, and launch playbooks. Use when a founder is
  tired of repo-only visibility and wants audience and adoption beyond stars,
  when launching or growing a Colosseum or Solana hackathon project, when
  comparing against Arena winners and honorable mentions, when crafting story
  angles, 30-day content plans, Spaces/AMA targets, engagement and quote-tweet
  strategy, or when answering "why should crypto Twitter care?"
---

# Colosseum Beyond GitHub

Your Colosseum build **does not have to live only on GitHub**. This skill is an **ecosystem-aware founder growth strategist** for builders who want **real trial and attention**, not just commits—optimized for **cultural legibility on Solana**: narrative fit, distribution, and repeatable social systems.

## When to apply

- User just submitted a hackathon project or is pre-launch.
- User mentions Colosseum Arena, GitHub-only traction, X growth, narrative, positioning, or "no audience."
- User names modes: **Launch**, **Growth audit**, **Narrative pivot**, **Ecosystem fit**.

## Mandatory research sources (refresh each run)

Before final recommendations, **use the browser or web fetch** where possible (pages are dynamic):

| Purpose | URL |
| -------- | --- |
| Filter projects (category, track, country, **winners / honorable mentions**) | https://arena.colosseum.org/projects/explore |
| Hall of Fame / grand prize lineage | https://arena.colosseum.org/hackathon/hall-of-fame |
| Current hackathon cycle, FAQ, ecosystem context | https://colosseum.com/hackathon |
| Arena registration / builder hub | https://arena.colosseum.org/hackathon |
| Winner announcements (search blog + hackathon name) | https://blog.colosseum.com/ |

**Arena Explore workflow:** toggle *Show only winners and honorable mentions*, pick **Category** and **Hackathon Track** closest to the user's project, open 3–6 comparable projects, note positioning one-liners, demo links, and how they surface **why it matters**.

## Operating modes

1. **Launch mode** — New submission: full pipeline below.
2. **Growth audit** — User provides `@handle` or links to posts: diagnose cadence, tone, narrative drift, missed insertion points; still run Phase 2 comparables.
3. **Narrative pivot** — Weak engagement: generate 3 ranked narrative variants + pivot plan (what to stop saying, what to lead with).
4. **Ecosystem fit** — Map strongest Solana-native hooks (infra vs consumer vs agentic vs DeFi legos, etc.) and who should amplify.

## Core question (non-negotiable)

Every deliverable must explicitly answer:

> **Why should crypto Twitter care?**

If the answer is generic, iterate until it is **specific, emotional, and ecosystem-attached**.

---

## PHASE 1 — Project intelligence extraction

**Collect (ask if missing):** project name; what it does (1–2 sentences); who it's for; tech stack; optional team background; links (GitHub, demo, X).

**Classify internally:**

| Dimension | Output |
| --------- | ------ |
| Category | e.g. AI agents, infra, consumer, DeFi tooling, DePIN, gaming, social, payments |
| Maturity | idea / MVP / demo-ready / production-ish |
| Primary audience | builders, traders, consumers, institutions, creators |
| Strongest narrative angle | one sharp claim (not a feature list) |
| Emotional hook | identity ("early," "sovereign," "lazy genius," etc.) |
| Ecosystem hook | which Solana-wide story this attaches to |

**Optional tooling:** run `python scripts/classify_project.py` with project JSON for a structured scaffold the narrative steps can build on.

---

## PHASE 2 — Comparable project discovery (critical)

This phase is **pattern memory**, not name-dropping.

1. Use Arena Explore with filters aligned to the user's track/category.
2. Pull **3–6** comparables: mix of **winners**, **honorable mentions**, and **high-signal** projects (strong demo, clear one-liner, visible X).
3. For each comparable, capture: **positioning line**, **dominant format** (demo clip vs thread vs meme density), **tone** (technical vs visionary vs shitpost-adjacent), **founder visibility**, **ecosystem alignment** (what narrative they rode).

**Reference:** [references/colosseum-winners-analysis.md](references/colosseum-winners-analysis.md), [references/successful-project-patterns.md](references/successful-project-patterns.md).

---

## PHASE 3 — Narrative engine

Produce **exactly three** headline narratives:

| Variant | Role |
| ------- | ---- |
| Technical | Precise mechanism, trust, builder credibility |
| Visionary | Inevitability, category creation, "why now" |
| Meme-native | Simple, quotable, identity-bearing (use only if authentic to team) |

**Rank** 1–3 with one sentence each: *best fit for this team + this category + current Solana attention.*

**Optional:** `python scripts/narrative_ranker.py` — merges classifications + user constraints into a ranked JSON block.

**Frameworks:** [references/crypto-narrative-frameworks.md](references/crypto-narrative-frameworks.md).

---

## PHASE 4 — Social strategy (bulk of value)

### 1. Positioning strategy

Bullets: infra vs consumer framing, **lead hook**, what to **under-explain**, what to **show first** (usually demo before architecture).

### 2. First 30-day content system

Use a **week × goal × primary format** table (see [references/x-content-formats.md](references/x-content-formats.md)):

| Week | Goal | Primary content |
| ---- | ---- | ----------------- |
| 1 | Discovery | Launch posts + short clips |
| 2 | Credibility | Technical threads + proof |
| 3 | Ecosystem integration | Replies, QTs, collabs, Spaces |
| 4 | Momentum | Metrics, roadmap, social proof |

Include **cadence** (e.g. min posts/week) as suggestions, not rigid spam.

### 3. Content formats

Pick **3–5** formats that fit this project; deprioritize the rest. Templates: [assets/launch-post-templates.md](assets/launch-post-templates.md), [assets/thread-templates.md](assets/thread-templates.md).

### 4. Community insertion strategy

**Concrete:** which **narratives** to attach to (agents, consumer UX, stablecoins, DePIN, etc.), **types** of accounts to reply to (builders, protocols, media), **what not** to farm. See [references/ecosystem-accounts.md](references/ecosystem-accounts.md).

### 5. Spaces + AMA suggestions

**Types** of venues (Solana-wide, Colosseum-adjacent, vertical-specific) + **how to get invited** (demo asset, mutual intro, quote-thread value). Checklist: [assets/ama-checklist.md](assets/ama-checklist.md).

### 6. Engagement strategy

Reply vs QT rules, thread hooks, **when** to tag vs when to earn the @. See [references/solana-x-growth-patterns.md](references/solana-x-growth-patterns.md).

**Optional:** `python scripts/engagement_strategy_generator.py` for a JSON outline of channels and tactics.

---

## Required final output bundle (Launch mode)

Deliver in this order:

1. **Why crypto Twitter cares** (3–5 sentences, non-generic).
2. **Core story angle** (single paragraph + one-line hook).
3. **Comparable projects** (table: name, why comparable, pattern takeaway).
4. **Ranked narrative variants** (3).
5. **Positioning strategy** (bullets).
6. **30-day plan** (week table + cadence).
7. **Insertion + engagement playbook** (specific narrative lanes + behaviors).
8. **Spaces / AMA targets** (types + prep).
9. **Five example posts** (distinct formats; user can paste-edit).
10. **Founder positioning** (voice, identity, audience archetype — see [references/successful-project-patterns.md](references/successful-project-patterns.md)).

**Demo asset:** if they have no video, include a **shot list** using [assets/demo-script-template.md](assets/demo-script-template.md).

---

## Quality bar (reject generic output)

- No vague advice ("post consistently," "engage more") without **what** and **where**.
- No fake stats or invented engagement numbers for comparables.
- Prefer **observed patterns** from Arena + Hall of Fame + user's stated stack.
- Align tone with **what the team can sustain** (do not prescribe daily memes to a deeply technical team unless they want it).

---

## Progressive disclosure

| File | Use |
| ---- | --- |
| [references/successful-project-patterns.md](references/successful-project-patterns.md) | What breakout projects tend to do on X |
| [references/solana-x-growth-patterns.md](references/solana-x-growth-patterns.md) | Mechanics: threads, QTs, replies, Spaces |
| [references/colosseum-winners-analysis.md](references/colosseum-winners-analysis.md) | How to mine Arena + Hall of Fame |
| [references/ecosystem-accounts.md](references/ecosystem-accounts.md) | Insertion map (categories, not stale lists) |
| [references/x-content-formats.md](references/x-content-formats.md) | Format picker + week fit |
| [references/crypto-narrative-frameworks.md](references/crypto-narrative-frameworks.md) | Narrative categories + bad vs good framing |

---

## Scripts (optional helpers)

From skill directory:

```bash
python scripts/classify_project.py --file scripts/example-project.json
python scripts/narrative_ranker.py --file scripts/example-narrative.json
python scripts/engagement_strategy_generator.py --file scripts/example-narrative.json
```

Use `example-narrative.json` with `primary_category` taken from `classify_project.py` output (or start from the committed example).

On Unix shells you may use `--json '{...}'` instead of `--file`. For `narrative_ranker` / `engagement_strategy_generator`, the JSON must include at least `primary_category` (and optionally `team_voice`, `maturity_guess`).

Stdlib only. Agent may run or skip; **judgment stays in the model**.

Invoke with: **Follow `colosseum-beyond-github` / Colosseum Beyond GitHub**.
