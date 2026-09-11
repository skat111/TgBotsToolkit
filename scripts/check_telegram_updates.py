"""Probe authoritative Telegram pages and signal whether the snapshot changed."""
import hashlib, json, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ['https://core.telegram.org/bots/api', 'https://core.telegram.org/tdlib/docs/', 'https://core.telegram.org/api']
manifest = json.loads((ROOT / 'docs' / 'manifest.json').read_text(encoding='utf-8'))
known = {x.get('url'): x.get('sha256') for x in manifest if x.get('url')}
changed = []
for url in SOURCES:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'TelegramBotToolkitUpdateProbe/1.0'})
        with urllib.request.urlopen(req, timeout=30) as response: digest = hashlib.sha256(response.read()).hexdigest()
        if known.get(url) and known[url] != digest: changed.append(url)
        elif url not in known: changed.append(url)
    except Exception as exc:
        print(json.dumps({'status': 'unavailable', 'url': url, 'error': str(exc)}))
print(json.dumps({'status': 'changed' if changed else 'current', 'changed_sources': changed}))
sys.exit(10 if changed else 0)
