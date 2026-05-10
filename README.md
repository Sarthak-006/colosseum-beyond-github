# colosseum-beyond-github

Portable [Agent Skill](https://agentskills.io/specification) for Cursor (and other agents that implement the standard). It helps Colosseum and Solana hackathon builders turn **GitHub-only** projects into **socially discoverable** launches: positioning on X, Arena comparables, narrative variants, a 30-day content system, and engagement playbooks grounded in Solana ecosystem culture.

**Repository name:** must match the skill id in `SKILL.md` (`colosseum-beyond-github`).  
**Public repo:** [https://github.com/Sarthak-006/colosseum-beyond-github](https://github.com/Sarthak-006/colosseum-beyond-github)

## Repository layout

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Required skill entry: YAML frontmatter + full agent instructions |
| [references/](references/) | Deep-dive markdown loaded on demand (Arena patterns, X mechanics, narratives) |
| [assets/](assets/) | Templates (threads, launch posts, AMA checklist, demo shot list) |
| [scripts/](scripts/) | Optional Python 3 **stdlib-only** JSON scaffolds (`classify_project.py`, `narrative_ranker.py`, `engagement_strategy_generator.py`) |
| [LICENSE](LICENSE) | MIT |
| [.gitattributes](.gitattributes) | Normalizes LF line endings for Markdown, Python, and JSON |

## Preflight before you push

1. `npx skills-ref validate .` → expect **Valid skill** ([Agent Skills](https://agentskills.io/specification)).
2. `python -m py_compile scripts/classify_project.py scripts/narrative_ranker.py scripts/engagement_strategy_generator.py`
3. Run the three example commands under **Technical implementation** and confirm JSON prints to stdout.
4. Submit **`repoLink`** without the `.git` suffix: `https://github.com/Sarthak-006/colosseum-beyond-github`.

## Security

Do not commit API keys, Colosseum agent keys, or wallet material. This repository is documentation and small stdlib scripts only.

## Technical implementation

- **Skill format:** Agent Skills YAML frontmatter (`name`, `description`, `license`, `compatibility`) plus Markdown body. See [Cursor Agent Skills](https://cursor.com/docs/context/skills) and [agentskills.io specification](https://agentskills.io/specification).
- **Validation:** From this directory run `npx skills-ref validate .` - expect `Valid skill`.
- **Scripts:** No third-party packages. Run from the skill root, for example:
  - `python scripts/classify_project.py --file scripts/example-project.json`
  - `python scripts/narrative_ranker.py --file scripts/example-narrative.json`
  - `python scripts/engagement_strategy_generator.py --file scripts/example-narrative.json`
- **Solana / Colosseum alignment:** The skill instructs agents to use official Arena and Colosseum URLs (explore, hall of fame, hackathon pages, blog) and to anchor recommendations in **Solana-native** narratives (agents, consumer UX, infra, DeFi, payments, etc.). It does not submit transactions; it improves **how builders communicate** projects that do.

## Install in Cursor

1. Cursor Settings → Rules → Add Rule → **Remote Rule (GitHub)**  
2. Repository URL: `https://github.com/Sarthak-006/colosseum-beyond-github`  
   Or clone into `.cursor/skills/colosseum-beyond-github/` so `SKILL.md` lives at `.cursor/skills/colosseum-beyond-github/SKILL.md`.

Invoke in Agent chat with: **Follow `colosseum-beyond-github` / Colosseum Beyond GitHub**.

## Colosseum Agent Hackathon note

If you attach this repo as your **`repoLink`**, also fill **`solanaIntegration`** honestly in the hackathon API (see [Colosseum skill / project fields](https://colosseum.com/agent-hackathon/skill.md)): this project is a **Cursor skill** that drives adoption and clarity for **Solana and Colosseum** builders (Arena research workflows, ecosystem positioning). It is not an on-chain program; describe it as tooling and methodology that improves how Solana hackathon projects are explained and distributed.

## Contributing

Issues and PRs welcome on GitHub. Keep `name` in `SKILL.md` identical to the repository name. When you tag meaningful releases, bump `metadata.version` in `SKILL.md` to match.
