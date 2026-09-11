"""Split the downloaded Bot API into individually searchable method/type files."""
import hashlib
import json
from pathlib import Path
import re
from bs4 import BeautifulSoup
from markdownify import markdownify

root = Path(__file__).resolve().parents[1]
url = 'https://core.telegram.org/bots/api'
key = hashlib.sha256(url.encode()).hexdigest()[:20]
meta = json.loads((root / 'docs/meta' / (key + '.json')).read_text(encoding='utf-8'))
soup = BeautifulSoup((root / meta['raw']).read_bytes(),'html.parser')
out = root / 'docs/bot-api'
out.mkdir(exist_ok=True)
index = ['# Bot API: methods and types', '', 'Source: '+url, '']
for heading in soup.select('#dev_page_content h4'):
    title = heading.get_text(' ',strip=True)
    anchor = heading.select_one('a[name]')
    fragment = anchor.get('name') if anchor else re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')
    parts = [str(heading)]
    for sib in heading.next_siblings:
        if getattr(sib,'name',None) in ('h1','h2','h3','h4'):
            break
        parts.append(str(sib))
    html = BeautifulSoup(''.join(parts),'html.parser')
    for a in html.select('a[href]'):
        from urllib.parse import urljoin
        a['href'] = urljoin(url,a['href'])
    filename = re.sub(r'[^a-zA-Z0-9_-]','_',fragment)+'.md'
    (out / filename).write_text('Source: '+url+'#'+fragment+'\nSnapshot: '+meta['fetched_at']+'\n\n'+markdownify(str(html),heading_style='ATX',escape_underscores=False),encoding='utf-8')
    index.append(f'- [{title}]({filename})')
(out / 'INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
print(f'Created {len(index)-4} Bot API sections')
