import ctypes, win32ui
from ctypes import windll
import threading

from PIL import Image
import win32gui
import win32con
import os
import time
import win32process
import psutil

pids=[]
hwid=[]
windows = {}

ProcessName = 'exefile.exe'

DungerShield = threading.Event()

def GetPIDList(ProcessName):
    for proc in psutil.process_iter():
        if ProcessName in proc.name():
            pid=proc.pid
            pids.append(pid)
def GetHWID(NumberWin, pid):
    def enum_window_callback(hwnd, pid):
        tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == current_pid and win32gui.IsWindowVisible(hwnd):
            windows[NumberWin] = hwnd

    win32gui.EnumWindows(enum_window_callback, pid)

def IMGInvisible(hwnd):
    f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    rect = ctypes.wintypes.RECT()
    dwma_extended_frame_bounds = 9
    f(ctypes.wintypes.HWND(hwnd),
        ctypes.wintypes.DWORD(dwma_extended_frame_bounds),
        ctypes.byref(rect),
        ctypes.sizeof(rect)
        )
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    hwnddc = win32gui.GetDC(hwnd)
    mfcdc = win32ui.CreateDCFromHandle(hwnddc)
    savedc = mfcdc.CreateCompatibleDC()

    savebitmap = win32ui.CreateBitmap()
    savebitmap.CreateCompatibleBitmap(mfcdc, width, height)
    savedc.SelectObject(savebitmap)
    windll.user32.PrintWindow(hwnd, savedc.GetSafeHdc(), 3)

    bmpinfo = savebitmap.GetInfo()
    bmpstr = savebitmap.GetBitmapBits(True)
    im_scr = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 3)
    
    win32gui.DeleteObject(savebitmap.GetHandle())

    savedc.DeleteDC()
    mfcdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnddc)

    im_scr.save(f'temp.jpeg', 'jpeg')
    return  f'temp.jpeg'
def WinCheckShield(DungerShield):
    im = Image.open('temp.jpeg')
    pix = im.load()
    if sum(pix[966,850])>700 and sum(pix[966,850])<750:
        #event set
        print('Dunger')
        DungerShield.set()
def TakeWinActive(winNumber):
    win32gui.ShowWindow(winNumber, win32con.SW_SHOWMAXIMIZED)
    win32gui.SetForegroundWindow(winNumber)

def CheckShieldStatus():
    GetPIDList(ProcessName)
    for NumberWin, pid in enumerate(pids, 1):
        GetHWID(NumberWin, pid)
    for i in windows.keys():
        IMGInvisible(windows[i])
        WinCheckShield(DungerShield)
        os.remove('Temp.jpeg')
        if DungerShield.is_set:
            TakeWinActive(windows[i])
            time.sleep(6)
