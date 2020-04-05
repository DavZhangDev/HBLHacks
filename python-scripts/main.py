import time
import pyautogui
import sys
import time
from funcn import *
SCREENHEIGHT = pyautogui.size()[1]
SCREENWIDTH = pyautogui.size()[0]
USERNAME = input("USERNAME: ")
PASSWORD = input("PASSWORD: ")
LOGINTIME = input("LOGIN TIME (24H FORMAT): ")
LOGINTIME = [int(str(LOGINTIME)[0] + str(LOGINTIME)[1]), int(str(LOGINTIME)[2] + str(LOGINTIME)[3])]
print(LOGINTIME)
print("Your screen dimensions are: " + str(SCREENWIDTH) + " * " + str(SCREENHEIGHT))
logged = True
try:
    while logged:
        time.sleep(5)
        t = time.localtime()
        if ([t[3], t[4]] == LOGINTIME):
            inputunpw(USERNAME, PASSWORD)
            logged = False
except KeyboardInterrupt:
    print('\n')
