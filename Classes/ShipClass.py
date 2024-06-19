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
        time.sleep(1)
        if sum(pag.pixel(Undock[0],Undock[2]))==262 or sum(pag.pixel(Undock[0],Undock[2]))==265:
            mouseMove(UndockCoordinate.x,UndockCoordinate.y)
            click()
        elif sum(pag.pixel(Undock1[0],Undock1[2]))==262 or sum(pag.pixel(Undock1[0],Undock1[2]))==265:
            mouseMove(UndockCoordinate1.x,UndockCoordinate1.y)
            click()
        CheckTarget(CheckUndockCoord[0],CheckUndockCoord[1],CheckUndockCoord[2])
    # @logs
    # def WarpTo(self, LockCheckWarpEvent):
    #     mouseMove(WarpTo.x,WarpTo.y)
    #     click()
    #     logging.info(f'start warp')
    #     # CheckWarp(LockCheckWarpEvent)
    #     logging.info(f'end warp')     
    #     time.sleep(1) 
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
        mouseMove(SelectItemFifthAction.x,SelectItemFifthAction.y)
        click()
        time.sleep(1)
    @reactionSleepTime
    @logs
    def LaunchDrns(self):
        mouseMove(LaunchDrones.x,LaunchDrones.y)
        click()
        time.sleep(3)
        color=sum(pag.pixel(LaunchDrnsCoord[0], LaunchDrnsCoord[1]))
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
            color=sum(pix[ReturnDrnsCoord[0], ReturnDrnsCoord[1]])
            time.sleep(1)
        ActivateWindow(hwnd)
    @logs
    def RareLoot(self, ActiveThread, hwnd):
        Loot.takeActive()
        if (sum(pag.pixel(RareCheckPosFirst[0], RareCheckPosFirst[1])) == RareCheckPosFirtValue) and (sum(pag.pixel(RareCheckPosSecond[0], RareCheckPosSecond[1])) == RareCheckPosSecondValue):
            mouseMove(FirstTarget.x, FirstTarget.y + 24*7)
            click()
            mouseMove(SelectItemThirdAction.x, SelectItemThirdAction.y)
            click()
            while True:
                time.sleep(1)
                WindowsClassArray[ActiveThread].IMGInvisible()
                pix = Image.open('temp.jpeg').load()
                if sum(pix[CargoShipMarkerCoord[0], CargoShipMarkerCoord[1]]) == CargoShipMarkerColor:
                    break
            os.remove('temp.jpeg')
            time.sleep(2)
            ActivateWindow(hwnd)
            mouseMove(WreckLootAll.x,WreckLootAll.y)
            click()
            mouseMove(ShipCargo.x,ShipCargo.y)
            click() 
    @logs
    def Dock(self):
        Nav.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
    @logs
    def UploadCargo(self):
        if sum(pag.pixel(286,414)) == 74:
            return
        mouseMove(SelectAllField.x,SelectAllField.y)
        rightClick()
        SelectAll=boxRelCoordinate(RightFirstRow)
        mouseMove(SelectAll.x,SelectAll.y)
        click()
        mouseMove(FirstItem.x,FirstItem.y)
        dragNdrop(Hangars.x,Hangars.y)  

    # def DangerShield(self, x=983, y=875):
    #     time.sleep(1)
    #     if (700<sum(pag.pixel(x,y))) and (sum(pag.pixel(x, y))<750):
    #         ShieldStatusVar = False
    #     else:
    #         logging.info(f'low shield')
    #         ShieldStatusVar = True
    # def OpenCargo(self):
    #     mouseMove(ShipCargo.x,ShipCargo.y)
    #     click()
    #     time.sleep(1)
    # def SelectChipCargo(self):
    #     mouseMove()
    #     click()
    # @logs
            
Ship = shipClass(config.get('UseShip','ShipName'), config.get('UseShip','PropModule'), config.get('UseShip','DefModule'))

