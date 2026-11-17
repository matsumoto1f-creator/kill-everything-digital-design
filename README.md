# Kill Everything Digital Design Repo

How Kill Everything Digital holds its websites, videos and social content to one quality bar.

It is written so a person can read it in ten minutes and so an AI coding assistant can follow it. The bar is built from **named references taken apart down to their code and frames**, with **pass/fail gates**, not adjectives.

## What is inside

| File | What it is |
|---|---|
| `THE-BAR.md` | Start here. The twelve rules, the tells of amateur work, and the four gates (brief, build, render, sign-off). |
| `bars/web.md` | The web bar: twelve gates, the habits behind them, a default stack, and how to verify. |
| `bars/video.md` | The video bar: the visual grammar with measured numbers, motion, sound, voice, and checks before handover. |
| `bars/content.md` | The social-content bar: scoring, scarcity, series rules. The thinnest part, flagged as such. |
| `references/registry.md` | What the bar was built from, what we took, what we left alone, and how to add a reference. |
| `tools/check_video.py` | Checks a finished video: size, length, file size, audio, loudness, true peak. Writes a frame every 2 seconds to read. |
| `SKILL.md` | The same procedure as instructions for Claude Code. |

## Use it by reading

Open `THE-BAR.md`, then the bar for what you are making. Before you call something finished, run through the four gates and write down which passed, which failed and which you did not run.

## Use it with Claude Code

Put the folder where Claude Code loads skills:

```bash
git clone <this repo's URL> ~/.claude/skills/kill-everything-digital-design
```

Claude Code will then pick it up whenever you design or build something visual, and will hold the result to the gates. You can also ask for it by name: "hold this to the Kill Everything Digital design repo".

## Check a video

Needs Python 3 and ffmpeg.

```bash
python3 tools/check_video.py my-film.mp4
```

It prints PASS or FAIL for each mechanical check and writes a frame every 2 seconds next to the file. The checks that matter most cannot be automated, so open the frames and read them.

Run the tests:

```bash
python3 -m unittest discover -s tools -v
```

## Make it yours

The video numbers (colours, type sizes, safe zones) are a starting point for one house style. Swap the palette for your own and keep the structure. The sound preferences are a taste call, so change them to yours, but make it a deliberate one.

To add a new reference to the bar, follow "Growing the bar" in `THE-BAR.md`.

## Credits

The web bar was built by taking apart the public work of Dominik Fojcik. The video bar was built from a short animated explainer in a video by Greg Isenberg. Details, and what we deliberately did not copy, are in `references/registry.md`. We are not affiliated with either, and the look, wording and assets of their work are theirs.
