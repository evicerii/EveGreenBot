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
    print('start checking local')
    while True:
        for n in range(765,953):
            #Проврка тикеров в чате
            if (sum(pag.pixel(318,n))==195 or sum(pag.pixel(318,n))==223 or sum(pag.pixel(318,n))==330):
                #Если корабль не в варпе установить флаг чата
                if not locker.is_set():
                    CheckLocalEvent.set()
                    time.sleep(1)
            else:
                CheckLocalEvent.clear()
        time.sleep(1)
def BotExit() :
    ...     
def StopFarm():
    while True:
        time.sleep(1)
        #Если нейтрал в локале и корабль не в варпе
        if DockEvent.is_set():
            #Если корабль андокнулся
            if UndockEvent.is_set():
                #Если дроны запущены вернуть
                if DronesLaunchedEvent.is_set():
                    Gila.ReturnDrns()
                Gila.Dock(Nav)
            time.sleep(120)
            DockEvent.clear()
            print('Stopping Farm')
def BotLoop():
    time.sleep(5)
    if CheckLocalEvent.is_set():
        DockEvent.set()
        return
    #Флаг андокнутого корабля
    Gila.Undock()
    UndockEvent.set()
    if CheckLocalEvent.is_set():
        DockEvent.set()
        return

    Gila.ActiveDefModule()

    while True:
        #select&warp
        AnomalyWin.SelectAnomaly(locker)

        if CheckLocalEvent.is_set():
            DockEvent.set()
            return
        #Флаг запущенных дронов
        Gila.LaunchDrns()
        DronesLaunchedEvent.set()

        Structure.takeActive()
        Gila.OrbitTarget(FirstTarget)
        Farm.takeActive()
        while True:
            if checkRedCross():
                break
            time.sleep(5)
            if CheckLocalEvent.is_set():
                DockEvent.set()
                return
        Gila.ReturnDrns()
        time.sleep(random.randint(60,65))

if __name__ == '__main__':
    CheckLocalEvent = threading.Event()
    UndockEvent = threading.Event()
    DronesLaunchedEvent = threading.Event()
    locker=threading.Event()
    DockEvent = threading.Event()

    # parent_conn, child_conn = Pipe(duplex=True)
    # BotExitProcess = Process(target=BotExit, args=(BotLoopEvent,))

    CheckLocalProcess = threading.Thread(target=CheckLocal, daemon=True)
    StopFarmProcess = threading.Thread(target=StopFarm)
    BotLoopProcess = threading.Thread(target=BotLoop, daemon=True)
    
    proc = [CheckLocalProcess, StopFarmProcess, BotLoopProcess]
    [p.start() for p in proc]
    [p.join() for p in proc]

    while True:
        if not DockEvent.is_set():
            BotLoopProcess.start()