from main import *
def relogin(numberWin, ship, status):
    tempColor = 0
    WindowsClassArray[numberWin].IMGInvisible('checkActiveWin')
    tempColor = sum(pix[logOff[0],logOff[1]])
    os.remove('checkActiveWin.jpeg')
    mouseMove(DropWindow)
    click()
    if 260<tempColor<270:
        login()
        tempColor = 0
    temp1=[]
    ActualInfoHWID(ProcessName)
    for win in windows:
        temp1.append(windows[win])
    time.sleep(60)
    ActualInfoHWID(ProcessName)
    temp2 = windows
    temp3 = []
    for element in temp2:
        if element not in temp1:
            temp3.append(element)
    while tempColor != 543:
        WindowsClassArray[numberWin].IMGInvisible('checkActiveWin')
        pix = Image.open('checkActiveWin.jpeg').load()
        tempColor = sum(pix[checkLogin[0],checkLogin[1]])
        os.remove('checkActiveWin.jpeg')
        time.sleep(1)
    ActivateWindow(temp3[0])
    time.sleep(3)
    mouseMove(LocalChat.x, LocalChat.y)
    click()
    if status=='dock':
        return
    elif status=='undock':
        Activate2D()
        ship.ActiveDefModule()
        super.CheckWarp(numberWin)
        return
    elif status=='dronesLaunched':
        Activate2D()
        ship.ActiveDefModule()
        super.CheckWarp(numberWin)
        ship.LaunchDrns()
        return
    else:
        ship.Dock()
