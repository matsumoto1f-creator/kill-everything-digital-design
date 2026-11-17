# Kill Everything Digital Design Repo: the quality bar

One quality standard for everything Kill Everything Digital makes that a person looks at: websites, videos, motion graphics, social content. "The bar" in these files means this standard.

It is defined by **named references and checkable gates**, not by adjectives. "Make it premium" is not a spec. "The headline is at least 8x the body size, there are two fonts, one accent, and the first frame after the loader does not stutter" is.

Two kinds of line appear below. **Rules** are the part that transfers between mediums. **Gates** are pass/fail checks you can run on the finished thing.

References that set the bar (details in `references/registry.md`):

- **Web:** a public immersive 3D site and its portfolio, taken apart down to the shipped code.
- **Video:** a short animated explainer (near-black frame, cream ink, one orange accent, giant counters, a diagram that moves).

We take their **structure and method**. We never take their look, their copy, or their name.

---

## The twelve rules

| # | Rule | Web | Video | Content |
|---|---|---|---|---|
| 1 | **One idea, said in one sentence.** Everything else serves it or is cut. | One trick or one journey per site. | Every spoken line has a number that lands or a diagram that moves. No number and no mechanism means redesign, not decorate. | One claim per piece. |
| 2 | **Restraint in colour and type.** | Two fonts at most, one accent at most, near-monochrome interface. Colour comes from the content (scene, film, illustration). | One ground colour, cream ink (never pure white), one accent. A second colour appears once, when a second object needs it. | One fixed shape per series, repeated every episode. |
| 3 | **Scale contrast.** One thing huge, the rest small. | Headline at least 8x the body size (the reference runs about 11x). Big type tracked tight, tiny labels tracked loose. | Hero number 15 to 20% of frame height, at least 5:1 over secondary text. | The hook is the biggest thing on screen in the first two seconds. |
| 4 | **One unit, one lens.** | Every size hangs off one viewport unit. One lens (grain, tint or distortion) covers every pixel, including photos and video. | One radial light lift and about 5% grain over every scene; content lives in fixed vertical bands. | Same template and safe zones for every piece. |
| 5 | **Motion is continuous and eased. Nothing pops.** | One easing family. Scroll moves a camera through one connected world. | Things draw, grow and count. Camera moves, not slide fades. Cuts land on the voice or the beat. | Cut tight. No dead air before the payoff. |
| 6 | **Real beats decorative.** | Real art-directed scene. The loader shows real bytes. | Real UI frames shown by a virtual camera, not labelled boxes. | Numbers come only from our own notes. |
| 7 | **Performance is design.** | Weight budget, adaptive resolution, nothing redraws when nothing changed, shaders warmed behind the loader. | File length, size, loudness and caption safe zones are measured (gates below). | Length fits the platform. |
| 8 | **Every failure is designed. A fallback is the same design, cheaper.** | No WebGPU, no WebGL, camera declined, reduced motion, phone, weak GPU: each tested. | Ship a no-music file beside the music one. Build the picture silent before any voice exists. | Makes sense with zero context and with sound off. |
| 9 | **Short, specific copy.** | Who it is for, what happens, one number, one link. | One caption clause at a time. No box behind it. | The hook is the claim itself. |
| 10 | **Credit what we did not make. Take structure, never wording.** | Credit models, photos, code. Grep new copy for the reference's phrases before it ships. | Free-licence assets only (see `bars/video.md`). | No named clients, no private data. |
| 11 | **Prove it by looking at the rendered thing.** | Real Chrome on a real GPU, scripted size matrix, measured frame time. | Extract frames every 2 seconds and read them. Hear the finished mix. | Watch the exported file, not the timeline. |
| 12 | **Ship the best, reject the rest.** | One finished lab piece beats five half-finished ones. | A draft shown to the owner already carries the real voice. | Of every batch of clips, post the top 2 or 3. |

Where a Content cell reads thin, that is because the bar is thinner there. It is the part to extend first.

---

## Tells of amateur work

If you see these, the bar has not been met, whatever the rest looks like.

1. Flat outlined shapes on one flat colour. No light, no shadow, no texture.
2. Everything fades or slides up at once on one ease.
3. Small elements floating in the middle of an empty frame.
4. Default purple/blue gradients, neon glow, or glass with nothing behind it.
5. Silence, or one looping music bed with no effects and cuts off the beat.
6. Decoration dressed as information: pill chips, corner labels, HUD readouts, three cards in a row, a docked logo.
7. A fallback that shows a *different picture*. People read it as "the site is broken". Degrade to a still of the same thing.
8. A layout unit tied only to window width. It looks fine at 1440x900 and collides on a 16:9 laptop.
9. Effects pasted in with no single motion language.
10. A number nobody can trace to a source.

---

## The four gates

Run them in order. A gate that was not run is reported as not run, never as passed.

**G0. Brief (before building).**
- The idea in one sentence. If it will not fit, stop and ask.
- Name the reference this is being held to.
- Video: a table of every spoken line with the number that lands and what the diagram does while it is said.
- Every figure has a source, or is marked `[NEED NUMBER]`.

**G1. Build checks (while building).** The medium's own gates: `bars/web.md`, `bars/video.md`, `bars/content.md`. Run `tools/check_video.py` on any video.

**G2. Render and look (before showing anyone).**
- Render the real thing and look at it. A description is not evidence.
- Web: real desktop Chrome on a real GPU, not a headless browser. At least three sizes: 1440x900, 1920x970 and 390 wide. Check overlaps by script across about ten sizes, not by eye on two screenshots.
- Video: a frame every 2 seconds, read. The paused-frame test: *could this frame be a poster?*
- Motion: capture every composited frame and count brightness jumps. Do not judge flicker by eye.

**G3. Sign-off (the owner's call).**
- Show the rendered thing, then ask.
- Ask about each ingredient by name (the picture, the voice, the copy). A short "keep it" approves the thing that was asked about, not every part inside it.
- Record the verdict at the grain it was given, in the owner's words, and say what was *not* judged.
- "Closer" is a direction, not a yes. Ask what is still missing before building the whole thing.

Finish every piece with a one-line-per-gate report: passed, failed, or not run.

---

## Growing the bar

The bar is a registry, not a monument. When the owner sends a new reference and says "this is the quality":

1. Take it apart from what it ships: the code, the frames, the response headers, the published tutorials. No logins.
2. Tag every claim: **[OBS]** read directly, **[SAID]** the author said it publicly, **[INF]** my inference. Anything unverified goes in a "not verified" list.
3. Pull out rules (what transfers) and gates (what can be checked). Add them to the matching file in `bars/`.
4. Add the reference to `references/registry.md`, credited.
5. Keep the look, wording and name of the reference out of what we build.

---

## Where each thing lives

| You need | Read |
|---|---|
| A website, an immersive page, a lab piece | `bars/web.md` |
| A video, explainer, motion graphic | `bars/video.md` |
| Reels, shorts, clips, written content | `bars/content.md` |
| Where the bar came from, how to add to it | `references/registry.md` |
| Check a finished video | `tools/check_video.py` |
