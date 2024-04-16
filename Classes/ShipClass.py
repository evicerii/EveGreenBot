from adds.coordinate import *
from adds.script import *
from adds.decorators import *

from Classes.OwerWin import *

class ship:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules
    @logs
    def Undock(self):
            mouseMove(UndockCoordinate.x,UndockCoordinate.y)
            click()
            CheckTarget(894,863,331)
            time.sleep(1)
    @logs
    def WarpTo(self, locker):
        mouseMove(WarpTo.x,WarpTo.y)
        click()
        print(f'{datetime.datetime.now()} start warp')
        CheckWarp(locker)
        print(f'{datetime.datetime.now()} end warp')     
        time.sleep(1) 
    @logs
    def ActivePropModule(self):
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
        time.sleep(1)
    @logs
    def ReturnDrns(self):
        mouseMove(ReturnDrones.x,ReturnDrones.y)
        click()
        time.sleep(1)
        color=...
        time.sleep(3)
        while color==500:
            color=sum(pag.pixel(1529,991))
            print(f'{datetime.datetime.now()} color {color} 2')
            time.sleep(1)
    @logs
    def Dock(self):
        #alt+p = probe window доделать
        Nav.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
        CheckTarget(1763,318,630)
    def DangerShield(self,status):
        time.sleep(1)
        if (700<sum(pag.pixel(935,877))) and (sum(pag.pixel(935,877))<710):
            status.clear()
        else:
            status.set()
Ishtar=ship('Ishtar',2)
Gila=ship('Gila',3)