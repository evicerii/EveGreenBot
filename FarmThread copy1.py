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

WinThreadArray = []

def CheckLocalFunc(LockCheckWarp):
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                #Если корабль не в варпе установить флаг чата
                if not LockCheckWarp.is_set():
                    CheckLocalEvent.set()
                    logging.info(f'local red')
                    time.sleep(1)
                    break
            else:
                if EndCyrcle.is_set():
                    CheckLocalEvent.set()
                    DockAllWindows(AllDockLock)
                    logging.info(f'CheckLocalFunc stop')
                    return
                CheckLocalEvent.clear()
def DockAllWindows(AllDockLock, DockEvent):
    AllDockLock.acquire()
    for win in windows.keys():
        WindowsClassArray[win-1].TakeWinActive()
        time.sleep(3)
        DockEvent.set()
        time.sleep(1)
    AllDockLock.release()
    return
def ShieldStatus(ship, UndockEvent, DronesLaunchedEvent, ShieldStatusEvent):
    while True:
        if EndCyrcle.is_set():
            logging.info(f'ShieldStatus stop')
            return
        UndockEvent.wait()
        DronesLaunchedEvent.wait()
        ship.DangerShield(ShieldStatusEvent)
        time.sleep(1)
def BotExit() :
    time.sleep(int(config.get('General','workTime'))*60+(random.randint(0,50))*6)
    EndCyrcle.set()
    logging.info(f'BotExit stop')
    return
def ShipDestroy(ShieldStatusEvent):
    while True:
        ShieldStatusEvent.wait()
        if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
            EndCyrcle.set()
            logging.info(f'ShipDestroy stop')
            return

class WinThread():
    def __init__(self, WinKeys, AShip):
        self.ship = AShip
        self.ActiveThread = WinKeys-1
        self.UndockEvent = threading.Event()
        self.DockEvent = threading.Event()
        self.StartFarmEvent = threading.Event()

        self.ActiveDefModuleEvent = threading.Event()
        self.DronesLaunchedEvent = threading.Event()
        
        self.StartFarmEvent.set()
    def StartFarm(self):
        if CheckLocalEvent.is_set():
            time.sleep(random.randint(3000,3600)/10)
            self.StartFarm()
        else:
            WindowsClassArray[self.ActiveThread].TakeWinActive()
            self.ship.Undock()
            self.UndockEvent.set()
            if self.CheckLocalEvent.is_set():
                self.DockEvent.set()
                return
            else:
                WindowsClassArray[self.ActiveThread].TakeWinActive()
                self.ship.ActiveDefModule(self.ActiveDefModuleEvent)
                return
    def BotLoop(self, LockCheckWarp):
        if not self.ActiveDefModuleEvent.is_set():
            return
        WindowsClassArray[self.ActiveThread].TakeWinActive()
        time.sleep(5)
        GreenAnomaly.SelectAnomaly(LockCheckWarp, self.DockEvent)
        if self.DockEvent.is_set():
            return
        if CheckLocalEvent.is_set():
            self.DockEvent.set()
            return
        #Флаг запущенных дронов
        WindowsClassArray[self.ActiveThread].TakeWinActive()
        self.ship.LaunchDrns()
        self.DronesLaunchedEvent.set()
        Structure.takeActive()
        self.ship.OrbitTarget(FirstTarget)
        ################################
        Farm.takeActive()
        while True:
            if CheckNothingFound():
                logging.info(f'red cross not detected')
                WindowsClassArray[self.ActiveThread].TakeWinActive()
                self.ship.ReturnDrns()
                break
            time.sleep(5)
            if CheckLocalEvent.is_set():
                time.sleep(1)
                self.DockEvent.set()
                break
        if self.DockEvent.is_set():
            return  
        logging.info(f'BotLoop end cyrcle')
        time.sleep(random.randint(600,650)/10)
    def StopFarm(self):
        self.DockEvent.clear()
        #Если корабль андокнулся
        if self.UndockEvent.is_set():
            self.UndockEvent.clear()
            #Если дроны запущены вернуть
            if self.DronesLaunchedEvent.is_set():
                WindowsClassArray[self.ActiveThread].TakeWinActive()
                self.ship.ReturnDrns()
                self.DronesLaunchedEvent.clear()
                self.ActiveDefModuleEvent.clear()
            WindowsClassArray[self.ActiveThread].TakeWinActive()
            self.ship.Dock()
        time.sleep(random.randint(3000,3600)/10)
    def EndCyrcle(self):
        if EndCyrcle.is_set():
            logging.info(f'finish')
            self.DockEvent.set()
            return

CheckLocalEvent = threading.Event()
EndCyrcle = threading.Event()

LockCheckWarp=threading.Lock()
AllDockLock = threading.Lock()

GetPIDList(ProcessName)
for NumberWin, pid in enumerate(pidsArray, 1):
    GetHWID(NumberWin, pid)
#во всех окнах
for win in windows.keys():
    WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    WinThreadArray.append(WinThread(win, Ship))

CheckLocalThread = threading.Thread(target=CheckLocalFunc, args=(LockCheckWarp,), daemon=True)
BotExitThread = threading.Thread(target=BotExit)

threads = [CheckLocalThread, BotExitThread]

[p.start() for p in threads]