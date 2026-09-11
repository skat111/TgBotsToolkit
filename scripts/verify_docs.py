"""Check archive hashes, traversal closure and the main API entry points."""
from collections import Counter
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parents[1]
rows = json.loads((root/'docs/manifest.json').read_text(encoding='utf-8'))
urls = {r['url'] for r in rows}
failures = []
counts = Counter()
total = 0
def check(r):
    if 'error' in r:
        return None
    raw = (root/r['raw']).read_bytes()
    problems = []
    if hashlib.sha256(raw).hexdigest() != r['sha256']:
        problems.append('Hash mismatch: '+r['url'])
    if r['markdown'] and (root/r['markdown']).stat().st_size < 50:
        problems.append('Empty Markdown: '+r['url'])
    missing = set(r['links']) - urls
    if missing:
        problems.append('Unvisited links: '+str(sorted(missing)))
    path = urlsplit(r['url']).path
    group = 'tdlib/docs' if path.startswith('/tdlib/docs/') else path.strip('/').split('/')[0] or 'home'
    return len(raw), group, problems
with ThreadPoolExecutor(max_workers=16) as pool:
    for checked in pool.map(check,rows):
        if checked:
            size, group, problems = checked
            total += size
            counts[group] += 1
            failures.extend(problems)
for path in ['bots/api','bots/webapps','bots/payments','api','mtproto','tdlib','tdlib/docs/','gateway/api','passport','widgets','schema/json']:
    url = 'https://core.telegram.org/'+path
    if not any(r['url']==url and 'error' not in r for r in rows):
        failures.append('Missing required entry point: '+url)
supplement = root/'docs/supplemental'
for r in json.loads((supplement/'manifest.json').read_text(encoding='utf-8')):
    if hashlib.sha256((supplement/r['file']).read_bytes()).hexdigest()!=r['sha256']:
        failures.append('Supplement hash mismatch: '+r['file'])
result = dict(saved=sum('error' not in r for r in rows),fetch_errors=[r for r in rows if 'error' in r],
              raw_bytes=total,groups=dict(sorted(counts.items())),verification_failures=failures,
              bot_api_sections=len(list((root/'docs/bot-api').glob('*.md')))-1)
(root/'docs/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
