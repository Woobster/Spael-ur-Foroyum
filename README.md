# Spæl úr Føroyum

Small browser games set in Faroese nature. The site is plain HTML with no build step: what is in this repo is exactly what the website shows.

Live site: **https://woobster.github.io/Spael-ur-Foroyum/**

```
index.html              Front page with a card for each game
hare-season/index.html  Hare Season · Haruveiða
fish-season/index.html  Fish Season · Fiskiskapur
sheep-season/index.html Sheep Season
kapprodur/index.html    Kappróður · Rowing Season
puffin-watch/index.html Puffin Watch · Lundi
shared/spael-bar.html   The menu bar every game shares (Menu, Music, Effects)
tools/sync-bar.py       Copies the menu bar into every game
NEW-GAME-PROMPT.md      Prompt for making more games in the same style
.nojekyll               Tells GitHub Pages to serve the files as they are
```

Each game is **one file**. To update a game, replace that one `index.html`.

## Updating the website

GitHub Pages republishes the site about a minute after every change on the `main` branch. Pick whichever way is easiest:

**1. Ask Claude.** In a chat where this repo is attached, say what to change ("make the hares faster", "fix this Faroese word"). Claude edits the file and pushes it, and the site updates by itself.

**2. Upload a new file on github.com.**
1. Open the game's folder in the repo, for example `hare-season`.
2. Click **Add file → Upload files** and drop in the new `index.html`. Keep the name `index.html`.
3. Click **Commit changes**.

**3. Edit text straight on github.com.**
Open the file, click the pencil icon, change the text, then click **Commit changes**.

To check that it has gone live, open the **Actions** tab. A green tick next to "pages build and deployment" means the site is updated. Refresh the page with Ctrl+Shift+R (Cmd+Shift+R on a Mac) if you still see the old version.

### First-time setup (only once)

If the site link doesn't work yet: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save.**

## English and Faroese

Every page has an **EN / FO** switch in the top corner. The choice is saved in the browser as `spael-lang`, so picking FO on the front page opens the games in Faroese too.

All the text is in one block near the top of each file's script, marked:

```
/* ================= LANGUAGE / MÁL =================
```

It has an `en:` list and a `fo:` list with the same keys:

```js
'up.spawn':'Fleiri harur',                      // plain text
'up.spawn.e':(a,b)=>`${a} → ${b} harur/min`,    // text with numbers put in
```

To fix a Faroese word, find it in the `fo:` list, change only the text inside the quotes, and leave the key on the left and any `${a}` placeholders as they are. If a key is missing from `fo:`, the game shows the English text instead.

## Menu bar, music and sound effects

Every game has the same small bar: **← Menu** goes back to the front page, **♪** turns the background music on or off, and **🔊** turns the game's sound effects on or off. On desktop it sits in the bottom-left corner. On phones it folds into one round button in a top corner.

- The music is a soft folk tune that the browser plays live, so there are no music files. It starts at the player's first tap or key press, because browsers block sound before that.
- The music and effects settings are shared by all games (`spael-music`, `spael-sfx`). Turning music off in one game turns it off everywhere.
- The bar is the block between `<!-- SPAEL-BAR START` and `<!-- SPAEL-BAR END -->` at the end of each game. To change it (a new label, a different tune, colours), edit `shared/spael-bar.html` and run `python3 tools/sync-bar.py`, which copies it into every game. Or ask Claude to do it.
- To move the bar in one game, set `--spael-bottom`, `--spael-left` (desktop) or `--spael-m-top`, `--spael-m-left`, `--spael-m-right` (phones) on `:root` in a small `<style>` just before the bar block. Puffin Watch and Kappróður do this.
- A game connects its own sound effects with one line: `addEventListener('spael:sfx', e => { /* e.detail is true when effects are on */ })`.

## Adding a new game

1. Make a new folder, for example `puffin-season/`, with the game in `index.html`. `NEW-GAME-PROMPT.md` has a prompt that gives the same look and the same EN/FO switch.
2. Run `python3 tools/sync-bar.py` to give it the menu bar, and connect its sound effects to the `spael:sfx` event (see above).
3. In the front page `index.html`, copy one of the `<a class="card …">` blocks, change the link, title and text, and add the new texts to both lists in the front page's `TEXT` block.
4. Commit. The new game is live about a minute later.

## Saved progress

Each game saves progress in the player's own browser (localStorage). Nothing is sent anywhere. Changing a game's file keeps players' progress, unless the save format itself changes.
