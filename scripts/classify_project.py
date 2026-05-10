#!/usr/bin/env python3
"""
Structured project classification scaffold for Colosseum Beyond GitHub.
Stdlib only. Outputs JSON to stdout.

Usage:
  python scripts/classify_project.py --json '{"name":"X","description":"...","audience":"...","stack":"..."}'
  python scripts/classify_project.py --file project.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


KEYWORD_BUCKETS: list[tuple[str, str]] = [
    ("ai-agents", r"\b(ai|agent|llm|model|inference|copilot|automation)\b"),
    ("consumer", r"\b(app|mobile|ios|android|consumer|user|wallet ui|onboard)\b"),
    ("infra", r"\b(rpc|indexer|infra|devtools|sdk|observability|monitor)\b"),
    ("defi", r"\b(swap|amm|dex|lend|perp|liquidity|yield|vault)\b"),
    ("depin", r"\b(depin|iot|sensor|hardware|gps|map|device)\b"),
    ("gaming", r"\b(game|player|unity|unreal|ugc|guild)\b"),
    ("social-creator", r"\b(social|creator|nft|content|fan|community)\b"),
    ("privacy-zk", r"\b(zk|zero knowledge|privacy|proof)\b"),
    ("payments-stable", r"\b(pay|payment|stable|remit|checkout|merchant)\b"),
    (
        "founder-growth",
        r"\b(colosseum|arena hackathon|hackathon submission|github-only|repo-only|social presence|"
        r"crypto twitter|no audience|discoverability|launch narrative|founder growth|go-to-market|gtm)\b",
    ),
]


def _text_blob(data: dict[str, Any]) -> str:
    parts = [
        str(data.get("name", "")),
        str(data.get("description", "")),
        str(data.get("audience", "")),
        str(data.get("stack", "")),
        str(data.get("team_background", "")),
    ]
    return " \n ".join(parts).lower()


def infer_categories(text: str) -> list[str]:
    hits: list[str] = []
    for slug, pattern in KEYWORD_BUCKETS:
        if re.search(pattern, text, re.I):
            hits.append(slug)
    return hits or ["general-solana"]


def primary_category(categories: list[str], text: str) -> str:
    priority = [
        "ai-agents",
        "defi",
        "infra",
        "consumer",
        "depin",
        "gaming",
        "social-creator",
        "privacy-zk",
        "payments-stable",
        "founder-growth",
        "general-solana",
    ]
    for p in priority:
        if p in categories:
            return p
    return categories[0]


def maturity_heuristic(text: str) -> str:
    if re.search(r"\b(mvp|prototype|demo|testnet|beta)\b", text):
        return "mvp-or-demo"
    if re.search(r"\b(idea|concept|planning|wip)\b", text):
        return "idea"
    if re.search(r"\b(mainnet|production|users:|live)\b", text):
        return "production-ish"
    return "unknown"


def emotional_hooks(category: str) -> list[str]:
    return {
        "ai-agents": ["sovereignty over repetitive onchain work", "trust-but-verify automation"],
        "consumer": ["delight and speed", "ownership without jargon"],
        "infra": ["fewer 3am outages", "shippable reliability"],
        "defi": ["transparent risk", "composable leverage with limits"],
        "depin": ["real world meets incentives", "coordination at scale"],
        "gaming": ["fun first", "player-owned upside"],
        "social-creator": ["portable audience", "direct fan relationship"],
        "privacy-zk": ["defense in depth", "selective disclosure"],
        "payments-stable": ["settlement that feels invisible", "global access"],
        "founder-growth": ["proof someone tried it", "visibility without cringe"],
        "general-solana": ["why this chain for this moment", "builder pragmatism"],
    }.get(category, ["why this chain for this moment", "builder pragmatism"])


def ecosystem_hooks(category: str) -> list[str]:
    return {
        "ai-agents": ["Solana AI / agent narrative", "wallet + agent safety"],
        "consumer": ["mobile and consumer crypto UX", "fee abstraction"],
        "infra": ["RPC, indexing, devex", "ecosystem reliability"],
        "defi": ["composability and risk culture", "liquidity legos"],
        "depin": ["coordination and proofs", "hardware meets crypto"],
        "gaming": ["distribution and economies", "onchain assets"],
        "social-creator": ["creator ownership", "social graphs"],
        "privacy-zk": ["privacy with pragmatism", "verifiable compute"],
        "payments-stable": ["payments and settlement", "merchant UX"],
        "founder-growth": ["Arena and hackathon discovery", "crypto Twitter builder culture"],
        "general-solana": ["Solana performance story", "founder pragmatism"],
    }.get(category, ["Solana performance story", "founder pragmatism"])


def classify(data: dict[str, Any]) -> dict[str, Any]:
    text = _text_blob(data)
    categories = infer_categories(text)
    primary = primary_category(categories, text)
    return {
        "input_echo": {
            "name": data.get("name"),
            "description": data.get("description"),
            "audience": data.get("audience"),
            "stack": data.get("stack"),
        },
        "classification": {
            "categories_detected": categories,
            "primary_category": primary,
            "maturity_guess": maturity_heuristic(text),
        },
        "narrative_seeds": {
            "emotional_hooks": emotional_hooks(primary),
            "ecosystem_hooks": ecosystem_hooks(primary),
        },
        "next_steps_for_model": [
            "Open Arena Explore with matching Category/Track; pick 3-6 comparables.",
            "Draft 3 narratives: technical, visionary, meme-native (if authentic).",
            "Answer explicitly: Why should crypto Twitter care?",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify hackathon project for social launch planning.")
    parser.add_argument("--json", help="JSON string with keys name, description, audience, stack, optional team_background")
    parser.add_argument("--file", help="Path to JSON file with same keys")
    args = parser.parse_args()

    if bool(args.json) == bool(args.file):
        print("Provide exactly one of --json or --file", file=sys.stderr)
        return 2

    if args.json:
        raw = args.json
    else:
        path = Path(args.file)
        try:
            raw = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"File not found: {path}", file=sys.stderr)
            return 2
        except OSError as exc:
            print(f"Could not read file: {exc}", file=sys.stderr)
            return 2
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("JSON root must be an object", file=sys.stderr)
        return 2

    out = classify(data)
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
