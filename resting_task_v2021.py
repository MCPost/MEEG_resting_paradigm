#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on September 04, 2026, at 15:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from funcs.response import Responder
# import re for some text substitutions
import re

# Additional Info for data file name
def add_info(expInfo):
    out = 'eyeop'
    if int(expInfo['eyesclosed_recording']):
        out += '_eyecl' 
    if int(expInfo['artifact_recording']):
        out += '_artfrec'
    return out


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'resting_task_v2021'  # from the Builder filename that created this script
expInfo = {'participant': '', 'gender': 'f', 'date_of_birth': 'DD.MM.YYYY', 'ethnicity': '', 'diagnosis': 'control', 'artifact_recording': '1', 'eyesclosed_recording': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, add_info(expInfo), expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Christopher\\ownCloud_MPI_GWDG\\Side_Projects\\Resting_Paradigm\\resting_task_v2021.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
from funcs.audio import VPixxTones
vpixx_tones = VPixxTones(start_freq=660, stop_freq=220, secs=1.0, volume=0.2)
from funcs.trigger import TriggerPatch, TRIGGER_VALUES
trigger_patch = TriggerPatch(win)
trigger_eyes_open = [TRIGGER_VALUES['eyes_open'], 0.0, 0.5]
trigger_eyes_closed = [TRIGGER_VALUES['eyes_closed'], 0.0, 0.5]
resp = Responder(defaultKeyboard, use_box=1)

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
# Change this instruction according to your setup!
continue_button = 'space'
continue_with_button_text = 'Weiter mit der Leertaste...'
welcome_screen_text = visual.TextStim(win=win, name='welcome_screen_text',
    text='Herzlich Willkommen und vielen Dank für Ihre Teilnahme an diesem Experiment!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcome_screen_cwb_text = visual.TextStim(win=win, name='welcome_screen_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
welcome_screen_keyboard = keyboard.Keyboard()

# Initialize components for Routine "artifact_instruction"
artifact_instructionClock = core.Clock()
artifact_instruction_text = visual.TextStim(win=win, name='artifact_instruction_text',
    text='Zu Beginn der Messung würden wir Sie bitten ein paar Störquellen aufzunehmen. Diese Aufnahmen helfen uns später Störungen aus dem Signal zu entfernen.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
artifact_instruction_cwb_text = visual.TextStim(win=win, name='artifact_instruction_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
artifact_instruction_keyboard = keyboard.Keyboard()

# Initialize components for Routine "artifact_explainer"
artifact_explainerClock = core.Clock()
artifact_running = False
artifact_explainer_text = visual.TextStim(win=win, name='artifact_explainer_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
artifact_explainer_cwb_text = visual.TextStim(win=win, name='artifact_explainer_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
artifact_explainer_keyboard = keyboard.Keyboard()

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
# count down from x (each number lasts 1 second)
countdown_from = 3
countdown_time = 1.0
countdown_text = visual.TextStim(win=win, name='countdown_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "artifact_recording"
artifact_recordingClock = core.Clock()
artifact_recording_text = visual.TextStim(win=win, name='artifact_recording_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "short_blank"
short_blankClock = core.Clock()
short_blank_text = visual.TextStim(win=win, name='short_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "eyesopen_instruction"
eyesopen_instructionClock = core.Clock()
eyesopen_instruction_text = visual.TextStim(win=win, name='eyesopen_instruction_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eyesopen_instruction_cwb_text = visual.TextStim(win=win, name='eyesopen_instruction_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eyesopen_instruction_keyboard = keyboard.Keyboard()

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
# count down from x (each number lasts 1 second)
countdown_from = 3
countdown_time = 1.0
countdown_text = visual.TextStim(win=win, name='countdown_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "eyesopen_recording"
eyesopen_recordingClock = core.Clock()
# Duration of Eyes open resting measure in seconds
eyesopen_duration = 300 # 300 s = 5 min
eyesopen_recording_polygon = visual.ShapeStim(
    win=win, name='eyesopen_recording_polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
eyesopen_recording_skip_keyboard = keyboard.Keyboard()

# Initialize components for Routine "short_blank"
short_blankClock = core.Clock()
short_blank_text = visual.TextStim(win=win, name='short_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "eyesclosed_instruction"
eyesclosed_instructionClock = core.Clock()
eyesclosed_running = False
eyesclosed_instruction_text = visual.TextStim(win=win, name='eyesclosed_instruction_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
eyesclosed_instruction_cwb_text = visual.TextStim(win=win, name='eyesclosed_instruction_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
eyesclosed_instruction_keyboard = keyboard.Keyboard()

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
# count down from x (each number lasts 1 second)
countdown_from = 3
countdown_time = 1.0
countdown_text = visual.TextStim(win=win, name='countdown_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "eyesclosed_recording"
eyesclosed_recordingClock = core.Clock()
# Duration of Eyes closed resting measure in seconds
eyesclosed_duration = 300 # 300 s = 5 min
eyesclosed_recording_polygon = visual.ShapeStim(
    win=win, name='eyesclosed_recording_polygon', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
eyesclosed_recording_start_sound = sound.Sound('660', secs=1.0, stereo=True, hamming=True,
    name='eyesclosed_recording_start_sound')
eyesclosed_recording_start_sound.setVolume(0.2)
eyesclosed_recording_stop_sound = sound.Sound('220', secs=1.0, stereo=True, hamming=True,
    name='eyesclosed_recording_stop_sound')
eyesclosed_recording_stop_sound.setVolume(0.2)
eyesclosed_recording_skip_keyboard = keyboard.Keyboard()

# Initialize components for Routine "short_blank"
short_blankClock = core.Clock()
short_blank_text = visual.TextStim(win=win, name='short_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "goodbye_screen"
goodbye_screenClock = core.Clock()
goodbye_screen_text = visual.TextStim(win=win, name='goodbye_screen_text',
    text='Das war´s auch schon...\n\nVielen Dank für Ihre Teilnahme!\n\nBitte warten sie auf weitere Anweisungen der Versuchsleitung.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
goodbye_screen_cwb_text = visual.TextStim(win=win, name='goodbye_screen_cwb_text',
    text='',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
goodbye_screen_keyboard = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_screen"-------
continueRoutine = True
# update component parameters for each repeat
resp.reset()
pressed_key, react_t = None, None
welcome_screen_cwb_text.setText(continue_with_button_text)
welcome_screen_keyboard.keys = []
welcome_screen_keyboard.rt = []
_welcome_screen_keyboard_allKeys = []
# keep track of which components have finished
welcome_screenComponents = [welcome_screen_text, welcome_screen_cwb_text, welcome_screen_keyboard]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_screen"-------
while continueRoutine:
    # get current time
    t = welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if pressed_key is None:
        pressed_key, react_t = resp.poll()
    if pressed_key is not None:
        continueRoutine = False
    
    # *welcome_screen_text* updates
    if welcome_screen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_screen_text.frameNStart = frameN  # exact frame index
        welcome_screen_text.tStart = t  # local t and not account for scr refresh
        welcome_screen_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_screen_text, 'tStartRefresh')  # time at next scr refresh
        welcome_screen_text.setAutoDraw(True)
    
    # *welcome_screen_cwb_text* updates
    if welcome_screen_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_screen_cwb_text.frameNStart = frameN  # exact frame index
        welcome_screen_cwb_text.tStart = t  # local t and not account for scr refresh
        welcome_screen_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_screen_cwb_text, 'tStartRefresh')  # time at next scr refresh
        welcome_screen_cwb_text.setAutoDraw(True)
    
    # *welcome_screen_keyboard* updates
    waitOnFlip = False
    if welcome_screen_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_screen_keyboard.frameNStart = frameN  # exact frame index
        welcome_screen_keyboard.tStart = t  # local t and not account for scr refresh
        welcome_screen_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_screen_keyboard, 'tStartRefresh')  # time at next scr refresh
        welcome_screen_keyboard.status = STARTED
        # AllowedKeys looks like a variable named `continue_button`
        if not type(continue_button) in [list, tuple, np.ndarray]:
            if not isinstance(continue_button, str):
                logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                core.quit()
            elif not ',' in continue_button:
                continue_button = (continue_button,)
            else:
                continue_button = eval(continue_button)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_screen_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_screen_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_screen_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = welcome_screen_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
        _welcome_screen_keyboard_allKeys.extend(theseKeys)
        if len(_welcome_screen_keyboard_allKeys):
            welcome_screen_keyboard.keys = _welcome_screen_keyboard_allKeys[-1].name  # just the last key pressed
            welcome_screen_keyboard.rt = _welcome_screen_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_response', pressed_key)
thisExp.addData('button_RT', react_t)
thisExp.addData('welcome_screen_text.started', welcome_screen_text.tStartRefresh)
thisExp.addData('welcome_screen_text.stopped', welcome_screen_text.tStopRefresh)
thisExp.addData('welcome_screen_cwb_text.started', welcome_screen_cwb_text.tStartRefresh)
thisExp.addData('welcome_screen_cwb_text.stopped', welcome_screen_cwb_text.tStopRefresh)
# check responses
if welcome_screen_keyboard.keys in ['', [], None]:  # No response was made
    welcome_screen_keyboard.keys = None
thisExp.addData('welcome_screen_keyboard.keys',welcome_screen_keyboard.keys)
if welcome_screen_keyboard.keys != None:  # we had a response
    thisExp.addData('welcome_screen_keyboard.rt', welcome_screen_keyboard.rt)
thisExp.addData('welcome_screen_keyboard.started', welcome_screen_keyboard.tStartRefresh)
thisExp.addData('welcome_screen_keyboard.stopped', welcome_screen_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "artifact_instruction"-------
continueRoutine = True
# update component parameters for each repeat
if not int(expInfo['artifact_recording']):
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
artifact_instruction_cwb_text.setText(continue_with_button_text)
artifact_instruction_keyboard.keys = []
artifact_instruction_keyboard.rt = []
_artifact_instruction_keyboard_allKeys = []
# keep track of which components have finished
artifact_instructionComponents = [artifact_instruction_text, artifact_instruction_cwb_text, artifact_instruction_keyboard]
for thisComponent in artifact_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
artifact_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "artifact_instruction"-------
while continueRoutine:
    # get current time
    t = artifact_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=artifact_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *artifact_instruction_text* updates
    if artifact_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        artifact_instruction_text.frameNStart = frameN  # exact frame index
        artifact_instruction_text.tStart = t  # local t and not account for scr refresh
        artifact_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(artifact_instruction_text, 'tStartRefresh')  # time at next scr refresh
        artifact_instruction_text.setAutoDraw(True)
    
    # *artifact_instruction_cwb_text* updates
    if artifact_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        artifact_instruction_cwb_text.frameNStart = frameN  # exact frame index
        artifact_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
        artifact_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(artifact_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
        artifact_instruction_cwb_text.setAutoDraw(True)
    
    # *artifact_instruction_keyboard* updates
    waitOnFlip = False
    if artifact_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        artifact_instruction_keyboard.frameNStart = frameN  # exact frame index
        artifact_instruction_keyboard.tStart = t  # local t and not account for scr refresh
        artifact_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(artifact_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
        artifact_instruction_keyboard.status = STARTED
        # AllowedKeys looks like a variable named `continue_button`
        if not type(continue_button) in [list, tuple, np.ndarray]:
            if not isinstance(continue_button, str):
                logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                core.quit()
            elif not ',' in continue_button:
                continue_button = (continue_button,)
            else:
                continue_button = eval(continue_button)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(artifact_instruction_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(artifact_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if artifact_instruction_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = artifact_instruction_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
        _artifact_instruction_keyboard_allKeys.extend(theseKeys)
        if len(_artifact_instruction_keyboard_allKeys):
            artifact_instruction_keyboard.keys = _artifact_instruction_keyboard_allKeys[-1].name  # just the last key pressed
            artifact_instruction_keyboard.rt = _artifact_instruction_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in artifact_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "artifact_instruction"-------
for thisComponent in artifact_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('artifact_instruction_text.started', artifact_instruction_text.tStartRefresh)
thisExp.addData('artifact_instruction_text.stopped', artifact_instruction_text.tStopRefresh)
thisExp.addData('artifact_instruction_cwb_text.started', artifact_instruction_cwb_text.tStartRefresh)
thisExp.addData('artifact_instruction_cwb_text.stopped', artifact_instruction_cwb_text.tStopRefresh)
# check responses
if artifact_instruction_keyboard.keys in ['', [], None]:  # No response was made
    artifact_instruction_keyboard.keys = None
thisExp.addData('artifact_instruction_keyboard.keys',artifact_instruction_keyboard.keys)
if artifact_instruction_keyboard.keys != None:  # we had a response
    thisExp.addData('artifact_instruction_keyboard.rt', artifact_instruction_keyboard.rt)
thisExp.addData('artifact_instruction_keyboard.started', artifact_instruction_keyboard.tStartRefresh)
thisExp.addData('artifact_instruction_keyboard.stopped', artifact_instruction_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "artifact_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_artifact_recording = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions/artifact_instruction.csv'),
    seed=None, name='loop_artifact_recording')
thisExp.addLoop(loop_artifact_recording)  # add the loop to the experiment
thisLoop_artifact_recording = loop_artifact_recording.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_artifact_recording.rgb)
if thisLoop_artifact_recording != None:
    for paramName in thisLoop_artifact_recording:
        exec('{} = thisLoop_artifact_recording[paramName]'.format(paramName))

for thisLoop_artifact_recording in loop_artifact_recording:
    currentLoop = loop_artifact_recording
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_artifact_recording.rgb)
    if thisLoop_artifact_recording != None:
        for paramName in thisLoop_artifact_recording:
            exec('{} = thisLoop_artifact_recording[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "artifact_explainer"-------
    continueRoutine = True
    # update component parameters for each repeat
    artifact_running = True
    if not int(expInfo['artifact_recording']):
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    # Delete formatting instructions if present
    text = re.sub(r'<.*?>', '', text)
    artifact_explainer_text.setText(text)
    artifact_explainer_cwb_text.setText(continue_with_button_text)
    artifact_explainer_keyboard.keys = []
    artifact_explainer_keyboard.rt = []
    _artifact_explainer_keyboard_allKeys = []
    # keep track of which components have finished
    artifact_explainerComponents = [artifact_explainer_text, artifact_explainer_cwb_text, artifact_explainer_keyboard]
    for thisComponent in artifact_explainerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    artifact_explainerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "artifact_explainer"-------
    while continueRoutine:
        # get current time
        t = artifact_explainerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=artifact_explainerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *artifact_explainer_text* updates
        if artifact_explainer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_explainer_text.frameNStart = frameN  # exact frame index
            artifact_explainer_text.tStart = t  # local t and not account for scr refresh
            artifact_explainer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_explainer_text, 'tStartRefresh')  # time at next scr refresh
            artifact_explainer_text.setAutoDraw(True)
        
        # *artifact_explainer_cwb_text* updates
        if artifact_explainer_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_explainer_cwb_text.frameNStart = frameN  # exact frame index
            artifact_explainer_cwb_text.tStart = t  # local t and not account for scr refresh
            artifact_explainer_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_explainer_cwb_text, 'tStartRefresh')  # time at next scr refresh
            artifact_explainer_cwb_text.setAutoDraw(True)
        
        # *artifact_explainer_keyboard* updates
        waitOnFlip = False
        if artifact_explainer_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_explainer_keyboard.frameNStart = frameN  # exact frame index
            artifact_explainer_keyboard.tStart = t  # local t and not account for scr refresh
            artifact_explainer_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_explainer_keyboard, 'tStartRefresh')  # time at next scr refresh
            artifact_explainer_keyboard.status = STARTED
            # AllowedKeys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                    core.quit()
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(artifact_explainer_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(artifact_explainer_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if artifact_explainer_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = artifact_explainer_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
            _artifact_explainer_keyboard_allKeys.extend(theseKeys)
            if len(_artifact_explainer_keyboard_allKeys):
                artifact_explainer_keyboard.keys = _artifact_explainer_keyboard_allKeys[-1].name  # just the last key pressed
                artifact_explainer_keyboard.rt = _artifact_explainer_keyboard_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in artifact_explainerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "artifact_explainer"-------
    for thisComponent in artifact_explainerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_artifact_recording.addData('artifact_explainer_text.started', artifact_explainer_text.tStartRefresh)
    loop_artifact_recording.addData('artifact_explainer_text.stopped', artifact_explainer_text.tStopRefresh)
    loop_artifact_recording.addData('artifact_explainer_cwb_text.started', artifact_explainer_cwb_text.tStartRefresh)
    loop_artifact_recording.addData('artifact_explainer_cwb_text.stopped', artifact_explainer_cwb_text.tStopRefresh)
    # check responses
    if artifact_explainer_keyboard.keys in ['', [], None]:  # No response was made
        artifact_explainer_keyboard.keys = None
    loop_artifact_recording.addData('artifact_explainer_keyboard.keys',artifact_explainer_keyboard.keys)
    if artifact_explainer_keyboard.keys != None:  # we had a response
        loop_artifact_recording.addData('artifact_explainer_keyboard.rt', artifact_explainer_keyboard.rt)
    loop_artifact_recording.addData('artifact_explainer_keyboard.started', artifact_explainer_keyboard.tStartRefresh)
    loop_artifact_recording.addData('artifact_explainer_keyboard.stopped', artifact_explainer_keyboard.tStopRefresh)
    # the Routine "artifact_explainer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "countdown"-------
    continueRoutine = True
    # update component parameters for each repeat
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    countdown_counter = countdown_from
    add_time = countdown_time
    # keep track of which components have finished
    countdownComponents = [countdown_text]
    for thisComponent in countdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countdown"-------
    while continueRoutine:
        # get current time
        t = countdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if (t >= add_time - frameTolerance):
            countdown_counter = np.max([countdown_counter - 1, 1])
            add_time += countdown_time
        
        # *countdown_text* updates
        if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_text.frameNStart = frameN  # exact frame index
            countdown_text.tStart = t  # local t and not account for scr refresh
            countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
            countdown_text.setAutoDraw(True)
        if countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
                # keep track of stop time/frame for later
                countdown_text.tStop = t  # not accounting for scr refresh
                countdown_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown_text, 'tStopRefresh')  # time at next scr refresh
                countdown_text.setAutoDraw(False)
        if countdown_text.status == STARTED:  # only update if drawing
            countdown_text.setText(countdown_counter, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdown"-------
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_artifact_recording.addData('countdown_text.started', countdown_text.tStartRefresh)
    loop_artifact_recording.addData('countdown_text.stopped', countdown_text.tStopRefresh)
    # the Routine "countdown" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "artifact_recording"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    trigger_artifact = [TRIGGER_VALUES[trigger_key], 0.0, 0.5]
    
    if not int(expInfo['artifact_recording']):
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    artifact_recording_text.setText(short)
    # keep track of which components have finished
    artifact_recordingComponents = [artifact_recording_text]
    for thisComponent in artifact_recordingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    artifact_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "artifact_recording"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = artifact_recordingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=artifact_recordingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Trigger recording
        trigger_patch.update(
            cur_t=tThisFlip, 
            value=trigger_artifact[0], 
            t_onset=trigger_artifact[1], 
            t_offset=trigger_artifact[2],
        )
        
        # *artifact_recording_text* updates
        if artifact_recording_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_recording_text.frameNStart = frameN  # exact frame index
            artifact_recording_text.tStart = t  # local t and not account for scr refresh
            artifact_recording_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_recording_text, 'tStartRefresh')  # time at next scr refresh
            artifact_recording_text.setAutoDraw(True)
        if artifact_recording_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > artifact_recording_text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                artifact_recording_text.tStop = t  # not accounting for scr refresh
                artifact_recording_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(artifact_recording_text, 'tStopRefresh')  # time at next scr refresh
                artifact_recording_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in artifact_recordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "artifact_recording"-------
    for thisComponent in artifact_recordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_artifact_recording.addData('artifact_recording_text.started', artifact_recording_text.tStartRefresh)
    loop_artifact_recording.addData('artifact_recording_text.stopped', artifact_recording_text.tStopRefresh)
    
    # ------Prepare to start Routine "short_blank"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    artifact_running = False
    eyesclosed_running = False
    # keep track of which components have finished
    short_blankComponents = [short_blank_text]
    for thisComponent in short_blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    short_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "short_blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = short_blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=short_blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *short_blank_text* updates
        if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_blank_text.frameNStart = frameN  # exact frame index
            short_blank_text.tStart = t  # local t and not account for scr refresh
            short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
            short_blank_text.setAutoDraw(True)
        if short_blank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                short_blank_text.tStop = t  # not accounting for scr refresh
                short_blank_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(short_blank_text, 'tStopRefresh')  # time at next scr refresh
                short_blank_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in short_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "short_blank"-------
    for thisComponent in short_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_artifact_recording.addData('short_blank_text.started', short_blank_text.tStartRefresh)
    loop_artifact_recording.addData('short_blank_text.stopped', short_blank_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_artifact_recording'


# set up handler to look after randomisation of conditions etc
loop_eyesopen_instruction = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions/eyesopen_instruction.csv'),
    seed=None, name='loop_eyesopen_instruction')
thisExp.addLoop(loop_eyesopen_instruction)  # add the loop to the experiment
thisLoop_eyesopen_instruction = loop_eyesopen_instruction.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesopen_instruction.rgb)
if thisLoop_eyesopen_instruction != None:
    for paramName in thisLoop_eyesopen_instruction:
        exec('{} = thisLoop_eyesopen_instruction[paramName]'.format(paramName))

for thisLoop_eyesopen_instruction in loop_eyesopen_instruction:
    currentLoop = loop_eyesopen_instruction
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesopen_instruction.rgb)
    if thisLoop_eyesopen_instruction != None:
        for paramName in thisLoop_eyesopen_instruction:
            exec('{} = thisLoop_eyesopen_instruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "eyesopen_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Delete formatting instructions if present
    text = re.sub(r'<.*?>', '', text)
    eyesopen_instruction_text.setText(text)
    eyesopen_instruction_cwb_text.setText(continue_with_button_text)
    eyesopen_instruction_keyboard.keys = []
    eyesopen_instruction_keyboard.rt = []
    _eyesopen_instruction_keyboard_allKeys = []
    # keep track of which components have finished
    eyesopen_instructionComponents = [eyesopen_instruction_text, eyesopen_instruction_cwb_text, eyesopen_instruction_keyboard]
    for thisComponent in eyesopen_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eyesopen_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eyesopen_instruction"-------
    while continueRoutine:
        # get current time
        t = eyesopen_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eyesopen_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *eyesopen_instruction_text* updates
        if eyesopen_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesopen_instruction_text.frameNStart = frameN  # exact frame index
            eyesopen_instruction_text.tStart = t  # local t and not account for scr refresh
            eyesopen_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesopen_instruction_text, 'tStartRefresh')  # time at next scr refresh
            eyesopen_instruction_text.setAutoDraw(True)
        
        # *eyesopen_instruction_cwb_text* updates
        if eyesopen_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesopen_instruction_cwb_text.frameNStart = frameN  # exact frame index
            eyesopen_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
            eyesopen_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesopen_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
            eyesopen_instruction_cwb_text.setAutoDraw(True)
        
        # *eyesopen_instruction_keyboard* updates
        waitOnFlip = False
        if eyesopen_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesopen_instruction_keyboard.frameNStart = frameN  # exact frame index
            eyesopen_instruction_keyboard.tStart = t  # local t and not account for scr refresh
            eyesopen_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesopen_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
            eyesopen_instruction_keyboard.status = STARTED
            # AllowedKeys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                    core.quit()
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(eyesopen_instruction_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(eyesopen_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if eyesopen_instruction_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = eyesopen_instruction_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
            _eyesopen_instruction_keyboard_allKeys.extend(theseKeys)
            if len(_eyesopen_instruction_keyboard_allKeys):
                eyesopen_instruction_keyboard.keys = _eyesopen_instruction_keyboard_allKeys[-1].name  # just the last key pressed
                eyesopen_instruction_keyboard.rt = _eyesopen_instruction_keyboard_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyesopen_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eyesopen_instruction"-------
    for thisComponent in eyesopen_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_eyesopen_instruction.addData('eyesopen_instruction_text.started', eyesopen_instruction_text.tStartRefresh)
    loop_eyesopen_instruction.addData('eyesopen_instruction_text.stopped', eyesopen_instruction_text.tStopRefresh)
    loop_eyesopen_instruction.addData('eyesopen_instruction_cwb_text.started', eyesopen_instruction_cwb_text.tStartRefresh)
    loop_eyesopen_instruction.addData('eyesopen_instruction_cwb_text.stopped', eyesopen_instruction_cwb_text.tStopRefresh)
    # check responses
    if eyesopen_instruction_keyboard.keys in ['', [], None]:  # No response was made
        eyesopen_instruction_keyboard.keys = None
    loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.keys',eyesopen_instruction_keyboard.keys)
    if eyesopen_instruction_keyboard.keys != None:  # we had a response
        loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.rt', eyesopen_instruction_keyboard.rt)
    loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.started', eyesopen_instruction_keyboard.tStartRefresh)
    loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.stopped', eyesopen_instruction_keyboard.tStopRefresh)
    # the Routine "eyesopen_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_eyesopen_instruction'


# ------Prepare to start Routine "countdown"-------
continueRoutine = True
# update component parameters for each repeat
if (not int(expInfo['artifact_recording'])) and artifact_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

countdown_counter = countdown_from
add_time = countdown_time
# keep track of which components have finished
countdownComponents = [countdown_text]
for thisComponent in countdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "countdown"-------
while continueRoutine:
    # get current time
    t = countdownClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=countdownClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (t >= add_time - frameTolerance):
        countdown_counter = np.max([countdown_counter - 1, 1])
        add_time += countdown_time
    
    # *countdown_text* updates
    if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        countdown_text.frameNStart = frameN  # exact frame index
        countdown_text.tStart = t  # local t and not account for scr refresh
        countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
        countdown_text.setAutoDraw(True)
    if countdown_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
            # keep track of stop time/frame for later
            countdown_text.tStop = t  # not accounting for scr refresh
            countdown_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown_text, 'tStopRefresh')  # time at next scr refresh
            countdown_text.setAutoDraw(False)
    if countdown_text.status == STARTED:  # only update if drawing
        countdown_text.setText(countdown_counter, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "countdown"-------
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('countdown_text.started', countdown_text.tStartRefresh)
thisExp.addData('countdown_text.stopped', countdown_text.tStopRefresh)
# the Routine "countdown" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "eyesopen_recording"-------
continueRoutine = True
# update component parameters for each repeat
eyesopen_recording_skip_keyboard.keys = []
eyesopen_recording_skip_keyboard.rt = []
_eyesopen_recording_skip_keyboard_allKeys = []
# keep track of which components have finished
eyesopen_recordingComponents = [eyesopen_recording_polygon, eyesopen_recording_skip_keyboard]
for thisComponent in eyesopen_recordingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eyesopen_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eyesopen_recording"-------
while continueRoutine:
    # get current time
    t = eyesopen_recordingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eyesopen_recordingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Trigger recording
    trigger_patch.update(
        cur_t=tThisFlip, 
        value=trigger_eyes_open[0], 
        t_onset=trigger_eyes_open[1], 
        t_offset=trigger_eyes_open[2],
    )
    
    # *eyesopen_recording_polygon* updates
    if eyesopen_recording_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eyesopen_recording_polygon.frameNStart = frameN  # exact frame index
        eyesopen_recording_polygon.tStart = t  # local t and not account for scr refresh
        eyesopen_recording_polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyesopen_recording_polygon, 'tStartRefresh')  # time at next scr refresh
        eyesopen_recording_polygon.setAutoDraw(True)
    if eyesopen_recording_polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyesopen_recording_polygon.tStartRefresh + eyesopen_duration-frameTolerance:
            # keep track of stop time/frame for later
            eyesopen_recording_polygon.tStop = t  # not accounting for scr refresh
            eyesopen_recording_polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyesopen_recording_polygon, 'tStopRefresh')  # time at next scr refresh
            eyesopen_recording_polygon.setAutoDraw(False)
    
    # *eyesopen_recording_skip_keyboard* updates
    waitOnFlip = False
    if eyesopen_recording_skip_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eyesopen_recording_skip_keyboard.frameNStart = frameN  # exact frame index
        eyesopen_recording_skip_keyboard.tStart = t  # local t and not account for scr refresh
        eyesopen_recording_skip_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyesopen_recording_skip_keyboard, 'tStartRefresh')  # time at next scr refresh
        eyesopen_recording_skip_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(eyesopen_recording_skip_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(eyesopen_recording_skip_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if eyesopen_recording_skip_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = eyesopen_recording_skip_keyboard.getKeys(keyList=['s'], waitRelease=False)
        _eyesopen_recording_skip_keyboard_allKeys.extend(theseKeys)
        if len(_eyesopen_recording_skip_keyboard_allKeys):
            eyesopen_recording_skip_keyboard.keys = _eyesopen_recording_skip_keyboard_allKeys[-1].name  # just the last key pressed
            eyesopen_recording_skip_keyboard.rt = _eyesopen_recording_skip_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eyesopen_recordingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eyesopen_recording"-------
for thisComponent in eyesopen_recordingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('eyesopen_recording_polygon.started', eyesopen_recording_polygon.tStartRefresh)
thisExp.addData('eyesopen_recording_polygon.stopped', eyesopen_recording_polygon.tStopRefresh)
# check responses
if eyesopen_recording_skip_keyboard.keys in ['', [], None]:  # No response was made
    eyesopen_recording_skip_keyboard.keys = None
thisExp.addData('eyesopen_recording_skip_keyboard.keys',eyesopen_recording_skip_keyboard.keys)
if eyesopen_recording_skip_keyboard.keys != None:  # we had a response
    thisExp.addData('eyesopen_recording_skip_keyboard.rt', eyesopen_recording_skip_keyboard.rt)
thisExp.addData('eyesopen_recording_skip_keyboard.started', eyesopen_recording_skip_keyboard.tStartRefresh)
thisExp.addData('eyesopen_recording_skip_keyboard.stopped', eyesopen_recording_skip_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "eyesopen_recording" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "short_blank"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
if (not int(expInfo['artifact_recording'])) and artifact_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

artifact_running = False
eyesclosed_running = False
# keep track of which components have finished
short_blankComponents = [short_blank_text]
for thisComponent in short_blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
short_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "short_blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = short_blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=short_blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *short_blank_text* updates
    if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        short_blank_text.frameNStart = frameN  # exact frame index
        short_blank_text.tStart = t  # local t and not account for scr refresh
        short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
        short_blank_text.setAutoDraw(True)
    if short_blank_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            short_blank_text.tStop = t  # not accounting for scr refresh
            short_blank_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(short_blank_text, 'tStopRefresh')  # time at next scr refresh
            short_blank_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in short_blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "short_blank"-------
for thisComponent in short_blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('short_blank_text.started', short_blank_text.tStartRefresh)
thisExp.addData('short_blank_text.stopped', short_blank_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_eyesclosed_instruction = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions/eyesclosed_instruction.csv'),
    seed=None, name='loop_eyesclosed_instruction')
thisExp.addLoop(loop_eyesclosed_instruction)  # add the loop to the experiment
thisLoop_eyesclosed_instruction = loop_eyesclosed_instruction.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesclosed_instruction.rgb)
if thisLoop_eyesclosed_instruction != None:
    for paramName in thisLoop_eyesclosed_instruction:
        exec('{} = thisLoop_eyesclosed_instruction[paramName]'.format(paramName))

for thisLoop_eyesclosed_instruction in loop_eyesclosed_instruction:
    currentLoop = loop_eyesclosed_instruction
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesclosed_instruction.rgb)
    if thisLoop_eyesclosed_instruction != None:
        for paramName in thisLoop_eyesclosed_instruction:
            exec('{} = thisLoop_eyesclosed_instruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "eyesclosed_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    eyesclosed_running = True
    if not int(expInfo['eyesclosed_recording']):
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    # Delete formatting instructions if present
    text = re.sub(r'<.*?>', '', text)
    eyesclosed_instruction_text.setText(text)
    eyesclosed_instruction_cwb_text.setText(continue_with_button_text)
    eyesclosed_instruction_keyboard.keys = []
    eyesclosed_instruction_keyboard.rt = []
    _eyesclosed_instruction_keyboard_allKeys = []
    # keep track of which components have finished
    eyesclosed_instructionComponents = [eyesclosed_instruction_text, eyesclosed_instruction_cwb_text, eyesclosed_instruction_keyboard]
    for thisComponent in eyesclosed_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eyesclosed_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eyesclosed_instruction"-------
    while continueRoutine:
        # get current time
        t = eyesclosed_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eyesclosed_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *eyesclosed_instruction_text* updates
        if eyesclosed_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_instruction_text.frameNStart = frameN  # exact frame index
            eyesclosed_instruction_text.tStart = t  # local t and not account for scr refresh
            eyesclosed_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesclosed_instruction_text, 'tStartRefresh')  # time at next scr refresh
            eyesclosed_instruction_text.setAutoDraw(True)
        
        # *eyesclosed_instruction_cwb_text* updates
        if eyesclosed_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_instruction_cwb_text.frameNStart = frameN  # exact frame index
            eyesclosed_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
            eyesclosed_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesclosed_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
            eyesclosed_instruction_cwb_text.setAutoDraw(True)
        
        # *eyesclosed_instruction_keyboard* updates
        waitOnFlip = False
        if eyesclosed_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_instruction_keyboard.frameNStart = frameN  # exact frame index
            eyesclosed_instruction_keyboard.tStart = t  # local t and not account for scr refresh
            eyesclosed_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesclosed_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
            eyesclosed_instruction_keyboard.status = STARTED
            # AllowedKeys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                    core.quit()
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(eyesclosed_instruction_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(eyesclosed_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if eyesclosed_instruction_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = eyesclosed_instruction_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
            _eyesclosed_instruction_keyboard_allKeys.extend(theseKeys)
            if len(_eyesclosed_instruction_keyboard_allKeys):
                eyesclosed_instruction_keyboard.keys = _eyesclosed_instruction_keyboard_allKeys[-1].name  # just the last key pressed
                eyesclosed_instruction_keyboard.rt = _eyesclosed_instruction_keyboard_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyesclosed_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eyesclosed_instruction"-------
    for thisComponent in eyesclosed_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_text.started', eyesclosed_instruction_text.tStartRefresh)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_text.stopped', eyesclosed_instruction_text.tStopRefresh)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_cwb_text.started', eyesclosed_instruction_cwb_text.tStartRefresh)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_cwb_text.stopped', eyesclosed_instruction_cwb_text.tStopRefresh)
    # check responses
    if eyesclosed_instruction_keyboard.keys in ['', [], None]:  # No response was made
        eyesclosed_instruction_keyboard.keys = None
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.keys',eyesclosed_instruction_keyboard.keys)
    if eyesclosed_instruction_keyboard.keys != None:  # we had a response
        loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.rt', eyesclosed_instruction_keyboard.rt)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.started', eyesclosed_instruction_keyboard.tStartRefresh)
    loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.stopped', eyesclosed_instruction_keyboard.tStopRefresh)
    # the Routine "eyesclosed_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop_eyesclosed_instruction'


# ------Prepare to start Routine "countdown"-------
continueRoutine = True
# update component parameters for each repeat
if (not int(expInfo['artifact_recording'])) and artifact_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

countdown_counter = countdown_from
add_time = countdown_time
# keep track of which components have finished
countdownComponents = [countdown_text]
for thisComponent in countdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
countdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "countdown"-------
while continueRoutine:
    # get current time
    t = countdownClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=countdownClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (t >= add_time - frameTolerance):
        countdown_counter = np.max([countdown_counter - 1, 1])
        add_time += countdown_time
    
    # *countdown_text* updates
    if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        countdown_text.frameNStart = frameN  # exact frame index
        countdown_text.tStart = t  # local t and not account for scr refresh
        countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
        countdown_text.setAutoDraw(True)
    if countdown_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
            # keep track of stop time/frame for later
            countdown_text.tStop = t  # not accounting for scr refresh
            countdown_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown_text, 'tStopRefresh')  # time at next scr refresh
            countdown_text.setAutoDraw(False)
    if countdown_text.status == STARTED:  # only update if drawing
        countdown_text.setText(countdown_counter, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "countdown"-------
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('countdown_text.started', countdown_text.tStartRefresh)
thisExp.addData('countdown_text.stopped', countdown_text.tStopRefresh)
# the Routine "countdown" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "eyesclosed_recording"-------
continueRoutine = True
# update component parameters for each repeat
_vpixx_start_played = False
_vpixx_stop_played = False

if not int(expInfo['eyesclosed_recording']):
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
eyesclosed_recording_start_sound.setSound('660', secs=1.0, hamming=True)
eyesclosed_recording_start_sound.setVolume(0.2, log=False)
eyesclosed_recording_stop_sound.setSound('220', secs=1.0, hamming=True)
eyesclosed_recording_stop_sound.setVolume(0.2, log=False)
eyesclosed_recording_skip_keyboard.keys = []
eyesclosed_recording_skip_keyboard.rt = []
_eyesclosed_recording_skip_keyboard_allKeys = []
# keep track of which components have finished
eyesclosed_recordingComponents = [eyesclosed_recording_polygon, eyesclosed_recording_start_sound, eyesclosed_recording_stop_sound, eyesclosed_recording_skip_keyboard]
for thisComponent in eyesclosed_recordingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eyesclosed_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eyesclosed_recording"-------
while continueRoutine:
    # get current time
    t = eyesclosed_recordingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eyesclosed_recordingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if eyesclosed_recording_start_sound.status == STARTED and not _vpixx_start_played:
        vpixx_tones.play_start()
        _vpixx_start_played = True
    if eyesclosed_recording_stop_sound.status == STARTED and not _vpixx_stop_played:
        vpixx_tones.play_stop()
        _vpixx_stop_played = True
    
    # Trigger recording
    trigger_patch.update(
        cur_t=tThisFlip, 
        value=trigger_eyes_closed[0], 
        t_onset=trigger_eyes_closed[1], 
        t_offset=trigger_eyes_closed[2],
    )
    
    # *eyesclosed_recording_polygon* updates
    if eyesclosed_recording_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eyesclosed_recording_polygon.frameNStart = frameN  # exact frame index
        eyesclosed_recording_polygon.tStart = t  # local t and not account for scr refresh
        eyesclosed_recording_polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyesclosed_recording_polygon, 'tStartRefresh')  # time at next scr refresh
        eyesclosed_recording_polygon.setAutoDraw(True)
    if eyesclosed_recording_polygon.status == STARTED:
        if bool(len(_eyesclosed_recording_skip_keyboard_allKeys)):
            # keep track of stop time/frame for later
            eyesclosed_recording_polygon.tStop = t  # not accounting for scr refresh
            eyesclosed_recording_polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyesclosed_recording_polygon, 'tStopRefresh')  # time at next scr refresh
            eyesclosed_recording_polygon.setAutoDraw(False)
    # start/stop eyesclosed_recording_start_sound
    if eyesclosed_recording_start_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eyesclosed_recording_start_sound.frameNStart = frameN  # exact frame index
        eyesclosed_recording_start_sound.tStart = t  # local t and not account for scr refresh
        eyesclosed_recording_start_sound.tStartRefresh = tThisFlipGlobal  # on global time
        eyesclosed_recording_start_sound.play(when=win)  # sync with win flip
    if eyesclosed_recording_start_sound.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyesclosed_recording_start_sound.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            eyesclosed_recording_start_sound.tStop = t  # not accounting for scr refresh
            eyesclosed_recording_start_sound.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyesclosed_recording_start_sound, 'tStopRefresh')  # time at next scr refresh
            eyesclosed_recording_start_sound.stop()
    # start/stop eyesclosed_recording_stop_sound
    if eyesclosed_recording_stop_sound.status == NOT_STARTED and len(_eyesclosed_recording_skip_keyboard_allKeys):
        # keep track of start time/frame for later
        eyesclosed_recording_stop_sound.frameNStart = frameN  # exact frame index
        eyesclosed_recording_stop_sound.tStart = t  # local t and not account for scr refresh
        eyesclosed_recording_stop_sound.tStartRefresh = tThisFlipGlobal  # on global time
        eyesclosed_recording_stop_sound.play(when=win)  # sync with win flip
    if eyesclosed_recording_stop_sound.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eyesclosed_recording_stop_sound.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            eyesclosed_recording_stop_sound.tStop = t  # not accounting for scr refresh
            eyesclosed_recording_stop_sound.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyesclosed_recording_stop_sound, 'tStopRefresh')  # time at next scr refresh
            eyesclosed_recording_stop_sound.stop()
    
    # *eyesclosed_recording_skip_keyboard* updates
    waitOnFlip = False
    if eyesclosed_recording_skip_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eyesclosed_recording_skip_keyboard.frameNStart = frameN  # exact frame index
        eyesclosed_recording_skip_keyboard.tStart = t  # local t and not account for scr refresh
        eyesclosed_recording_skip_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eyesclosed_recording_skip_keyboard, 'tStartRefresh')  # time at next scr refresh
        eyesclosed_recording_skip_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(eyesclosed_recording_skip_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(eyesclosed_recording_skip_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if eyesclosed_recording_skip_keyboard.status == STARTED:
        if bool(len(_eyesclosed_recording_skip_keyboard_allKeys)):
            # keep track of stop time/frame for later
            eyesclosed_recording_skip_keyboard.tStop = t  # not accounting for scr refresh
            eyesclosed_recording_skip_keyboard.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eyesclosed_recording_skip_keyboard, 'tStopRefresh')  # time at next scr refresh
            eyesclosed_recording_skip_keyboard.status = FINISHED
    if eyesclosed_recording_skip_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = eyesclosed_recording_skip_keyboard.getKeys(keyList=['s'], waitRelease=False)
        _eyesclosed_recording_skip_keyboard_allKeys.extend(theseKeys)
        if len(_eyesclosed_recording_skip_keyboard_allKeys):
            eyesclosed_recording_skip_keyboard.keys = _eyesclosed_recording_skip_keyboard_allKeys[-1].name  # just the last key pressed
            eyesclosed_recording_skip_keyboard.rt = _eyesclosed_recording_skip_keyboard_allKeys[-1].rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eyesclosed_recordingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eyesclosed_recording"-------
for thisComponent in eyesclosed_recordingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('eyesclosed_recording_polygon.started', eyesclosed_recording_polygon.tStartRefresh)
thisExp.addData('eyesclosed_recording_polygon.stopped', eyesclosed_recording_polygon.tStopRefresh)
eyesclosed_recording_start_sound.stop()  # ensure sound has stopped at end of routine
thisExp.addData('eyesclosed_recording_start_sound.started', eyesclosed_recording_start_sound.tStartRefresh)
thisExp.addData('eyesclosed_recording_start_sound.stopped', eyesclosed_recording_start_sound.tStopRefresh)
eyesclosed_recording_stop_sound.stop()  # ensure sound has stopped at end of routine
thisExp.addData('eyesclosed_recording_stop_sound.started', eyesclosed_recording_stop_sound.tStartRefresh)
thisExp.addData('eyesclosed_recording_stop_sound.stopped', eyesclosed_recording_stop_sound.tStopRefresh)
# check responses
if eyesclosed_recording_skip_keyboard.keys in ['', [], None]:  # No response was made
    eyesclosed_recording_skip_keyboard.keys = None
thisExp.addData('eyesclosed_recording_skip_keyboard.keys',eyesclosed_recording_skip_keyboard.keys)
if eyesclosed_recording_skip_keyboard.keys != None:  # we had a response
    thisExp.addData('eyesclosed_recording_skip_keyboard.rt', eyesclosed_recording_skip_keyboard.rt)
thisExp.addData('eyesclosed_recording_skip_keyboard.started', eyesclosed_recording_skip_keyboard.tStartRefresh)
thisExp.addData('eyesclosed_recording_skip_keyboard.stopped', eyesclosed_recording_skip_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "eyesclosed_recording" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "short_blank"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
if (not int(expInfo['artifact_recording'])) and artifact_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
    continueRoutine = False
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)

artifact_running = False
eyesclosed_running = False
# keep track of which components have finished
short_blankComponents = [short_blank_text]
for thisComponent in short_blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
short_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "short_blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = short_blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=short_blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *short_blank_text* updates
    if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        short_blank_text.frameNStart = frameN  # exact frame index
        short_blank_text.tStart = t  # local t and not account for scr refresh
        short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
        short_blank_text.setAutoDraw(True)
    if short_blank_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            short_blank_text.tStop = t  # not accounting for scr refresh
            short_blank_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(short_blank_text, 'tStopRefresh')  # time at next scr refresh
            short_blank_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in short_blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "short_blank"-------
for thisComponent in short_blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('short_blank_text.started', short_blank_text.tStartRefresh)
thisExp.addData('short_blank_text.stopped', short_blank_text.tStopRefresh)

# ------Prepare to start Routine "goodbye_screen"-------
continueRoutine = True
# update component parameters for each repeat
goodbye_screen_cwb_text.setText(continue_with_button_text)
goodbye_screen_keyboard.keys = []
goodbye_screen_keyboard.rt = []
_goodbye_screen_keyboard_allKeys = []
# keep track of which components have finished
goodbye_screenComponents = [goodbye_screen_text, goodbye_screen_cwb_text, goodbye_screen_keyboard]
for thisComponent in goodbye_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbye_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye_screen"-------
while continueRoutine:
    # get current time
    t = goodbye_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbye_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye_screen_text* updates
    if goodbye_screen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_screen_text.frameNStart = frameN  # exact frame index
        goodbye_screen_text.tStart = t  # local t and not account for scr refresh
        goodbye_screen_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_screen_text, 'tStartRefresh')  # time at next scr refresh
        goodbye_screen_text.setAutoDraw(True)
    
    # *goodbye_screen_cwb_text* updates
    if goodbye_screen_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_screen_cwb_text.frameNStart = frameN  # exact frame index
        goodbye_screen_cwb_text.tStart = t  # local t and not account for scr refresh
        goodbye_screen_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_screen_cwb_text, 'tStartRefresh')  # time at next scr refresh
        goodbye_screen_cwb_text.setAutoDraw(True)
    
    # *goodbye_screen_keyboard* updates
    waitOnFlip = False
    if goodbye_screen_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_screen_keyboard.frameNStart = frameN  # exact frame index
        goodbye_screen_keyboard.tStart = t  # local t and not account for scr refresh
        goodbye_screen_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_screen_keyboard, 'tStartRefresh')  # time at next scr refresh
        goodbye_screen_keyboard.status = STARTED
        # AllowedKeys looks like a variable named `continue_button`
        if not type(continue_button) in [list, tuple, np.ndarray]:
            if not isinstance(continue_button, str):
                logging.error('AllowedKeys variable `continue_button` is not string- or list-like.')
                core.quit()
            elif not ',' in continue_button:
                continue_button = (continue_button,)
            else:
                continue_button = eval(continue_button)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(goodbye_screen_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(goodbye_screen_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if goodbye_screen_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = goodbye_screen_keyboard.getKeys(keyList=list(continue_button), waitRelease=False)
        _goodbye_screen_keyboard_allKeys.extend(theseKeys)
        if len(_goodbye_screen_keyboard_allKeys):
            goodbye_screen_keyboard.keys = _goodbye_screen_keyboard_allKeys[-1].name  # just the last key pressed
            goodbye_screen_keyboard.rt = _goodbye_screen_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbye_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye_screen"-------
for thisComponent in goodbye_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbye_screen_text.started', goodbye_screen_text.tStartRefresh)
thisExp.addData('goodbye_screen_text.stopped', goodbye_screen_text.tStopRefresh)
thisExp.addData('goodbye_screen_cwb_text.started', goodbye_screen_cwb_text.tStartRefresh)
thisExp.addData('goodbye_screen_cwb_text.stopped', goodbye_screen_cwb_text.tStopRefresh)
# check responses
if goodbye_screen_keyboard.keys in ['', [], None]:  # No response was made
    goodbye_screen_keyboard.keys = None
thisExp.addData('goodbye_screen_keyboard.keys',goodbye_screen_keyboard.keys)
if goodbye_screen_keyboard.keys != None:  # we had a response
    thisExp.addData('goodbye_screen_keyboard.rt', goodbye_screen_keyboard.rt)
thisExp.addData('goodbye_screen_keyboard.started', goodbye_screen_keyboard.tStartRefresh)
thisExp.addData('goodbye_screen_keyboard.stopped', goodbye_screen_keyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "goodbye_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
