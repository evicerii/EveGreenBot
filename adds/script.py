import pyautogui as pag
from .mouseMove.mousemove import *
from .coordinate import *
import time
import datetime
import pytesseract
import os
from PIL import Image
import pyautogui as pag
from .decorators import logs
import adds.Value.settings as settings

pytesseract.pytesseract.tesseract_cmd = r'D:/EveBot/tesseract/tesseract.exe'
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
            print(f'{datetime.datetime.now()}  use {(charNum)} win')
def CheckWarp(locker):
    #запретить взаимодействие на время варпа
    locker.set()
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
    locker.clear()
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
    if (sum(pag.pixel(1586,333))==393 or sum(pag.pixel(1586,333))==396):
        return True
@logs
def RewriteSettings(txt, name):
    res = format(txt.get()) 
    with open ('./adds/Value/settings.py', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(f'{name}={settings.values[name]}', f'{name}={res}')
    with open ('./adds/Value/settings.py', 'w') as f:
        f.write(new_data)
    settings.values[name] = res