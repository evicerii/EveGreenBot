from FarmThread import *
from adds.WinAction import *

from concurrent.futures import ThreadPoolExecutor

WindowsClassArray = []

if __name__ == '__main__':
    # os.system(f'C:/Users/{os.getlogin()}/AppData/Local/eve-online/eve-online.exe')
    # time.sleep(30)
    # mouseMove(LaunchWindow.x, LaunchWindow.y)
    # click()
    # time.sleep(60)
    GetPIDList(ProcessName)
    for NumberWin, pid in enumerate(pidsArray, 1):
        GetHWID(NumberWin, pid)
    #во всех окнах
    # for win in windows.keys():
    #     WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    #     WindowsClassArray[win-1].TakeWinActive()
    #     time.sleep(6)
    #     mouseMove(LocalChat.x, LocalChat.y)
    #     click()
    #     Gila.Undock()
    #     time.sleep(10)
    #     Gila.Dock()

    with ThreadPoolExecutor() as executor:
        executor.map(runThread, windows.keys())