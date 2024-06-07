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
    def __init__(self, number, hwnd):
        self.ProcessName = ProcessName
        self.number = number
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
    def CheckWarp(self):
        time.sleep(10)
        while True:
            WindowsClassArray[self.number - 1].IMGInvisible()
            pix = Image.open('temp.jpeg').load()
            rgb1 = sum(pix[CheckWarpCoord[0], CheckWarpCoord[1]])
            os.remove('temp.jpeg')
            if rgb1 == 545:
                time.sleep(1)
                break
            else:
                time.sleep(5)
        while True:
            WindowsClassArray[self.number - 1].IMGInvisible()
            pix = Image.open('temp.jpeg').load()
            rgb1 = sum(pix[CheckWarpCoord[0], CheckWarpCoord[1]])
            os.remove('temp.jpeg')
            if rgb1 == 545:
                time.sleep(1)
            else:
                time.sleep(10)
                break
        ActivateWindow(self.hwnd)
class ScreenAction():
    def __init__(self):
        ...
        
    def TakeLocalStatus(self, LokalStatus):
        pix = Image.open('temp.jpeg').load()
        for n in range(LocalStatusRange[0], LocalStatusRange[1], LocalStatusRange[2]):
            #Проврка тикеров в чате /red,orange,grey
            if (pix[LocalStatusXCoord,n]==(LocalStatusColorsFirst[0], LocalStatusColorsFirst[1], LocalStatusColorsFirst[2]) or pix[LocalStatusXCoord,n]==(LocalStatusColorsSecond[0], LocalStatusColorsSecond[1], LocalStatusColorsSecond[2]) or pix[LocalStatusXCoord,n]==(LocalStatusColorsThird[0], LocalStatusColorsThird[1], LocalStatusColorsThird[2])):
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
        if (sum(pix(OwerWinStatusPos))) == 402:
            OverWinStatus.set()
    def TakeStatus(self):
        print(self.LokalStatus)
        print(self.ShieldStatus)
        print(self.OverWinStatus)

GetPIDList(ProcessName)
for NumberWin, pid in enumerate(pidsArray, 1):
    GetHWID(NumberWin, pid)
for win in windows.keys():
    WindowsClassArray.append(Character(win, windows[win]))
    ScreenClassArray.append(ScreenAction())