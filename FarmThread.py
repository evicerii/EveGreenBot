import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.ScreenSubWin import *

from Classes.ShipClass import *
from Classes.OwerWin import *

from datetime import date

#pyinstaller --add-data "tesseract:tesseract" --add-data "config.ini:."  -add-data "logs:logs" farmthread.py

config.read('config.ini')

logging.basicConfig(level=logging.INFO, filename=f'logs/{date.today()}.log', filemode='w')
pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

def CheckLocalFunc():
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                #Если корабль не в варпе установить флаг чата
                if not LockCheckWarpEvent.is_set():
                    CheckLocalEvent.set()
                    logging.info(f'local red')
                    break
            else:
                if EndCyrcle.is_set():
                    CheckLocalEvent.set()
                    return
                CheckLocalEvent.clear()
def ShieldStatus(ship):
    while True:
        DronesLaunchedEvent.wait()
        ship.DangerShield(ShieldStatusEvent)
        logging.info(f'low shield')
        time.sleep(1)
def BotExit() :
    time.sleep(int(config.get('General','workTime'))*60+(random.randint(0,50))*6)
    EndCyrcle.set()
    StartFarmEvent.wait()
    logging.info(f'shut down')
    os.system(f"taskkill /f /PID {os.getpid()}")
def ShipDestroy():
    while True:
        ShieldStatusEvent.wait()
        if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
            logging.info(f'ship destruct')
            os.system(f"taskkill /f /PID {os.getpid()}")
def StartFarm(ship):
    while True:
        StartFarmEvent.wait()
        time.sleep(1)
        StartFarmEvent.clear()
        if not UndockEvent.is_set():
            time.sleep(5)
            if CheckLocalEvent.is_set():
                time.sleep(random.randint(3000,3600)/10)
                StartFarmEvent.set()
            else:
                ship.Undock()
                UndockEvent.set()
                if CheckLocalEvent.is_set():
                    DockEvent.set()
                    time.sleep(1)
                else:
                    ship.ActiveDefModule(ActiveDefModuleEvent)
                    # Флаг андокнутого корабля
                    time.sleep(1)
def BotLoop(ship):
    while True:
        UndockEvent.wait()
        ActiveDefModuleEvent.wait()
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
        ship.LaunchDrns()
        DronesLaunchedEvent.set()
        Structure.takeActive()
        ship.OrbitTarget(FirstTarget)
        Farm.takeActive()
        while True:
            if CheckNothingFound():
                logging.info(f'red cross not detected')
                time.sleep(1)
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
def StopFarm(ship):
    while True:
        DockEvent.wait()
        DockEvent.clear()
        #Если корабль андокнулся
        if UndockEvent.is_set():
            UndockEvent.clear()
            #Если дроны запущены вернуть
            if DronesLaunchedEvent.is_set():
                ship.ReturnDrns()
                DronesLaunchedEvent.clear()
                ActiveDefModuleEvent.clear()
            ship.Dock()
        time.sleep(random.randint(3000,3600)/10)
        StartFarmEvent.set()

ShieldStatusEvent=threading.Event()

UndockEvent = threading.Event()
DockEvent = threading.Event()
StartFarmEvent = threading.Event()

LockCheckWarpEvent=threading.Event()
ActiveDefModuleEvent = threading.Event()
DronesLaunchedEvent = threading.Event()

CheckLocalEvent = threading.Event()
EndCyrcle = threading.Event()
#Блокировать поток пока дроны не вернутся
DronesLock = threading.Lock()

StartFarmEvent.set()

if __name__ == '__main__':
    CheckLocalProcess = threading.Thread(target=CheckLocalFunc, daemon=True)
    ShieldStatusThread = threading.Thread(target=ShieldStatus, args=(Gila,), daemon=True)
    StartFarmThread = threading.Thread(target=StartFarm, args=(Gila,), daemon=True)
    BotLoopThread = threading.Thread(target=BotLoop, args=(Gila,), daemon=True)
    StopFarmThread = threading.Thread(target=StopFarm, args=(Gila,), daemon=True)
    BotExitThread = threading.Thread(target=BotExit)

    threads = [CheckLocalProcess, ShieldStatusThread, StartFarmThread, BotLoopThread, StopFarmThread, BotExitThread]

    [p.start() for p in threads]
    [p.join() for p in threads]