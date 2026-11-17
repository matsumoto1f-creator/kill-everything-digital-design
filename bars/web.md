# Web bar

For websites and any page someone is meant to be impressed by. Two lanes:

- **Immersive:** product launches, events, campaigns, a studio's own showpiece. A real 3D or filmic scene with a thin interface on top.
- **Editorial:** studios, artists, brands with work to show. No 3D at all: one grotesque, one giant headline, hairline-ruled rows, one large film.

The same twelve gates apply to both. Immersive adds the performance and fallback work.

Confidence tags: **[OBS]** read directly in shipped code or seen on screen. **[INF]** inference.

---

## The twelve gates

A page is "at the bar" only when each of these passes. Report each one as passed, failed or not run.

1. **One idea.** It fits in a sentence, and nothing on the page serves a second idea.
2. **Two fonts at most, one accent at most.**
3. **Headline at least 8x body size, with negative tracking.** The reference sets 158 px headline over 14 px copy at 1440 wide (about 11x). Tiny labels are uppercase with a little added spacing.
4. **Everything hangs off one unit, tied to height as well as width.** Use `min(100vw/1440, 100svh/900)`. A width-only unit collided on 16:9 laptops (1920x970) while looking perfect at 1440x900. The first screen must look composed at 1440x900, 1920x970 and 390 wide, and be overlap-checked by script across about ten sizes.
5. **One easing family.** Nothing appears without easing. Scroll and camera are continuous.
6. **One lens.** Grain, tint or distortion covers every pixel, including photos and video. This is what makes bought models, stills and screenshots read as one world.
7. **Fallbacks proven by test, and each is the same design, cheaper.** No WebGPU, no WebGL, camera declined, reduced motion, phone, weak GPU. A fallback that swaps to a *different* visual reads as "the site is broken". Render a still of the exact asset offscreen and serve that.
8. **The loader reports real bytes, and the first frame after it does not stutter.** The percentage is computed from the known sizes of the big downloads and can only go up. Compile shaders behind the loader.
9. **Weight budget.** Under 1 MB for a toy. About 3.5 MB for an immersive page. One large asset is allowed if it is the whole point (the reference's splat is 11.4 MB). Pixel ratio capped at 1.5 to 2 and adaptive.
10. **Frame time measured** on a mid laptop and a four-year-old phone. Never in a headless browser.
11. **Copy is short and specific.** Who it is for, what happens, one number, one link. If selling: the lanes, the steps, a price band.
12. **Anything we did not make is credited.** Models, photos, code, fonts, with what we changed.

---

## Why it reads as expensive: the transferable habits

These are visible in at least two of the reference's sites, so they are method, not accident. [OBS]

- **One idea carried all the way.** One trick, one journey, one film on bent screens. Nothing competes.
- **Almost no interface colour.** Black, white, a few greys, one or two small accents. Colour comes from the scene.
- **The interface is a thin layer over the scene.** Name top left, credit top right, headline bottom left, short paragraph and one link bottom right. Soft gradients tinted to the scene's own dark (not pure black) keep text readable.
- **Motion never pops.** Scrolling moves a camera through one connected world with no cuts. A small set of long ease-out curves handles the interface.
- **Input is filtered and honest.** Head, tilt or mouse all drive the same view. The signal is smoothed and predicted. Losing the signal eases back, never snaps. Clicks land correctly even under lens distortion.
- **Performance is treated as design.** Heavy rendering runs off the main thread. Resolution steps down a quarter when frames run slow and back up when they recover. Rendering pauses when the tab is hidden or the canvas is off screen. Every asset is compressed.
- **Every failure is designed.** No camera gives mouse control. No WebGPU gives WebGL. A broken scene gives a plain human sentence. Reduced motion is respected. Assets from other people are credited on their own page.

### Reference measurements (starting points, not rules to copy)

| Thing | Reference value |
|---|---|
| Layout unit | viewport width / 1440 on a one-screen piece; a root font size from a `clamp()` and everything in `rem` on a full portfolio |
| Display tracking | -0.01 to -0.08 em |
| Label tracking | about 0.12 em |
| Reveal easing | 0.5 s `cubic-bezier(.25, 1, .5, 1)` |
| Menu easing | 0.35 s `cubic-bezier(.22, 1, .36, 1)` |
| Page fade | 1 s `cubic-bezier(.645, .045, .355, 1)` |
| Pixel ratio | capped at 1.5 |
| Redraw | only when the view or a setting changes |
| Weight, one-screen immersive | one 11.4 MB splat file is nearly all of it |
| Weight, full immersive pages | 3.4 to 5.8 MB on first visit (the top end is mostly video) |

---

## Default stack (all free)

- **Page:** Astro with static output, or plain Vite for a one-screen piece. Tailwind v4 tokens.
- **3D:** Three.js with the WebGPU renderer and the WebGL fallback switched on. Move rendering into a worker once the scene is heavy.
- **Scroll and motion:** Lenis for scroll. anime.js or GSAP for tweens. Small shared stores for state.
- **Assets:** glTF with Draco or Meshopt, KTX2 textures, AVIF stills, Gaussian splats in SOG, self-hosted subset fonts.
- **One post-processing lens per site.**
- **Head tracking, if the idea needs it:** MediaPipe face landmarker in a worker, a One-Euro filter, an off-axis projection, and gyroscope plus mouse fallbacks.

Editorial builds need none of the 3D.

### Where the pictures come from (cheap and legal)

- **Gaussian splats** for photoreal places: baked from a scene we lit ourselves and rendered, or generated.
- **Depth maps** to make flat images react to light: estimate depth with a model, blur it so steps disappear, derive normals, trace toward the light through the depth map for soft shadows.
- **Bought or free 3D models, optimised and credited.** Simplify, compress textures, remove detail, swap materials, and say so on a credits page.
- **Blender** for custom shapes.
- **AI for code and shader maths, not for the look.**

---

## How to verify (the part that is easy to skip)

- **Use real desktop Chrome on a real GPU for anything 3D.** Embedded browser panes and headless runs usually have no GPU context and will show a blank canvas, or a different design.
- **If you must run headless**, software rendering (SwiftShader flags) gives a WebGL context good enough for stills and stepped frames, but never for judging speed.
- **Capture frames deterministically.** Give the page a `step(dt)` hook on its own clock, screenshot each frame, then encode with ffmpeg. Do not screen-record.
- **Film the built page, not the dev server.** A hot-reload edit mid-capture kills the run.
- **Measure flicker, do not eyeball it.** Capture every composited frame with Chrome DevTools Protocol `Page.startScreencast` while moving the mouse, then count per-region brightness jumps. Never tie an effect's brightness to pointer speed.
- **Check overlap by script** across about ten viewport sizes. Two screenshots miss what a script catches.
- **Test the fallbacks for real:** disable WebGPU, disable WebGL, decline the camera, set reduced motion, throttle the CPU.

---

## What not to copy

- The reference's identity: its fonts, its lens, its scenes, its portrait.
- Its concept, name or wording. A public technique (for example a head-tracked "window") belongs to everyone; one author's scene, title and copy do not.
- Its copy. Take the structure (lanes, steps, budget bands) and write your own words. After any competitor-inspired copy, save the competitor's page text and grep the new HTML for their headings and distinctive phrases before committing.

---

## Not verified in the reference

- Mobile behaviour of the portfolio (read from code, not tested on a phone).
- Whether the frame and draw-call figures in its decorative terminal log are real measurements.
- Some award claims.
