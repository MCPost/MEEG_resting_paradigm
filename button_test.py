"""Standalone RESPONSEPixx button-box diagnostic.

Run this alone (no PsychoPy window, no participant) to confirm the box is
detected and to see which DIN bit changes on every press. Compare the bits
against BOX_BUTTONS in funcs/response.py -- currently {'left': 0, 'right': 2}.

Ctrl+C to quit.
"""
from pypixxlib import _libdpx as dp

dp.DPxOpen()
ready = dp.DPxIsReady()
print('--- DPxOpen() called, DPxIsReady():', ready, '---')
if not ready:
    print('Warning! DATAPixx not ready -- check cabling/power, then re-run.')
    raise SystemExit(1)

dp.DPxEnableDinDebounce()
dp.DPxWriteRegCache()
dp.DPxUpdateRegCache()
idle = dp.DPxGetDinValue()
print('--- idle DIN value:', idle, '---')
print('--- press buttons on the RESPONSEPixx handheld; Ctrl+C to quit ---')

last = idle
try:
    while True:
        dp.DPxUpdateRegCache()
        din = dp.DPxGetDinValue()
        if din != last:
            changed = din ^ last
            bits = [b for b in range(24) if (changed >> b) & 1]
            print('DIN changed:', din, ' bits flipped:', bits, ' (idle was', idle, ')')
            last = din
except KeyboardInterrupt:
    print('--- stopped ---')
