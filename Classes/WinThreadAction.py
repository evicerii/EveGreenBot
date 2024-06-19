import threading
import logging
import time
from adds.mouseMove.mousemove import *
from Classes.OwerWin import *
from Classes.WinAction import *

WinThreadArray = []


class WinThreadClass(Character):
    def __init__(self, WinKeys, AShip):
        self.ship = AShip
        self.ActiveThread = WinKeys-1
        self.hwnd = WindowsClassArray[WinKeys-1].hwnd

        self.UndockEvent = threading.Event()
        self.LocalChatStatus = threading.Event()
        self.ShieldStatus = threading.Event()
        self.OverWinStatus = threading.Event()
        
        self.TempLock = threading.Lock()
        self.GreenAnomaly=AnomalyWin('green', self.ActiveThread, self.hwnd)
    def StartFarm(self):
        self.LocalChatStatus.clear()
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.hwnd}')
            return
        WindowsClassArray[self.ActiveThread].IMGInvisible()
        ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus, self.hwnd)
        os.remove('temp.jpeg')
        if self.LocalChatStatus.is_set():
            time.sleep(random.randint(3000,3600)/10)
            self.StartFarm()
            if EndCyrcleEvent.is_set():
                logging.info(f'CheckLocalFunc stop')
                return
        else:
            time.sleep(random.randint(20,25)/10)
            ActivateWindow(self.hwnd)
            self.ship.Undock()
            self.UndockEvent.set()
            mouseMove(StopShip.x, StopShip.y)
            click()
        time.sleep(random.randint(20,25)/10)
        WindowsClassArray[self.ActiveThread].IMGInvisible()
        ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus, self.hwnd)    
        os.remove('temp.jpeg')
        if  self.LocalChatStatus.is_set():
            self.ship.Dock()
            self.UndockEvent.clear()
            time.sleep(random.randint(3000,3600)/10)
            self.self.StartFarm()
        else:
            self.ship.ActiveDefModule()
    def BotLoop(self):
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.ActiveThread}')
            return
        while True:
            time.sleep(random.randint(20,25)/10)
            WindowsClassArray[self.ActiveThread].IMGInvisible()
            os.remove('temp.jpeg')
            if self.GreenAnomaly.SelectAnomaly(self.ActiveThread, self.hwnd) == False:
                self.UndockEvent.clear()
                return
            TempLock.acquire()
            WindowsClassArray[self.ActiveThread].IMGInvisible()    
            ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus, self.hwnd)
            os.remove('temp.jpeg')
            if self.LocalChatStatus.is_set():
                TempLock.release()
                return
            ActivateWindow(self.hwnd)
            self.ship.ActivePropModule()
            self.ship.LaunchDrns()
            StructureNav.takeActive()
            self.ship.OrbitTarget(FirstTarget)
            Farm.takeActive()
            TempLock.release()
            time.sleep(random.randint(20,25)/10)
            while True:
                time.sleep(random.randint(20,25)/10)
                WindowsClassArray[self.ActiveThread].IMGInvisible(self.ActiveThread)
                ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus, self.hwnd, self.ActiveThread)
                ScreenClassArray[self.ActiveThread].TakeOverWinStatus(self.OverWinStatus, self.ActiveThread)
                os.remove(f'{self.ActiveThread}.jpeg')
                if self.OverWinStatus.is_set():
                    TempLock.acquire()
                    ActivateWindow(self.hwnd)
                    logging.info(f'red cross not detected  {self.hwnd}')
                    self.ship.ReturnDrns(self.hwnd)
                    TempLock.release()
                    break
                if self.LocalChatStatus.is_set():
                    TempLock.acquire()
                    ActivateWindow(self.hwnd)
                    self.ship.ReturnDrns(self.hwnd)
                    self.OverWinStatus.clear()
                    TempLock.release()
                    return
            time.sleep(1)
            TempLock.acquire()
            self.ship.RareLoot(self.ActiveThread, self.hwnd)
            self.OverWinStatus.clear()
            TempLock.release()
            logging.info(f'BotLoop cyrcle  {self.hwnd}')
            time.sleep(random.randint(600,650)/10)
    def StopFarm(self):
        TempLock.acquire()
        logging.info(f'StopFarm  {self.hwnd}')
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.ActiveThread}')
            TempLock.release()
            return
        time.sleep(random.randint(20,25)/10)
        ActivateWindow(self.hwnd)
        self.ship.Dock()
        TempLock.release()
        
        time.sleep(30)
        TempLock.acquire()
        while CheckTarget(CheckUndockCoord[0],CheckUndockCoord[1],CheckUndockCoord[2])==True:
            time.sleep(random.randint(20,25)/10)
        time.sleep(random.randint(20,25))
        logging.info(f'ShipDock  {self.hwnd}')
        self.UndockEvent.clear()
        mouseMove(ShipCargo.x,ShipCargo.y)
        click()
        self.ship.UploadCargo()
        mouseMove(ShipCargo.x,ShipCargo.y)
        click()
        TempLock.release()
        time.sleep(random.randint(3000,3600)/10)
    def ShipDestroy(self, ShieldStatusEvent):
        while True:
            ShieldStatusEvent.wait()
            if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
                EndCyrcleEvent.set()
                logging.info(f'ShipDestroy stop  {self.hwnd}')
                return
