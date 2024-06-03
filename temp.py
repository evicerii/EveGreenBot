from main import *

f1Active=[1064,918]
f2Active=[1114,918]
f3Active=[1166,918]
f4Active=[1216,918]
f5Active=False


while True:
    WindowsClassArray[0].IMGInvisible()
    pix = Image.open('temp.jpeg').load()
    print(sum(pix[1794, 968]))
    time.sleep(1)
