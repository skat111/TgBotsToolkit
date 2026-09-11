#!/usr/bin/env python3
"""Install a small adapter prompt for popular coding agents.

The documentation stays in one toolkit directory; adapters only point agents to it.
"""
from __future__ import annotations
import argparse, os, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
TARGETS = {
    'claude': (HOME / '.claude' / 'skills' / 'telegram-bot-toolkit' / 'SKILL.md', 'global'),
    'cursor': (Path('.cursor') / 'rules' / 'telegram-bot-toolkit.mdc', 'project'),
    'gemini': (Path('GEMINI.md'), 'project'),
    'cline': (Path('.clinerules') / 'telegram-bot-toolkit.md', 'project'),
    'roo': (Path('.roo') / 'rules' / 'telegram-bot-toolkit.md', 'project'),
    'continue': (Path('.continue') / 'rules' / 'telegram-bot-toolkit.md', 'project'),
    'windsurf': (Path('.windsurf') / 'rules' / 'telegram-bot-toolkit.md', 'project'),
    'opencode': (Path('AGENTS.md'), 'project'),
    'aider': (Path('CONVENTIONS.md'), 'project'),
    'codex': (HOME / '.agents' / 'plugins' / 'telegram-bot-toolkit' / 'INSTALL.md', 'global'),
}

def prompt(agent, toolkit):
    return f'''# Telegram Bot Toolkit ({agent})

Use the Telegram Bot Toolkit at `{toolkit}` for Telegram bot work.

Before implementation, run:
`python "{toolkit / 'scripts' / 'check_updates.py'}" --check`
If an update is available, install it with `--install` and then use the refreshed files.
Read `{toolkit / 'skills' / 'telegram-bot-builder' / 'SKILL.md'}` for UI design, Bot API rules, Premium/custom emoji eligibility, and framework starters. Read `{toolkit / 'skills' / 'telegram-docs' / 'SKILL.md'}` for documentation lookup. Prefer the bundled official snapshot over guesses, and cite the relevant local source when explaining an API choice.
'''

def main():
    ap = argparse.ArgumentParser(description='Install Telegram Bot Toolkit adapters')
    ap.add_argument('--target', default='all', help='all or comma-separated: ' + ','.join(TARGETS))
    ap.add_argument('--project', default='.', help='project directory for project-scoped adapters')
    ap.add_argument('--toolkit', default=str(ROOT), help='path to this toolkit')
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args(); toolkit = Path(args.toolkit).resolve(); project = Path(args.project).resolve()
    names = list(TARGETS) if args.target == 'all' else [x.strip().lower() for x in args.target.split(',')]
    unknown = sorted(set(names) - set(TARGETS))
    if unknown: ap.error('unknown targets: ' + ', '.join(unknown))
    for name in names:
        relative, scope = TARGETS[name]
        path = (project / relative) if scope == 'project' else relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not args.force:
            print(f'skipped {name}: {path} exists (use --force to replace)'); continue
        if path.exists():
            backup = path.with_suffix(path.suffix + '.telegram-toolkit.bak')
            shutil.copy2(path, backup)
        path.write_text(prompt(name, toolkit), encoding='utf-8')
        print(f'installed {name}: {path}')

if __name__ == '__main__': main()
