# Spæl úr Føroyum

Small browser games set in Faroese nature. The site is plain HTML with no build step: what is in this repo is exactly what the website shows.

Live site: **https://woobster.github.io/Spael-ur-Foroyum/**

```
index.html              Front page with a card for each game
hare-season/index.html  Hare Season · Haruveiða
fish-season/index.html  Fish Season · Fiskiskapur
puffin-watch/index.html Puffin Watch · Lundi
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

## Adding a new game

1. Make a new folder, for example `puffin-season/`, with the game in `index.html`. `NEW-GAME-PROMPT.md` has a prompt that gives the same look and the same EN/FO switch.
2. In the front page `index.html`, copy one of the `<a class="card …">` blocks, change the link, title and text, and add the new texts to both lists in the front page's `TEXT` block.
3. Commit. The new game is live about a minute later.

## Saved progress

Each game saves progress in the player's own browser (localStorage). Nothing is sent anywhere. Changing a game's file keeps players' progress, unless the save format itself changes.
