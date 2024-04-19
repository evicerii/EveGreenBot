import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *

from Classes.ShipClass import *
from Classes.OwerWin import *

def CheckLocalFunc(CheckLocalEvent, locker, EndCyrcle):
    while True:
        #первая иконка
        for n in range(775,953,17):
            #Проврка тикеров в чате /red,orange,grey
            if (pag.pixel(322,n)==(117, 10, 10) or pag.pixel(322,n)==(153, 60, 10) or pag.pixel(322,n)==(110,110,110)):
                #Если корабль не в варпе установить флаг чата
                if not locker.is_set():
                    CheckLocalEvent.set()
                    print(f'{datetime.datetime.now()} local red')
                    break
            else:
                if EndCyrcle.is_set():
                    CheckLocalEvent.set()
                    return
                CheckLocalEvent.clear()
        time.sleep(5)
def ShieldStatus(ship,ShieldStatusEvent,DronesLaunchedEvent):
    while True:
        DronesLaunchedEvent.wait()
        ship.DangerShield(ShieldStatusEvent)
        time.sleep(1)
def BotExit(StartFarmEvent, EndCyrcle) :
    time.sleep(workTime*60+(random.randint(0,50))*6)
    EndCyrcle.set()
    StartFarmEvent.wait()
    print(f'{datetime.datetime.now()} shut down')
    os.system(f"taskkill /f /PID {os.getpid()}")
def StartFarm(ship, UndockEvent, DockEvent, StartFarmEvent):
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
                    ship.ActiveDefModule()
                    # Флаг андокнутого корабля
                    time.sleep(1)
def BotLoop(ship, CheckLocalEvent, DockEvent, UndockEvent, DronesLaunchedEvent, ShieldStatusEvent, locker):
    while True:
        UndockEvent.wait()
        time.sleep(5)
        AnomalyWin.SelectAnomaly(locker, DockEvent)
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
                DockEvent.set()
                break
        if DockEvent.is_set():
            time.sleep(1)
            continue   
        print(f'{datetime.datetime.now()} BotLoop end cyrcle')
        time.sleep(random.randint(600,650)/10)
def StopFarm(ship, DockEvent, UndockEvent, DronesLaunchedEvent, StartFarmEvent):
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
            ship.Dock()
        time.sleep(random.randint(3000,3600)/10)
        StartFarmEvent.set()

if __name__ == '__main__':
    CheckLocalEvent = threading.Event()
    ShieldStatusEvent=threading.Event()

    UndockEvent = threading.Event()
    DockEvent = threading.Event()
    StartFarmEvent = threading.Event()

    locker=threading.Event()
    DronesLaunchedEvent = threading.Event()

    EndCyrcle = threading.Event()
    #Блокировать поток пока дроны не вернутся
    DronesLock = threading.Lock()

    StartFarmEvent.set()
    # parent_conn, child_conn = Pipe(duplex=True)
    # BotExitProcess = Process(target=BotExit, args=(BotLoopEvent,))

    CheckLocalProcess = threading.Thread(target=CheckLocalFunc, args=(CheckLocalEvent,locker, EndCyrcle,), daemon=True)
    ShieldStatusProcess = threading.Thread(target=ShieldStatus, args=(Gila,ShieldStatusEvent,DronesLaunchedEvent,), daemon=True)
    StartFarmProcess = threading.Thread(target=StartFarm, args=(Gila, UndockEvent, DockEvent, StartFarmEvent,), daemon=True)
    BotLoopProcess = threading.Thread(target=BotLoop, args=(Gila, CheckLocalEvent, DockEvent, UndockEvent, DronesLaunchedEvent, ShieldStatusEvent, locker,), daemon=True)
    StopFarmProcess = threading.Thread(target=StopFarm, args=(Gila, DockEvent, UndockEvent, DronesLaunchedEvent, StartFarmEvent,), daemon=True)
    BotExitProcess = threading.Thread(target=BotExit, args=(StartFarmEvent, EndCyrcle,))

    proc = [CheckLocalProcess, ShieldStatusProcess, StartFarmProcess, BotLoopProcess, StopFarmProcess, BotExitProcess]
    [p.start() for p in proc]
    [p.join() for p in proc]