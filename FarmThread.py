import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from Classes.WinAction import *

from Classes.ShipClass import *
from Classes.OwerWin import *

from datetime import date

config.read('config.ini')

logging.basicConfig(level=logging.INFO, filename=f'logs/{date.today()}.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

LocalChatVar = False
EndCyrcleVar = False
WinThreadArray = []
def CheckLocalFunc(LockCheckWarpEvent):
    print(f'Start Check Local')
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                if not LockCheckWarpEvent.is_set():
                    logging.info(f'local red')
                    LocalChatVar = True
                    time.sleep(1)
                    break
            else:
                if EndCyrcleVar == True:
                    logging.info(f'CheckLocalFunc stop')
                    return
def BotExit() :
    time.sleep(int(config.get('General','workTime'))*60+(random.randint(0,50))*6)
    EndCyrcleVar = True
    logging.info(f'BotExit stop')
    return


class WinThreadClass():
    def __init__(self, WinKeys, AShip):
        self.ship = AShip
        self.ActiveThread = WinKeys-1
        
        self.UndockVar = False
        self.LaunchDronesVar = False
        self.ShieldStatusVar = False
    def StartFarm(self):
        logging.info(f'StartFarm')
        time.sleep(1)
        if LocalChatVar == True:
            time.sleep(random.randint(3000,3600)/10)
            self.StartFarm()
        else:
            TempLock.acquire()
            WindowsClassArray[self.ActiveThread].TakeWinActive()
            time.sleep(1)
            self.ship.Undock()
            UndockVar = True
            if LocalChatVar == True:
                self.ship.Dock()
                UndockVar = False
                time.sleep(random.randint(3000,3600)/10)
                self.self.StartFarm()
            else:
                self.ship.ActiveDefModule()
            TempLock.release()
            time.sleep(1)
    def BotLoop(self, LockCheckWarp):
        logging.info(f'BotLoop')
        TempLock.acquire()
        WindowsClassArray[self.ActiveThread].TakeWinActive()
        time.sleep(1)
        if GreenAnomaly.SelectAnomaly(LockCheckWarp) == False:
            self.ship.Dock()
        if LocalChatVar == True:
            UndockVar = False
            return
        #Флаг запущенных дронов
        self.ship.LaunchDrns()
        LaunchDronesVar = True
        Structure.takeActive()
        self.ship.OrbitTarget(FirstTarget)
        ################################
        Farm.takeActive()
        TempLock.release()
        while True:
            TempLock.acquire()
            WindowsClassArray[self.ActiveThread].TakeWinActive()
            time.sleep(1)
            if CheckNothingFound():
                logging.info(f'red cross not detected')
                self.ship.ReturnDrns()
                LaunchDronesVar = False
                break
            time.sleep(5)
            if LocalChatVar == True:
                UndockVar = False
                break
            TempLock.release()
        logging.info(f'BotLoop end cyrcle')
        time.sleep(random.randint(600,650)/10)
    def StopFarm(self):
        logging.info(f'StopFarm')
        TempLock.acquire()
        WindowsClassArray[self.ActiveThread].TakeWinActive()
        time.sleep(1)
        if self.LaunchDronesVar == True:
            self.ship.ReturnDrns()
            self.LaunchDronesVar == False
        self.ship.Dock()
        TempLock.release()
        time.sleep(random.randint(3000,3600)/10)
    def ShieldStatus(self):
        logging.info(f'Start Shield Status')
        while True:
            if EndCyrcleVar == True:
                logging.info(f'ShieldStatus stop')
                return
            self.ship.DangerShield()
            time.sleep(1)
    def ShipDestroy(ShieldStatusEvent):
        while True:
            ShieldStatusEvent.wait()
            if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
                EndCyrcleVar = True
                logging.info(f'ShipDestroy stop')
                return

GetPIDList(ProcessName)
for NumberWin, pid in enumerate(pidsArray, 1):
    GetHWID(NumberWin, pid)
#во всех окнах
for win in windows.keys():
    WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    WinThreadArray.append(WinThreadClass(win, Ship))

LockCheckWarp = threading.Lock()
TempLock = threading.Lock()
CheckLocalThread =  threading.Thread(target=CheckLocalFunc, args=(LockCheckWarp,))

def GreenThread(WinKeys):
    ActiveThread = WinKeys - 1
    while True:
        if EndCyrcleVar == True:
            logging.info(f'Farm stop')
            return
        WinThreadArray[ActiveThread].StartFarm()
        WinThreadArray[ActiveThread].BotLoop(LockCheckWarp)
        WinThreadArray[ActiveThread].StopFarm()

CheckLocalThread = threading.Thread(target=CheckLocalFunc, args=(LockCheckWarp,), daemon=True)
BotExitThread = threading.Thread(target=BotExit)
threads = [CheckLocalThread, BotExitThread]

[p.start() for p in threads]