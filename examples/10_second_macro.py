"""
Macro that records all keyboard events for 10 seconds and then replays them.
"""
import sys

sys.path.append('../')

import time

import keyboard

keyboard.start_recording()
time.sleep(10)
events = keyboard.stop_recording()
keyboard.replay(events)
