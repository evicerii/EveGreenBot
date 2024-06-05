import threading
import logging
import time
from adds.mouseMove.mousemove import *
from Classes.OwerWin import *
from Classes.WinAction import *

WinThreadArray = []

EndCyrcleEvent = threading.Event()

class WinThreadClass(Character):
    def __init__(self, WinKeys, AShip):
        self.ship = AShip
        self.ActiveThread = WinKeys-1
        self.hwnd = WindowsClassArray[WinKeys-1].hwnd

        self.UndockEvent = threading.Event()
        self.LocalChatStatus = threading.Event()
        self.ShieldStatus = threading.Event()
        self.OverWinStatus = threading.Event()
        
        self.GreenAnomaly=AnomalyWin('green', self.ActiveThread, self.hwnd)
    def StartFarm(self):
        self.LocalChatStatus.clear()
        logging.info(f'StartFarm  {self.ActiveThread}')
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.ActiveThread}')
            return
        WindowsClassArray[self.ActiveThread].IMGInvisible()
        ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus)
        os.remove('temp.jpeg')
        if self.LocalChatStatus.is_set():
            time.sleep(random.randint(3000,3600)/10)
            self.StartFarm()
            if EndCyrcleEvent.is_set():
                logging.info(f'CheckLocalFunc stop')
        else:
            time.sleep(random.randint(20,25)/10)
            ActivateWindow(self.hwnd)
            self.ship.Undock()
            self.UndockEvent.set()
            mouseMove(StopShip.x, StopShip.y)
            click()
        time.sleep(random.randint(20,25)/10)
        ActivateWindow(self.hwnd)
        WindowsClassArray[self.ActiveThread].IMGInvisible()
        ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus)    
        os.remove('temp.jpeg')
        if  self.LocalChatStatus.is_set():
            self.ship.Dock()
            self.UndockEvent.clear()
            time.sleep(random.randint(3000,3600)/10)
            self.self.StartFarm()
        else:
            self.ship.ActiveDefModule()
    def BotLoop(self):
        logging.info(f'BotLoop  {self.ActiveThread}')
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.ActiveThread}')
            return
        while True:
            time.sleep(random.randint(20,25)/10)
            WindowsClassArray[self.ActiveThread].IMGInvisible()    
            ActivateWindow(self.hwnd)
            os.remove('temp.jpeg')
            if self.GreenAnomaly.SelectAnomaly() == False:
                self.UndockEvent.clear()
                return
            WindowsClassArray[self.ActiveThread].IMGInvisible()    
            ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus)
            os.remove('temp.jpeg')
            if self.LocalChatStatus.is_set():
                return
            self.ship.ActivePropModule()
            self.ship.LaunchDrns()
            Structure.takeActive()
            self.ship.OrbitTarget(FirstTarget)
            Farm.takeActive()
            while True:
                time.sleep(random.randint(20,25)/10)
                WindowsClassArray[self.ActiveThread].IMGInvisible()
                ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus)
                ScreenClassArray[self.ActiveThread].TakeOverWinStatus(self.OverWinStatus)
                os.remove('temp.jpeg')
                if self.OverWinStatus.is_set():
                    ActivateWindow(self.hwnd)
                    logging.info(f'red cross not detected  {self.ActiveThread}')
                    self.ship.ReturnDrns(self.hwnd)
                    break
                if self.LocalChatStatus.is_set():
                    ActivateWindow(self.hwnd)
                    self.ship.ReturnDrns(self.hwnd)
                    self.OverWinStatus.clear()
                    return
            self.OverWinStatus.clear()
            logging.info(f'BotLoop cyrcle  {self.ActiveThread}')
            time.sleep(random.randint(600,650)/10)
    def StopFarm(self):
        logging.info(f'StopFarm  {self.ActiveThread}')
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.ActiveThread}')
            return
        time.sleep(random.randint(20,25)/10)
        ActivateWindow(self.hwnd)
        self.ship.Dock()
        logging.info(f'ShipDock  {self.ActiveThread}')
        self.UndockEvent.clear()
        time.sleep(random.randint(3000,3600)/10)
    def ShipDestroy(self, ShieldStatusEvent):
        while True:
            ShieldStatusEvent.wait()
            if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
                EndCyrcleEvent.set()
                logging.info(f'ShipDestroy stop  {self.ActiveThread}')
                return
