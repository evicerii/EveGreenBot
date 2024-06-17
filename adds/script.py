import pyautogui as pag
from .mouseMove.mousemove import *
from .coordinate import *
import time
import os
from PIL import Image
from .decorators import logs
import logging
import win32con
import time
import win32process
import psutil
import threading
config = configparser.ConfigParser()

pidsArray=[]
windows = {}

EndCyrcleEvent = threading.Event()
TempLock = threading.Lock()
CheckEnemyLock = threading.Lock()
def CheckTarget(x, y, z):
    while True:
        time.sleep(random.randint(3,5))
        rgb1 = sum(pag.pixel(x,y))
        if rgb1==z:
            break
@logs
def RewriteSettings(name, txt):
    config.read('config.ini')
    config.set("General", name, txt)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
def GetPIDList(ProcessName):
    for proc in psutil.process_iter():
        if ProcessName in proc.name():
            pid=proc.pid
            pidsArray.append(pid)
def GetHWID(NumberWin, pid):
    def enum_window_callback(hwnd, pid):
        tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == current_pid and win32gui.IsWindowVisible(hwnd):
            windows[NumberWin] = hwnd

    win32gui.EnumWindows(enum_window_callback, pid)
def ActivateWindow(hwnd):
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)
        logging.info(f'ActivateWindow {hwnd}')
    except IndexError:
        logging.error('Окно с указанным идентификатором не найдено.')
    finally:
        time.sleep(random.randint(20,25)/10)
