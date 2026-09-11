import json, os, urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
repo = os.environ.get('GITHUB_REPOSITORY', 'skat111/TgBotsToolkit')
request = urllib.request.Request('https://api.github.com/repos/' + repo, headers={'User-Agent': 'TgBotsToolkit'})
try:
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.load(response)
except Exception:
    data = {}
stars = int(data.get('stargazers_count', 0))
forks = int(data.get('forks_count', 0))
issues = int(data.get('open_issues_count', 0))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="210" viewBox="0 0 900 210"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#111827"/><stop offset="1" stop-color="#164e63"/></linearGradient></defs><rect width="900" height="210" rx="24" fill="url(#g)"/><circle cx="790" cy="38" r="110" fill="#22d3ee" opacity=".09"/><circle cx="850" cy="180" r="130" fill="#facc15" opacity=".08"/><text x="48" y="58" fill="#67e8f9" font-family="Arial" font-size="18" font-weight="700">TELEGRAM BOT TOOLKIT</text><text x="48" y="105" fill="white" font-family="Arial" font-size="34" font-weight="800">Community leaderboard</text><text x="48" y="138" fill="#cbd5e1" font-family="Arial" font-size="16">Documentation, UI patterns and agent adapters for serious bots</text><text x="610" y="102" fill="#facc15" font-family="Arial" font-size="50" font-weight="800">★ {stars}</text><text x="614" y="132" fill="#cbd5e1" font-family="Arial" font-size="13">STARS</text><text x="720" y="180" fill="#cbd5e1" font-family="Arial" font-size="13">⑂ {forks} forks · {issues} issues</text></svg>'''
(root / 'docs' / 'leaderboard.svg').write_text(svg, encoding='utf-8')
(root / 'docs' / 'leaderboard.json').write_text(json.dumps({'repository': repo, 'stars': stars, 'forks': forks, 'open_issues': issues}, indent=2), encoding='utf-8')
print(json.dumps({'repository': repo, 'stars': stars, 'forks': forks, 'issues': issues}))
