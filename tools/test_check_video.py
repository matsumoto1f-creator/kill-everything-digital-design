"""Tests for check_video.py. Builds tiny synthetic clips with ffmpeg, so they
need ffmpeg on PATH and take a few seconds.

    python3 -m unittest discover -s tools -v
"""
from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_video  # noqa: E402

FFMPEG = check_video.tool("ffmpeg")


def make_clip(path: Path, *, seconds: float = 10, size: str = "1080x1920",
              audio_seconds: float | None = 10, volume: float = 0.25) -> Path:
    """A test-pattern video with a 1 kHz sine. volume 0.25 measures about
    -15 LUFS and -12 dBTP; 0.9 measures about -4 LUFS and -0.9 dBTP."""
    cmd = [FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
           "-f", "lavfi", "-i", f"testsrc2=size={size}:rate=10:duration={seconds}"]
    if audio_seconds is not None:
        cmd += ["-f", "lavfi", "-i",
                f"sine=f=1000:r=48000:duration={audio_seconds}",
                "-af", f"volume={volume}/0.125"]
    cmd += ["-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p"]
    if audio_seconds is not None:
        cmd += ["-c:a", "aac", "-b:a", "192k"]
    cmd.append(str(path))
    subprocess.run(cmd, check=True)
    return path


def failed(results) -> set[str]:
    return {name for name, ok, _ in results if not ok}


class CheckVideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = Path(tempfile.mkdtemp(prefix="ked-design-test-"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.dir, ignore_errors=True)

    def clip(self, name: str, **kw) -> Path:
        return make_clip(self.dir / name, **kw)

    def test_good_clip_passes_everything(self):
        path = self.clip("good.mp4")
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), set(), results)
        names = {n for n, _, _ in results}
        self.assertEqual(names, {"frame size", "duration", "file size",
                                 "audio present", "audio/video length",
                                 "loudness", "true peak"})

    def test_too_short_fails_duration_only(self):
        path = self.clip("short.mp4", seconds=3, audio_seconds=3)
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), {"duration"})

    def test_wrong_size_fails_frame_size_only(self):
        path = self.clip("small.mp4", size="720x1280")
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), {"frame size"})

    def test_custom_size_is_respected(self):
        path = self.clip("landscape.mp4", size="1920x1080")
        results = check_video.run_checks(path, "1920x1080", long_form=False)
        self.assertEqual(failed(results), set())

    def test_no_audio_fails_audio_present(self):
        path = self.clip("mute.mp4", audio_seconds=None)
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertIn("audio present", failed(results))

    def test_audio_much_longer_than_video_fails_length_match(self):
        path = self.clip("drift.mp4", seconds=10, audio_seconds=12)
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), {"audio/video length"})

    def test_too_loud_fails_loudness_and_true_peak(self):
        path = self.clip("loud.mp4", volume=0.9)
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), {"loudness", "true peak"})

    def test_too_quiet_fails_loudness_only(self):
        path = self.clip("quiet.mp4", volume=0.05)
        results = check_video.run_checks(path, "1080x1920", long_form=False)
        self.assertEqual(failed(results), {"loudness"})

    def test_long_flag_lifts_the_upper_duration_limit(self):
        path = self.clip("long.mp4", seconds=100, size="320x568",
                         audio_seconds=100)
        strict = check_video.run_checks(path, "320x568", long_form=False)
        relaxed = check_video.run_checks(path, "320x568", long_form=True)
        self.assertEqual(failed(strict), {"duration"})
        self.assertEqual(failed(relaxed), set())

    def test_cli_exit_codes_and_frames(self):
        good = self.clip("cli_good.mp4")
        frames = self.dir / "cli_good_frames"
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check_video.main([str(good), "--frames", str(frames)])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("ALL MECHANICAL CHECKS PASSED", out.getvalue())
        # 10 s at one frame per 2 s is 5 frames; allow one either way
        self.assertGreaterEqual(len(list(frames.glob("frame_*.jpg"))), 4)

        bad = self.clip("cli_bad.mp4", seconds=3, audio_seconds=3)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check_video.main([str(bad), "--frames", str(self.dir / "bf")])
        self.assertEqual(code, 1)
        self.assertIn("FAILED: duration", out.getvalue())

    def test_cli_missing_file_exits_2(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code = check_video.main([str(self.dir / "nope.mp4")])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
