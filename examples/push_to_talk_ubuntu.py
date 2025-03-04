"""
Quick and dirty push-to-talk example by Abd Azrad
"""
import sys

sys.path.append('../')

import subprocess

import keyboard

is_muted = False

def unmute():
    global is_muted
    if not is_muted: # if mic is already enabled
        return # do nothing
    is_muted = False
    subprocess.call('amixer set Capture cap', shell=True) # unmute mic

def mute():
    global is_muted
    is_muted = True
    subprocess.call('amixer set Capture nocap', shell=True) # mute mic

if __name__ == "__main__":
    is_muted = True
    mute() # mute on startup

    keyboard.add_hotkey('win', unmute) # unmute on keydown
    keyboard.add_hotkey('win', mute, trigger_on_release=True) # mute on keyup

    keyboard.wait() # wait forever
