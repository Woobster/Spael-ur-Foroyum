#!/usr/bin/env python3
"""Copy shared/spael-bar.html into every game's index.html.

Run from the repo folder:   python3 tools/sync-bar.py

The bar sits between <!-- SPAEL-BAR START and <!-- SPAEL-BAR END --> in each game.
If a game doesn't have it yet, it is added just before </body>.
Folders without an index.html, and the front page, are skipped.
"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
bar = (root / 'shared' / 'spael-bar.html').read_text(encoding='utf-8').strip()
block = re.compile(r'<!-- SPAEL-BAR START.*?<!-- SPAEL-BAR END -->', re.S)

changed = 0
for game in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(('.', 'shared', 'tools'))):
    f = game / 'index.html'
    if not f.exists():
        continue
    html = f.read_text(encoding='utf-8')
    if block.search(html):
        new = block.sub(lambda m: bar, html, count=1)
    else:
        i = html.lower().rfind('</body>')
        new = (html[:i] + bar + '\n' + html[i:]) if i >= 0 else (html + '\n' + bar + '\n')
    if new != html:
        f.write_text(new, encoding='utf-8')
        changed += 1
        print('updated', game.name)
    else:
        print('already up to date', game.name)
print(f'{changed} game(s) changed')
