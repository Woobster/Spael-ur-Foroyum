# Prompt for a new game

Paste this into a new chat, attach this repo (Woobster/Spael-ur-Foroyum), and replace the last line with your idea.

```
Make a new game for my site Spæl úr Føroyum (repo Woobster/Spael-ur-Foroyum, served by GitHub Pages).
Look at hare-season/index.html and fish-season/index.html first and match them.

FILES
- One self-contained file: <game-folder>/index.html. three.js r128 from cdnjs, everything else inline.
- Add a card for it on the front page index.html (both EN and FO texts), then commit and push to main.
- Add the shared menu bar with `python3 tools/sync-bar.py` (Menu back to the front page, Music, Effects).
  Don't make a separate sound button: listen for `addEventListener('spael:sfx', e => ...)` and mute the game's
  own effects when e.detail is false. Keep the bottom-left corner (desktop) and a top corner (phones) free for the bar,
  or move it with the --spael-* CSS variables described in the README.

LANGUAGE
- English and Faroese from the start. Put every visible text in one TEXT block at the top of the script,
  marked "/* ================= LANGUAGE / MÁL =================", with en: and fo: lists using the same keys.
  Texts with numbers are small functions: 'key':(a,b)=>`${a} → ${b} ...`.
- Use an EN / FO pill switch in the top-left HUD. Save the choice in localStorage as "spael-lang" and read it on load,
  so the language follows the player between the front page and all games. Switching re-renders everything at once.
- Faroese decimals use a comma (3,4 km²). Dates as "2. november". Keep real Faroese place names in both languages.

SETTING
- Faroese nature, built on real places, species, seasons and traditions. Look the facts up and put them in the game
  (level names, facts on the map, small details). Cartoony and friendly, no gore.
- Treeless green-ochre hills, basalt cliffs, sea stacks, fjords, stone walls (garðar), cairns (varðar),
  black or red tarred houses with white windows and turf roofs, drying sheds (hjallur).

ART STYLE
- Low-poly with flat shading, no textures: MeshPhongMaterial({flatShading:true,shininess:0,specular:0}), cached per colour.
- Chunky, cute characters built from low-poly spheres, boxes, cones and cylinders, each with a "pivot" child for squash and stretch.
  Procedural animation: hops, leg swings, wagging tails, ear twitches, pop-in scale.
- Terrain from a 2-unit heightmap grid with value noise, one colour per triangle from height, slope and noise.
  An exact groundY(x,z). InstancedMesh grass tufts, heather, boulders and walls.
- Gradient sky dome, fog matching the horizon, drifting low-poly clouds, a few gulls.
  HemisphereLight about 0.8 plus a soft warm DirectionalLight with PCF soft shadows.

PALETTE
- Fog #dfd8e8, sky #b8cfe4, sea #93b7c9, grass #a9b77f, moss #94a770, ochre #d1b77d, heather #9e8a80,
  rock #8f8a9b, snow #f3f1f7, turf #8ea56a, tarred wall #3e3b45, red house #b8473d,
  ink #352f45, flag red #d9493a, flag blue #2c5597, gold #f0b23a.

UI
- Fonts: "Bagel Fat One" for big numbers and titles, "Figtree" for UI.
- Big white centre counter ("127 hares"), money pill top-left, area chip with a Map button and a progress bar to the next unlock.
- Frosted rounded panels; shop docked right on desktop, bottom sheet on phones.
- Floating text, combos, frenzy mode, screen shake, WebAudio synth sounds that start on the first tap.

STRUCTURE
- Idle/incremental: act → earn kr → upgrade → more chaos. Upgrades change how it feels. Cost = base × mult^level.
- 5 levels in real Faroese places, unlocked with cash, each with its own mood and a fact list on the map.
- A final goal with an ending screen, then keep playing. Save in localStorage with try/catch, sound toggle, two-tap "Start over".
- Works with mouse and touch.

MY GAME IDEA:
[describe the new game here]
```
