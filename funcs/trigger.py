"""MEG/OPM trigger patch: single source of truth for trigger values and the
patch-based encoding shared by both experiment versions.

The OPM system reads triggers via VPixx Pixel Mode B: the blue channel of a
small patch drawn at the screen's top-left corner (pixel (0,0)) is decoded
into DOut 16-23 in hardware (see OPM_PSYCHOPY_GUIDE.md for the hardware
side) -- this module only concerns the PsychoPy-side patch.
"""
from psychopy import visual

# Trigger values sent to the OPM system. Single source of truth -- the
# artifact instruction CSV's trigger_key column references these by name,
# never by raw number, so there is only one place these can drift.
TRIGGER_VALUES = {
    'eyes_open': 10,
    'eyes_closed': 20,
    'eyes_roll': 30,
    'eyes_blink': 32,
    'eyes_saccade': 34,
    'clench_jaw': 36,
    'swallow': 38,
}


class TriggerPatch:
    """Draws the trigger patch and updates its color on demand."""

    def __init__(self, win):
        self.patch = visual.Rect(
            win=win, name='trigger_patch', units='pix',
            size=[5, 5],
            fillColor=[0, 0, 0],
            pos=[-win.size[0] / 2, win.size[1] / 2],
            lineWidth=0.0, colorSpace='rgb255',
            opacity=None, depth=-1.0, interpolate=True,
            autoDraw=True)

    def update(self, cur_t, value, t_onset=0.0, t_offset=0.5):
        """Blue channel = value between t_onset and t_offset, else off.
        cur_t is the routine's current flip time (same convention as the
        old change_trigger()).
        """
        if t_onset < cur_t <= t_offset:
            self.patch.color = [0, 0, value]
        else:
            self.patch.color = [0, 0, 0]
