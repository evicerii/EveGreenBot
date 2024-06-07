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
            if (sum(pag.pixel(CheckAnomalyCoordFirst[0], CheckAnomalyCoordFirst[1])) == CheckAnomalyCoordFirstValue[0] and sum(pag.pixel(CheckAnomalyCoordSecond[0], CheckAnomalyCoordSecond[1])) == CheckAnomalyCoordSecondValue[0]) or (sum(pag.pixel(CheckAnomalyCoordFirst[0], CheckAnomalyCoordFirst[1])) == CheckAnomalyCoordFirstValue[1] and sum(pag.pixel(CheckAnomalyCoordSecond[0], CheckAnomalyCoordSecond[1])) == CheckAnomalyCoordSecondValue[1]) or (sum(pag.pixel(CheckAnomalyCoordFirst[0], CheckAnomalyCoordFirst[1])) == CheckAnomalyCoordFirstValue[2] and sum(pag.pixel(CheckAnomalyCoordSecond[0], CheckAnomalyCoordSecond[1])) == CheckAnomalyCoordSecondValue[2]):
                self.WarpAnomalyAction()
                super().CheckWarp()
                self.OccupiedAnomaly(self.hwnd)
                break
            elif sum(pag.pixel(CheckLastAnomalyCoord[0], CheckLastAnomalyCoord[1])) == CheckLastAnomalyValue:
                self.HideAnomaly()
            else:
                return False
            time.sleep(1)
    def OccupiedAnomaly(self, hwnd):
        PvPWin.takeActive()
        if sum(pag.pixel(OccupiedAnomalyCoord[0], OccupiedAnomalyCoord[1])) == OccupiedAnomalyValue:
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
StructureNav=owerWin('structure',4)
PvPWin=owerWin('test',5)


LocalChatClass=ChatWindows('localchat', LocalChat)