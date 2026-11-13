# kids-lib

Shared helpers for the Wilson kids' iPad games (Alex 7, Zoe 4): **per-kid profiles and saves**, and **sound with the iPad audio guard** (mute, pause, clip loading).

Fun is primary: nothing here gates play. Zoe's profile is `little: true` so games can default her to an easy mode.

## Use it (vendor a copy, no runtime cross-repo loads)
1. Copy `kids.js` into the game's `src/` (or run `python3 /workspace/kids-lib/vendor.py <game>/src`).
2. Inline it before the game code at build time, or add `<script src="kids.js"></script>` and precache `kids.js` in the game's `sw.js`.
3. Bump the game's service-worker version as usual.

```js
const kid = KIDS.kid();                                   // 'alex' | 'zoe' (from ?kid=, else last kid on this iPad)
const save = KIDS.store('wwp', {migrate:['best','hard']}); // keys 'wwp_<kid>_best'; old per-device saves copied to Alex once
save.set('best', 120); save.json('badges', {});
if (KIDS.profile(kid).little) { /* easy defaults for Zoe */ }
const snd = KIDS.sound('wwp');                            // one AudioContext + audio guard; mute remembered as 'wwp_muted'
snd.load('pop','sfx/pop.mp3'); snd.play('pop'); snd.tone(660, .12);
snd.setMuted(!snd.muted); snd.setPaused(true);
```

The key scheme (`<game>_<kid>_<key>`, migration marker `<game>_mig_kid`) matches what Bee Game (`tbg_`) and Water Pirates (`wwp_`) already use, so those saves stay compatible.

## Test
`python3 test.py http://127.0.0.1:<port>/kids-lib/` (serve /workspace) → all PASS.

## Who uses it
- Water Pirates (vendored, Together mode, Nov 2026)
