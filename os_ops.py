import os
import subprocess as sp

paths = {'word':'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016',
         'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
         'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
         'calculator': "C:\\Windows\\System32\\calc.exe",
         'clock':"C:\\Users\\Pelumi\\Desktop\\clock.exe",
         'tic-tac-toe':"C:\\Users\\Pelumi\\Desktop\\XO.exe"}

def open_camera():
    sp.run('start.microsoft.windows.camera', shell=True)

def open_word():
    os.startfile(paths['word'])

def open_chrome():
    os.startfile(paths['chrome'])

def open_ppt():
    os.startfile(paths["powerpoint"])

def open_calc():
    sp.Popen(paths["calculator"])

def open_cmd():
    os.system('start cmd')

def open_XO():
    os.startfile(paths["tic-tac-toe"])

def open_clock():
    os.startfile(paths["clock"])


