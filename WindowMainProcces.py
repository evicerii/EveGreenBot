import threading

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

def CheckLocal():
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
        time.sleep(1)
def ShieldStatus(ship,status):
    while True:
        ship.DangerShield(status)
        time.sleep(1)
def BotExit() :
    ...     
def StopFarm(ship):
    while True:
        time.sleep(1)
        #Если нейтрал в локале и корабль не в варпе
        if DockEvent.is_set():
            #Если корабль андокнулся
            if UndockEvent.is_set():
                #Если дроны запущены вернуть
                if DronesLaunchedEvent.is_set():
                    ship.ReturnDrns()
                ship.Dock()
                print(f'{datetime.datetime.now()} ship dock')
            time.sleep(120)
            DockEvent.clear()
            print('Stopping Farm')
def BotLoop(ship, ShieldStatusProcess):
    time.sleep(5)
    if CheckLocalEvent.is_set():
        DockEvent.set()
        return
    # Флаг андокнутого корабля
    ship.Undock()
    UndockEvent.set()
    if CheckLocalEvent.is_set():
        DockEvent.set()
        return

    ship.ActiveDefModule()

    while True:
        #select&warp
        AnomalyWin.SelectAnomaly(locker, ship)

        if CheckLocalEvent.is_set():
            DockEvent.set()
            return
        #Флаг запущенных дронов
        ship.LaunchDrns()
        DronesLaunchedEvent.set()

        Structure.takeActive()
        ship.OrbitTarget(FirstTarget)
        Farm.takeActive()
        while True:
            if checkRedCross():
                ...
            else:
                print(f'{datetime.datetime.now()} red cross not detected')
                break
            time.sleep(5)
            if CheckLocalEvent.is_set() or ShieldStatusEvent.is_set():
                DockEvent.set()
                time.sleep(1)
                return
        ship.ReturnDrns()
        print(f'{datetime.datetime.now()} end cyrcle')
        time.sleep(random.randint(60,65))

if __name__ == '__main__':
    CheckLocalEvent = threading.Event()
    ShieldStatusEvent=threading.Event()
    UndockEvent = threading.Event()
    DronesLaunchedEvent = threading.Event()
    locker=threading.Event()
    DockEvent = threading.Event()

    # parent_conn, child_conn = Pipe(duplex=True)
    # BotExitProcess = Process(target=BotExit, args=(BotLoopEvent,))

    CheckLocalProcess = threading.Thread(target=CheckLocal, daemon=True)
    ShieldStatusProcess = threading.Thread(target=ShieldStatus, args=(Gila,ShieldStatusEvent,), daemon=True)
    StopFarmProcess = threading.Thread(target=StopFarm, args=(Gila,))
    BotLoopProcess = threading.Thread(target=BotLoop, args=(Gila, ShieldStatusProcess), daemon=True)


    proc = [CheckLocalProcess, ShieldStatusProcess, StopFarmProcess, BotLoopProcess]
    [p.start() for p in proc]
    [p.join() for p in proc]

    while True:
        if not DockEvent.is_set():
            BotLoopProcess.start()