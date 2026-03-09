#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on März 09, 2026, at 15:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from welcome_screen_code
# Additional Info for data file name
def add_info(expInfo):
    out = 'eyeop'
    if int(expInfo['eyesclosed_recording']):
        out += '_eyecl' 
    if int(expInfo['artifact_recording']):
        out += '_artfrec'
    return out
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'resting_task_v2026'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'gender': 'f',
    'date_of_birth': 'DD.MM.YYYY',
    'ethnicity': 'asian',
    'diagnosis': 'control',
    'artifact_recording': '1',
    'eyesclosed_recording': '1',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, add_info(expInfo), expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='E:\\Christopher\\ownCloud_MPI_GWDG\\Side_Projects\\Resting_Paradigm\\resting_task_v2026.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome_screen" ---
    # Run 'Begin Experiment' code from welcome_screen_code
    # Change this instruction according to your setup!
    continue_button = 'space'
    continue_with_button_text = 'Weiter mit der Leertaste...'
    welcome_screen_text = visual.TextStim(win=win, name='welcome_screen_text',
        text='Herzlich Willkommen und vielen Dank für Ihre Teilnahme an diesem Experiment!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_screen_cwb_text = visual.TextStim(win=win, name='welcome_screen_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    welcome_screen_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "artifact_instruction" ---
    artifact_instruction_text = visual.TextStim(win=win, name='artifact_instruction_text',
        text='Zu Beginn der Messung würden wir Sie bitten ein paar Störquellen aufzunehmen. Diese Aufnahmen helfen uns später Störungen aus dem Signal zu entfernen.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    artifact_instruction_cwb_text = visual.TextStim(win=win, name='artifact_instruction_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    artifact_instruction_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "artifact_explainer" ---
    # Run 'Begin Experiment' code from artifact_explainer_code
    artifact_running = False
    artifact_explainer_textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
         size=(1.1, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='artifact_explainer_textbox',
         depth=-1, autoLog=True,
    )
    artifact_explainer_cwb_text = visual.TextStim(win=win, name='artifact_explainer_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    artifact_explainer_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "countdown" ---
    # Run 'Begin Experiment' code from countdown_code
    # count down from x (each number lasts 1 second)
    countdown_from = 3
    countdown_time = 1.0
    countdown_text = visual.TextStim(win=win, name='countdown_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "artifact_recording" ---
    artifact_recording_text = visual.TextStim(win=win, name='artifact_recording_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "short_blank" ---
    short_blank_text = visual.TextStim(win=win, name='short_blank_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "eyesopen_instruction" ---
    eyesopen_instruction_textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
         size=(1.1, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='eyesopen_instruction_textbox',
         depth=-1, autoLog=True,
    )
    eyesopen_instruction_cwb_text = visual.TextStim(win=win, name='eyesopen_instruction_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    eyesopen_instruction_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "countdown" ---
    # Run 'Begin Experiment' code from countdown_code
    # count down from x (each number lasts 1 second)
    countdown_from = 3
    countdown_time = 1.0
    countdown_text = visual.TextStim(win=win, name='countdown_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "eyesopen_recording" ---
    # Run 'Begin Experiment' code from eyesopen_recording_code
    # Duration of Eyes open resting measure in seconds
    eyesopen_duration = 300 # 300 s = 5 min
    eyesopen_recording_polygon = visual.ShapeStim(
        win=win, name='eyesopen_recording_polygon', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    eyesopen_recording_skip_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "short_blank" ---
    short_blank_text = visual.TextStim(win=win, name='short_blank_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "eyesclosed_instruction" ---
    # Run 'Begin Experiment' code from eyesclosed_instruction_code
    eyesclosed_running = False
    eyesclosed_instruction_textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
         size=(1.1, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='eyesclosed_instruction_textbox',
         depth=-1, autoLog=True,
    )
    eyesclosed_instruction_cwb_text = visual.TextStim(win=win, name='eyesclosed_instruction_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    eyesclosed_instruction_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "countdown" ---
    # Run 'Begin Experiment' code from countdown_code
    # count down from x (each number lasts 1 second)
    countdown_from = 3
    countdown_time = 1.0
    countdown_text = visual.TextStim(win=win, name='countdown_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "eyesclosed_recording" ---
    # Run 'Begin Experiment' code from eyesclosed_recording_code
    # Duration of Eyes closed resting measure in seconds
    eyesclosed_duration = 300 # 300 s = 5 min
    eyesclosed_recording_polygon = visual.ShapeStim(
        win=win, name='eyesclosed_recording_polygon', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    # set audio backend
    sound.Sound.backend = 'ptb'
    eyesclosed_recording_start_sound = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='eyesclosed_recording_start_sound'
    )
    eyesclosed_recording_start_sound.setVolume(0.2)
    eyesclosed_recording_stop_sound = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='eyesclosed_recording_stop_sound'
    )
    eyesclosed_recording_stop_sound.setVolume(0.2)
    eyesclosed_recording_skip_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "short_blank" ---
    short_blank_text = visual.TextStim(win=win, name='short_blank_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "goodbye_screen" ---
    goodbye_screen_text = visual.TextStim(win=win, name='goodbye_screen_text',
        text='Das war´s auch schon...\n\nVielen Dank für Ihre Teilnahme!\n\nBitte warten sie auf weitere Anweisungen der Versuchsleitung.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    goodbye_screen_cwb_text = visual.TextStim(win=win, name='goodbye_screen_cwb_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    goodbye_screen_keyboard = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome_screen" ---
    # create an object to store info about Routine welcome_screen
    welcome_screen = data.Routine(
        name='welcome_screen',
        components=[welcome_screen_text, welcome_screen_cwb_text, welcome_screen_keyboard],
    )
    welcome_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    welcome_screen_cwb_text.setText(continue_with_button_text)
    # create starting attributes for welcome_screen_keyboard
    welcome_screen_keyboard.keys = []
    welcome_screen_keyboard.rt = []
    _welcome_screen_keyboard_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'continue_button' in globals():
        continue_button = globals()['continue_button']
    # store start times for welcome_screen
    welcome_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome_screen.tStart = globalClock.getTime(format='float')
    welcome_screen.status = STARTED
    thisExp.addData('welcome_screen.started', welcome_screen.tStart)
    welcome_screen.maxDuration = None
    # keep track of which components have finished
    welcome_screenComponents = welcome_screen.components
    for thisComponent in welcome_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome_screen" ---
    thisExp.currentRoutine = welcome_screen
    welcome_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_screen_text* updates
        
        # if welcome_screen_text is starting this frame...
        if welcome_screen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_screen_text.frameNStart = frameN  # exact frame index
            welcome_screen_text.tStart = t  # local t and not account for scr refresh
            welcome_screen_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_screen_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_screen_text.started')
            # update status
            welcome_screen_text.status = STARTED
            welcome_screen_text.setAutoDraw(True)
        
        # if welcome_screen_text is active this frame...
        if welcome_screen_text.status == STARTED:
            # update params
            pass
        
        # *welcome_screen_cwb_text* updates
        
        # if welcome_screen_cwb_text is starting this frame...
        if welcome_screen_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_screen_cwb_text.frameNStart = frameN  # exact frame index
            welcome_screen_cwb_text.tStart = t  # local t and not account for scr refresh
            welcome_screen_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_screen_cwb_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_screen_cwb_text.started')
            # update status
            welcome_screen_cwb_text.status = STARTED
            welcome_screen_cwb_text.setAutoDraw(True)
        
        # if welcome_screen_cwb_text is active this frame...
        if welcome_screen_cwb_text.status == STARTED:
            # update params
            pass
        
        # *welcome_screen_keyboard* updates
        waitOnFlip = False
        
        # if welcome_screen_keyboard is starting this frame...
        if welcome_screen_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_screen_keyboard.frameNStart = frameN  # exact frame index
            welcome_screen_keyboard.tStart = t  # local t and not account for scr refresh
            welcome_screen_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_screen_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_screen_keyboard.started')
            # update status
            welcome_screen_keyboard.status = STARTED
            # allowed keys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    continue_button = str(continue_button)
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_screen_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_screen_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_screen_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = welcome_screen_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
            _welcome_screen_keyboard_allKeys.extend(theseKeys)
            if len(_welcome_screen_keyboard_allKeys):
                welcome_screen_keyboard.keys = _welcome_screen_keyboard_allKeys[-1].name  # just the last key pressed
                welcome_screen_keyboard.rt = _welcome_screen_keyboard_allKeys[-1].rt
                welcome_screen_keyboard.duration = _welcome_screen_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcome_screen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            welcome_screen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if welcome_screen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in welcome_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome_screen" ---
    for thisComponent in welcome_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome_screen
    welcome_screen.tStop = globalClock.getTime(format='float')
    welcome_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome_screen.stopped', welcome_screen.tStop)
    # check responses
    if welcome_screen_keyboard.keys in ['', [], None]:  # No response was made
        welcome_screen_keyboard.keys = None
    thisExp.addData('welcome_screen_keyboard.keys',welcome_screen_keyboard.keys)
    if welcome_screen_keyboard.keys != None:  # we had a response
        thisExp.addData('welcome_screen_keyboard.rt', welcome_screen_keyboard.rt)
        thisExp.addData('welcome_screen_keyboard.duration', welcome_screen_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "artifact_instruction" ---
    # create an object to store info about Routine artifact_instruction
    artifact_instruction = data.Routine(
        name='artifact_instruction',
        components=[artifact_instruction_text, artifact_instruction_cwb_text, artifact_instruction_keyboard],
    )
    artifact_instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from artifact_instruction_code
    if not int(expInfo['artifact_recording']):
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    artifact_instruction_cwb_text.setText(continue_with_button_text)
    # create starting attributes for artifact_instruction_keyboard
    artifact_instruction_keyboard.keys = []
    artifact_instruction_keyboard.rt = []
    _artifact_instruction_keyboard_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'continue_button' in globals():
        continue_button = globals()['continue_button']
    # store start times for artifact_instruction
    artifact_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    artifact_instruction.tStart = globalClock.getTime(format='float')
    artifact_instruction.status = STARTED
    thisExp.addData('artifact_instruction.started', artifact_instruction.tStart)
    artifact_instruction.maxDuration = None
    # keep track of which components have finished
    artifact_instructionComponents = artifact_instruction.components
    for thisComponent in artifact_instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "artifact_instruction" ---
    thisExp.currentRoutine = artifact_instruction
    artifact_instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *artifact_instruction_text* updates
        
        # if artifact_instruction_text is starting this frame...
        if artifact_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_instruction_text.frameNStart = frameN  # exact frame index
            artifact_instruction_text.tStart = t  # local t and not account for scr refresh
            artifact_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'artifact_instruction_text.started')
            # update status
            artifact_instruction_text.status = STARTED
            artifact_instruction_text.setAutoDraw(True)
        
        # if artifact_instruction_text is active this frame...
        if artifact_instruction_text.status == STARTED:
            # update params
            pass
        
        # *artifact_instruction_cwb_text* updates
        
        # if artifact_instruction_cwb_text is starting this frame...
        if artifact_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_instruction_cwb_text.frameNStart = frameN  # exact frame index
            artifact_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
            artifact_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'artifact_instruction_cwb_text.started')
            # update status
            artifact_instruction_cwb_text.status = STARTED
            artifact_instruction_cwb_text.setAutoDraw(True)
        
        # if artifact_instruction_cwb_text is active this frame...
        if artifact_instruction_cwb_text.status == STARTED:
            # update params
            pass
        
        # *artifact_instruction_keyboard* updates
        waitOnFlip = False
        
        # if artifact_instruction_keyboard is starting this frame...
        if artifact_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            artifact_instruction_keyboard.frameNStart = frameN  # exact frame index
            artifact_instruction_keyboard.tStart = t  # local t and not account for scr refresh
            artifact_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(artifact_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'artifact_instruction_keyboard.started')
            # update status
            artifact_instruction_keyboard.status = STARTED
            # allowed keys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    continue_button = str(continue_button)
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(artifact_instruction_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(artifact_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if artifact_instruction_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = artifact_instruction_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
            _artifact_instruction_keyboard_allKeys.extend(theseKeys)
            if len(_artifact_instruction_keyboard_allKeys):
                artifact_instruction_keyboard.keys = _artifact_instruction_keyboard_allKeys[-1].name  # just the last key pressed
                artifact_instruction_keyboard.rt = _artifact_instruction_keyboard_allKeys[-1].rt
                artifact_instruction_keyboard.duration = _artifact_instruction_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=artifact_instruction,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            artifact_instruction.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if artifact_instruction.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in artifact_instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "artifact_instruction" ---
    for thisComponent in artifact_instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for artifact_instruction
    artifact_instruction.tStop = globalClock.getTime(format='float')
    artifact_instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('artifact_instruction.stopped', artifact_instruction.tStop)
    # check responses
    if artifact_instruction_keyboard.keys in ['', [], None]:  # No response was made
        artifact_instruction_keyboard.keys = None
    thisExp.addData('artifact_instruction_keyboard.keys',artifact_instruction_keyboard.keys)
    if artifact_instruction_keyboard.keys != None:  # we had a response
        thisExp.addData('artifact_instruction_keyboard.rt', artifact_instruction_keyboard.rt)
        thisExp.addData('artifact_instruction_keyboard.duration', artifact_instruction_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "artifact_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_artifact_recording = data.TrialHandler2(
        name='loop_artifact_recording',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('instructions/artifact_instruction.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loop_artifact_recording)  # add the loop to the experiment
    thisLoop_artifact_recording = loop_artifact_recording.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_artifact_recording.rgb)
    if thisLoop_artifact_recording != None:
        for paramName in thisLoop_artifact_recording:
            globals()[paramName] = thisLoop_artifact_recording[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_artifact_recording in loop_artifact_recording:
        loop_artifact_recording.status = STARTED
        if hasattr(thisLoop_artifact_recording, 'status'):
            thisLoop_artifact_recording.status = STARTED
        currentLoop = loop_artifact_recording
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_artifact_recording.rgb)
        if thisLoop_artifact_recording != None:
            for paramName in thisLoop_artifact_recording:
                globals()[paramName] = thisLoop_artifact_recording[paramName]
        
        # --- Prepare to start Routine "artifact_explainer" ---
        # create an object to store info about Routine artifact_explainer
        artifact_explainer = data.Routine(
            name='artifact_explainer',
            components=[artifact_explainer_textbox, artifact_explainer_cwb_text, artifact_explainer_keyboard],
        )
        artifact_explainer.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from artifact_explainer_code
        artifact_running = True
        if not int(expInfo['artifact_recording']):
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        artifact_explainer_textbox.reset()
        artifact_explainer_textbox.setText(text)
        artifact_explainer_cwb_text.setText(continue_with_button_text)
        # create starting attributes for artifact_explainer_keyboard
        artifact_explainer_keyboard.keys = []
        artifact_explainer_keyboard.rt = []
        _artifact_explainer_keyboard_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'continue_button' in globals():
            continue_button = globals()['continue_button']
        # store start times for artifact_explainer
        artifact_explainer.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        artifact_explainer.tStart = globalClock.getTime(format='float')
        artifact_explainer.status = STARTED
        thisExp.addData('artifact_explainer.started', artifact_explainer.tStart)
        artifact_explainer.maxDuration = None
        # keep track of which components have finished
        artifact_explainerComponents = artifact_explainer.components
        for thisComponent in artifact_explainer.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "artifact_explainer" ---
        thisExp.currentRoutine = artifact_explainer
        artifact_explainer.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_artifact_recording, 'status') and thisLoop_artifact_recording.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *artifact_explainer_textbox* updates
            
            # if artifact_explainer_textbox is starting this frame...
            if artifact_explainer_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                artifact_explainer_textbox.frameNStart = frameN  # exact frame index
                artifact_explainer_textbox.tStart = t  # local t and not account for scr refresh
                artifact_explainer_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(artifact_explainer_textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'artifact_explainer_textbox.started')
                # update status
                artifact_explainer_textbox.status = STARTED
                artifact_explainer_textbox.setAutoDraw(True)
            
            # if artifact_explainer_textbox is active this frame...
            if artifact_explainer_textbox.status == STARTED:
                # update params
                pass
            
            # *artifact_explainer_cwb_text* updates
            
            # if artifact_explainer_cwb_text is starting this frame...
            if artifact_explainer_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                artifact_explainer_cwb_text.frameNStart = frameN  # exact frame index
                artifact_explainer_cwb_text.tStart = t  # local t and not account for scr refresh
                artifact_explainer_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(artifact_explainer_cwb_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'artifact_explainer_cwb_text.started')
                # update status
                artifact_explainer_cwb_text.status = STARTED
                artifact_explainer_cwb_text.setAutoDraw(True)
            
            # if artifact_explainer_cwb_text is active this frame...
            if artifact_explainer_cwb_text.status == STARTED:
                # update params
                pass
            
            # *artifact_explainer_keyboard* updates
            waitOnFlip = False
            
            # if artifact_explainer_keyboard is starting this frame...
            if artifact_explainer_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                artifact_explainer_keyboard.frameNStart = frameN  # exact frame index
                artifact_explainer_keyboard.tStart = t  # local t and not account for scr refresh
                artifact_explainer_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(artifact_explainer_keyboard, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'artifact_explainer_keyboard.started')
                # update status
                artifact_explainer_keyboard.status = STARTED
                # allowed keys looks like a variable named `continue_button`
                if not type(continue_button) in [list, tuple, np.ndarray]:
                    if not isinstance(continue_button, str):
                        continue_button = str(continue_button)
                    elif not ',' in continue_button:
                        continue_button = (continue_button,)
                    else:
                        continue_button = eval(continue_button)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(artifact_explainer_keyboard.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(artifact_explainer_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if artifact_explainer_keyboard.status == STARTED and not waitOnFlip:
                theseKeys = artifact_explainer_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
                _artifact_explainer_keyboard_allKeys.extend(theseKeys)
                if len(_artifact_explainer_keyboard_allKeys):
                    artifact_explainer_keyboard.keys = _artifact_explainer_keyboard_allKeys[-1].name  # just the last key pressed
                    artifact_explainer_keyboard.rt = _artifact_explainer_keyboard_allKeys[-1].rt
                    artifact_explainer_keyboard.duration = _artifact_explainer_keyboard_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=artifact_explainer,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                artifact_explainer.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if artifact_explainer.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in artifact_explainer.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "artifact_explainer" ---
        for thisComponent in artifact_explainer.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for artifact_explainer
        artifact_explainer.tStop = globalClock.getTime(format='float')
        artifact_explainer.tStopRefresh = tThisFlipGlobal
        thisExp.addData('artifact_explainer.stopped', artifact_explainer.tStop)
        # check responses
        if artifact_explainer_keyboard.keys in ['', [], None]:  # No response was made
            artifact_explainer_keyboard.keys = None
        loop_artifact_recording.addData('artifact_explainer_keyboard.keys',artifact_explainer_keyboard.keys)
        if artifact_explainer_keyboard.keys != None:  # we had a response
            loop_artifact_recording.addData('artifact_explainer_keyboard.rt', artifact_explainer_keyboard.rt)
            loop_artifact_recording.addData('artifact_explainer_keyboard.duration', artifact_explainer_keyboard.duration)
        # the Routine "artifact_explainer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "countdown" ---
        # create an object to store info about Routine countdown
        countdown = data.Routine(
            name='countdown',
            components=[countdown_text],
        )
        countdown.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from countdown_code
        if (not int(expInfo['artifact_recording'])) and artifact_running:
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        
        if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        
        countdown_counter = countdown_from
        add_time = countdown_time
        # store start times for countdown
        countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        countdown.tStart = globalClock.getTime(format='float')
        countdown.status = STARTED
        thisExp.addData('countdown.started', countdown.tStart)
        countdown.maxDuration = None
        # keep track of which components have finished
        countdownComponents = countdown.components
        for thisComponent in countdown.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "countdown" ---
        thisExp.currentRoutine = countdown
        countdown.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_artifact_recording, 'status') and thisLoop_artifact_recording.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from countdown_code
            if (t >= add_time - frameTolerance):
                countdown_counter -= 1
                add_time += countdown_time
            
            # *countdown_text* updates
            
            # if countdown_text is starting this frame...
            if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                countdown_text.frameNStart = frameN  # exact frame index
                countdown_text.tStart = t  # local t and not account for scr refresh
                countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countdown_text.started')
                # update status
                countdown_text.status = STARTED
                countdown_text.setAutoDraw(True)
            
            # if countdown_text is active this frame...
            if countdown_text.status == STARTED:
                # update params
                countdown_text.setText(countdown_counter, log=False)
            
            # if countdown_text is stopping this frame...
            if countdown_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
                    # keep track of stop time/frame for later
                    countdown_text.tStop = t  # not accounting for scr refresh
                    countdown_text.tStopRefresh = tThisFlipGlobal  # on global time
                    countdown_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'countdown_text.stopped')
                    # update status
                    countdown_text.status = FINISHED
                    countdown_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=countdown,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                countdown.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if countdown.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in countdown.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "countdown" ---
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for countdown
        countdown.tStop = globalClock.getTime(format='float')
        countdown.tStopRefresh = tThisFlipGlobal
        thisExp.addData('countdown.stopped', countdown.tStop)
        # the Routine "countdown" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "artifact_recording" ---
        # create an object to store info about Routine artifact_recording
        artifact_recording = data.Routine(
            name='artifact_recording',
            components=[artifact_recording_text],
        )
        artifact_recording.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from artifact_recording_code
        if not int(expInfo['artifact_recording']):
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        artifact_recording_text.setText(short)
        # store start times for artifact_recording
        artifact_recording.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        artifact_recording.tStart = globalClock.getTime(format='float')
        artifact_recording.status = STARTED
        thisExp.addData('artifact_recording.started', artifact_recording.tStart)
        artifact_recording.maxDuration = None
        # keep track of which components have finished
        artifact_recordingComponents = artifact_recording.components
        for thisComponent in artifact_recording.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "artifact_recording" ---
        thisExp.currentRoutine = artifact_recording
        artifact_recording.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_artifact_recording, 'status') and thisLoop_artifact_recording.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *artifact_recording_text* updates
            
            # if artifact_recording_text is starting this frame...
            if artifact_recording_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                artifact_recording_text.frameNStart = frameN  # exact frame index
                artifact_recording_text.tStart = t  # local t and not account for scr refresh
                artifact_recording_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(artifact_recording_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'artifact_recording_text.started')
                # update status
                artifact_recording_text.status = STARTED
                artifact_recording_text.setAutoDraw(True)
            
            # if artifact_recording_text is active this frame...
            if artifact_recording_text.status == STARTED:
                # update params
                pass
            
            # if artifact_recording_text is stopping this frame...
            if artifact_recording_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > artifact_recording_text.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    artifact_recording_text.tStop = t  # not accounting for scr refresh
                    artifact_recording_text.tStopRefresh = tThisFlipGlobal  # on global time
                    artifact_recording_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'artifact_recording_text.stopped')
                    # update status
                    artifact_recording_text.status = FINISHED
                    artifact_recording_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=artifact_recording,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                artifact_recording.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if artifact_recording.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in artifact_recording.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "artifact_recording" ---
        for thisComponent in artifact_recording.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for artifact_recording
        artifact_recording.tStop = globalClock.getTime(format='float')
        artifact_recording.tStopRefresh = tThisFlipGlobal
        thisExp.addData('artifact_recording.stopped', artifact_recording.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if artifact_recording.maxDurationReached:
            routineTimer.addTime(-artifact_recording.maxDuration)
        elif artifact_recording.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "short_blank" ---
        # create an object to store info about Routine short_blank
        short_blank = data.Routine(
            name='short_blank',
            components=[short_blank_text],
        )
        short_blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from short_blank_code
        if (not int(expInfo['artifact_recording'])) and artifact_running:
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        
        if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        
        artifact_running = False
        eyesclosed_running = False
        # store start times for short_blank
        short_blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        short_blank.tStart = globalClock.getTime(format='float')
        short_blank.status = STARTED
        thisExp.addData('short_blank.started', short_blank.tStart)
        short_blank.maxDuration = None
        # keep track of which components have finished
        short_blankComponents = short_blank.components
        for thisComponent in short_blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "short_blank" ---
        thisExp.currentRoutine = short_blank
        short_blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_artifact_recording, 'status') and thisLoop_artifact_recording.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *short_blank_text* updates
            
            # if short_blank_text is starting this frame...
            if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                short_blank_text.frameNStart = frameN  # exact frame index
                short_blank_text.tStart = t  # local t and not account for scr refresh
                short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'short_blank_text.started')
                # update status
                short_blank_text.status = STARTED
                short_blank_text.setAutoDraw(True)
            
            # if short_blank_text is active this frame...
            if short_blank_text.status == STARTED:
                # update params
                pass
            
            # if short_blank_text is stopping this frame...
            if short_blank_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    short_blank_text.tStop = t  # not accounting for scr refresh
                    short_blank_text.tStopRefresh = tThisFlipGlobal  # on global time
                    short_blank_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'short_blank_text.stopped')
                    # update status
                    short_blank_text.status = FINISHED
                    short_blank_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=short_blank,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                short_blank.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if short_blank.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in short_blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "short_blank" ---
        for thisComponent in short_blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for short_blank
        short_blank.tStop = globalClock.getTime(format='float')
        short_blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('short_blank.stopped', short_blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if short_blank.maxDurationReached:
            routineTimer.addTime(-short_blank.maxDuration)
        elif short_blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisLoop_artifact_recording as finished
        if hasattr(thisLoop_artifact_recording, 'status'):
            thisLoop_artifact_recording.status = FINISHED
        # if awaiting a pause, pause now
        if loop_artifact_recording.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_artifact_recording.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_artifact_recording'
    loop_artifact_recording.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    loop_eyesopen_instruction = data.TrialHandler2(
        name='loop_eyesopen_instruction',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('instructions/eyesopen_instruction.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loop_eyesopen_instruction)  # add the loop to the experiment
    thisLoop_eyesopen_instruction = loop_eyesopen_instruction.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesopen_instruction.rgb)
    if thisLoop_eyesopen_instruction != None:
        for paramName in thisLoop_eyesopen_instruction:
            globals()[paramName] = thisLoop_eyesopen_instruction[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_eyesopen_instruction in loop_eyesopen_instruction:
        loop_eyesopen_instruction.status = STARTED
        if hasattr(thisLoop_eyesopen_instruction, 'status'):
            thisLoop_eyesopen_instruction.status = STARTED
        currentLoop = loop_eyesopen_instruction
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesopen_instruction.rgb)
        if thisLoop_eyesopen_instruction != None:
            for paramName in thisLoop_eyesopen_instruction:
                globals()[paramName] = thisLoop_eyesopen_instruction[paramName]
        
        # --- Prepare to start Routine "eyesopen_instruction" ---
        # create an object to store info about Routine eyesopen_instruction
        eyesopen_instruction = data.Routine(
            name='eyesopen_instruction',
            components=[eyesopen_instruction_textbox, eyesopen_instruction_cwb_text, eyesopen_instruction_keyboard],
        )
        eyesopen_instruction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        eyesopen_instruction_textbox.reset()
        eyesopen_instruction_textbox.setText(text)
        eyesopen_instruction_cwb_text.setText(continue_with_button_text)
        # create starting attributes for eyesopen_instruction_keyboard
        eyesopen_instruction_keyboard.keys = []
        eyesopen_instruction_keyboard.rt = []
        _eyesopen_instruction_keyboard_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'continue_button' in globals():
            continue_button = globals()['continue_button']
        # store start times for eyesopen_instruction
        eyesopen_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        eyesopen_instruction.tStart = globalClock.getTime(format='float')
        eyesopen_instruction.status = STARTED
        thisExp.addData('eyesopen_instruction.started', eyesopen_instruction.tStart)
        eyesopen_instruction.maxDuration = None
        # keep track of which components have finished
        eyesopen_instructionComponents = eyesopen_instruction.components
        for thisComponent in eyesopen_instruction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "eyesopen_instruction" ---
        thisExp.currentRoutine = eyesopen_instruction
        eyesopen_instruction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_eyesopen_instruction, 'status') and thisLoop_eyesopen_instruction.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *eyesopen_instruction_textbox* updates
            
            # if eyesopen_instruction_textbox is starting this frame...
            if eyesopen_instruction_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesopen_instruction_textbox.frameNStart = frameN  # exact frame index
                eyesopen_instruction_textbox.tStart = t  # local t and not account for scr refresh
                eyesopen_instruction_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesopen_instruction_textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesopen_instruction_textbox.started')
                # update status
                eyesopen_instruction_textbox.status = STARTED
                eyesopen_instruction_textbox.setAutoDraw(True)
            
            # if eyesopen_instruction_textbox is active this frame...
            if eyesopen_instruction_textbox.status == STARTED:
                # update params
                pass
            
            # *eyesopen_instruction_cwb_text* updates
            
            # if eyesopen_instruction_cwb_text is starting this frame...
            if eyesopen_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesopen_instruction_cwb_text.frameNStart = frameN  # exact frame index
                eyesopen_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
                eyesopen_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesopen_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesopen_instruction_cwb_text.started')
                # update status
                eyesopen_instruction_cwb_text.status = STARTED
                eyesopen_instruction_cwb_text.setAutoDraw(True)
            
            # if eyesopen_instruction_cwb_text is active this frame...
            if eyesopen_instruction_cwb_text.status == STARTED:
                # update params
                pass
            
            # *eyesopen_instruction_keyboard* updates
            waitOnFlip = False
            
            # if eyesopen_instruction_keyboard is starting this frame...
            if eyesopen_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesopen_instruction_keyboard.frameNStart = frameN  # exact frame index
                eyesopen_instruction_keyboard.tStart = t  # local t and not account for scr refresh
                eyesopen_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesopen_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesopen_instruction_keyboard.started')
                # update status
                eyesopen_instruction_keyboard.status = STARTED
                # allowed keys looks like a variable named `continue_button`
                if not type(continue_button) in [list, tuple, np.ndarray]:
                    if not isinstance(continue_button, str):
                        continue_button = str(continue_button)
                    elif not ',' in continue_button:
                        continue_button = (continue_button,)
                    else:
                        continue_button = eval(continue_button)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(eyesopen_instruction_keyboard.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(eyesopen_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if eyesopen_instruction_keyboard.status == STARTED and not waitOnFlip:
                theseKeys = eyesopen_instruction_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
                _eyesopen_instruction_keyboard_allKeys.extend(theseKeys)
                if len(_eyesopen_instruction_keyboard_allKeys):
                    eyesopen_instruction_keyboard.keys = _eyesopen_instruction_keyboard_allKeys[-1].name  # just the last key pressed
                    eyesopen_instruction_keyboard.rt = _eyesopen_instruction_keyboard_allKeys[-1].rt
                    eyesopen_instruction_keyboard.duration = _eyesopen_instruction_keyboard_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=eyesopen_instruction,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                eyesopen_instruction.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if eyesopen_instruction.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in eyesopen_instruction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "eyesopen_instruction" ---
        for thisComponent in eyesopen_instruction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for eyesopen_instruction
        eyesopen_instruction.tStop = globalClock.getTime(format='float')
        eyesopen_instruction.tStopRefresh = tThisFlipGlobal
        thisExp.addData('eyesopen_instruction.stopped', eyesopen_instruction.tStop)
        # check responses
        if eyesopen_instruction_keyboard.keys in ['', [], None]:  # No response was made
            eyesopen_instruction_keyboard.keys = None
        loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.keys',eyesopen_instruction_keyboard.keys)
        if eyesopen_instruction_keyboard.keys != None:  # we had a response
            loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.rt', eyesopen_instruction_keyboard.rt)
            loop_eyesopen_instruction.addData('eyesopen_instruction_keyboard.duration', eyesopen_instruction_keyboard.duration)
        # the Routine "eyesopen_instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLoop_eyesopen_instruction as finished
        if hasattr(thisLoop_eyesopen_instruction, 'status'):
            thisLoop_eyesopen_instruction.status = FINISHED
        # if awaiting a pause, pause now
        if loop_eyesopen_instruction.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_eyesopen_instruction.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_eyesopen_instruction'
    loop_eyesopen_instruction.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[countdown_text],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    countdown_counter = countdown_from
    add_time = countdown_time
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    thisExp.addData('countdown.started', countdown.tStart)
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countdown" ---
    thisExp.currentRoutine = countdown
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from countdown_code
        if (t >= add_time - frameTolerance):
            countdown_counter -= 1
            add_time += countdown_time
        
        # *countdown_text* updates
        
        # if countdown_text is starting this frame...
        if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_text.frameNStart = frameN  # exact frame index
            countdown_text.tStart = t  # local t and not account for scr refresh
            countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'countdown_text.started')
            # update status
            countdown_text.status = STARTED
            countdown_text.setAutoDraw(True)
        
        # if countdown_text is active this frame...
        if countdown_text.status == STARTED:
            # update params
            countdown_text.setText(countdown_counter, log=False)
        
        # if countdown_text is stopping this frame...
        if countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
                # keep track of stop time/frame for later
                countdown_text.tStop = t  # not accounting for scr refresh
                countdown_text.tStopRefresh = tThisFlipGlobal  # on global time
                countdown_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countdown_text.stopped')
                # update status
                countdown_text.status = FINISHED
                countdown_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=countdown,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            countdown.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if countdown.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    thisExp.addData('countdown.stopped', countdown.tStop)
    thisExp.nextEntry()
    # the Routine "countdown" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "eyesopen_recording" ---
    # create an object to store info about Routine eyesopen_recording
    eyesopen_recording = data.Routine(
        name='eyesopen_recording',
        components=[eyesopen_recording_polygon, eyesopen_recording_skip_keyboard],
    )
    eyesopen_recording.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for eyesopen_recording_skip_keyboard
    eyesopen_recording_skip_keyboard.keys = []
    eyesopen_recording_skip_keyboard.rt = []
    _eyesopen_recording_skip_keyboard_allKeys = []
    # store start times for eyesopen_recording
    eyesopen_recording.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyesopen_recording.tStart = globalClock.getTime(format='float')
    eyesopen_recording.status = STARTED
    thisExp.addData('eyesopen_recording.started', eyesopen_recording.tStart)
    eyesopen_recording.maxDuration = None
    # keep track of which components have finished
    eyesopen_recordingComponents = eyesopen_recording.components
    for thisComponent in eyesopen_recording.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eyesopen_recording" ---
    thisExp.currentRoutine = eyesopen_recording
    eyesopen_recording.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *eyesopen_recording_polygon* updates
        
        # if eyesopen_recording_polygon is starting this frame...
        if eyesopen_recording_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesopen_recording_polygon.frameNStart = frameN  # exact frame index
            eyesopen_recording_polygon.tStart = t  # local t and not account for scr refresh
            eyesopen_recording_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesopen_recording_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eyesopen_recording_polygon.started')
            # update status
            eyesopen_recording_polygon.status = STARTED
            eyesopen_recording_polygon.setAutoDraw(True)
        
        # if eyesopen_recording_polygon is active this frame...
        if eyesopen_recording_polygon.status == STARTED:
            # update params
            pass
        
        # if eyesopen_recording_polygon is stopping this frame...
        if eyesopen_recording_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesopen_recording_polygon.tStartRefresh + eyesopen_duration-frameTolerance:
                # keep track of stop time/frame for later
                eyesopen_recording_polygon.tStop = t  # not accounting for scr refresh
                eyesopen_recording_polygon.tStopRefresh = tThisFlipGlobal  # on global time
                eyesopen_recording_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesopen_recording_polygon.stopped')
                # update status
                eyesopen_recording_polygon.status = FINISHED
                eyesopen_recording_polygon.setAutoDraw(False)
        
        # *eyesopen_recording_skip_keyboard* updates
        waitOnFlip = False
        
        # if eyesopen_recording_skip_keyboard is starting this frame...
        if eyesopen_recording_skip_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesopen_recording_skip_keyboard.frameNStart = frameN  # exact frame index
            eyesopen_recording_skip_keyboard.tStart = t  # local t and not account for scr refresh
            eyesopen_recording_skip_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesopen_recording_skip_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eyesopen_recording_skip_keyboard.started')
            # update status
            eyesopen_recording_skip_keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(eyesopen_recording_skip_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(eyesopen_recording_skip_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if eyesopen_recording_skip_keyboard is stopping this frame...
        if eyesopen_recording_skip_keyboard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesopen_recording_skip_keyboard.tStartRefresh + eyesclosed_duration-frameTolerance:
                # keep track of stop time/frame for later
                eyesopen_recording_skip_keyboard.tStop = t  # not accounting for scr refresh
                eyesopen_recording_skip_keyboard.tStopRefresh = tThisFlipGlobal  # on global time
                eyesopen_recording_skip_keyboard.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesopen_recording_skip_keyboard.stopped')
                # update status
                eyesopen_recording_skip_keyboard.status = FINISHED
                eyesopen_recording_skip_keyboard.status = FINISHED
        if eyesopen_recording_skip_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = eyesopen_recording_skip_keyboard.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
            _eyesopen_recording_skip_keyboard_allKeys.extend(theseKeys)
            if len(_eyesopen_recording_skip_keyboard_allKeys):
                eyesopen_recording_skip_keyboard.keys = _eyesopen_recording_skip_keyboard_allKeys[-1].name  # just the last key pressed
                eyesopen_recording_skip_keyboard.rt = _eyesopen_recording_skip_keyboard_allKeys[-1].rt
                eyesopen_recording_skip_keyboard.duration = _eyesopen_recording_skip_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=eyesopen_recording,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            eyesopen_recording.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if eyesopen_recording.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in eyesopen_recording.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyesopen_recording" ---
    for thisComponent in eyesopen_recording.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyesopen_recording
    eyesopen_recording.tStop = globalClock.getTime(format='float')
    eyesopen_recording.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyesopen_recording.stopped', eyesopen_recording.tStop)
    # check responses
    if eyesopen_recording_skip_keyboard.keys in ['', [], None]:  # No response was made
        eyesopen_recording_skip_keyboard.keys = None
    thisExp.addData('eyesopen_recording_skip_keyboard.keys',eyesopen_recording_skip_keyboard.keys)
    if eyesopen_recording_skip_keyboard.keys != None:  # we had a response
        thisExp.addData('eyesopen_recording_skip_keyboard.rt', eyesopen_recording_skip_keyboard.rt)
        thisExp.addData('eyesopen_recording_skip_keyboard.duration', eyesopen_recording_skip_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "eyesopen_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "short_blank" ---
    # create an object to store info about Routine short_blank
    short_blank = data.Routine(
        name='short_blank',
        components=[short_blank_text],
    )
    short_blank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from short_blank_code
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    artifact_running = False
    eyesclosed_running = False
    # store start times for short_blank
    short_blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    short_blank.tStart = globalClock.getTime(format='float')
    short_blank.status = STARTED
    thisExp.addData('short_blank.started', short_blank.tStart)
    short_blank.maxDuration = None
    # keep track of which components have finished
    short_blankComponents = short_blank.components
    for thisComponent in short_blank.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "short_blank" ---
    thisExp.currentRoutine = short_blank
    short_blank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *short_blank_text* updates
        
        # if short_blank_text is starting this frame...
        if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_blank_text.frameNStart = frameN  # exact frame index
            short_blank_text.tStart = t  # local t and not account for scr refresh
            short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_blank_text.started')
            # update status
            short_blank_text.status = STARTED
            short_blank_text.setAutoDraw(True)
        
        # if short_blank_text is active this frame...
        if short_blank_text.status == STARTED:
            # update params
            pass
        
        # if short_blank_text is stopping this frame...
        if short_blank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                short_blank_text.tStop = t  # not accounting for scr refresh
                short_blank_text.tStopRefresh = tThisFlipGlobal  # on global time
                short_blank_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'short_blank_text.stopped')
                # update status
                short_blank_text.status = FINISHED
                short_blank_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=short_blank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            short_blank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if short_blank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in short_blank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "short_blank" ---
    for thisComponent in short_blank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for short_blank
    short_blank.tStop = globalClock.getTime(format='float')
    short_blank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('short_blank.stopped', short_blank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if short_blank.maxDurationReached:
        routineTimer.addTime(-short_blank.maxDuration)
    elif short_blank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    loop_eyesclosed_instruction = data.TrialHandler2(
        name='loop_eyesclosed_instruction',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('instructions/eyesclosed_instruction.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loop_eyesclosed_instruction)  # add the loop to the experiment
    thisLoop_eyesclosed_instruction = loop_eyesclosed_instruction.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesclosed_instruction.rgb)
    if thisLoop_eyesclosed_instruction != None:
        for paramName in thisLoop_eyesclosed_instruction:
            globals()[paramName] = thisLoop_eyesclosed_instruction[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_eyesclosed_instruction in loop_eyesclosed_instruction:
        loop_eyesclosed_instruction.status = STARTED
        if hasattr(thisLoop_eyesclosed_instruction, 'status'):
            thisLoop_eyesclosed_instruction.status = STARTED
        currentLoop = loop_eyesclosed_instruction
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_eyesclosed_instruction.rgb)
        if thisLoop_eyesclosed_instruction != None:
            for paramName in thisLoop_eyesclosed_instruction:
                globals()[paramName] = thisLoop_eyesclosed_instruction[paramName]
        
        # --- Prepare to start Routine "eyesclosed_instruction" ---
        # create an object to store info about Routine eyesclosed_instruction
        eyesclosed_instruction = data.Routine(
            name='eyesclosed_instruction',
            components=[eyesclosed_instruction_textbox, eyesclosed_instruction_cwb_text, eyesclosed_instruction_keyboard],
        )
        eyesclosed_instruction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from eyesclosed_instruction_code
        eyesclosed_running = True
        if not int(expInfo['eyesclosed_recording']):
            continueRoutine = False
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        eyesclosed_instruction_textbox.reset()
        eyesclosed_instruction_textbox.setText(text)
        eyesclosed_instruction_cwb_text.setText(continue_with_button_text)
        # create starting attributes for eyesclosed_instruction_keyboard
        eyesclosed_instruction_keyboard.keys = []
        eyesclosed_instruction_keyboard.rt = []
        _eyesclosed_instruction_keyboard_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'continue_button' in globals():
            continue_button = globals()['continue_button']
        # store start times for eyesclosed_instruction
        eyesclosed_instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        eyesclosed_instruction.tStart = globalClock.getTime(format='float')
        eyesclosed_instruction.status = STARTED
        thisExp.addData('eyesclosed_instruction.started', eyesclosed_instruction.tStart)
        eyesclosed_instruction.maxDuration = None
        # keep track of which components have finished
        eyesclosed_instructionComponents = eyesclosed_instruction.components
        for thisComponent in eyesclosed_instruction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "eyesclosed_instruction" ---
        thisExp.currentRoutine = eyesclosed_instruction
        eyesclosed_instruction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_eyesclosed_instruction, 'status') and thisLoop_eyesclosed_instruction.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *eyesclosed_instruction_textbox* updates
            
            # if eyesclosed_instruction_textbox is starting this frame...
            if eyesclosed_instruction_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesclosed_instruction_textbox.frameNStart = frameN  # exact frame index
                eyesclosed_instruction_textbox.tStart = t  # local t and not account for scr refresh
                eyesclosed_instruction_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesclosed_instruction_textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_instruction_textbox.started')
                # update status
                eyesclosed_instruction_textbox.status = STARTED
                eyesclosed_instruction_textbox.setAutoDraw(True)
            
            # if eyesclosed_instruction_textbox is active this frame...
            if eyesclosed_instruction_textbox.status == STARTED:
                # update params
                pass
            
            # *eyesclosed_instruction_cwb_text* updates
            
            # if eyesclosed_instruction_cwb_text is starting this frame...
            if eyesclosed_instruction_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesclosed_instruction_cwb_text.frameNStart = frameN  # exact frame index
                eyesclosed_instruction_cwb_text.tStart = t  # local t and not account for scr refresh
                eyesclosed_instruction_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesclosed_instruction_cwb_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_instruction_cwb_text.started')
                # update status
                eyesclosed_instruction_cwb_text.status = STARTED
                eyesclosed_instruction_cwb_text.setAutoDraw(True)
            
            # if eyesclosed_instruction_cwb_text is active this frame...
            if eyesclosed_instruction_cwb_text.status == STARTED:
                # update params
                pass
            
            # *eyesclosed_instruction_keyboard* updates
            waitOnFlip = False
            
            # if eyesclosed_instruction_keyboard is starting this frame...
            if eyesclosed_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eyesclosed_instruction_keyboard.frameNStart = frameN  # exact frame index
                eyesclosed_instruction_keyboard.tStart = t  # local t and not account for scr refresh
                eyesclosed_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eyesclosed_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_instruction_keyboard.started')
                # update status
                eyesclosed_instruction_keyboard.status = STARTED
                # allowed keys looks like a variable named `continue_button`
                if not type(continue_button) in [list, tuple, np.ndarray]:
                    if not isinstance(continue_button, str):
                        continue_button = str(continue_button)
                    elif not ',' in continue_button:
                        continue_button = (continue_button,)
                    else:
                        continue_button = eval(continue_button)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(eyesclosed_instruction_keyboard.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(eyesclosed_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if eyesclosed_instruction_keyboard.status == STARTED and not waitOnFlip:
                theseKeys = eyesclosed_instruction_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
                _eyesclosed_instruction_keyboard_allKeys.extend(theseKeys)
                if len(_eyesclosed_instruction_keyboard_allKeys):
                    eyesclosed_instruction_keyboard.keys = _eyesclosed_instruction_keyboard_allKeys[-1].name  # just the last key pressed
                    eyesclosed_instruction_keyboard.rt = _eyesclosed_instruction_keyboard_allKeys[-1].rt
                    eyesclosed_instruction_keyboard.duration = _eyesclosed_instruction_keyboard_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=eyesclosed_instruction,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                eyesclosed_instruction.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if eyesclosed_instruction.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in eyesclosed_instruction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "eyesclosed_instruction" ---
        for thisComponent in eyesclosed_instruction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for eyesclosed_instruction
        eyesclosed_instruction.tStop = globalClock.getTime(format='float')
        eyesclosed_instruction.tStopRefresh = tThisFlipGlobal
        thisExp.addData('eyesclosed_instruction.stopped', eyesclosed_instruction.tStop)
        # check responses
        if eyesclosed_instruction_keyboard.keys in ['', [], None]:  # No response was made
            eyesclosed_instruction_keyboard.keys = None
        loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.keys',eyesclosed_instruction_keyboard.keys)
        if eyesclosed_instruction_keyboard.keys != None:  # we had a response
            loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.rt', eyesclosed_instruction_keyboard.rt)
            loop_eyesclosed_instruction.addData('eyesclosed_instruction_keyboard.duration', eyesclosed_instruction_keyboard.duration)
        # the Routine "eyesclosed_instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLoop_eyesclosed_instruction as finished
        if hasattr(thisLoop_eyesclosed_instruction, 'status'):
            thisLoop_eyesclosed_instruction.status = FINISHED
        # if awaiting a pause, pause now
        if loop_eyesclosed_instruction.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_eyesclosed_instruction.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_eyesclosed_instruction'
    loop_eyesclosed_instruction.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "countdown" ---
    # create an object to store info about Routine countdown
    countdown = data.Routine(
        name='countdown',
        components=[countdown_text],
    )
    countdown.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    countdown_counter = countdown_from
    add_time = countdown_time
    # store start times for countdown
    countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    countdown.tStart = globalClock.getTime(format='float')
    countdown.status = STARTED
    thisExp.addData('countdown.started', countdown.tStart)
    countdown.maxDuration = None
    # keep track of which components have finished
    countdownComponents = countdown.components
    for thisComponent in countdown.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countdown" ---
    thisExp.currentRoutine = countdown
    countdown.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from countdown_code
        if (t >= add_time - frameTolerance):
            countdown_counter -= 1
            add_time += countdown_time
        
        # *countdown_text* updates
        
        # if countdown_text is starting this frame...
        if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_text.frameNStart = frameN  # exact frame index
            countdown_text.tStart = t  # local t and not account for scr refresh
            countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'countdown_text.started')
            # update status
            countdown_text.status = STARTED
            countdown_text.setAutoDraw(True)
        
        # if countdown_text is active this frame...
        if countdown_text.status == STARTED:
            # update params
            countdown_text.setText(countdown_counter, log=False)
        
        # if countdown_text is stopping this frame...
        if countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_text.tStartRefresh + float(countdown_time*countdown_from)-frameTolerance:
                # keep track of stop time/frame for later
                countdown_text.tStop = t  # not accounting for scr refresh
                countdown_text.tStopRefresh = tThisFlipGlobal  # on global time
                countdown_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countdown_text.stopped')
                # update status
                countdown_text.status = FINISHED
                countdown_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=countdown,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            countdown.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if countdown.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in countdown.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdown.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for countdown
    countdown.tStop = globalClock.getTime(format='float')
    countdown.tStopRefresh = tThisFlipGlobal
    thisExp.addData('countdown.stopped', countdown.tStop)
    thisExp.nextEntry()
    # the Routine "countdown" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "eyesclosed_recording" ---
    # create an object to store info about Routine eyesclosed_recording
    eyesclosed_recording = data.Routine(
        name='eyesclosed_recording',
        components=[eyesclosed_recording_polygon, eyesclosed_recording_start_sound, eyesclosed_recording_stop_sound, eyesclosed_recording_skip_keyboard],
    )
    eyesclosed_recording.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from eyesclosed_recording_code
    if not int(expInfo['eyesclosed_recording']):
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    eyesclosed_recording_start_sound.setSound('660', secs=1.0, hamming=True)
    eyesclosed_recording_start_sound.setVolume(0.2, log=False)
    eyesclosed_recording_start_sound.seek(0)
    eyesclosed_recording_stop_sound.setSound('220', secs=1.0, hamming=True)
    eyesclosed_recording_stop_sound.setVolume(0.2, log=False)
    eyesclosed_recording_stop_sound.seek(0)
    # create starting attributes for eyesclosed_recording_skip_keyboard
    eyesclosed_recording_skip_keyboard.keys = []
    eyesclosed_recording_skip_keyboard.rt = []
    _eyesclosed_recording_skip_keyboard_allKeys = []
    # store start times for eyesclosed_recording
    eyesclosed_recording.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyesclosed_recording.tStart = globalClock.getTime(format='float')
    eyesclosed_recording.status = STARTED
    thisExp.addData('eyesclosed_recording.started', eyesclosed_recording.tStart)
    eyesclosed_recording.maxDuration = None
    # keep track of which components have finished
    eyesclosed_recordingComponents = eyesclosed_recording.components
    for thisComponent in eyesclosed_recording.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eyesclosed_recording" ---
    thisExp.currentRoutine = eyesclosed_recording
    eyesclosed_recording.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *eyesclosed_recording_polygon* updates
        
        # if eyesclosed_recording_polygon is starting this frame...
        if eyesclosed_recording_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_recording_polygon.frameNStart = frameN  # exact frame index
            eyesclosed_recording_polygon.tStart = t  # local t and not account for scr refresh
            eyesclosed_recording_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesclosed_recording_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eyesclosed_recording_polygon.started')
            # update status
            eyesclosed_recording_polygon.status = STARTED
            eyesclosed_recording_polygon.setAutoDraw(True)
        
        # if eyesclosed_recording_polygon is active this frame...
        if eyesclosed_recording_polygon.status == STARTED:
            # update params
            pass
        
        # if eyesclosed_recording_polygon is stopping this frame...
        if eyesclosed_recording_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesclosed_recording_polygon.tStartRefresh + eyesclosed_duration-frameTolerance:
                # keep track of stop time/frame for later
                eyesclosed_recording_polygon.tStop = t  # not accounting for scr refresh
                eyesclosed_recording_polygon.tStopRefresh = tThisFlipGlobal  # on global time
                eyesclosed_recording_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_recording_polygon.stopped')
                # update status
                eyesclosed_recording_polygon.status = FINISHED
                eyesclosed_recording_polygon.setAutoDraw(False)
        
        # *eyesclosed_recording_start_sound* updates
        
        # if eyesclosed_recording_start_sound is starting this frame...
        if eyesclosed_recording_start_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_recording_start_sound.frameNStart = frameN  # exact frame index
            eyesclosed_recording_start_sound.tStart = t  # local t and not account for scr refresh
            eyesclosed_recording_start_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('eyesclosed_recording_start_sound.started', tThisFlipGlobal)
            # update status
            eyesclosed_recording_start_sound.status = STARTED
            eyesclosed_recording_start_sound.play(when=win)  # sync with win flip
        
        # if eyesclosed_recording_start_sound is stopping this frame...
        if eyesclosed_recording_start_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesclosed_recording_start_sound.tStartRefresh + 1.0-frameTolerance or eyesclosed_recording_start_sound.isFinished:
                # keep track of stop time/frame for later
                eyesclosed_recording_start_sound.tStop = t  # not accounting for scr refresh
                eyesclosed_recording_start_sound.tStopRefresh = tThisFlipGlobal  # on global time
                eyesclosed_recording_start_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_recording_start_sound.stopped')
                # update status
                eyesclosed_recording_start_sound.status = FINISHED
                eyesclosed_recording_start_sound.stop()
        
        # *eyesclosed_recording_stop_sound* updates
        
        # if eyesclosed_recording_stop_sound is starting this frame...
        if eyesclosed_recording_stop_sound.status == NOT_STARTED and tThisFlip >= eyesclosed_duration - 1.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_recording_stop_sound.frameNStart = frameN  # exact frame index
            eyesclosed_recording_stop_sound.tStart = t  # local t and not account for scr refresh
            eyesclosed_recording_stop_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('eyesclosed_recording_stop_sound.started', tThisFlipGlobal)
            # update status
            eyesclosed_recording_stop_sound.status = STARTED
            eyesclosed_recording_stop_sound.play(when=win)  # sync with win flip
        
        # if eyesclosed_recording_stop_sound is stopping this frame...
        if eyesclosed_recording_stop_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesclosed_recording_stop_sound.tStartRefresh + 1.0-frameTolerance or eyesclosed_recording_stop_sound.isFinished:
                # keep track of stop time/frame for later
                eyesclosed_recording_stop_sound.tStop = t  # not accounting for scr refresh
                eyesclosed_recording_stop_sound.tStopRefresh = tThisFlipGlobal  # on global time
                eyesclosed_recording_stop_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_recording_stop_sound.stopped')
                # update status
                eyesclosed_recording_stop_sound.status = FINISHED
                eyesclosed_recording_stop_sound.stop()
        
        # *eyesclosed_recording_skip_keyboard* updates
        waitOnFlip = False
        
        # if eyesclosed_recording_skip_keyboard is starting this frame...
        if eyesclosed_recording_skip_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            eyesclosed_recording_skip_keyboard.frameNStart = frameN  # exact frame index
            eyesclosed_recording_skip_keyboard.tStart = t  # local t and not account for scr refresh
            eyesclosed_recording_skip_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eyesclosed_recording_skip_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eyesclosed_recording_skip_keyboard.started')
            # update status
            eyesclosed_recording_skip_keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(eyesclosed_recording_skip_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(eyesclosed_recording_skip_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if eyesclosed_recording_skip_keyboard is stopping this frame...
        if eyesclosed_recording_skip_keyboard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eyesclosed_recording_skip_keyboard.tStartRefresh + eyesclosed_duration-frameTolerance:
                # keep track of stop time/frame for later
                eyesclosed_recording_skip_keyboard.tStop = t  # not accounting for scr refresh
                eyesclosed_recording_skip_keyboard.tStopRefresh = tThisFlipGlobal  # on global time
                eyesclosed_recording_skip_keyboard.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eyesclosed_recording_skip_keyboard.stopped')
                # update status
                eyesclosed_recording_skip_keyboard.status = FINISHED
                eyesclosed_recording_skip_keyboard.status = FINISHED
        if eyesclosed_recording_skip_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = eyesclosed_recording_skip_keyboard.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
            _eyesclosed_recording_skip_keyboard_allKeys.extend(theseKeys)
            if len(_eyesclosed_recording_skip_keyboard_allKeys):
                eyesclosed_recording_skip_keyboard.keys = _eyesclosed_recording_skip_keyboard_allKeys[-1].name  # just the last key pressed
                eyesclosed_recording_skip_keyboard.rt = _eyesclosed_recording_skip_keyboard_allKeys[-1].rt
                eyesclosed_recording_skip_keyboard.duration = _eyesclosed_recording_skip_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=eyesclosed_recording,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            eyesclosed_recording.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if eyesclosed_recording.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in eyesclosed_recording.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyesclosed_recording" ---
    for thisComponent in eyesclosed_recording.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyesclosed_recording
    eyesclosed_recording.tStop = globalClock.getTime(format='float')
    eyesclosed_recording.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyesclosed_recording.stopped', eyesclosed_recording.tStop)
    eyesclosed_recording_start_sound.pause()  # ensure sound has stopped at end of Routine
    eyesclosed_recording_stop_sound.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if eyesclosed_recording_skip_keyboard.keys in ['', [], None]:  # No response was made
        eyesclosed_recording_skip_keyboard.keys = None
    thisExp.addData('eyesclosed_recording_skip_keyboard.keys',eyesclosed_recording_skip_keyboard.keys)
    if eyesclosed_recording_skip_keyboard.keys != None:  # we had a response
        thisExp.addData('eyesclosed_recording_skip_keyboard.rt', eyesclosed_recording_skip_keyboard.rt)
        thisExp.addData('eyesclosed_recording_skip_keyboard.duration', eyesclosed_recording_skip_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "eyesclosed_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "short_blank" ---
    # create an object to store info about Routine short_blank
    short_blank = data.Routine(
        name='short_blank',
        components=[short_blank_text],
    )
    short_blank.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from short_blank_code
    if (not int(expInfo['artifact_recording'])) and artifact_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    if (not int(expInfo['eyesclosed_recording'])) and eyesclosed_running:
        continueRoutine = False
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    artifact_running = False
    eyesclosed_running = False
    # store start times for short_blank
    short_blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    short_blank.tStart = globalClock.getTime(format='float')
    short_blank.status = STARTED
    thisExp.addData('short_blank.started', short_blank.tStart)
    short_blank.maxDuration = None
    # keep track of which components have finished
    short_blankComponents = short_blank.components
    for thisComponent in short_blank.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "short_blank" ---
    thisExp.currentRoutine = short_blank
    short_blank.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *short_blank_text* updates
        
        # if short_blank_text is starting this frame...
        if short_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            short_blank_text.frameNStart = frameN  # exact frame index
            short_blank_text.tStart = t  # local t and not account for scr refresh
            short_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(short_blank_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'short_blank_text.started')
            # update status
            short_blank_text.status = STARTED
            short_blank_text.setAutoDraw(True)
        
        # if short_blank_text is active this frame...
        if short_blank_text.status == STARTED:
            # update params
            pass
        
        # if short_blank_text is stopping this frame...
        if short_blank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > short_blank_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                short_blank_text.tStop = t  # not accounting for scr refresh
                short_blank_text.tStopRefresh = tThisFlipGlobal  # on global time
                short_blank_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'short_blank_text.stopped')
                # update status
                short_blank_text.status = FINISHED
                short_blank_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=short_blank,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            short_blank.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if short_blank.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in short_blank.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "short_blank" ---
    for thisComponent in short_blank.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for short_blank
    short_blank.tStop = globalClock.getTime(format='float')
    short_blank.tStopRefresh = tThisFlipGlobal
    thisExp.addData('short_blank.stopped', short_blank.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if short_blank.maxDurationReached:
        routineTimer.addTime(-short_blank.maxDuration)
    elif short_blank.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "goodbye_screen" ---
    # create an object to store info about Routine goodbye_screen
    goodbye_screen = data.Routine(
        name='goodbye_screen',
        components=[goodbye_screen_text, goodbye_screen_cwb_text, goodbye_screen_keyboard],
    )
    goodbye_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    goodbye_screen_cwb_text.setText(continue_with_button_text)
    # create starting attributes for goodbye_screen_keyboard
    goodbye_screen_keyboard.keys = []
    goodbye_screen_keyboard.rt = []
    _goodbye_screen_keyboard_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'continue_button' in globals():
        continue_button = globals()['continue_button']
    # store start times for goodbye_screen
    goodbye_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    goodbye_screen.tStart = globalClock.getTime(format='float')
    goodbye_screen.status = STARTED
    thisExp.addData('goodbye_screen.started', goodbye_screen.tStart)
    goodbye_screen.maxDuration = None
    # keep track of which components have finished
    goodbye_screenComponents = goodbye_screen.components
    for thisComponent in goodbye_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "goodbye_screen" ---
    thisExp.currentRoutine = goodbye_screen
    goodbye_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_screen_text* updates
        
        # if goodbye_screen_text is starting this frame...
        if goodbye_screen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_screen_text.frameNStart = frameN  # exact frame index
            goodbye_screen_text.tStart = t  # local t and not account for scr refresh
            goodbye_screen_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_screen_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_screen_text.started')
            # update status
            goodbye_screen_text.status = STARTED
            goodbye_screen_text.setAutoDraw(True)
        
        # if goodbye_screen_text is active this frame...
        if goodbye_screen_text.status == STARTED:
            # update params
            pass
        
        # *goodbye_screen_cwb_text* updates
        
        # if goodbye_screen_cwb_text is starting this frame...
        if goodbye_screen_cwb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_screen_cwb_text.frameNStart = frameN  # exact frame index
            goodbye_screen_cwb_text.tStart = t  # local t and not account for scr refresh
            goodbye_screen_cwb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_screen_cwb_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_screen_cwb_text.started')
            # update status
            goodbye_screen_cwb_text.status = STARTED
            goodbye_screen_cwb_text.setAutoDraw(True)
        
        # if goodbye_screen_cwb_text is active this frame...
        if goodbye_screen_cwb_text.status == STARTED:
            # update params
            pass
        
        # *goodbye_screen_keyboard* updates
        waitOnFlip = False
        
        # if goodbye_screen_keyboard is starting this frame...
        if goodbye_screen_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_screen_keyboard.frameNStart = frameN  # exact frame index
            goodbye_screen_keyboard.tStart = t  # local t and not account for scr refresh
            goodbye_screen_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_screen_keyboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_screen_keyboard.started')
            # update status
            goodbye_screen_keyboard.status = STARTED
            # allowed keys looks like a variable named `continue_button`
            if not type(continue_button) in [list, tuple, np.ndarray]:
                if not isinstance(continue_button, str):
                    continue_button = str(continue_button)
                elif not ',' in continue_button:
                    continue_button = (continue_button,)
                else:
                    continue_button = eval(continue_button)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goodbye_screen_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goodbye_screen_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goodbye_screen_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = goodbye_screen_keyboard.getKeys(keyList=list(continue_button), ignoreKeys=["escape"], waitRelease=False)
            _goodbye_screen_keyboard_allKeys.extend(theseKeys)
            if len(_goodbye_screen_keyboard_allKeys):
                goodbye_screen_keyboard.keys = _goodbye_screen_keyboard_allKeys[-1].name  # just the last key pressed
                goodbye_screen_keyboard.rt = _goodbye_screen_keyboard_allKeys[-1].rt
                goodbye_screen_keyboard.duration = _goodbye_screen_keyboard_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=goodbye_screen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            goodbye_screen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if goodbye_screen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in goodbye_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbye_screen" ---
    for thisComponent in goodbye_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for goodbye_screen
    goodbye_screen.tStop = globalClock.getTime(format='float')
    goodbye_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('goodbye_screen.stopped', goodbye_screen.tStop)
    # check responses
    if goodbye_screen_keyboard.keys in ['', [], None]:  # No response was made
        goodbye_screen_keyboard.keys = None
    thisExp.addData('goodbye_screen_keyboard.keys',goodbye_screen_keyboard.keys)
    if goodbye_screen_keyboard.keys != None:  # we had a response
        thisExp.addData('goodbye_screen_keyboard.rt', goodbye_screen_keyboard.rt)
        thisExp.addData('goodbye_screen_keyboard.duration', goodbye_screen_keyboard.duration)
    thisExp.nextEntry()
    # the Routine "goodbye_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
