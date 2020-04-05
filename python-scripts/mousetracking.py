import pyautogui
import sys
import time
print("Press Ctrl-C to quit.")
try:
    while True:
        time.sleep(0.1)
        mousex, mousey = pyautogui.position()
        positionStr = "X: " + str(mousex).rjust(4) + ", Y: " + str(mousey).rjust(4)
        print(positionStr, end = "")
        print("\b" * len(positionStr), end = "", flush = True)
except KeyboardInterrupt:
    print("\n")
