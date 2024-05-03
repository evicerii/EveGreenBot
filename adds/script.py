import pyautogui as pag
from .mouseMove.mousemove import *
from .coordinate import *
import time
import pytesseract
import os
from PIL import Image
import pyautogui as pag
from .decorators import logs
import logging
import win32con
import configparser

config = configparser.ConfigParser()

@logs
def SelectCharWin(charNum):
    for x in range(1079):
        if sum(pag.pixel(x,1053)) == 105:
            a=(x-402)/49+1
            pag.keyDown('win')
            b=1
            while b<=charNum:
                time.sleep(random.randint(150,250)/1000)
                b=b+1
                pag.press(str(int(a)))
            a=str(int(a))
            time.sleep(random.randint(500,1000)/1000)
            pag.keyUp('win')
            logging.info(f'use {(charNum)} win')
def CheckWarp(LockCheckWarpEvent):
    #запретить взаимодействие на время варпа
    LockCheckWarpEvent.set()
    while True:
        x=963
        y=995
        rgb1 = pag.pixel(x,y)
        rgb1 = sum(rgb1)
        if 700<rgb1<710:
            time.sleep(1)
            break
        else:
            time.sleep(5)
    while True:
        x=963
        y=995
        rgb1 = pag.pixel(x,y)
        rgb1 = sum(rgb1)
        if 700<rgb1<710:
            time.sleep(1)
        else:
            time.sleep(5)
            break
    LockCheckWarpEvent.clear()
def CheckTarget(x, y, z):
    while True:
        time.sleep(random.randint(3,5))
        rgb1 = sum(pag.pixel(x,y))
        if rgb1==z:
            break
def cvName(temp):
    pag.screenshot('Temp.png',region=temp)
    Temp=Image.open('Temp.png').convert('L').save('Temp.png')
    Temp=Image.open('Temp.png')
    Text = pytesseract.image_to_string(Temp, lang='eng')
    Text=Text[:-1]
    os.remove('Temp.png')
    return Text
def CheckNothingFound():
    if (sum(pag.pixel(1586,333))>390 and sum(pag.pixel(1586,333))<400):
        return True
@logs
def RewriteSettings(name, txt):
    config.read('config.ini')
    config.set("General", name, txt)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def ActivateWindow(hwnd):
    try:
        logging.info('Active Window')
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)
    except IndexError:
        logging.error('Окно с указанным идентификатором не найдено.')