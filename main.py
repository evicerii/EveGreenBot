from FarmThread import *
from Classes.WinAction import *
from concurrent.futures import ThreadPoolExecutor


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
    #во всех окнах
    for index, win in enumerate(windows):
        ActivateWindow(win)
        # click()
        # Activate2D()
        # Ship.Undock()
        # mouseMove(StopShip.x, StopShip.y)
        # click()
        # time.sleep(10)
        # mouseMove(StopShip.x, StopShip.y)
        # click()
        # time.sleep(10)
        # Ship.Dock(WinThreadArray[index].DronsLaunchStatus, WinThreadArray[index].LocalChatStatus)
    [p.start() for p in threads]
    i=1
    indexWindows=[]
    for win in windows:
        indexWindows.append(i)
        i+=1
    with ThreadPoolExecutor() as executor:
        executor.map(GreenThread, indexWindows)