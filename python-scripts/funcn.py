import pyautogui
import sys
import time
import math
SCREENHEIGHT = pyautogui.size()[1]
SCREENWIDTH = pyautogui.size()[0]

def navigatetourl(URL, MORW):
    if MORW.lower() == "m":
        pyautogui.hotkey("command", "t")
    else:
        pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.write(URL)
    pyautogui.hotkey("enter")

def inputunpw(USERNAME, PASSWORD):
    pyautogui.moveTo(math.floor((1156/1440)*SCREENWIDTH), math.floor((431/900)*SCREENHEIGHT))
    pyautogui.click()
    pyautogui.hotkey("ctrl", "shift", "a", "backspace")
    pyautogui.write(USERNAME)
    time.sleep(0.1)
    pyautogui.click(math.floor((10/1440)*SCREENWIDTH), math.floor((450/900)*SCREENHEIGHT))
    time.sleep(0.1)
    pyautogui.click(math.floor((1156/1440)*SCREENWIDTH), math.floor((471/900)*SCREENHEIGHT))
    pyautogui.hotkey("ctrl", "shift", "a", "backspace")
    pyautogui.write(PASSWORD)
    time.sleep(0.1)
    pyautogui.click(math.floor((1032/1440)*SCREENWIDTH), math.floor((540/900)*SCREENHEIGHT))
