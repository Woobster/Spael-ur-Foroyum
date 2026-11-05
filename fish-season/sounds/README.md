# Fish Season sounds

Put sound files in this folder and the game uses them automatically. Any sound without a file keeps the game's built-in synth sound, so you can add them one at a time.

## How to add a sound

1. Search on [Openverse](https://openverse.org/) and switch the search type to **Audio**.
2. Under **Filters → License**, tick **CC0** (free to use, no credit needed). **CC BY** is fine too, but then add a line to the credits table below.
3. Open a result, listen to it, and download it. The **Get this audio** button takes you to the original site, often Freesound or Wikimedia Commons, where you download the file.
4. Rename the file to the name in the table below and keep its extension (`.mp3`, `.ogg`, `.wav` or `.m4a`). For example, a seagull recording becomes `gull.mp3`.
5. On GitHub, open this `fish-season/sounds/` folder, click **Add file → Upload files**, drop the file in and click **Commit changes**.
6. After a minute or two, reload the game with Ctrl+Shift+R and the new sound plays.

Keep each file small. A short sound should be under 300 KB. The waves loop can be up to about 2 MB, and a clip of 20–40 seconds loops well.

## File names

| File name | When it plays | Search ideas on Openverse | Good length |
| --- | --- | --- | --- |
| `waves` | Background, on a loop | `ocean waves shore`, `sea waves rocks`, `wind sea` | 20–40 s |
| `gull` | Now and then in the background | `seagull`, `gull call`, `herring gull` | 1–3 s |
| `cast` | You cast the rod | `whoosh`, `fishing rod cast`, `swish` | under 1 s |
| `plop` | The float lands in the water | `plop`, `pebble water`, `drop in water` | under 1 s |
| `bite` | A fish takes the bait | `water splash small`, `fish splash` | under 1 s |
| `reel` | You strike and reel in | `fishing reel`, `reel spin`, `ratchet` | under 1 s |
| `splash` | A fish jumps | `splash`, `fish jump water` | under 1 s |
| `catch` | A fish lands (pitch rises with the combo) | `pop`, `bubble pop`, `plip` | under 0.5 s |
| `coin` | Extra coin sound for golden fish | `coin`, `coins jingle` | under 1 s |
| `buy` | You buy an upgrade | `cash register`, `coins purchase`, `kaching` | under 1 s |
| `fanfare` | New area and the giant halibut | `fanfare`, `success jingle`, `win` | 1–3 s |
| `frenzy` | A frenzy starts | `rising whoosh`, `power up` | 1–2 s |
| `miss` | Too early or too slow | `fail`, `bloop`, `wrong` | under 1 s |

To change how loud a sound is, open `fish-season/index.html`, find `SOUND_FILES` and change its `vol` number (1 = as recorded, 0.5 = half).

## Credits

CC0 sounds need no credit. For any **CC BY** sound, add a row here, using the details shown on its Openverse page.

| File | Title | Creator | Source link | License |
| --- | --- | --- | --- | --- |
| | | | | |
