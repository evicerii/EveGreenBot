from tkinter import *
from FarmThread import *

config.read('config.ini')

window = Tk()  
window.title("Общие настройки")  
window.geometry('400x250')  
lblWin = Label(window, text="Количество окон")  
lblWin.grid(column=0, row=0)  
txtWin = Entry(window,width=10)  
txtWin.grid(column=1, row=0) 
txtWin.insert(0,config.get('General','charQua'))

lblTime = Label(window, text="Время работы")  
lblTime.grid(column=0, row=1)  
txtTime = Entry(window,width=10)  
txtTime.grid(column=1, row=1)  
txtTime.insert(0, config.get('General','workTime'))

SaveConfigBtn = Button(window, text="сохранить настройки", command= lambda: [RewriteSettings('charQua',txtWin.get()),RewriteSettings('workTime',txtTime.get())])  
SaveConfigBtn.grid(column=2, row=3) 


LaunchBtn = Button(window, text="запуск", command= lambda: [window.destroy(), LaunchBot()])
LaunchBtn.grid(column=2, row=4)

window.mainloop()