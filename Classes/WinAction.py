import ctypes, win32ui
from ctypes import windll
from PIL import Image
import win32gui
import logging
import pyautogui as pag

from adds.script import *

WindowsClassArray = []
ScreenClassArray = []

ProcessName = 'exefile.exe'

class Character:
    def __init__(self, hwnd):
        self.ProcessName = ProcessName
        self.hwnd = hwnd
    def IMGInvisible(self, ActiveThread = 'temp'):
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

        im_scr.save(f'{ActiveThread}.jpeg', 'jpeg')
        return  f'{ActiveThread}.jpeg'
    def CheckWarp(self, numberWin):
        time.sleep(10)
        while True:
            WindowsClassArray[numberWin].IMGInvisible()
            pix = Image.open('temp.jpeg').load()
            rgb1 = sum(pix[CheckWarpCoord[0], CheckWarpCoord[1]])
            os.remove('temp.jpeg')
            if 205 < rgb1 < 240:
                time.sleep(3)
                break
            else:
                time.sleep(5)
        while True:
            WindowsClassArray[numberWin].IMGInvisible()
            pix = Image.open('temp.jpeg').load()
            rgb1 = sum(pix[CheckWarpCoord[0], CheckWarpCoord[1]])
            os.remove('temp.jpeg')
            if 205 < rgb1 < 240:
                time.sleep(1)
            else:
                time.sleep(10)
                break

class ScreenAction():
    def __init__(self):
        ...
        
    def TakeLocalStatus(self, LokalStatus, hwnd, ActiveThread = 'temp'):
        pix = Image.open(f'{ActiveThread}.jpeg').load()
        for n in range(LocalStatusRange[0], LocalStatusRange[1], LocalStatusRange[2]):
            #Проврка тикеров в чате /red,orange,grey
            if (pix[LocalStatusXCoord,n][0]>70):
                logging.info(f'local red {hwnd}')
                LokalStatus.set()
    def TakeShieldStatus(self, ShieldStatus, ActiveThread = 'Temp'):
        pix = Image.open(f'{ActiveThread}.jpeg').load()
        if (sum(pix[965,850])>700 and sum(pix[965,850])<800) or (sum(pix[966,850])>700 and sum(pix[966,850])<800) or (sum(pix[967,850])>700 and sum(pix[967,850])<800):
            ...
        else:
            logging.info(f'low shield')
            ShieldStatus.set()
    def TakeOverWinStatus(self, OverWinStatus, ActiveThread = 'Temp'):
        pix = Image.open(f'{ActiveThread}.jpeg').load()
        if (sum(pix[OwerWinStatusPos[0], OwerWinStatusPos[1]])) == OwerWinStatusValue:
            OverWinStatus.set()
    def TakeStatus(self):
        print(self.LokalStatus)
        print(self.ShieldStatus)
        print(self.OverWinStatus)

GetPIDList(ProcessName)
for pid in pidsArray:
    GetHWID(pid)
for hwnd in windows:
    WindowsClassArray.append(Character(hwnd))
    ScreenClassArray.append(ScreenAction())
    