"""
get_position.py — Mouse Position Finder
----------------------------------------
Run this script, hover your mouse over any part of the screen,
and it will print the X, Y coordinates every second.

Use this to find:
  - The region you want to watch (top-left corner + size)
  - The exact pixel to click (the Discord link location)

Press Ctrl+C to stop.
"""

import time
import pyautogui

print("Move your mouse around. Coordinates will print every second.")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"  Mouse position → X: {x:>5},  Y: {y:>5}", end="\r", flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\nDone!")
