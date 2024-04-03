from tkinter import *  
from adds.decorators import *
from adds.script import *

window = Tk()  
window.title("Общие настройки")  
window.geometry('400x250')  
lbl = Label(window, text="Количество окон")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0) 
txt.insert(0, settings.charQua)


lbl1 = Label(window, text="Время работы")  
lbl1.grid(column=0, row=1)  
txt1 = Entry(window,width=10)  
txt1.grid(column=1, row=1)  
txt1.insert(0, settings.workTime)

btn = Button(window, text="сохранить настройки", command= lambda: [RewriteSettings('charQua',txt),RewriteSettings('workTime',txt1)])  
btn.grid(column=2, row=3) 
window.mainloop()