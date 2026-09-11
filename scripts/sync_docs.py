"""Download the public documentation linked from Telegram's developer portals.
Install dependencies: python -m pip install requests beautifulsoup4 markdownify
Run: python scripts/sync_docs.py (resumes cached successful downloads).
"""
import concurrent.futures as cf
import hashlib
import json
from pathlib import Path
import time
import threading
from urllib.parse import urljoin, urlsplit, urlunsplit
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
SEEDS = ['https://core.telegram.org/', 'https://core.telegram.org/bots/api',
         'https://core.telegram.org/api', 'https://core.telegram.org/mtproto',
         'https://core.telegram.org/tdlib', 'https://core.telegram.org/tdlib/docs/',
         'https://core.telegram.org/gateway', 'https://core.telegram.org/widgets',
         'https://core.telegram.org/passport', 'https://core.telegram.org/schema',
         'https://core.telegram.org/schema/json', 'https://core.telegram.org/schema/mtproto',
         'https://telegra.ph/api']
SKIP_EXT = ('.png','.jpg','.jpeg','.gif','.svg','.webp','.mp4','.zip','.gz','.pdf','.css','.js','.ico','.woff','.ttf')
LOCAL = threading.local()

def canonical(url):
    p = urlsplit(url)
    if p.scheme not in ('https','http') or p.hostname != 'core.telegram.org':
        return None
    if p.query or p.path.lower().endswith(SKIP_EXT):
        return None
    return urlunsplit(('https', p.netloc, p.path or '/', '', ''))

def fetch(url, refresh=False):
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    meta = DOCS / 'meta' / (key + '.json')
    if meta.exists() and not refresh:
        try:
            return json.loads(meta.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            pass
    if not hasattr(LOCAL, 'session'):
        LOCAL.session = requests.Session()
    for attempt in range(3):
        try:
            r = LOCAL.session.get(url, timeout=60, headers={'User-Agent':'TelegramDocsLocalArchive/0.1'})
            r.raise_for_status()
            mime = r.headers.get('Content-Type','')
            is_html = 'html' in mime
            ext = { 'application/json': '.json', 'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp', 'image/gif': '.gif' }.get(mime.split(';')[0], '.txt')
            raw = DOCS / 'raw' / (key + ('.html' if is_html else ext))
            raw.write_bytes(r.content)
            links = []
            title = url
            mdpath = None
            if is_html:
                soup = BeautifulSoup(r.content, 'html.parser')
                title = soup.title.get_text(' ', strip=True) if soup.title else url
                content = soup.select_one('#dev_page_content') or soup.select_one('.contents') or soup.body or soup
                links = sorted({v for a in soup.select('a[href]') if (v := canonical(urljoin(r.url,a['href'])))})
                for a in content.select('a[href]'):
                    a['href'] = urljoin(r.url, a['href'])
                for item in content.select('script,style'):
                    item.decompose()
                mdpath = DOCS / 'pages' / (key + '.md')
                mdpath.write_text('# ' + title + '\n\nSource: ' + url + '\n\n' + markdownify(str(content),heading_style='ATX',escape_underscores=False), encoding='utf-8')
            record = dict(url=url, final_url=r.url, title=title, fetched_at=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                          sha256=hashlib.sha256(r.content).hexdigest(), bytes=len(r.content), content_type=mime,
                          raw=str(raw.relative_to(ROOT)).replace('\\','/'),
                          markdown=str(mdpath.relative_to(ROOT)).replace('\\','/') if mdpath else None, links=links)
            meta.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
            return record
        except Exception as e:
            if attempt == 2:
                return dict(url=url,error=str(e))
            time.sleep(2 ** attempt)

def main():
    refresh = '--refresh' in __import__('sys').argv
    for name in ('raw','pages','meta'):
        (DOCS / name).mkdir(parents=True,exist_ok=True)
    seen, pending, results = set(), set(SEEDS), []
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        while pending:
            batch = sorted(pending)[:160]
            pending.difference_update(batch)
            seen.update(batch)
            for row in pool.map(lambda url: fetch(url, refresh),batch):
                results.append(row)
                pending.update(set(row.get('links',[])) - seen)
            print(f'Fetched {len(results)}, remaining {len(pending)}, errors {sum("error" in x for x in results)}',flush=True)
    results.sort(key=lambda x:x['url'])
    (DOCS / 'manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    errors = [r for r in results if 'error' in r]
    report = dict(completed_at=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()), seeds=SEEDS,
                  discovered=len(results), saved=len(results)-len(errors), errors=errors,
                  scope='Reachable query-free links on core.telegram.org, plus telegra.ph/api. Common asset extensions, query variants, other external sites and unlinked pages excluded. Extensionless linked attachments may be retained; this is not a complete offline asset mirror. Cached pages retain original download dates.')
    (DOCS / 'coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    lines = ['# Telegram documentation index','',report['scope'],'']
    for r in results:
        if 'error' not in r:
            target = r['markdown'] or r['raw']
            lines.append(f"- [{r['title']}]({target.removeprefix('docs/')}) — {r['url']}")
    (DOCS / 'INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__ == '__main__':
    main()
