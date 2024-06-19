from FarmThread import *
from Classes.WinAction import *
from concurrent.futures import ThreadPoolExecutor

from win32gui import FindWindow, GetWindowRect

#pyinstaller --add-data "config.ini:." --add-data "logs:logs" main.py

def BotExit():
    logging.info(f'BotExit start')
    time.sleep(int(config.get('General','workTime'))*60+(random.randint(0,50))*6)
    EndCyrcleEvent.set()
    logging.info(f'BotExit stop')
    return

BotExitThread = threading.Thread(target=BotExit)
threads = [BotExitThread]

if __name__ == '__main__':
    # os.system(f'C:/Users/{os.getlogin()}/AppData/Local/eve-online/eve-online.exe')
    # time.sleep(30)
    # window_handle = FindWindow(None, "EVE Online Launcher")
    # window_rect = GetWindowRect(window_handle)
    # mouseMove(launchWinsCoords.x + window_rect[0],launchWinsCoords.y + window_rect[1])
    # click()
    # time.sleep(60)
    # GetPIDList(ProcessName)
    # for NumberWin, pid in enumerate(pidsArray, 1):
    #     GetHWID(NumberWin, pid)
    # #во всех окнах
    # for win in windows.keys():
    #     ActivateWindow(windows[win])
    #     mouseMove(LocalChat.x, LocalChat.y)
    #     click()
    #     pag.keyDown('ctrl')
    #     time.sleep(random.randint(10,30)/100)
    #     pag.keyDown('shift')
    #     time.sleep(random.randint(10,30)/100)
    #     pag.press('f9')
    #     time.sleep(random.randint(10,30)/100)
    #     pag.keyUp('shift')
    #     time.sleep(random.randint(10,30)/100)
    #     pag.keyUp('ctrl')
    #     Ship.Undock()
    #     mouseMove(StopShip.x, StopShip.y)
    #     click()
    #     time.sleep(10)
    #     Ship.Dock()
    # del WindowsClassArray[:]
    # del ScreenClassArray[:]
    [p.start() for p in threads]
    with ThreadPoolExecutor() as executor:
        executor.map(GreenThread, windows.keys())