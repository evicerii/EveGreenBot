import win32gui
from numpy import *
import json

with open('./adds/Value/general.json',"r",encoding="utf-8") as json_file:
    general = json.load(json_file)
with open('./adds/Value/green.json',"r",encoding="utf-8") as json_file:
    green = json.load(json_file)

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

#Static Coordinate
UndockCoordinate=boxCoordinate(general['Undock'])
WarpTo=boxCoordinate(general['WarpTo'])
LockTarget=boxCoordinate(general['LockTarget'])
SelectItemFirstAction=boxCoordinate(general['SelectItemFirstAction'])
SelectItemThirdAction=boxCoordinate(general['SelectItemThirdAction'])
FirstTarget=boxCoordinate(general['FirstTarget'])
FirstItem=boxCoordinate(general['FirstItem'])
SelectAllField=boxCoordinate(general['SelectAllField'])
# NavOwerWindow=boxCoordinate(general['NavOwerWindow'])
f1=boxCoordinate(general['f1'])
f2=boxCoordinate(general['f2'])
f3=boxCoordinate(general['f3'])
f4=boxCoordinate(general['f4'])
f5=boxCoordinate(general['f5'])
f6=boxCoordinate(general['f6'])

OwerWindow1=boxCoordinate(general['OwerWindow1'])
OwerWindow2=boxCoordinate(general['OwerWindow2'])
OwerWindow3=boxCoordinate(general['OwerWindow3'])
OwerWindow4=boxCoordinate(general['OwerWindow4'])
OwerWindow5=boxCoordinate(general['OwerWindow5'])
OwerWindow6=boxCoordinate(general['OwerWindow6'])


Dock=boxCoordinate(general['Dock'])
DockMark=boxCoordinate(general['DockMark'])
StationWin=boxCoordinate(general['StationWin'])
Station=boxCoordinate(general['Station'])
Hangars=boxCoordinate(general['Hangars'])
ShipHangar=boxCoordinate(general['ShipHangar'])
ShipSearch=boxCoordinate(general['ShipSearch'])
ActualShip=boxCoordinate(general['ActualShip'])
HangarCargo=boxCoordinate(general['HangarCargo'])
LaunchDrones=boxCoordinate(general['LaunchDrones'])
ReturnDrones=boxCoordinate(general['ReturnDrones'])
LaunchWin=boxCoordinate(general['LaunchWin'])
CloseEve=boxCoordinate(general['CloseEve'])

AnomalyCoord=boxCoordinate(green['AnomalyCoord'])
FirstAnomalyWarp=boxCoordinate(green['FirstAnomalyWarp'])