from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from Classes.WinAction import Character

class owerWin(Character):
    def __init__(self, name, number):
        self.name = name
        self.number = number-1
    def takeActive(self):
        owerWindow = [OwerWindow1, OwerWindow2, OwerWindow3, OwerWindow4, OwerWindow5, OwerWindow6]
        mouseMove(owerWindow[self.number].x,owerWindow[self.number].y)
        click()
    
    @logs
    def RareLoot(self, ship):
        self.takeActive()
        #if есть доми врек
        #   mouseMove()
        #   click()
        #   ship.SelectItemThirdAction()
        #   ship.LootAll()
    def checkElement(self):
        ...
class AnomalyWin(Character):
    def __init__(self, name, number, hwnd):
        self.name = name
        super().__init__(number, hwnd)
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
    def SelectAnomaly(self):
        while True:
            name = cvName(FirstAnomalyCoord)
            if name in AnomalyList:
                self.WarpAnomalyAction()
                super().CheckWarp()
                self.OccupiedAnomaly(self.hwnd)
                break
            elif name=='':
                return False
            else:
                self.HideAnomaly()
            time.sleep(1)
    def OccupiedAnomaly(self, hwnd):
        PvPWin.takeActive()
        if sum(pag.pixel(1365,320)) == 765:
            logging.info(f'Occupied Anomaly')
            self.HideAnomaly()
            self.SelectAnomaly(hwnd)
class ChatWindows(Character):
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
    def takeActive(self):
        mouseMove(self.coordinates.x,self.coordinates.y)
        click()
    def CheckChatEnemy(self):
        #первая иконка
        ...

Nav=owerWin('nav',1)
Farm=owerWin('farm',2)
Loot=owerWin('loot',3)
Structure=owerWin('structure',4)
PvPWin=owerWin('test',5)


LocalChatClass=ChatWindows('localchat', LocalChat)