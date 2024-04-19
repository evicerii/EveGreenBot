import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *

from Classes.ShipClass import *
from Classes.OwerWin import *



def ShieldStatus(ship):
    while True:
        DronesLaunchedEvent.wait()
        ship.DangerShield(ShieldStatusEvent)
        time.sleep(1)
def BotExit(EndCyrcle) :
    time.sleep(workTime*60+(random.randint(0,50))*6)
    EndCyrcle.set()
    StartFarmEvent.wait()
    print(f'{datetime.datetime.now()} shut down')
    os.system(f"taskkill /f /PID {os.getpid()}")
def ShipDestroy():
    while True:
        ShieldStatusEvent.wait()
        if CheckTarget():
            print(f'{datetime.datetime.now()} ship destruct')
            os.system(f"taskkill /f /PID {os.getpid()}")
def StartFarm(ship, CheckLocalEvent):
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
def BotLoop(ship, CheckLocalEvent):
    while True:
        UndockEvent.wait()
        ActiveDefModuleEvent.wait()
        time.sleep(5)
        AnomalyWin.SelectAnomaly(LockCheckWarpEvent, DockEvent)
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
                print(f'{datetime.datetime.now()} red cross not detected')
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
        print(f'{datetime.datetime.now()} BotLoop end cyrcle')
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

#Блокировать поток пока дроны не вернутся
DronesLock = threading.Lock()

StartFarmEvent.set()


