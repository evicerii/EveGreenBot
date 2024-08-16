from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from Classes.WinAction import *
from Classes.WinThreadAction import *

from Classes.ShipClass import *
from Classes.OwerWin import *
from datetime import date

config.read('config.ini')

logging.basicConfig(level=logging.INFO, filename=f'logs/{date.today()}.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

#во всех окнах
a=0
for win in windows:
    WinThreadArray.append(WinThreadClass(a, Ship))
    a=a+1

def GreenThread(WinKeys):
    ActiveThread = WinKeys - 1
    while True:
        TempLock.acquire()
        WinThreadArray[ActiveThread].StartFarm()
        TempLock.release()
        time.sleep(1)
        WinThreadArray[ActiveThread].BotLoop()
        WinThreadArray[ActiveThread].StopFarm()
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {ActiveThread}')
            return
