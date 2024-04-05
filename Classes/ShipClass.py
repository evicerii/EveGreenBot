from adds.coordinate import *
from adds.script import *
from adds.decorators import *

class ship:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules
    @logs
    def Undock(self):
        mouseMove(UndockCoordinate.x,UndockCoordinate.y)
        click()
        CheckTarget(894,863,331)
    @logs
    def WarpTo(self):
        mouseMove(WarpTo.x,WarpTo.y)
        click()
        print(f'{datetime.datetime.now()} start warp')
        CheckWarp()
        print(f'{datetime.datetime.now()} end warp')       
    @logs
    def ActiveModule(self):
        fButton = [f1,f2,f3,f4,f5,f6]
        for a in range(0,self.modules):
            mouseMove(fButton[a].x,fButton[a].y)
            click()
    @reactionSleepTime
    @logs
    def OrbitTarget(self, target):
        mouseMove(target.x,target.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
    @reactionSleepTime
    @logs
    def AprochTarget(self):
        mouseMove(SelectItemFirstAction.x,SelectItemFirstAction.y)
        click()
    @reactionSleepTime
    @logs
    def LockTarget(self):
        mouseMove(LockTarget.x,LockTarget.y)
        click()
    @reactionSleepTime
    @logs
    def LaunchDrns(self):
        mouseMove(LaunchDrones.x,LaunchDrones.y)
        click()
    @logs
    def ReturnDrns(self):
        mouseMove(ReturnDrones.x,ReturnDrones.y)
        click()
        
        time.sleep(2)
        color=500
        while color==500:
            color=sum(pag.pixel(1529,991))
            time.sleep(1)
    @logs
    def Dock(self, useWin):
        #alt+p = probe window доделать
        useWin.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        mouseMove(SelectItemThirdAction.x,SelectItemThirdAction.y)
        click()
        CheckWarp()
        time.sleep(random.randint(3000,5000)/1000)
        CheckTarget(1763,318,630)

Ishtar=ship('Ishtar',2)