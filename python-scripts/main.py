try:
    import time
    import pyautogui
    import sys
    import math
    from funcn import *
    SCREENHEIGHT = pyautogui.size()[1]
    SCREENWIDTH = pyautogui.size()[0]
    USERNAME = input("USERNAME: ")
    PASSWORD = input("PASSWORD: ")
    LOGINTIME = input("LOGIN TIME (24H FORMAT): ")
    LOGINTIME = [int(str(LOGINTIME)[0] + str(LOGINTIME)[1]), int(str(LOGINTIME)[2] + str(LOGINTIME)[3])]
    URL = input("INPUT URL: ")
    MORW = input("MAC OR WINDOWS (M/W): ")
    print("Your screen dimensions are: " + str(SCREENWIDTH) + " * " + str(SCREENHEIGHT))
    logged = True
    while logged:
        time.sleep(5)
        t = time.localtime()
        if ([t[3], t[4]] == LOGINTIME):
            navigatetourl(URL, MORW)
            time.sleep(10)
            inputunpw(USERNAME, PASSWORD)
            logged = False
            print("Logged in at " + str(t[3]) + ":" + str(t[4]))
except KeyboardInterrupt:
    print("\nProgram stopped.")
except:
    print("\nError encountered, please rerun program!")
