import win32gui
from numpy import *
import pyautogui as pag
def drawLine(x1, y1, x2, y2):
    coordinates = []

    dx = x2 - x1
    dy = y2 - y1

    #Сколько до конечного значения
    if dx > 0:
        sign_x = 1
    elif dx < 0:
        sign_x = -1
    else:
        sign_x = 0

    if dy > 0:
        sign_y = 1
    elif dy < 0:
        sign_y = -1
    else:
        sign_y = 0

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    coordinates.append([x, y])

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        coordinates.append([x, y])

    return coordinates

def smoothMove(x, y):
    flags, hcursor, (startX, startY) = win32gui.GetCursorInfo()
    coordinates = drawLine(startX, startY, x, y)
    for dot in coordinates:
        pag.moveTo(dot[0], dot[1])
        pag.PAUSE = random.random()/3000

