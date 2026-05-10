#!/usr/bin/env python3
"""
Engagement strategy JSON scaffold from category + maturity.
Stdlib only.

Usage:
  python scripts/engagement_strategy_generator.py --json '{"primary_category":"infra","maturity_guess":"mvp-or-demo"}'
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


def tactics(category: str, maturity: str) -> dict[str, Any]:
    base = {
        "reply_strategy": "Add technical or user-value substance; avoid naked self-links.",
        "qt_strategy": "Attach to news with a reframing + demo clip when possible.",
        "cadence_hint_posts_per_week": 3 if maturity == "idea" else 4,
        "spaces": "Target 1 Space or co-hosted AMA in weeks 3-4 once demo is stable.",
    }

    lane = {
        "ai-agents": "Join AI x Solana and agent safety conversations with reproducible mini-demos.",
        "consumer": "Join consumer UX and onboarding threads; show screen recordings over jargon.",
        "infra": "Join devex and reliability threads; share benchmarks with methodology.",
        "defi": "Join risk and mechanism design discussions; disclose limits early.",
        "depin": "Join hardware + incentive design threads; show field photos or maps.",
        "gaming": "Join distribution and UGC threads; lead with fun clip.",
        "social-creator": "Join creator economy threads; emphasize ownership mechanics.",
        "privacy-zk": "Join privacy pragmatism threads; avoid academic pile-ons without code.",
        "payments-stable": "Join payments and merchant UX threads; show settlement clarity.",
        "founder-growth": "Join Arena / hackathon recap and builder growth threads; lead with demo completion and user proof, not repo links.",
        "general-solana": "Join whichever Solana narrative honestly fits the product.",
    }.get(category, "Join whichever Solana narrative honestly fits the product.")

    base["ecosystem_insertion_lane"] = lane
    base["metrics_to_collect"] = [
        "demo completion rate",
        "reply quality (subjective weekly review)",
        "inbound DMs from builders",
    ]
    return base


def main() -> int:
    parser = argparse.ArgumentParser(description="Engagement strategy scaffold.")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--json", help="JSON string with primary_category, maturity_guess")
    g.add_argument("--file", help="Path to JSON file with same keys")
    args = parser.parse_args()
    raw = args.json if args.json else open(args.file, encoding="utf-8").read()
    try:
        data: dict[str, Any] = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 2

    category = str(data.get("primary_category") or "general-solana")
    maturity = str(data.get("maturity_guess") or "unknown")

    out = {
        "inputs": {"primary_category": category, "maturity_guess": maturity},
        "engagement_strategy": tactics(category, maturity),
        "reminder": "Agent should replace generics with named venues, threads, and accounts found live.",
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
