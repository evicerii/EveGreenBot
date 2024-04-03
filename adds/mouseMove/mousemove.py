from .brazenhem import *
from ..decorators import reactionSleepTime

@reactionSleepTime
def mouseMove(x4, y4):
    flags, hcursor, (x1,y1) = win32gui.GetCursorInfo()

    x2 = abs(x4 - (x4 - x1)*0.33)
    y2 = abs(y4 - (y4 - y1)*0.33)

    x3 = abs(x4 - (x4 - x1)*0.66)
    y3 = abs(y4 - (y4 - y1)*0.66)

    t=0
    while(t<1.01):
        x = (1-t)**3*x1+3*t*(1-t)**2*x2+3*t**2*(1-t)*x3+t**3*x4
        y = (1-t)**3*y1+3*t*(1-t)**2*y2+3*t**2*(1-t)*y3+t**3*y4
        
        smoothMove(x, y)
        t+=0.01

@reactionSleepTime
def rightClick():
    pag.rightClick()

@reactionSleepTime
def click():
    pag.click()

@reactionSleepTime
def dragNdrop(x,y):
    pag.mouseDown()
    mouseMove(x,y)
    pag.mouseUp()