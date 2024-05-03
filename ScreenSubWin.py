from FarmThread import *
import ctypes, win32ui
from ctypes import windll

from PIL import Image
import win32gui
import win32process
import psutil
windows = []
def GetHWID(ProcessName):
    # Список процессов с именем файла notepad.exe:
    notepads = [item for item in psutil.process_iter() if item.name() == ProcessName]
    pid = next(item for item in psutil.process_iter() if item.name() == ProcessName).pid

    def enum_window_callback(hwnd, pid):
        tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == current_pid and win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(enum_window_callback, pid)

    print([win32gui.GetWindowText(item) for item in windows])
def invisible(hwnd):
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

def ScreenSubWin(ProccessName):
    GetHWID(ProccessName)
    invisible(windows[0])
