import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / '.codex-plugin' / 'plugin.json').read_text(encoding='utf-8'))
assert manifest.get('name') == 'telegram-bot-toolkit' and manifest.get('version')
for path in (root / 'skills').glob('*/SKILL.md'):
    text = path.read_text(encoding='utf-8')
    assert text.startswith('---') and 'name:' in text and 'description:' in text
assert (root / 'docs' / 'START_HERE.md').exists()
print('release validation passed')
