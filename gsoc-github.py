"""
Little script to help me follow all my fellow gsocers on github

Requirements:
i3/sway or a compatible wm
Firefox with vimium add-on on left
Spreadsheet with a cell of the column targeted selected

"""
from pyautogui import press, typewrite, hotkey
import subprocess
import time

time.sleep(5)  # give the time to focus on the window

while(True):
    press('down')
    hotkey('ctrl', 'c')
    hotkey('winleft', 'left')
    press('escape')
    press('f')
    press('e')
    hotkey('ctrl', 'q')
    hotkey('ctrl', 'v')
    press('enter')
    time.sleep(5)
    press('escape')
    press('f')
    press('o')
    hotkey('winleft', 'right')

