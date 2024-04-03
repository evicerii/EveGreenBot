import pyautogui as pag
rgb1 = sum(pag.pixel(476,899))
print(rgb1)
def CheckLocal():
    for y in range(770,960):
        if sum(pag.pixel(476,y)) in range[193,223,330]:
            print(f'local red')
            return False
CheckLocal()