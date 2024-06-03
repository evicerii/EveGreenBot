from FarmThread import *
from Classes.WinAction import *
from concurrent.futures import ThreadPoolExecutor

#pyinstaller --add-data "tesseract:tesseract" --add-data "config.ini:."  --add-data "logs:logs" main.py

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
    # mouseMove(LaunchWindow.x, LaunchWindow.y)
    # click()
    # time.sleep(60)
    # GetPIDList(ProcessName)
    # for NumberWin, pid in enumerate(pidsArray, 1):
    #     GetHWID(NumberWin, pid)
    # #во всех окнах
    # for win in windows.keys():
    #     WindowsClassArray[win-1].TakeWinActive()
    #     time.sleep(6)
    #     mouseMove(LocalChat.x, LocalChat.y)
    #     click()
    #     Ship.Undock()
    #     time.sleep(10)
    #     Ship.Dock()
    [p.start() for p in threads]
    with ThreadPoolExecutor() as executor:
        executor.map(GreenThread, windows.keys())