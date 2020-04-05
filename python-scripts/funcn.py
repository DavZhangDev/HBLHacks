import pyautogui
import sys
import time
SCREENHEIGHT = pyautogui.size()[1]
SCREENWIDTH = pyautogui.size()[0]
def inputunpw(USERNAME, PASSWORD):
    pyautogui.moveTo((1156/1440)*SCREENWIDTH, (431/900)*SCREENHEIGHT)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "shift", "a", "backspace")
    pyautogui.write(USERNAME)
    time.sleep(0.1)
    pyautogui.click((10/1440)*SCREENWIDTH, (450/900)*SCREENHEIGHT)
    time.sleep(0.1)
    pyautogui.click((1156/1440)*SCREENWIDTH, (471/900)*SCREENHEIGHT)
    pyautogui.hotkey("ctrl", "shift", "a", "backspace")
    pyautogui.write(PASSWORD)
    time.sleep(0.1)
    pyautogui.click((1032/1440)*SCREENWIDTH, (540/900)*SCREENHEIGHT)
