import threading

from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *

from Classes.ShipClass import *
from Classes.OwerWin import *
from Classes.Anomaly import *
from Classes.Cargo import *

from WindowMainProcces import *

import time
import os

CheckLocalEvent = threading.Event()
DockEvent = threading.Event()
UndockEvent = threading.Event()
DronesLaunchedEvent = threading.Event()
DockEvent.set()
UndockEvent.set()
DronesLaunchedEvent.set()
while True:
# #     if checkRedCross():
# #         print(f'red')
# #     else:
# #         print(f'green')
#     Gila.DangerShield(CheckLocalEvent)
    print(sum(pag.pixel(1586,333)))
    time.sleep(1)
# for n in range(300, 330):
#         if sum(pag.pixel(1359,n))==259:
#             print(f'red')
# StopFarm(Gila, DockEvent, UndockEvent, DronesLaunchedEvent)