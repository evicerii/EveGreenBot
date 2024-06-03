import ctypes, win32ui
from ctypes import windll
import threading

from PIL import Image
import win32gui
import logging
import pyautogui as pag

from adds.script import *

WindowsClassArray = []
ScreenClassArray = []

ProcessName = 'exefile.exe'

class Character:
    def __init__(self, number, pid, hwnd):
        self.number = number
        self.ProcessName = ProcessName
        self.pid = pid
        self.hwnd = hwnd
    def IMGInvisible(self):
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        rect = ctypes.wintypes.RECT()
        dwma_extended_frame_bounds = 9
        f(ctypes.wintypes.HWND(self.hwnd),
            ctypes.wintypes.DWORD(dwma_extended_frame_bounds),
            ctypes.byref(rect),
            ctypes.sizeof(rect)
            )
        width = rect.right - rect.left
        height = rect.bottom - rect.top

        hwnddc = win32gui.GetDC(self.hwnd)
        mfcdc = win32ui.CreateDCFromHandle(hwnddc)
        savedc = mfcdc.CreateCompatibleDC()

        savebitmap = win32ui.CreateBitmap()
        savebitmap.CreateCompatibleBitmap(mfcdc, width, height)
        savedc.SelectObject(savebitmap)
        windll.user32.PrintWindow(self.hwnd, savedc.GetSafeHdc(), 3)

        bmpinfo = savebitmap.GetInfo()
        bmpstr = savebitmap.GetBitmapBits(True)
        im_scr = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 3)
        
        win32gui.DeleteObject(savebitmap.GetHandle())

        savedc.DeleteDC()
        mfcdc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnddc)

        im_scr.save(f'temp.jpeg', 'jpeg')
        return  f'temp.jpeg'

class ScreenAction():
    def __init__(self):
        ...
        
    def TakeLocalStatus(self, LokalStatus):
        pix = Image.open('temp.jpeg').load()
        for n in range(754,952,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pix[321,n]==(79, 5, 6) or pix[321,n]==(146, 69, 27) or pix[321,n]==(103, 103, 103)):
                logging.info(f'local red')
                LokalStatus.set()
    def TakeShieldStatus(self, ShieldStatus):
        pix = Image.open('temp.jpeg').load()
        if (sum(pix[965,850])>700 and sum(pix[965,850])<750) or (sum(pix[966,850])>700 and sum(pix[966,850])<750) or (sum(pix[967,850])>700 and sum(pix[967,850])<750):
            ShieldStatus.set()
        else:
            logging.info(f'low shield')
            ShieldStatus.clear()
    def TakeOverWinStatus(self, OverWinStatus):
        pix = Image.open('temp.jpeg').load()
        if (sum(pix[1576,306])) == 402:
            OverWinStatus.set()
    def TakeStatus(self):
        print(self.LokalStatus)
        print(self.ShieldStatus)
        print(self.OverWinStatus)

GetPIDList(ProcessName)
for NumberWin, pid in enumerate(pidsArray, 1):
    GetHWID(NumberWin, pid)
for win in windows.keys():
    WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    ScreenClassArray.append(ScreenAction())