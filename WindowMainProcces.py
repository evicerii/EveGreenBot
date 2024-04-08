from multiprocessing import Process, Pipe, Event
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

def CheckLocal(event):
    while True:
        time.sleep(1)
        if cvName(general['CheckLocal'])=="Local":
            event.clear()
        else:
            event.set()
            print('dunger')
def BotExit() :
    ...     
def StopFarm(connection, CheckLocal, ProcessKill, UndockEvent, DronsLaunched, ship):
    FarmPID=...
    while True:
        time.sleep(5)

        while True:
            if FarmPID != 0:
                FarmPID = connection.recv()
                print(FarmPID)
            else:
                break

        #Если нейтрал в локале
        if CheckLocal.is_set():
            #Если корабль андокнулся
            if UndockEvent.is_set():
                os.system(f"taskkill /PID {FarmPID} /T /F")
                FarmPID=0
                #Если дроны запущены вернуть
                if DronsLaunched.is_set():
                    ship.ReturnDrns()

            ship.Dock(Nav)
            time.sleep(120)
            #Добавить флаг убитого процесса
            ProcessKill.set()
def BotLoop(connection, ProcessKill, UndockFlag, CheckDrons, ship):
    #Убирает флаг убитого процесса
    ProcessKill.clear()

    connection.send(os.getpid())
    time.sleep(5)
    #Флаг андокнутого корабля
    ship.Undock()
    UndockFlag.set()

    ship.ActiveDefModule()

    while True:
        #select&warp
        AnomalyWin.SelectAnomaly()
        #Флаг запущенных дронов
        ship.LaunchDrns()
        CheckDrons.set()
        
        ship.ActivePropModule()

        Structure.takeActive()
        ship.OrbitTarget(FirstTarget)
        Farm.takeActive()
        while cvName(general['NothingFound'])!= "Nothing Found":
            time.sleep(5)
        ship.ReturnDrns()

if __name__ == '__main__':
    CheckLocalEvent = Event()
    BotLoopEvent = Event()
    UndockEvent = Event()
    DronesLaunchedEvent = Event()

    parent_conn, child_conn = Pipe(duplex=True)

    CheckLocalProcess = Process(target=CheckLocal, args=(CheckLocalEvent,))
    # BotExitProcess = Process(target=BotExit, args=(BotLoopEvent,))
    StopFarmProcess = Process(target=StopFarm, args=(parent_conn, CheckLocalEvent, BotLoopEvent, UndockEvent, DronesLaunchedEvent, Gila))
    BotLoopProcess = Process(target=BotLoop, args=(child_conn, BotLoopEvent, UndockEvent, DronesLaunchedEvent, Gila))

    proc = [CheckLocalProcess, StopFarmProcess, BotLoopProcess]
    [p.start() for p in proc]
    [p.join() for p in proc]

    while True:
        if BotLoopEvent.is_set():
            BotLoopProcess.start()