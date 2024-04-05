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
    @logs
    def SelectAnomaly(self):
        Temp=green['FirstAnomalyCoord']
        for a in range(0,10):
            name = cvName(green['FirstAnomalyCoord'])
            if name in green['AnomalyList']:
                mouseMove(FirstAnomalyWarp.x,FirstAnomalyWarp.y+(a)*20)
                click()
                CheckWarp()
                green['FirstAnomalyCoord']=Temp
                break
            else:
                green['FirstAnomalyCoord'][1]=green['FirstAnomalyCoord'][1]+20
                print(f'{datetime.datetime.now()} {name} not found')
    def checkElement(self):
        ...

Nav=owerWin('nav',1)
Farm=owerWin('farm',2)
Loot=owerWin('loot',3)
Structure=owerWin('structure',4)
Test=owerWin('test',5)
AnomalyWin=owerWin('anomaly',6)