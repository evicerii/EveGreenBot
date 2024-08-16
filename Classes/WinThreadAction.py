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
        self.ActiveThread = WinKeys
        self.hwnd = WindowsClassArray[WinKeys].hwnd

        self.UndockEvent = threading.Event()
        self.LocalChatStatus = threading.Event()
        self.ShieldStatus = threading.Event()
        self.OverWinStatus = threading.Event()
        self.DronsLaunchStatus = threading.Event()
        
        self.TempLock = threading.Lock()
        self.GreenAnomaly=AnomalyWin('green', self.ActiveThread, self.hwnd)
    def StartFarm(self):
        self.LocalChatStatus.clear()
        if EndCyrcleEvent.is_set():
            logging.info(f'Farm stop  {self.hwnd}')
            return
        WindowsClassArray[self.ActiveThread].IMGInvisible()
        print(1)
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
            self.ship.Dock(self.DronsLaunchStatus, self.LocalChatStatus)
            self.UndockEvent.clear()
            time.sleep(random.randint(3000,3600)/10)
            self.self.StartFarm()
        else:
            self.ship.ActiveDefModule(self.hwnd)
    def BotLoop(self):
        logging.info(f'BotLoop start {self.hwnd} {self.ActiveThread}')
        while True:
            if EndCyrcleEvent.is_set():
                logging.info(f'Farm stop  {self.ActiveThread}')
                return
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
            self.ship.LaunchDrns(self.DronsLaunchStatus)
            StructureNav.takeActive()
            self.ship.OrbitTarget(FirstTarget)
            Farm.takeActive()
            TempLock.release()
            self.ship.FirstTargetAgreDrones(self.hwnd)
            time.sleep(random.randint(20,25)/10)
            while True:
                time.sleep(random.randint(20,25)/10)
                WindowsClassArray[self.ActiveThread].IMGInvisible(self.ActiveThread)
                ScreenClassArray[self.ActiveThread].TakeLocalStatus(self.LocalChatStatus, self.hwnd, self.ActiveThread)
                ScreenClassArray[self.ActiveThread].TakeOverWinStatus(self.OverWinStatus, self.ActiveThread)
                ScreenClassArray[self.ActiveThread].TakeShieldStatus(self.ShieldStatus, self.ActiveThread)
                os.remove(f'{self.ActiveThread}.jpeg')
                if self.ShieldStatus.is_set():
                    TempLock.acquire()
                    ActivateWindow(self.hwnd)
                    self.ship.ReturnDrns(self.ActiveThread, self.hwnd, self.DronsLaunchStatus, self.LocalChatStatus)
                    logging.info(f'shield status warning {self.hwnd}')
                    self.ShieldStatus.clear()
                    TempLock.release()
                    return
                if self.OverWinStatus.is_set():
                    TempLock.acquire()
                    ActivateWindow(self.hwnd)
                    logging.info(f'red cross not detected  {self.hwnd}')
                    self.ship.ReturnDrns(self.ActiveThread, self.hwnd, self.DronsLaunchStatus, self.LocalChatStatus)
                    TempLock.release()
                    break
                if self.LocalChatStatus.is_set():
                    TempLock.acquire()
                    ActivateWindow(self.hwnd)
                    self.ship.ReturnDrns(self.ActiveThread, self.hwnd, self.DronsLaunchStatus, self.LocalChatStatus)
                    self.OverWinStatus.clear()
                    TempLock.release()
                    return
            time.sleep(1)
            TempLock.acquire()
            self.ship.RareLoot(self.ActiveThread, self.hwnd)
            self.OverWinStatus.clear()
            TempLock.release()
            logging.info(f'BotLoop cyrcle  {self.hwnd}')
            time.sleep(random.randint(30,70)/10)
    def StopFarm(self):
        TempLock.acquire()
        logging.info(f'StopFarm  {self.hwnd}')
        time.sleep(random.randint(20,25)/10)
        ActivateWindow(self.hwnd)
        self.ship.Dock(self.DronsLaunchStatus, self.LocalChatStatus)
        TempLock.release()
        time.sleep(30)
        while True:
            if (sum(pag.pixel(CheckUndockCoord[0],CheckUndockCoord[1]))==CheckUndockCoord[2]):
                time.sleep(random.randint(20,25)/10)
            else:
                TempLock.acquire()
                logging.info(f'ship docking {self.hwnd}')
                time.sleep(random.randint(20,25)/10)
                TempLock.release()
                break
        time.sleep(random.randint(20,25))
        # TempLock.acquire()
        logging.info(f'ShipDock  {self.hwnd}')
        self.UndockEvent.clear()
        # mouseMove(ShipCargo.x,ShipCargo.y)
        # click()
        # self.ship.UploadCargo()
        # mouseMove(ShipCargo.x,ShipCargo.y)
        # click()
        # TempLock.release()
        time.sleep(random.randint(3000,3600)/10)
    def ShipDestroy(self, ShieldStatusEvent):
        while True:
            ShieldStatusEvent.wait()
            if (CheckTarget(1724,321,262) or CheckTarget(1724,321,265)):
                EndCyrcleEvent.set()
                logging.info(f'ShipDestroy stop  {self.hwnd}')
                return
    def relogin(self, numberWin, status):
        tempColor = 0
        WindowsClassArray[numberWin].IMGInvisible('checkActiveWin')
        tempColor = sum(pix[logOff[0],logOff[1]])
        os.remove('checkActiveWin.jpeg')
        mouseMove(DropWindow)
        click()
        if 260<tempColor<270:
            login()
            tempColor = 0
        temp1=[]
        ActualInfoHWID(ProcessName)
        for win in windows:
            temp1.append(windows[win])
        time.sleep(60)
        ActualInfoHWID(ProcessName)
        temp2 = windows
        temp3 = []
        for element in temp2:
            if element not in temp1:
                temp3.append(element)
        while tempColor != 543:
            WindowsClassArray[numberWin].IMGInvisible('checkActiveWin')
            pix = Image.open('checkActiveWin.jpeg').load()
            tempColor = sum(pix[checkLogin[0],checkLogin[1]])
            os.remove('checkActiveWin.jpeg')
            time.sleep(1)
        ActivateWindow(temp3[0])
        time.sleep(3)
        mouseMove(LocalChat.x, LocalChat.y)
        click()
        if status=='dock':
            return
        elif status=='undock':
            Activate2D()
            self.ship.ActiveDefModule()
            super.CheckWarp(numberWin)
            return
        elif status=='dronesLaunched':
            Activate2D()
            self.ship.ActiveDefModule()
            super.CheckWarp(numberWin)
            self.ship.LaunchDrns()
            return
        else:
            self.ship.Dock(self.DronsLaunchStatus)