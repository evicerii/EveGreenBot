from adds.coordinate import *
from adds.script import *
from adds.decorators import *


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
class AnomalyWin:
    def __init__(self, name):
        self.name = name
    def HideAnomaly(self):
        mouseMove(AnomalyCoord.x,AnomalyCoord.y)
        rightClick()
        IgnoreResult = boxRelCoordinate(IgnoreResultValue)
        mouseMove(IgnoreResult.x,IgnoreResult.y)
        click()
    def WarpAnomalyAction(self):
        mouseMove(AnomalyCoord.x,AnomalyCoord.y)
        rightClick()
        WarpAnomaly = boxRelCoordinate(WarpAnomalyString)
        mouseMove(WarpAnomaly.x,WarpAnomaly.y)
        click()
    @logs
    def SelectAnomaly(self, locker, DockEvent):
        while True:
            name = cvName(FirstAnomalyCoord)
            if name in AnomalyList:
                self.WarpAnomalyAction()
                CheckWarp(locker)
                break
            elif name=='':
                DockEvent.set()
            else:
                self.HideAnomaly()
            time.sleep(1)
     
Nav=owerWin('nav',1)
Farm=owerWin('farm',2)
Loot=owerWin('loot',3)
Structure=owerWin('structure',4)
Test=owerWin('test',5)

GreenAnomaly=AnomalyWin('green')