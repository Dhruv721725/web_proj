import pyautogui as ptg
import time 
def ss():
    ptg.keyDown("win")
    ptg.keyDown("prtscr")
    ptg.keyUp("win")
    ptg.keyUp("prtscr")

time.sleep(3)
ss()