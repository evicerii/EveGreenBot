import multiprocessing
from multiprocessing import Event
from FarmThread import *

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'./_internal/tesseract.exe'

def CheckLocalFunc(CheckLocalEvent, EndCyrcle):
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                #Если корабль не в варпе установить флаг чата
                if not LockCheckWarpEvent.is_set():
                    CheckLocalEvent.set()
                    print(f'{datetime.datetime.now()} local red')
                    break
            else:
                if EndCyrcle.is_set():
                    CheckLocalEvent.set()
                    return
                CheckLocalEvent.clear()
        time.sleep(5)
def ActiveWindow(CheckLocalEvent, EndCyrcle):
    ShieldStatusThread = threading.Thread(target=ShieldStatus, args=(Gila,), daemon=True)
    StartFarmThread = threading.Thread(target=StartFarm, args=(Gila, CheckLocalEvent,), daemon=True)
    BotLoopThread = threading.Thread(target=BotLoop, args=(Gila, CheckLocalEvent,), daemon=True)
    StopFarmThread = threading.Thread(target=StopFarm, args=(Gila,), daemon=True)
    BotExitThread = threading.Thread(target=BotExit, args=(EndCyrcle,))

    threads = [ShieldStatusThread, StartFarmThread, BotLoopThread, StopFarmThread, BotExitThread]

    [p.start() for p in threads]
    [p.join() for p in threads]

if __name__ == '__main__':
    CheckLocalEvent = multiprocessing.Event()
    EndCyrcle = multiprocessing.Event()
    
    CheckLocalProcess = multiprocessing.Process(target=CheckLocalFunc, args=(CheckLocalEvent, EndCyrcle,), daemon=True)
    ActiveWindowProcess = multiprocessing.Process(target=ActiveWindow, args=(CheckLocalEvent,EndCyrcle,))

    proc = []
    CheckLocalProcess.start()
    proc.append(CheckLocalProcess)
    ActiveWindowProcess.start()
    for i in range(0, charQua):
        proc.append(ActiveWindowProcess)
    [p.join() for p in proc]