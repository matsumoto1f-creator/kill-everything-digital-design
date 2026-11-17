# Reference registry

The Kill Everything Digital design repo's bar is held against **named references**. This file says what they are, what we took from each, and how to add a new one.

We take **structure and method**. We do not take anyone's look, wording, name or assets. We are not affiliated with any author listed here, and nothing here is their endorsement. Everything below comes from what a browser or a video player shows anyone: shipped HTML, CSS, JS, response headers, frames, and the authors' own public posts and tutorials. No logins, no forms, nothing private.

---

## Web: an immersive 3D site and its portfolio

- **Author:** Dominik Fojcik, an independent design engineer.
- **Looked at:** a public head-tracked 3D demo (`immersive-website.fojcikdominik.com`), his portfolio (`fojcikdominik.com`), five live client and lab projects, and his three published Codrops tutorials.
- **What we took:** twelve habits and twelve gates. See `bars/web.md`.
- **What we left alone:** his fonts, his post-processing look, his scenes and portrait, the demo's concept and title, all of his copy.

Short version of why it counts as the bar: one idea per site, two fonts, a headline about 11x the body, one unit that scales the whole layout like a poster, one "lens" over every pixel, motion that never pops, and engineering that keeps a heavy scene smooth and every failure designed.

Credit him wherever work built to this bar goes public, in the way he credits others: on a credits page, with what we changed.

### Not verified for this reference

- Mobile behaviour of the portfolio (read from code, not tested on a phone).
- Whether the frame and draw-call figures in its decorative terminal log are real.
- Some award and recognition claims.
- The built-in preview panes of some AI tools could not render the 3D pages; every visual check was done in desktop Chrome.

---

## Video: a short animated explainer

- **Author:** Greg Isenberg, in the video "Claude Fable 5.2: How I'd Make Money With It", about 11:35 to 12:05 (an animated rocket explainer). A neighbouring cinematic 3D shot at about 11:21 to 11:33 (a laptop on a desk as day turns to night) is noted for a later attempt.
- **What we took:** the grammar in `bars/video.md`: near-black ground, cream ink, one accent, giant counters, a diagram that moves, chapter numerals, one-clause captions, small mono labels.
- **What we left alone:** the rocket, the analogy, the wording, the sound.
- **How it was read:** frame by frame from the video itself, with the numbers in `bars/video.md` then measured on our own builds.

### Premium motion research (supporting)

A web research pass behind `bars/video.md`'s "big moves". Sources it drew on: getlago.com (a design team's write-up on replacing a motion-design job with code), a classic list of 25 simple animation tricks, Pro Video Coalition on grain and glow, a study of Linear's grain, motiondesign.school on parallax, aejuice on depth of field, a ByteByteGo-style diagram guide, Vercel's Geist colour rules, and the HyperFrames guides on story, look, motion and sound. Where a number came from a source it is tagged **[S]**; where it is a starting value to tune by eye it is **[I]**.

---

## How to add a reference

When the owner sends a link and says "this is the quality I mean":

1. **Take it apart from what it ships.** Code, frames, headers, published write-ups. Look at it live in a real browser or player, not only in a description.
2. **Tag each claim.** **[OBS]** you saw it in shipped code or on screen. **[SAID]** the author said it publicly. **[INF]** your inference from strong signals. Put anything you could not check in a "not verified" list.
3. **Pull out rules and gates.** A rule is what transfers. A gate is what a person or script can check as pass or fail. Add them to the matching file in `bars/`, with a measured starting value where there is one.
4. **Add the reference to this file,** credited, with what you took and what you left alone.
5. **Check your own wording.** After any competitor-inspired copy, save the reference's page text and grep your draft for their headings and distinctive phrases before it ships. Structure is borrowed; words are not.
6. **Cover the whole body of work, not one page.** One impressive page might be a fluke. Two or more sites sharing a habit is a method.
