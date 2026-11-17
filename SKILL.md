---
name: kill-everything-digital-design
description: The Kill Everything Digital design quality bar. Use before designing or building anything a person will look at (a website or landing page, a video or motion graphic, a reel or social clip, a lab piece), and again before asking anyone to sign off on it. Holds the twelve rules, the four gates, the web, video and content bars, and a video checker. Skip for backend work, CLIs, data, plain text answers, code diffs, or throwaway internal pages.
---

# Kill Everything Digital Design Repo: apply the bar

This is the standard everything visual is held to. Other skills (design, motion, video engines) are the tools you build with. This is the bar you hold the result to.

## What to do

1. **Read `THE-BAR.md`.** It has the twelve rules, the amateur tells, and the four gates.
2. **Read the bar for the medium:**
   - website or page: `bars/web.md`
   - video or motion graphic: `bars/video.md`
   - reel, short, clip, written content: `bars/content.md`
3. **If `LOCAL.md` exists in this folder, read it.** It holds this owner's private overlay (house numbers, project paths, standing preferences). It is never shared.
4. **Gate G0, brief, before building.** Write the idea in one sentence. Name the reference it is held to. For a video, a table of each spoken line with the number that lands and what the diagram does. Every figure has a source or is marked `[NEED NUMBER]`. If the idea will not fit one sentence, stop and ask.
5. **Build.** Use whatever skills fit the medium.
6. **Gate G1, build checks.** Run the medium's gates. For any video run `python3 tools/check_video.py <file>` and read the frames it writes.
7. **Gate G2, render and look.** Render the real thing and look at it. Web: real desktop Chrome on a real GPU, three sizes, scripted overlap check. Video: read a frame every 2 seconds. Never judge motion by eye when it can be measured.
8. **Gate G3, sign-off.** Show the rendered thing before asking for approval. Ask about each ingredient by name. Record the verdict at the grain it was given, and say what was not judged.

## What to report

End with one line per gate: **passed**, **failed**, or **not run**. Never write "meets the bar" without that list. A gate you did not run is "not run".

## Do not

- Copy a reference's look, wording, name or assets. Structure and method only.
- Invent a number. Mark it `[NEED NUMBER]`.
- Name a client or include private details in anything shared.
- Ship a fallback that shows a different picture from the main design.
- Add a paid service, trial or per-use API without asking.

## Adding to the bar

When the owner sends a new reference and says "this is the quality I mean", follow "Growing the bar" in `THE-BAR.md` and `references/registry.md`.
