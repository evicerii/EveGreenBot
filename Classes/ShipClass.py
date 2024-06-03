from adds.coordinate import *
from adds.script import *
from adds.decorators import *

from Classes.WinAction import WindowsClassArray
from Classes.OwerWin import *

config.read('config.ini')

class shipClass:
    def __init__(self, name, PropModule, modules):
        self.name = name
        self.PropModule = PropModule
        self.modules = int(modules)
        self.droneBuy = True
        self.SpecialCargo = True
    @logs
    def Undock(self):
            mouseMove(UndockCoordinate.x,UndockCoordinate.y)
            click()
            CheckTarget(894,863,331)
            time.sleep(1)
    @logs
    def WarpTo(self, LockCheckWarpEvent):
        mouseMove(WarpTo.x,WarpTo.y)
        click()
        logging.info(f'start warp')
        CheckWarp(LockCheckWarpEvent)
        logging.info(f'end warp')     
        time.sleep(1) 
    @logs
    def ActivePropModule(self):
        if self.PropModule == 'True':
            mouseMove(f1.x,f1.y)
            click()
        time.sleep(1) 
    @logs
    def ActiveDefModule(self):
        fButton = [f2,f3,f4,f5]
        for a in range(0,self.modules):
            mouseMove(fButton[a].x,fButton[a].y)
            click()
        time.sleep(1)
    @reactionSleepTime
    @logs
    def OrbitTarget(self, target):
        mouseMove(target.x,target.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
        time.sleep(1)
    @reactionSleepTime
    @logs
    def AprochTarget(self):
        mouseMove(SelectItemFirstAction.x,SelectItemFirstAction.y)
        click()
        time.sleep(1)
    @reactionSleepTime
    @logs
    def LockTarget(self):
        mouseMove(LockTarget.x,LockTarget.y)
        click()
        time.sleep(1)
    @reactionSleepTime
    @logs
    def LaunchDrns(self):
        mouseMove(LaunchDrones.x,LaunchDrones.y)
        click()
        time.sleep(3)
        color=sum(pag.pixel(1361,976))
        if color!=101:
            self.LaunchDrns()
    @logs
    def ReturnDrns(self, hwnd):
        mouseMove(ReturnDrones.x,ReturnDrones.y)
        click()
        color=605
        time.sleep(5)
        while color==605:
            WindowsClassArray[0].IMGInvisible()
            pix = Image.open('temp.jpeg').load()
            color=sum(pix[1794, 968])
            time.sleep(1)
        ActivateWindow(hwnd)
    @logs
    def Dock(self):
        Nav.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
    def DangerShield(self, x=983, y=875):
        time.sleep(1)
        if (700<sum(pag.pixel(x,y))) and (sum(pag.pixel(x, y))<750):
            ShieldStatusVar = False
        else:
            logging.info(f'low shield')
            ShieldStatusVar = True
    def OpenCargo(self):
        mouseMove(ShipCargo.x,ShipCargo.y)
        click()
        time.sleep(1)
    def SelectChipCargo(self):
        mouseMove()
        click()
    @logs
    def LootAll(self):
        mouseMove(WreckLootAll.x,WreckLootAll.y)
        click()
        time.sleep(1)
    @logs
    def UploadCargo(self):
        mouseMove(SelectAllField.x,SelectAllField.y)
        rightClick()
        SelectAll=boxRelCoordinate(RightFirstRow)
        mouseMove(SelectAll.x,SelectAll.y)
        click()
        mouseMove(FirstItem.x,FirstItem.y)
        dragNdrop(Hangars.x,Hangars.y)  
        
Ship = shipClass(config.get('UseShip','ShipName'), config.get('UseShip','PropModule'), config.get('UseShip','DefModule'))

