import threading

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

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

#во всех окнах
for win in windows.keys():
    WindowsClassArray.append(Character(win, pidsArray[win-1], windows[win]))
    WinThreadArray.append(WinThreadClass(win, Ship))

def GreenThread(WinKeys):
    ActiveThread = WinKeys - 1
    while True:
        WinThreadArray[ActiveThread].StartFarm()
        WinThreadArray[ActiveThread].BotLoop()
        WinThreadArray[ActiveThread].StopFarm()
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {ActiveThread}')
            return
