from adds.coordinate import *
from adds.script import *
from adds.decorators import *

from Classes.OwerWin import *

config.read('config.ini')

class shipClass:
    def __init__(self, name, PropModule, modules):
        self.name = name
        self.PropModule = PropModule
        self.modules = int(modules)
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
        if self.PropModule == True:
            mouseMove(f1.x,f1.y)
            click()
        time.sleep(1) 
    @logs
    def ActiveDefModule(self, ActiveDefModuleEvent):
        fButton = [f2,f3,f4,f5]
        for a in range(0,self.modules):
            mouseMove(fButton[a].x,fButton[a].y)
            click()
        time.sleep(1)
        ActiveDefModuleEvent.set()
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
        time.sleep(1)
    @logs
    def ReturnDrns(self):
        mouseMove(ReturnDrones.x,ReturnDrones.y)
        click()
        color=508
        time.sleep(3)
        while color==508:
            color=sum(pag.pixel(1531,991))
            time.sleep(1)
    @logs
    def Dock(self):
        #alt+p = probe window доделать
        Nav.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
    def DangerShield(self,ShieldStatusEvent, x=983, y=875):
        time.sleep(1)
        if (700<sum(pag.pixel(x,y))) and (sum(pag.pixel(x, y))<750):
            ShieldStatusEvent.clear()
        else:
            logging.info(f'low shield')
            ShieldStatusEvent.set()

Ship = shipClass(config.get('UseShip','ShipName'), config.get('UseShip','PropModule'), config.get('UseShip','DefModule'))

