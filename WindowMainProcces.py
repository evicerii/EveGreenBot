import threading
from queue import Queue

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *

from Classes.ShipClass import *
from Classes.OwerWin import *
from Classes.Anomaly import *
from Classes.Cargo import *

import time
import os

def CheckLocalFunc(CheckLocalEvent, locker):
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
                CheckLocalEvent.clear()
        time.sleep(5)
def ShieldStatus(ship,ShieldStatusEvent,DronesLaunchedEvent):
    while True:
        DronesLaunchedEvent.wait()
        ship.DangerShield(ShieldStatusEvent)
        time.sleep(1)
def BotExit() :
    ...     
def StartFarm(ship, DockEvent, UndockEvent, UndockLock):
    while True:
        if not UndockEvent.is_set():
            time.sleep(5)
            if CheckLocalEvent.is_set():
                DockEvent.set()
                time.sleep(1)
                UndockLock.acquire()
            else:
                ship.Undock()
                if CheckLocalEvent.is_set():
                    DockEvent.set()
                    time.sleep(1)
                    UndockLock.acquire()
                else:
                    ship.ActiveDefModule()
                    # Флаг андокнутого корабля
                    UndockEvent.set()
                    time.sleep(1)
                    UndockLock.acquire()
        time.sleep(300)
def StopFarm(ship, DockEvent, UndockEvent, DronesLaunchedEvent, DronesLock, UndockLock):
    while True:
        DockEvent.wait()
        #Если корабль андокнулся
        if UndockEvent.is_set():
            UndockEvent.clear()
            #Если дроны запущены вернуть
            if DronesLaunchedEvent.is_set():
                ship.ReturnDrns(DronesLock)
                DronesLaunchedEvent.clear()
            ship.Dock()
        time.sleep(120)
        DockEvent.clear()
        UndockLock.release()
def BotLoop(ship, UndockEvent, CheckLocalEvent, DockEvent, DronesLaunchedEvent, ShieldStatusEvent, locker, DronesLock):
    while True:
        UndockEvent.wait()
        time.sleep(1)
        
        if CheckLocalEvent.is_set():
            DockEvent.set()
            time.sleep(1)
            continue

        #select&warp
        AnomalyWin.SelectAnomaly(locker, DockEvent)
        if DockEvent.is_set():
            time.sleep(1)
            continue
        time.sleep(1)

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
                ship.ReturnDrns(DronesLock)
                break
            time.sleep(5)
            if CheckLocalEvent.is_set() or ShieldStatusEvent.is_set():
                DockEvent.set()
                time.sleep(1)
                break
        print(f'{datetime.datetime.now()} end cyrcle')
        time.sleep(random.randint(60,65))

if __name__ == '__main__':
    CheckLocalEvent = threading.Event()
    ShieldStatusEvent=threading.Event()
    UndockEvent = threading.Event()
    DronesLaunchedEvent = threading.Event()
    locker=threading.Event()
    DockEvent = threading.Event()
    #Блокировать поток пока дроны не вернутся
    DronesLock = threading.Lock()
    #Блокировать поток андока корабля
    UndockLock = threading.Lock()
    BotLoopLock = threading.Lock()

    # parent_conn, child_conn = Pipe(duplex=True)
    # BotExitProcess = Process(target=BotExit, args=(BotLoopEvent,))

    CheckLocalProcess = threading.Thread(target=CheckLocalFunc, args=(CheckLocalEvent,locker,), daemon=True)
    ShieldStatusProcess = threading.Thread(target=ShieldStatus, args=(Gila,ShieldStatusEvent,DronesLaunchedEvent,), daemon=True)
    BotLoopProcess = threading.Thread(target=BotLoop, args=(Gila, UndockEvent, CheckLocalEvent, DockEvent, DronesLaunchedEvent, ShieldStatusEvent, locker, DronesLock,), daemon=True)
    StartFarmProcess = threading.Thread(target=StartFarm, args=(Gila, DockEvent, UndockEvent, UndockLock,))
    StopFarmProcess = threading.Thread(target=StopFarm, args=(Gila, DockEvent, UndockEvent, DronesLaunchedEvent, DronesLock, UndockLock,))

    # queue1 = Queue()
    # queue1.put([CheckLocalProcess, ShieldStatusProcess, StopFarmProcess])
    proc = [CheckLocalProcess, ShieldStatusProcess, StartFarmProcess, BotLoopProcess, StopFarmProcess]
    [p.start() for p in proc]
    [p.join() for p in proc]