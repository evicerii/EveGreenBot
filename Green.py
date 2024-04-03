import asyncio
from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from adds.Value.settings import *
class ship:
    def __init__(self, name):
        self.name = name
        self.acceptMission=...
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
    def ActiveModule(self, module=2):
        fButton = [f1,f2,f3,f4,f5,f6]
        for a in range(0,module):
            mouseMove(fButton[a].x,fButton[a].y)
            click()
    @reactionSleepTime
    @logs
    def OrbitTarget(self):
        mouseMove(OrbitTarget.x,OrbitTarget.y)
        click()
    @reactionSleepTime
    @logs
    def AprochTarget(self):
        mouseMove(AprochTarget.x,AprochTarget.y)
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
    async def afk(self, x, useWin):
        useWin.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        click()
        self.OrbitTarget()
        await asyncio.sleep(x*60+random.randint(1,60))
    @logs
    def Dock(self):
        #alt+p = probe window доделать
        mouseMove(StationWin.x,StationWin.y)
        click()
        mouseMove(DockMark.x,DockMark.y)
        rightClick()
        print(f'{datetime.datetime.now()} dock')
        DockWarpMark=boxRelCoordinate(general['DockWarpMark'])
        mouseMove(DockWarpMark.x,DockWarpMark.y)
        click()
        CheckWarp()
        time.sleep(random.randint(3000,5000)/1000)
        mouseMove(Station.x,Station.y)
        click()
        mouseMove(Dock.x,Dock.y)
        click()
        CheckTarget(1763,318,630)
class owerWin:
    def __init__(self, name, number):
        self.name = name
        self.number = number-1
    def takeActive(self):
        owerWindow = [OwerWindow1, OwerWindow2, OwerWindow3, OwerWindow4, OwerWindow5, OwerWindow6]
        mouseMove(owerWindow[self.number].x,owerWindow[self.number].y)
        click()
    def checkElement(self):
        ...
class cargo:
    def __init__(self, name):
        self.name = name
        self.position =...
    def takeActive(self):
        mouseMove(self.position.x,self.position.y)
        click()
    @logs
    def dropMTU(self):
        mouseMove(FirstItem.x,FirstItem.y)
        rightClick()
        DropItem=boxRelCoordinate(general['RightFirstRow'])
        mouseMove(DropItem.x,DropItem.y)
        click()
    @logs
    def UpMTU(self, usewin):
        mouseMove(usewin.x,usewin.y)
        click()
        mouseMove(FirstItem.x,FirstItem.y)
        rightClick()
    @logs
    def ClearCargo(self):
        mouseMove(SelectAllField.x,SelectAllField.y)
        rightClick()
        SelectAll=boxRelCoordinate(general['RightFirstRow'])
        mouseMove(SelectAll.x,SelectAll.y)
        click()
        mouseMove(FirstItem.x,FirstItem.y)
        dragNdrop(Hangars.x,Hangars.y)       
class Anomaly:
    def __init__(self, name):
        self.name = name
    @logs
    def SelectAnomaly(self):
        Temp=green['FirstAnomalyCoord']
        for AnomalyNumber in range(0,9):
            name = cvName(green['FirstAnomalyCoord'])
            if name in green['AnomalyList']:
                mouseMove(FirstAnomalyWarp.x,FirstAnomalyWarp.y+(AnomalyNumber)*20)
                click()
                CheckWarp()
                green['FirstAnomalyCoord']=Temp
                break
            else:
                green['FirstAnomalyCoord'][1]=green['FirstAnomalyCoord'][1]+20
            
Ishtar=ship('Ishtar')

Nav=owerWin('nav',1)
Farm=owerWin('farm',2)
Loot=owerWin('loot',3)
Test=owerWin('loot',5)

IshtarCargo=cargo('IshtarCargo')
GreenList=Anomaly('GreenList')

async def farm(ship,cargo,anomaly):
    ship.Undock()
    anomaly.SelectAnomaly()
    ship.LaunchDrns()
    ship.ActiveModule()
    # cargo.dropMTU()
    await ship.afk(20, Loot)
    ship.ReturnDrns()
    # cargo.UpMTU()
    ship.Dock()

def DockActive():
    cargo.ClearCargo()

    
async def main():
    while True:
        nowTime=datetime.datetime.now().hour*60 + datetime.datetime.now().minute
        actualNum = int(asyncio.current_task().get_name())
        if actualNum!=1:
            SelectCharWin(actualNum)

        await farm(Ishtar, IshtarCargo, GreenList)

        worked=nowTime-startTime
        break
        if worked>=workTime:
            break



async def runBot():
    tasks=[asyncio.create_task(main(), name=x) for x in range (1,charQua+1)]
    for task in tasks:
        await task
startTime=datetime.datetime.now().hour*60 + datetime.datetime.now().minute

asyncio.run(runBot())