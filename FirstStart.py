import pyautogui as pag

from adds.mouseMove.mousemove import *
from adds.script import *

import pyperclip
################################################################
#servermode on
os.system(f'C:/Users/{os.getlogin()}/AppData/Local/eve-online/eve-online.exe')
time.sleep(10)
mouseMove(1758, 16)
click()
mouseMove(102, 216)
click()
mouseMove(449,565)
click()
GetPIDList('LogLite.exe')
GetHWID(pidsArray[0])
ActivateWindow(windows[0])
mouseMove(15, 39)
click()
mouseMove(77, 160)
click()
os.system("taskkill /im LogLite.exe")

mouseMove(1821, 124)
click()
################################################################
#launch game 
mouseMove(789, 443)
click()
while sum(pag.pixel(291, 13)) != 765:
    time.sleep(1)
time.sleep(60)

########################################################################
#open setting
mouseMove(24, 43)
click()
time.sleep(random.randint(2,5)/10)
mouseMove(147, 661)
click()
#open display settings
mouseMove(661,151)
click()

########################
#optimize settings memory
mouseMove(1075, 894)
click()
time.sleep(random.randint(2,5)/10)
mouseMove(1163, 939)
click()

########################
#   open UI settings
mouseMove(602, 289)
click()
time.sleep(random.randint(2,5)/10)

###########
#transparency settings off
mouseMove(1142, 716)
click()
time.sleep(random.randint(2,5)/10)
mouseMove(1142, 716)
pag.mouseDown()
mouseMove(1030, 703)
pag.mouseUp()

############
#light mode transparency settings off
mouseMove(1141, 762)
click()
time.sleep(random.randint(2,5)/10)
mouseMove(1141, 762)
pag.mouseDown()
mouseMove(984, 755)
pag.mouseUp()

########################
#scroll user interface
mouseMove(1437, 177)
pag.mouseDown()
mouseMove(1467, 885)
pag.mouseUp()

############
#interface color
mouseMove(1179, 483)
click()

#########################
#chat invite off
mouseMove(694,347)
click()
mouseMove(870,774)
click()

########################################################################
#close settings
mouseMove(1449, 53)
click()

#########################
#lock chat window
mouseMove(472, 722)
click()
mouseMove(608, 750)
click()

#########################
#chat member list update
mouseMove(449, 722)
click()
mouseMove(705, 848)
mouseMove(872, 887)
click()

########################################################################
#search player
pyperclip.copy("Kisusanen Kautsuo")
mouseMove(177, 108)
click()

pag.keyDown("ctrl")
time.sleep(random.randint(2,5)/10)
pag.keyDown("v")
time.sleep(random.randint(2,5)/10)
pag.keyUp("v")
time.sleep(random.randint(2,5)/10)
pag.keyUp("ctrl")
time.sleep(random.randint(2,5)/10)

pag.press("enter")

mouseMove(1031, 570)
pag.click()
time.sleep(0.08)
pag.click()

mouseMove(1052, 846)
click()

##########################
#updte owerview
mouseMove(860, 483)
click()
mouseMove(819, 622)
click()

mouseMove(1190, 247)
click()

################################################################
#space
#probe scanner
time.sleep(5)
pag.keyDown("alt")
time.sleep(random.randint(2,5)/10)
pag.keyDown("p")
time.sleep(random.randint(2,5)/10)
pag.keyUp("p")
time.sleep(random.randint(2,5)/10)
pag.keyUp("alt")

mouseMove(944, 333)
pag.mouseDown()
mouseMove(816, 15)
pag.mouseUp()

###############################################################
#drones
mouseMove(1862, 872)
click()
mouseMove(1591, 1022)
click()