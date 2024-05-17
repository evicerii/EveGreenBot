import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.WinAction import *

from Classes.ShipClass import *
from Classes.OwerWin import *

from datetime import date

#pyinstaller --add-data "tesseract:tesseract" --add-data "config.ini:."  -add-data "logs:logs" farmthread.py

config.read('config.ini')

logging.basicConfig(level=logging.INFO, filename=f'logs/{date.today()}.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

def CheckLocalFunc(LockCheckWarpEvent):
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                #Если корабль не в варпе установить флаг чата
                if not LockCheckWarpEvent.is_set():
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
def StartFarm(ship, ActiveThread, StartFarmEvent, UndockEvent, ActiveDefModuleEvent, DockEvent):
    while True:
        StartFarmEvent.wait()
        if EndCyrcle.is_set():
            logging.info(f'StartFarm stop')
            UndockEvent.set()
            ActiveDefModuleEvent.set()
            return
        time.sleep(1)
        StartFarmEvent.clear()
        if not UndockEvent.is_set():
            time.sleep(5)
            if CheckLocalEvent.is_set():
                time.sleep(random.randint(3000,3600)/10)
                StartFarmEvent.set()
            else:
                WindowsClassArray[ActiveThread].TakeWinActive()
                ship.Undock()
                UndockEvent.set()
                if CheckLocalEvent.is_set():
                    DockEvent.set()
                    time.sleep(1)
                else:
                    WindowsClassArray[ActiveThread].TakeWinActive()
                    ship.ActiveDefModule(ActiveDefModuleEvent)
                    # Флаг андокнутого корабля
                    time.sleep(1)
def BotLoop(ship, ActiveThread, UndockEvent, ActiveDefModuleEvent, DockEvent, LockCheckWarpEvent, DronesLaunchedEvent, ShieldStatusEvent):
    while True:
        UndockEvent.wait()
        ActiveDefModuleEvent.wait()
        if EndCyrcle.is_set():
            logging.info(f'BotLoop stop')
            DockEvent.set()
            return
        WindowsClassArray[ActiveThread].TakeWinActive()
        time.sleep(5)
        GreenAnomaly.SelectAnomaly(LockCheckWarpEvent, DockEvent)
        if DockEvent.is_set():
            time.sleep(1)
            continue
        if CheckLocalEvent.is_set():
            DockEvent.set()
            time.sleep(1)
            continue
        #Флаг запущенных дронов
        WindowsClassArray[ActiveThread].TakeWinActive()
        ship.LaunchDrns()
        DronesLaunchedEvent.set()
        Structure.takeActive()
        ship.OrbitTarget(FirstTarget)
        ################################
        Farm.takeActive()
        while True:
            if CheckNothingFound():
                logging.info(f'red cross not detected')
                WindowsClassArray[ActiveThread].TakeWinActive()
                ship.ReturnDrns()
                break
            time.sleep(5)
            if CheckLocalEvent.is_set() or ShieldStatusEvent.is_set():
                time.sleep(1)
                DockEvent.set()
                break
        if DockEvent.is_set():
            time.sleep(1)
            continue   
        logging.info(f'BotLoop end cyrcle')
        time.sleep(random.randint(600,650)/10)
def StopFarm(ship, ActiveThread, DockEvent, UndockEvent, DronesLaunchedEvent, ActiveDefModuleEvent, StartFarmEvent):
    while True:
        DockEvent.wait()
        DockEvent.clear()
        if EndCyrcle.is_set():
            logging.info(f'StopFarm stop')
            return
        #Если корабль андокнулся
        if UndockEvent.is_set():
            UndockEvent.clear()
            #Если дроны запущены вернуть
            if DronesLaunchedEvent.is_set():
                WindowsClassArray[ActiveThread].TakeWinActive()
                ship.ReturnDrns()
                DronesLaunchedEvent.clear()
                ActiveDefModuleEvent.clear()
            WindowsClassArray[ActiveThread].TakeWinActive()
            ship.Dock()
        time.sleep(random.randint(3000,3600)/10)
        StartFarmEvent.set()     


#Блокировать поток пока дроны не вернутся
# DronesLock = threading.Lock()

CheckLocalEvent = threading.Event()
EndCyrcle = threading.Event()

AllDockLock = threading.Lock()

GetPIDList(ProcessName)
for NumberWin, pid in enumerate(pidsArray, 1):
    GetHWID(NumberWin, pid)
#во всех окнах
for win in windows.keys():
    WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    

def runThread(WinKeys):
    ShieldStatusEvent=threading.Event()

    UndockEvent = threading.Event()
    DockEvent = threading.Event()
    StartFarmEvent = threading.Event()

    LockCheckWarpEvent=threading.Event()
    ActiveDefModuleEvent = threading.Event()
    DronesLaunchedEvent = threading.Event()

    StartFarmEvent.set()

    ActiveThread = WinKeys-1
    
    CheckLocalThread = threading.Thread(target=CheckLocalFunc, args=(LockCheckWarpEvent,), daemon=True)
    ShieldStatusThread = threading.Thread(target=ShieldStatus, args=(Ship,UndockEvent, DronesLaunchedEvent, ShieldStatusEvent,), daemon=True)
    StartFarmThread = threading.Thread(target=StartFarm, args=(Ship, ActiveThread, StartFarmEvent, UndockEvent, ActiveDefModuleEvent, DockEvent,), daemon=True)
    BotLoopThread = threading.Thread(target=BotLoop, args=(Ship, ActiveThread, UndockEvent, ActiveDefModuleEvent, DockEvent, LockCheckWarpEvent, DronesLaunchedEvent, ShieldStatusEvent,), daemon=True)
    StopFarmThread = threading.Thread(target=StopFarm, args=(Ship, ActiveThread, DockEvent, UndockEvent, DronesLaunchedEvent, ActiveDefModuleEvent, StartFarmEvent,), daemon=True)
    BotExitThread = threading.Thread(target=BotExit)

    threads = [CheckLocalThread, ShieldStatusThread, StartFarmThread, BotLoopThread, StopFarmThread, BotExitThread]
    
    [p.start() for p in threads]