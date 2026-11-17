# Video bar

For short animated explainers, motion graphics, launch films and vertical social video. The reference is a short animated explainer: a near-black frame, cream ink, one orange accent, giant climbing counters, and a line-art diagram that moves to explain the idea.

Starting values below are for **1080x1920** vertical video. They are a house starting point. Swap the palette for your own brand; keep the structure.

Tags: **[S]** a source gave it. **[I]** practice-based starting value, tune by eye.

---

## The grammar (read from the reference's frames)

- **Ground.** One near-black. Never a second background colour. A faint vignette.
- **Ink.** Cream, not white.
- **One accent.** Orange, used on the number or object that matters. A second colour appears once, when a second object needs it.
- **Giant counters.** A number 15 to 20% of frame height that climbs while the picture changes, with a small mono caps label under it. It turns to the accent at the punchline.
- **A diagram that explains by moving.** A stacked bar that grows block by block while the counter climbs. A curve that draws itself with a glowing dot and a live value. Then the bar turns into the thing it describes. Thin strokes, flat fills.
- **An analogy shot.** Two objects side by side with a label each.
- **Chapters.** A giant numeral alone on screen, which then shrinks to the top-left as accent number plus a mono label that stays for the chapter.
- **Captions.** One clause at a time, medium-weight sans, centred near the bottom, no box, no word highlight.
- **Motion.** Calm and exact. Things draw, grow and count. Nothing bounces around.

### The test for every scene

For each spoken line, name:

1. the **number** that lands or changes, and
2. what the **diagram** does while it is said.

A line with neither gets a redesign, not a decoration. Then pause the frame and ask: could it be a poster?

---

## Starting numbers (1080x1920)

| Thing | Value |
|---|---|
| Ground | `#05080B` |
| Ink | `#EEE8DB` |
| Label grey | `#7B808A` |
| Line | `#2B3038` |
| Accent | `#F05A1E` |
| Second accent (once per film) | amber `#FFB224` or green `#52D08A` |
| Hero number | 280 to 310 px tall, spanning most of its column or the frame |
| Numbers and headlines | Inter 900, tracking -0.045em, tabular figures |
| Captions | Inter 700, 54 px |
| Labels | JetBrains Mono 700 capitals, 29 to 34 px, tracking 0.17 to 0.22em |
| Diagram strokes | 4 to 5 px |
| Dots | 44 to 52 px |
| Layout | chapter label y 184; content y 250 to 1290; captions about y 1318; bottom quarter empty (platform buttons and text cover it) |
| Background | one radial lift behind the content, plus 5% grain on top to stop banding |
| Caption entry | fade in 0.12 s, text shadow instead of a box |

Leave the caption out when the scene prints the same words large.

---

## The big moves, in order of impact (premium motion)

1. **A camera through a world, not slides.** One large stage, a camera wrapper over it. Push-ins 1.0 to 1.25x over 3 to 5 s. Whip-pans 0.25 to 0.4 s with motion blur. 3 to 6 px drift on holds. Transitions are the camera or an object that grows into the next world. No fades between scenes. [S, numbers I]
2. **Real artifacts, filmed.** Real UI frames (terminal, run log, chat message, settings toggle, code diff) shown by a virtual camera. One user action and one product reaction per shot. Screens bleed off the frame instead of floating as small cards. [S]
3. **Hero fills 40%+ of the frame.** Secondary text 44 to 56 px, a scale contrast of 5:1 or more. Flows stack vertically on 9:16. [S, I]
4. **Depth.** 4 or 5 layers (background, mid, hero, foreground). Parallax at about 0.3x / 0.6x / 1x / 1.4x of the camera move. Background blur 6 to 14 px. A rack focus of 0.5 to 0.8 s on the emphasis moment. [S, numbers I]
5. **Light and material instead of outlines.** Layered soft shadows, a 1 px inner top highlight, one implied key light from the top-left, a radial light pool behind the hero, vignette 30 to 50%. Glow only on a state that matters. [S]
6. **Grain.** A noise tile at 4 to 8% opacity, overlay or soft-light, so flat fills never sit dead. [S, I]
7. **Sound.** Effects on visible actions: whoosh on camera moves, tick on text, pop on a stamp, riser into the payoff, one impact. [S, I]
8. **Lock cuts to the music or the voice.** At 120 BPM a beat is 0.5 s and a bar 2 s. The big change lands on a downbeat; a move that must hit starts 40 to 190 ms early. [S]

### Diagrams that look rich

- Real icons and real UI, not labelled boxes. Reveal parts one at a time when the voice names them.
- Connectors as light: a stroke with a moving bright head and a fading tail. A blocked path dies against a barrier.
- Counters: tabular figures, odometer roll 0.8 to 1.2 s, expo.out, a flash on the final value.
- Show absence: an empty lane, a queue that drains and is not refilled.

### Type

Inter, Geist, Space Grotesk, Instrument Serif and JetBrains Mono as display type are where generated design tends to land, so use them deliberately or choose something with more character. A condensed face suits giant numbers on 9:16. Inside a UI mock, a UI font is fine.

---

## Sound

- **Music** only where it earns its place: ads and short cuts, where a driving electronic bed around 120 to 126 BPM suits slick software. Narrated explainers and case studies default to **voice plus light effects on visible actions**. Ask before adding a bed. This is a taste call; change it to yours, but make it a deliberate call.
- Music about 14 dB under the voice. Effects 3 to 6 dB over the bed. Peak at or below -1 dBTP. Mix about -16 to -14 LUFS. Rotate takes of repeated sounds. [S, I]
- If a busy bed eats short unstressed words, cut its 1 to 4 kHz range by about 6 dB.
- **Check every line on the finished mix**, with the music in, using speech-to-text. A rare proper noun is the first thing a bed eats.
- Ship a no-music file beside the music one.

### Voice

- **The voice leads and the picture follows.** Never cut sentences out and pin them to a beat grid; it sounds fake. Fit the music to the voice.
- Judge a voice **by ear**, by the owner. Nothing you can measure stands in for that.
- Send a 10-second voice-only sample before any full build. "Closer" on a sample is a direction, not a yes: ask what is missing, send the next small sample.
- A draft the owner is shown carries the real voice, even if their own recording will replace it later.

### Order of work for a narrated film

1. Script, with a table of number and mechanism per line (gate G0).
2. A storyboard of real frames.
3. A silent draft, with timing guessed from the words (a cloned voice runs about 3 words a second inside a sentence).
4. Voice sample, then voice.
5. Final mix, then checks.

---

## Checks before handing over (gate G1)

Run `python3 tools/check_video.py <file>`. It checks what a machine can check:

| Check | Pass |
|---|---|
| Frame size | 1080x1920 (or the size you pass) |
| Duration | 5 to 90 s for a social short (`--long` skips the upper limit) |
| File size | under 100 MB |
| Audio | present |
| Audio and video length | within 0.2 s of each other |
| Loudness | integrated -16 to -14 LUFS |
| True peak | at or below -1 dBTP |

It also writes a frame every 2 seconds into a folder, because the rest cannot be automated: **open them and read them.** No text cut off, no overlapping elements, captions readable, nothing important in the bottom quarter or under the right-hand buttons.

Also by hand:

- Write the caption: a hook line, two short lines of context, 3 to 5 hashtags.
- Export a cover image from the strongest frame.
- Every stat in the script came from your notes or is marked `[NEED NUMBER]`.

---

## Build lessons (what not to try)

- **Never build scenes straight from the script.** The first version of a film that skipped the look step landed on small outlined boxes floating in a dark frame, with pills, tags and no sound. It was rejected outright. Follow the grammar above and give every line a number or a mechanism.
- **A GSAP position that is `undefined` does not error:** the tween is appended at the end of the timeline. Assert that every cue exists before using it.
- **A `fromTo` placed late in a timeline needs `immediateRender: false`,** or its "from" values are applied at build time and restyle an earlier moment. Put initial hidden states in `gsap.set`.
- **Speech-to-text word starts absorb the pause before them.** Move each start to the first real sound. Keep 100 ms before a sentence's first loud sound or a soft "f" or "s" gets clipped.
- **Compare heard and written text by value.** Transcripts write "$25 ,000" in two pieces and "$100" for "a hundred dollars".
- **Cache by folder and file, not file name alone,** or a re-pick hands back the wrong take.
- **Check what else is using the graphics chip** before estimating a render. A game on the same machine turned 45 seconds into 3.5 minutes.
- **Shell:** a generator script that ends with `| grep -v` can hide a failure behind exit 0 and a printed "done". Use `set -o pipefail` and end by counting the files it was meant to make.

---

## Free assets (commercial use)

- Icons: Lucide (ISC), Tabler (MIT).
- Fonts: OFL-licensed.
- Shaders: Paper Shaders (Apache 2.0).
- Sound: CC0 on freesound.org (filter to CC0), Pixabay Content License.
- Any new download needs the owner's OK first.

## Rules that are not negotiable

- Free and local tools unless the owner has approved a paid one.
- No real client names, patient data or private details in any video. Describe clients generically ("a physical-therapy practice").
- Never invent numbers.
- The owner uploads the finished file. Never drive a logged-in social account from automation.
