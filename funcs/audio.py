"""VPixx SoundPixx tone playback.

Writes short synthesized tones into DATAPixx onboard RAM and plays them via
the low-level VPixx audio schedule (setAudioSchedule/startSchedule), the same
mechanism documented in OPM_PSYCHOPY_GUIDE.md #9 from the earlier VPixx
project. This bypasses the normal Windows audio device entirely, which is
the point: the VPixx earphones in the shielded room are wired to the
DATAPixx, not to the PC's sound card.
"""
import numpy as np

# 16 MB / 17 MB -- comfortably clear of the DOut buffer (~6.3 MB) and of each
# other; each tone here is under 200 KB at these settings.
AUDIO_RAM_START_ADDR = 0x1000000
AUDIO_RAM_STOP_ADDR = 0x1100000
SAMPLE_RATE = 48000  # verify against what the DATAPixx audio out actually supports


def _make_tone(freq, secs, fs, hamming=True):
    n = int(round(secs * fs))
    t = np.arange(n) / fs
    tone = np.sin(2 * np.pi * freq * t).astype('float32')
    if hamming:
        tone *= np.hamming(n).astype('float32')
    return tone


class VPixxTones:
    """Prepares and plays the eyes-closed start/stop tones over SoundPixx.

    Never raises: if setup fails, self.ready stays False and play_*() becomes
    a no-op, so a missing/unavailable DATAPixx degrades to silence rather than
    crashing the task.
    """

    def __init__(self, start_freq=660, stop_freq=220, secs=1.0,
                 fs=SAMPLE_RATE, volume=0.2):
        self.ready = False
        self.n_samples_start = 0
        self.n_samples_stop = 0
        try:
            from pypixxlib import _libdpx as dp
            from pypixxlib.datapixx import DATAPixx3
            dp.DPxOpen()
            if not dp.DPxIsReady():
                raise RuntimeError('DATAPixx not ready after DPxOpen()')
            start_tone = _make_tone(start_freq, secs, fs)
            stop_tone = _make_tone(stop_freq, secs, fs)
            dp.DPxWriteAudioBuffer(start_tone, AUDIO_RAM_START_ADDR)
            dp.DPxWriteAudioBuffer(stop_tone, AUDIO_RAM_STOP_ADDR)
            dp.DPxWriteRegCache()
            self.dp = dp
            self.dpx = DATAPixx3()
            self.fs = fs
            self.n_samples_start = len(start_tone)
            self.n_samples_stop = len(stop_tone)
            self.volume = volume
            self.ready = True
            print('--- VPixx audio ready: start=%dHz stop=%dHz fs=%d volume=%.2f ---'
                  % (start_freq, stop_freq, fs, volume))
        except Exception as e:
            print('Warning! VPixx audio setup failed, tones will not play: ', e)

    def _play(self, addr, n_samples):
        if not self.ready:
            return
        try:
            self.dpx.audio.stopSchedule()
            self.dpx.audio.setAudioSchedule(0.0, self.fs, n_samples, 'mono', addr)
            self.dpx.audio.setReadAddress(addr)  # essential -- schedule alone does not reset it
            self.dpx.audio.setVolume(self.volume)
            self.dpx.audio.startSchedule()
            self.dpx.writeRegisterCache()
        except Exception as e:
            print('Warning! VPixx tone playback failed: ', e)

    def play_start(self):
        self._play(AUDIO_RAM_START_ADDR, self.n_samples_start)

    def play_stop(self):
        self._play(AUDIO_RAM_STOP_ADDR, self.n_samples_stop)
