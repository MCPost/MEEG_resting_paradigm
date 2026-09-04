from psychopy import core

# RESPONSEPixx handheld DIN bits: 0=red, 1=yellow, 2=green, 3=blue, 4=white
# CHECK THESE AGAINST WHAT button_test.py PRINTS
BOX_BUTTONS = {'left': 0, 'right': 2}  # red -> left, green -> right
DEBUG_DIN = 0  # 1 prints the raw DIN value on every change


class Responder:
    """Collects the left/right answer. Uses the RESPONSEPixx when use_box is on
    and the DATAPixx answers, otherwise falls back to the keyboard. Escape
    always comes from the keyboard (experimenter).
    A bit counts as pressed when it differs from the idle value read at startup,
    so the polarity does not have to be known in advance.
    """

    def __init__(self, kb, use_box=0):
        self.kb = kb
        self.clock = core.Clock()
        self.box = False
        self.dp = None
        self.idle = 0
        self.last = None
        self.ready = True  # False while a button from the last trial is still down
        if use_box:
            try:
                from pypixxlib import _libdpx as dp
                dp.DPxOpen()
                ready = dp.DPxIsReady()
                print('--- DPxOpen() called, DPxIsReady():', ready, '---')
                if not ready:
                    raise RuntimeError('DATAPixx not ready after DPxOpen()')
                dp.DPxEnableDinDebounce()  # ignores transitions for 30 ms
                dp.DPxWriteRegCache()
                dp.DPxUpdateRegCache()
                self.idle = dp.DPxGetDinValue()
                self.dp = dp
                self.box = True
                print('--- response box active, idle DIN value: ', self.idle, ' ---')
                print('--- watching bits: ', BOX_BUTTONS, ' ---')
            except Exception as e:
                print('Warning! Response box setup failed, using keyboard: ', e)

    def reset(self):
        """Zero the response clock. Call it right after the flip that shows the
        stimulus, so the reaction time counts from stimulus onset.
        """
        self.kb.clock.reset()
        self.kb.clearEvents()
        self.clock.reset()
        self.ready = not self.box  # box: wait for a release before accepting

    def _down(self):
        """Name of a pressed button, or None. Falls back to keyboard on error."""
        if not self.box:
            return None
        try:
            self.dp.DPxUpdateRegCache()
            din = self.dp.DPxGetDinValue()
        except Exception as e:
            print('Warning! Response box read failed, using keyboard: ', e)
            self.box = False
            return None
        if DEBUG_DIN and din != self.last:
            print('DIN ', din, ' (idle ', self.idle, ')')
            self.last = din
        for name, bit in BOX_BUTTONS.items():
            if (din >> bit & 1) != (self.idle >> bit & 1):
                return name
        return None

    def poll(self):
        """One look, no waiting. Returns (name, rt) or (None, None).
        Costs one USB round trip when the box is on, so only call it inside the
        response window, not while a stimulus onset is being timed.
        """
        if self.kb.getKeys(keyList=['escape'], waitRelease=False):
            return 'escape', self.clock.getTime()
        if self.box:
            name = self._down()
            if not self.ready:
                self.ready = name is None  # button from the last trial released
                return None, None
            if name:
                return name, self.clock.getTime()
            return None, None
        keys = self.kb.getKeys(keyList=['left', 'right'], waitRelease=False)
        if keys:
            return keys[0].name, keys[0].rt
        return None, None

    def wait(self):
        """Blocks until an answer or escape. Returns (name, rt)."""
        while True:
            name, rt = self.poll()
            if name:
                return name, rt