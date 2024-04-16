from adds.coordinate import *
from adds.script import *
from adds.decorators import *
from .OwerWin import *

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
        DropMTU=boxRelCoordinate(DropMTU)
        mouseMove(DropMTU.x,DropMTU.y)
        click()
    @logs
    def UpMTU(self):
        Loot.takeActive()
        mouseMove(FirstTarget.x,FirstTarget.y)
        rightClick()
        ScopeToCargo=boxRelCoordinate(ScopeToCargo)
        mouseMove(ScopeToCargo.x,ScopeToCargo.y)
        click()
        while True:
            if cvName(NothingFound)=='Nothing Found':
                break
            else:
                time.sleep(5)
    @logs
    def ClearCargo(self):
        mouseMove(SelectAllField.x,SelectAllField.y)
        rightClick()
        SelectAll=boxRelCoordinate(RightFirstRow)
        mouseMove(SelectAll.x,SelectAll.y)
        click()
        mouseMove(FirstItem.x,FirstItem.y)
        dragNdrop(Hangars.x,Hangars.y)       

IshtarCargo=cargo('IshtarCargo')
GilaCargo=cargo('GilaCargo')