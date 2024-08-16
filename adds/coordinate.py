import win32gui
from numpy import *
# from adds.Value.HDPlus import *
import configparser
from ctypes  import *
ScreenX = windll.user32.GetSystemMetrics(0)
ScreenY = windll.user32.GetSystemMetrics(1)


class boxCoordinate:
    def __init__(self, data):
        self.x = random.randint(data[0], data[1])
        self.y = random.randint(data[2], data[3])

class boxRelCoordinate:
    def __init__(self, data):
        x = random.randint(data[0], data[1])
        y = random.randint(data[2], data[3])
        flags, hcursor, (startX, startY) = win32gui.GetCursorInfo()
        self.x=x+startX
        self.y=y+startY
if ScreenX==1920 and ScreenY==1080:
    from adds.Value.FHD import *
    #Static Coordinate
    UndockCoordinate=boxCoordinate(Undock)
    UndockCoordinate1=boxCoordinate(Undock1)
    # WarpTo=boxCoordinate(WarpTo)
    SelectItemFirstAction=boxCoordinate(SelectItemFirstAction)
    SelectItemThirdAction=boxCoordinate(SelectItemThirdAction)
    SelectItemFourthAction=boxCoordinate(SelectItemFourthAction)
    SelectItemFifthAction=boxCoordinate(SelectItemFifthAction)
    FirstTarget=boxCoordinate(FirstTarget)
    WreckLootAll=boxCoordinate(WreckLootAll)
    # NavOwerWindow=boxCoordinate(NavOwerWindow)
    f1=boxCoordinate(f1)
    f2=boxCoordinate(f2)
    f3=boxCoordinate(f3)
    f4=boxCoordinate(f4)
    f5=boxCoordinate(f5)
    f6=boxCoordinate(f6)

    StopShip=boxCoordinate(StopShip)

    OwerWindow1=boxCoordinate(OwerWindow1)
    OwerWindow2=boxCoordinate(OwerWindow2)
    OwerWindow3=boxCoordinate(OwerWindow3)
    OwerWindow4=boxCoordinate(OwerWindow4)
    OwerWindow5=boxCoordinate(OwerWindow5)
    OwerWindow6=boxCoordinate(OwerWindow6)

    LocalChat=boxCoordinate(LocalChatValue)

    # Dock=boxCoordinate(Dock)
    # DockMark=boxCoordinate(DockMark)
    # StationWin=boxCoordinate(StationWin)
    # Station=boxCoordinate(Station)
    # ShipHangar=boxCoordinate(ShipHangar)
    # ShipSearch=boxCoordinate(ShipSearch)
    # ActualShip=boxCoordinate(ActualShip)
    # HangarCargo=boxCoordinate(HangarCargo)
    LaunchDrones=boxCoordinate(LaunchDrones)
    ReturnDrones=boxCoordinate(ReturnDrones)
    AgreDrones=boxCoordinate(AgreDrones)
    
    LaunchWin=boxCoordinate(LaunchWin)
    CloseEve=boxCoordinate(CloseEve)

    ShipCargo = boxCoordinate(ShipCargo)
    FirstItem=boxCoordinate(FirstItem)
    SelectAllField=boxCoordinate(SelectAllField)
    Hangars=boxCoordinate(Hangars)

    FittingCoord = boxCoordinate(FittingCoord)
    AnomalyCoord=boxCoordinate(AnomalyCoord)
    # FirstAnomalyWarp=boxCoordinate(FirstAnomalyWarp)
    # IfFirstAnomalyWarp=boxCoordinate(IfFirstAnomalyWarp)

    LaunchWindow=boxCoordinate(LaunchwindowValue)
    
    launchWinsCoords = boxCoordinate(launchWins)
    DropWindow = boxCoordinate(DropWindow)
# elif ScreenX==1600 and ScreenY==800:
#     UndockCoordinate=boxCoordinate(Undock)
#     WarpTo=boxCoordinate(WarpTo)
#     LockTarget=boxCoordinate(LockTarget)
#     SelectItemFirstAction=boxCoordinate(SelectItemFirstAction)
#     SelectItemThirdAction=boxCoordinate(SelectItemThirdAction)
#     SelectItemFourthAction=boxCoordinate(SelectItemFourthAction)
#     FirstTarget=boxCoordinate(FirstTarget)
#     FirstItem=boxCoordinate(FirstItem)
#     WreckLootAll=boxCoordinate(WreckLootAll)
#     SelectAllField=boxCoordinate(SelectAllField)
#     # NavOwerWindow=boxCoordinate(NavOwerWindow)
#     f1=boxCoordinate(f1)
#     f2=boxCoordinate(f2)
#     f3=boxCoordinate(f3)
#     f4=boxCoordinate(f4)
#     f5=boxCoordinate(f5)
#     f6=boxCoordinate(f6)

#     StopShip=boxCoordinate(StopShip)

#     OwerWindow1=boxCoordinate(OwerWindow1)
#     OwerWindow2=boxCoordinate(OwerWindow2)
#     OwerWindow3=boxCoordinate(OwerWindow3)
#     OwerWindow4=boxCoordinate(OwerWindow4)
#     OwerWindow5=boxCoordinate(OwerWindow5)
#     OwerWindow6=boxCoordinate(OwerWindow6)

#     LocalChat=boxCoordinate(LocalChatValue)

#     Dock=boxCoordinate(Dock)
#     DockMark=boxCoordinate(DockMark)
#     StationWin=boxCoordinate(StationWin)
#     Station=boxCoordinate(Station)
#     Hangars=boxCoordinate(Hangars)
#     ShipHangar=boxCoordinate(ShipHangar)
#     ShipSearch=boxCoordinate(ShipSearch)
#     ActualShip=boxCoordinate(ActualShip)
#     HangarCargo=boxCoordinate(HangarCargo)
#     LaunchDrones=boxCoordinate(LaunchDrones)
#     ReturnDrones=boxCoordinate(ReturnDrones)
#     LaunchWin=boxCoordinate(LaunchWin)
#     CloseEve=boxCoordinate(CloseEve)

#     ShipCargo = boxCoordinate(ShipCargo)

#     AnomalyCoord=boxCoordinate(AnomalyCoord)
#     FirstAnomalyWarp=boxCoordinate(FirstAnomalyWarp)
#     IfFirstAnomalyWarp=boxCoordinate(IfFirstAnomalyWarp)

#     LaunchWindow=boxCoordinate(LaunchwindowValue)