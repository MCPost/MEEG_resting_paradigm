"""Standalone VPixx SoundPixx tone diagnostic.

Run this alone (no PsychoPy window, no participant) to confirm the DATAPixx
audio path reaches the VPixx earphones before wiring it into the full task.
"""
import time

from funcs.audio import VPixxTones

tones = VPixxTones(start_freq=660, stop_freq=220, secs=1.0, volume=0.2)
if not tones.ready:
    raise SystemExit(1)

print('--- playing start tone (660 Hz) ---')
tones.play_start()
time.sleep(1.5)

print('--- playing stop tone (220 Hz) ---')
tones.play_stop()
time.sleep(1.5)

print('--- done -- did you hear both tones through the VPixx earphones (both ears)? ---')
