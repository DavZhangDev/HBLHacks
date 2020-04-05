import time
import pyautogui
import sys
import time
from funcn import *
SCREENHEIGHT = pyautogui.size()[1]
SCREENWIDTH = pyautogui.size()[0]
USERNAME, PASSWORD = "22yzhan147c", "khzqtkq5"
LOGINTIME = [07,39]
print("Your screen dimensions are: " + str(SCREENWIDTH) + " * " + str(SCREENHEIGHT))
try:
    while True:
        time.sleep(60)
        t = time.localtime()
        if ([t[3], t[4]] == loginTime):
            inputunpw(USERNAME, PASSWORD)
except KeyboardInterrupt:
    print('\n')
