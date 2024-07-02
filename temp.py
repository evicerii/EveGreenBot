from main import *
from win32gui import FindWindow, GetWindowRect
WindowsClassArray[1].IMGInvisible()   
pix = Image.open(f'temp.jpeg').load()
for n in range(LocalStatusRange[0], LocalStatusRange[1], LocalStatusRange[2]):
    #Проврка тикеров в чате /red,orange,grey
    print(pix[LocalStatusXCoord,n][0])
    if (pix[LocalStatusXCoord,n][0]>70):
        logging.info(f'local red 7210720')