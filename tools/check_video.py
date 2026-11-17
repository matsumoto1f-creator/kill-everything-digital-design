#!/usr/bin/env python3
"""Mechanical checks for a finished video, per bars/video.md (gate G1).

    python3 tools/check_video.py FILE [--size 1080x1920] [--long] [--frames DIR]

Checks: frame size, duration, file size, audio present, audio/video length,
integrated loudness, true peak. Also writes a frame every 2 seconds so a person
can READ them: text cut off, overlaps, caption legibility, safe zones. Those
cannot be automated, so a pass here is necessary and not sufficient.

Exit code 0 only if every check passes. Needs ffmpeg and ffprobe on PATH.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

MIN_SECONDS = 5.0
MAX_SECONDS = 90.0
MAX_BYTES = 100 * 1024 * 1024
AV_TOLERANCE = 0.2
LUFS_RANGE = (-16.0, -14.0)
TRUE_PEAK_MAX = -1.0


def tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        for prefix in ("/opt/homebrew/bin", "/usr/local/bin"):
            candidate = Path(prefix) / name
            if candidate.exists():
                return str(candidate)
        sys.exit(f"{name} not found on PATH")
    return path


def probe(path: Path) -> dict:
    out = subprocess.run(
        [tool("ffprobe"), "-v", "error", "-print_format", "json",
         "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)


def measure_loudness(path: Path) -> tuple[float, float] | None:
    """Return (integrated LUFS, true peak dBTP) via ffmpeg loudnorm, or None."""
    proc = subprocess.run(
        [tool("ffmpeg"), "-hide_banner", "-nostats", "-i", str(path), "-vn",
         "-af", "loudnorm=I=-15:TP=-1:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    match = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", proc.stderr, re.S)
    if not match:
        return None
    data = json.loads(match.group(0))
    try:
        return float(data["input_i"]), float(data["input_tp"])
    except (KeyError, ValueError):
        return None


def stream(info: dict, kind: str) -> dict | None:
    return next((s for s in info["streams"] if s.get("codec_type") == kind), None)


def duration_of(s: dict | None, fallback: float) -> float:
    if s and s.get("duration") not in (None, "N/A"):
        return float(s["duration"])
    return fallback


def extract_frames(path: Path, out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("frame_*.jpg"):
        old.unlink()
    subprocess.run(
        [tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-i", str(path),
         "-vf", "fps=1/2", "-q:v", "3", str(out_dir / "frame_%03d.jpg")],
        check=True,
    )
    return len(list(out_dir.glob("frame_*.jpg")))


def run_checks(path: Path, size: str, long_form: bool) -> list[tuple[str, bool, str]]:
    results: list[tuple[str, bool, str]] = []

    def add(name: str, ok: bool, detail: str) -> None:
        results.append((name, ok, detail))

    info = probe(path)
    video = stream(info, "video")
    audio = stream(info, "audio")
    container = float(info["format"].get("duration", 0.0))

    if not video:
        add("video stream", False, "none found")
        return results

    want_w, want_h = (int(x) for x in size.lower().split("x"))
    got_w, got_h = int(video["width"]), int(video["height"])
    add("frame size", (got_w, got_h) == (want_w, want_h),
        f"{got_w}x{got_h}, want {want_w}x{want_h}")

    v_dur = duration_of(video, container)
    upper = float("inf") if long_form else MAX_SECONDS
    add("duration", MIN_SECONDS <= v_dur <= upper,
        f"{v_dur:.1f}s, want {MIN_SECONDS:g}s to "
        f"{'no limit' if long_form else f'{MAX_SECONDS:g}s'}")

    size_bytes = path.stat().st_size
    add("file size", size_bytes < MAX_BYTES,
        f"{size_bytes / 1048576:.1f} MB, want under {MAX_BYTES // 1048576} MB")

    if not audio:
        add("audio present", False, "no audio stream")
        return results
    add("audio present", True, audio.get("codec_name", "audio"))

    a_dur = duration_of(audio, container)
    gap = abs(a_dur - v_dur)
    add("audio/video length", gap <= AV_TOLERANCE,
        f"audio {a_dur:.2f}s vs video {v_dur:.2f}s, gap {gap:.2f}s, "
        f"want within {AV_TOLERANCE}s")

    loud = measure_loudness(path)
    if loud is None:
        add("loudness", False, "could not measure")
    else:
        lufs, peak = loud
        add("loudness", LUFS_RANGE[0] <= lufs <= LUFS_RANGE[1],
            f"{lufs:.1f} LUFS, want {LUFS_RANGE[0]:g} to {LUFS_RANGE[1]:g}")
        add("true peak", peak <= TRUE_PEAK_MAX,
            f"{peak:.1f} dBTP, want at or below {TRUE_PEAK_MAX:g}")
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    ap.add_argument("file", type=Path)
    ap.add_argument("--size", default="1080x1920", help="expected WxH")
    ap.add_argument("--long", action="store_true", help="no upper duration limit")
    ap.add_argument("--frames", type=Path, help="folder for the 2-second frames")
    args = ap.parse_args(argv)

    if not args.file.is_file():
        print(f"not a file: {args.file}", file=sys.stderr)
        return 2

    results = run_checks(args.file, args.size, args.long)
    width = max(len(n) for n, _, _ in results)
    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name.ljust(width)}  {detail}")

    frames_dir = args.frames or args.file.with_suffix("").parent / (
        args.file.stem + "-frames")
    count = extract_frames(args.file, frames_dir)
    print(f"\n{count} frames written to {frames_dir}")
    print("Now open them and read them: text cut off, overlaps, caption "
          "legibility, nothing important in the bottom quarter.")

    failed = [n for n, ok, _ in results if not ok]
    print(f"\n{'ALL MECHANICAL CHECKS PASSED' if not failed else 'FAILED: ' + ', '.join(failed)}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
