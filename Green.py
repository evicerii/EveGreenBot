import asyncio
from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *

from Classes.ShipClass import Ishtar
from Classes.OwerWin import *
from Classes.Anomaly import *
from Classes.Cargo import *

async def farm(ship):
    ship.Undock()
    AnomalyWin.SelectAnomaly()
    ship.LaunchDrns()
    ship.ActiveModule()
    Structure.takeActive()
    ship.OrbitTarget(FirstTarget)
    Farm.takeActive()
    await asyncio.sleep(60+random.randint(1,60))
    ship.ReturnDrns()
    ship.Dock(Nav)

def DockActive():
    cargo.ClearCargo()

    
async def main():
    while True:
        # nowTime=datetime.datetime.now().hour*60 + datetime.datetime.now().minute
        actualNum = int(asyncio.current_task().get_name())
        if actualNum!=1:
            SelectCharWin(actualNum)

        await farm(Ishtar)

        # worked=nowTime-startTime
        # break
        # if worked>=workTime:
        #     break



async def runBot():
    tasks=[asyncio.create_task(main(), name=x) for x in range (1,charQua+1)]
    for task in tasks:
        await task