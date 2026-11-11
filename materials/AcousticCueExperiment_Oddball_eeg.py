#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on February 07, 2025, at 16:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
from psychopy.plugins import activatePlugins
plugins.activatePlugins()
import sounddevice as sd
import soundfile as sf
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from time import sleep



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    #originPath='C:\\Users\\Lab User\\Desktop\\Experiments\\Chiara\\Part4_Oddball\\AcousticCueExperiment_oddball4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.INFO)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    winType='pyglet', allowStencil=False,
    monitor='default', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome! Are you ready to begin part 2? Press "space" to start.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_welcome = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
textblank500 = visual.TextStim(win=win, name='textblank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "oddball_intro" ---
textOddballtask = visual.TextStim(win=win, name='textOddballtask',
    text='You will now begin a new block. Press "space" when you are ready. The target word will be shown on the screen. Press "n" if you hear the target word and "m" if you hear a word that isn\'t the target.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respOddball = keyboard.Keyboard()

# --- Initialize components for Routine "oddball_task" ---
#block1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
 #   name='block1')
#block1.setVolume(1.0)
def play_audio(file_path):
    audio_data,sample_rate=sf.read(file_path)
    sd.default.device='ASIO Fireface USB'
    sd.play(audio_data,samplerate=sample_rate,mapping=[1,2,3])
    sd.wait

oddball_response = keyboard.Keyboard()
textTarget_2 = visual.TextStim(win=win, name='textTarget_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "pause" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Break" ---
textBreak = visual.TextStim(win=win, name='textBreak',
    text='You may take a break. Feel free to pause as long as you want. Press "space" to continue the experiment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respBreak = keyboard.Keyboard()

# --- Initialize components for Routine "textEnd" ---
textEndExp = visual.TextStim(win=win, name='textEndExp',
    text='Congratulations! You have completed the experiment. Press "space" to end.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_welcome.keys = []
key_resp_welcome.rt = []
_key_resp_welcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [textWelcome, key_resp_welcome]
for thisComponent in WelcomeComponents:
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

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *key_resp_welcome* updates
    waitOnFlip = False
    if key_resp_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_welcome.frameNStart = frameN  # exact frame index
        key_resp_welcome.tStart = t  # local t and not account for scr refresh
        key_resp_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_welcome, 'tStartRefresh')  # time at next scr refresh
        key_resp_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_welcome.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_welcome_allKeys.extend(theseKeys)
        if len(_key_resp_welcome_allKeys):
            key_resp_welcome.keys = _key_resp_welcome_allKeys[-1].name  # just the last key pressed
            key_resp_welcome.rt = _key_resp_welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textblank500]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textblank500* updates
    if textblank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textblank500.frameNStart = frameN  # exact frame index
        textblank500.tStart = t  # local t and not account for scr refresh
        textblank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textblank500, 'tStartRefresh')  # time at next scr refresh
        textblank500.setAutoDraw(True)
    if textblank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textblank500.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            textblank500.tStop = t  # not accounting for scr refresh
            textblank500.frameNStop = frameN  # exact frame index
            textblank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
trialBlock = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('continuuaStim.xlsx'),
    seed=None, name='trialBlock')
thisExp.addLoop(trialBlock)  # add the loop to the experiment
thisTrialBlock = trialBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
if thisTrialBlock != None:
    for paramName in thisTrialBlock:
        exec('{} = thisTrialBlock[paramName]'.format(paramName))

for thisTrialBlock in trialBlock:
    currentLoop = trialBlock
    # abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
    if thisTrialBlock != None:
        for paramName in thisTrialBlock:
            exec('{} = thisTrialBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "oddball_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    respOddball.keys = []
    respOddball.rt = []
    _respOddball_allKeys = []
    # keep track of which components have finished
    oddball_introComponents = [textOddballtask, respOddball]
    for thisComponent in oddball_introComponents:
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
    
    # --- Run Routine "oddball_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textOddballtask* updates
        if textOddballtask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textOddballtask.frameNStart = frameN  # exact frame index
            textOddballtask.tStart = t  # local t and not account for scr refresh
            textOddballtask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textOddballtask, 'tStartRefresh')  # time at next scr refresh
            textOddballtask.setAutoDraw(True)
        
        # *respOddball* updates
        waitOnFlip = False
        if respOddball.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respOddball.frameNStart = frameN  # exact frame index
            respOddball.tStart = t  # local t and not account for scr refresh
            respOddball.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respOddball, 'tStartRefresh')  # time at next scr refresh
            respOddball.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respOddball.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respOddball.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respOddball.status == STARTED and not waitOnFlip:
            theseKeys = respOddball.getKeys(keyList=['space'], waitRelease=False)
            _respOddball_allKeys.extend(theseKeys)
            if len(_respOddball_allKeys):
                respOddball.keys = _respOddball_allKeys[-1].name  # just the last key pressed
                respOddball.rt = _respOddball_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in oddball_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "oddball_intro" ---
    for thisComponent in oddball_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "oddball_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialBreak = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trialBreak')
    thisExp.addLoop(trialBreak)  # add the loop to the experiment
    thisTrialBreak = trialBreak.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialBreak.rgb)
    if thisTrialBreak != None:
        for paramName in thisTrialBreak:
            exec('{} = thisTrialBreak[paramName]'.format(paramName))
    
    for thisTrialBreak in trialBreak:
        currentLoop = trialBreak
        # abbreviate parameter names if possible (e.g. rgb = thisTrialBreak.rgb)
        if thisTrialBreak != None:
            for paramName in thisTrialBreak:
                exec('{} = thisTrialBreak[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trialOddball = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('oddballStim.xlsx'),
            seed=None, name='trialOddball')
        thisExp.addLoop(trialOddball)  # add the loop to the experiment
        thisTrialOddball = trialOddball.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialOddball.rgb)
        if thisTrialOddball != None:
            for paramName in thisTrialOddball:
                exec('{} = thisTrialOddball[paramName]'.format(paramName))
        
        for thisTrialOddball in trialOddball:
            currentLoop = trialOddball
            # abbreviate parameter names if possible (e.g. rgb = thisTrialOddball.rgb)
            if thisTrialOddball != None:
                for paramName in thisTrialOddball:
                    exec('{} = thisTrialOddball[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "oddball_task" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            #block1.setSound(audio_clip, secs=4, hamming=True)
            #block1.setVolume(1.0, log=False)
            audio_file_path = os.path.join(thisTrialOddball['audio_clip'])
            oddball_response.keys = []
            oddball_response.rt = []
            _oddball_response_allKeys = []
            textTarget_2.setText(target)
            # keep track of which components have finished
            oddball_taskComponents = [oddball_response, textTarget_2] #block1,
            for thisComponent in oddball_taskComponents:
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
            
            # --- Run Routine "oddball_task" ---
            sleep(0.1)
            play_audio(audio_file_path)
            while continueRoutine and routineTimer.getTime() < 4.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop block1
                #if tThisFlip >= 0.1-frameTolerance: #block1.status == NOT_STARTED and
                    # keep track of start time/frame for later
                    # block1.frameNStart = frameN  # exact frame index
                    # block1.tStart = t  # local t and not account for scr refresh
                    # block1.tStartRefresh = tThisFlipGlobal  # on global time
                    # # add timestamp to datafile
                    #thisExp.addData('block1.started', tThisFlipGlobal)
                    #play_audio(audio_file_path)
                    # block1.play(when=win)  # sync with win flip
                # if status == STARTED: #block1.
                #     # is it time to stop? (based on local clock)
                #     if tThisFlip > 4-frameTolerance:
                #         # keep track of stop time/frame for later
                #         block1.tStop = t  # not accounting for scr refresh
                #         block1.frameNStop = frameN  # exact frame index
                #         # add timestamp to datafile
                #         thisExp.timestampOnFlip(win, 'block1.stopped')
                #         block1.stop()
                
                # *oddball_response* updates
                waitOnFlip = False
                if oddball_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    oddball_response.frameNStart = frameN  # exact frame index
                    oddball_response.tStart = t  # local t and not account for scr refresh
                    oddball_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(oddball_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'oddball_response.started')
                    oddball_response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(oddball_response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(oddball_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if oddball_response.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > oddball_response.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        oddball_response.tStop = t  # not accounting for scr refresh
                        oddball_response.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'oddball_response.stopped')
                        oddball_response.status = FINISHED
                if oddball_response.status == STARTED and not waitOnFlip:
                    theseKeys = oddball_response.getKeys(keyList=['n','m'], waitRelease=False)
                    _oddball_response_allKeys.extend(theseKeys)
                    if len(_oddball_response_allKeys):
                        oddball_response.keys = _oddball_response_allKeys[-1].name  # just the last key pressed
                        oddball_response.rt = _oddball_response_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *textTarget_2* updates
                if textTarget_2.status == NOT_STARTED and tThisFlip >= .0-frameTolerance:
                    # keep track of start time/frame for later
                    textTarget_2.frameNStart = frameN  # exact frame index
                    textTarget_2.tStart = t  # local t and not account for scr refresh
                    textTarget_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textTarget_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textTarget_2.started')
                    textTarget_2.setAutoDraw(True)
                if textTarget_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textTarget_2.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        textTarget_2.tStop = t  # not accounting for scr refresh
                        textTarget_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textTarget_2.stopped')
                        textTarget_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in oddball_taskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "oddball_task" ---
            for thisComponent in oddball_taskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #block1.stop()  # ensure sound has stopped at end of routine
            # check responses
            if oddball_response.keys in ['', [], None]:  # No response was made
                oddball_response.keys = None
            trialOddball.addData('oddball_response.keys',oddball_response.keys)
            if oddball_response.keys != None:  # we had a response
                trialOddball.addData('oddball_response.rt', oddball_response.rt)
            # Run 'End Routine' code from code
            if not oddball_response.keys:  # key_resp is the name of your Keyboard component
                oddball_response.keys = "NA"
                oddball_response.rt = "NA"  # Optional: leave reaction time empty if no response
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            
            # --- Prepare to start Routine "pause" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            text_4.setText(target)
            # Run 'Begin Routine' code from code_4
            pause_duration = 0.75 + (0.25 * (2 * random() - 1))
            
            # keep track of which components have finished
            pauseComponents = [text_4]
            for thisComponent in pauseComponents:
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
            
            # --- Run Routine "pause" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + pause_duration -frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.frameNStop = frameN  # exact frame index
                        text_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pauseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pause" ---
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "pause" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'trialOddball'
        
        
        # --- Prepare to start Routine "Break" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        respBreak.keys = []
        respBreak.rt = []
        _respBreak_allKeys = []
        # keep track of which components have finished
        BreakComponents = [textBreak, respBreak]
        for thisComponent in BreakComponents:
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
        
        # --- Run Routine "Break" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBreak* updates
            if textBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBreak.frameNStart = frameN  # exact frame index
                textBreak.tStart = t  # local t and not account for scr refresh
                textBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBreak, 'tStartRefresh')  # time at next scr refresh
                textBreak.setAutoDraw(True)
            
            # *respBreak* updates
            waitOnFlip = False
            if respBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respBreak.frameNStart = frameN  # exact frame index
                respBreak.tStart = t  # local t and not account for scr refresh
                respBreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respBreak, 'tStartRefresh')  # time at next scr refresh
                respBreak.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respBreak.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respBreak.status == STARTED and not waitOnFlip:
                theseKeys = respBreak.getKeys(keyList=['space'], waitRelease=False)
                _respBreak_allKeys.extend(theseKeys)
                if len(_respBreak_allKeys):
                    respBreak.keys = _respBreak_allKeys[-1].name  # just the last key pressed
                    respBreak.rt = _respBreak_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Break" ---
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trialBreak'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialBlock'


# --- Prepare to start Routine "textEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
respEnd.keys = []
respEnd.rt = []
_respEnd_allKeys = []
# keep track of which components have finished
textEndComponents = [textEndExp, respEnd]
for thisComponent in textEndComponents:
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

# --- Run Routine "textEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndExp* updates
    if textEndExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndExp.frameNStart = frameN  # exact frame index
        textEndExp.tStart = t  # local t and not account for scr refresh
        textEndExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndExp, 'tStartRefresh')  # time at next scr refresh
        textEndExp.setAutoDraw(True)
    
    # *respEnd* updates
    waitOnFlip = False
    if respEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respEnd.frameNStart = frameN  # exact frame index
        respEnd.tStart = t  # local t and not account for scr refresh
        respEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respEnd, 'tStartRefresh')  # time at next scr refresh
        respEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respEnd.status == STARTED and not waitOnFlip:
        theseKeys = respEnd.getKeys(keyList=['space'], waitRelease=False)
        _respEnd_allKeys.extend(theseKeys)
        if len(_respEnd_allKeys):
            respEnd.keys = _respEnd_allKeys[-1].name  # just the last key pressed
            respEnd.rt = _respEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in textEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "textEnd" ---
for thisComponent in textEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "textEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
