"""
Little script to help me follow all my fellow gsocers on github

Requirements:
i3/sway or a compatible wm
Firefox with vimium add-on on left
Spreadsheet with a cell of the column targeted selected

"""
from pyautogui import press, typewrite, hotkey
import subprocess

sleep(2)  # give the time to focus on the window

press('down')
hotkey('ctrl', 'c')
hotkey('winleft', 'left')
press('escape')
press('f')
press('e')
pseudo = subprocess.check_output(["wl-paste"]).decode("utf-8")
typewrite(pseudo)
press('enter')
press('escape')
press('f')
press('o')
hotkey('winleft', 'right')

