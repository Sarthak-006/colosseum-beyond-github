#!/usr/bin/env python3
"""
Ranks narrative variants from classification + optional user hints.
Stdlib only. Outputs JSON.

Usage:
  python scripts/narrative_ranker.py --json '{"primary_category":"ai-agents","team_voice":"technical",...}'
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


def build_variants(category: str) -> dict[str, str]:
    templates = {
        "ai-agents": {
            "technical": "Agents that execute repeatable onchain workflows with explicit trust boundaries and observability.",
            "visionary": "Coordination layer for machine-native commerce—humans set intent, systems settle work.",
            "meme_native": "Your intern is now onchain and auditable.",
        },
        "consumer": {
            "technical": "Latency- and fee-aware UX that keeps custody assumptions explicit while hiding chain noise.",
            "visionary": "Consumer crypto that feels like software people already understand—until ownership surprises them.",
            "meme_native": "Crypto UX that passes the mom test.",
        },
        "infra": {
            "technical": "Production-grade infrastructure primitives with measurable reliability and operator ergonomics.",
            "visionary": "The missing layer teams reach for after their first mainnet incident.",
            "meme_native": "Sleep through mainnet upgrades.",
        },
        "defi": {
            "technical": "Risk-transparent mechanisms with bounded assumptions and clear failure modes.",
            "visionary": "Liquidity and leverage that respect how humans actually behave.",
            "meme_native": "Fewer rugs, more receipts.",
        },
        "depin": {
            "technical": "Incentive-aligned hardware and data flows with verification hooks.",
            "visionary": "Real-world coordination markets that only crypto can price honestly.",
            "meme_native": "Proof of grass-touching, onchain.",
        },
        "gaming": {
            "technical": "Composable game economies with performance-first client loops.",
            "visionary": "Players own the upside without sacrificing fun.",
            "meme_native": "Touch grass later—loot now.",
        },
        "social-creator": {
            "technical": "Portable reputation and audience graphs with explicit consent surfaces.",
            "visionary": "Creators keep the relationship—not the platform.",
            "meme_native": "Fans in, rent-seekers out.",
        },
        "privacy-zk": {
            "technical": "Selective disclosure and verifiable compute with pragmatic threat modeling.",
            "visionary": "Privacy as a default product surface, not a whitepaper.",
            "meme_native": "Show less, prove more.",
        },
        "payments-stable": {
            "technical": "Settlement paths tuned for real merchants and real latency constraints.",
            "visionary": "Money that moves at internet speed with adult supervision.",
            "meme_native": "Tap, pay, done.",
        },
        "founder-growth": {
            "technical": "Repeatable distribution systems: demo funnel, proof assets, and insertion points builders can execute weekly.",
            "visionary": "Arena-grade builds deserve Arena-grade attention—social discovery as first-class shipping, not an afterthought.",
            "meme_native": "Stars don't ship your demo—you do.",
        },
        "general-solana": {
            "technical": "Solana-native implementation choices driven by measurable constraints.",
            "visionary": "A product that only makes sense in a high-throughput, composable ecosystem.",
            "meme_native": "Fast chain, slow excuses.",
        },
    }
    return templates.get(category, templates["general-solana"])


def rank_order(team_voice: str | None) -> list[str]:
    voice = (team_voice or "").lower()
    if "meme" in voice or "shitpost" in voice:
        return ["meme_native", "visionary", "technical"]
    if "vision" in voice or "founder" in voice or "story" in voice:
        return ["visionary", "technical", "meme_native"]
    if "technical" in voice or "engineer" in voice:
        return ["technical", "visionary", "meme_native"]
    return ["visionary", "technical", "meme_native"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank narrative variants.")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--json", help="JSON string with primary_category and optional team_voice")
    g.add_argument("--file", help="Path to JSON file with same keys")
    args = parser.parse_args()
    raw = args.json if args.json else open(args.file, encoding="utf-8").read()
    try:
        data: dict[str, Any] = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 2

    category = str(data.get("primary_category") or "general-solana")
    variants = build_variants(category)
    order = rank_order(data.get("team_voice"))
    ranked = [{"slot": i + 1, "key": k, "narrative": variants[k]} for i, k in enumerate(order)]

    out = {
        "primary_category": category,
        "variants": variants,
        "ranked": ranked,
        "note": "Model must still tailor copy to the user's actual product - this is a scaffold.",
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
