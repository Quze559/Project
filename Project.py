from tkinter import *
import datetime
import time

a=0
b=0

def taketime():
    global a,b
    a = datetime.datetime.now
    b = datetime.datetime.now

root = Tk()
root.geometry("1280x1024")
f_top=Frame(root)
f_middle=Frame(root)
f_bot=Frame(root)

while True:
    time.sleep(1)
    label1=Label(f_top , font="Arial 12", width=50, height=15, bg="green")
    label1.config(text=str(a.strftime("%m/%d/%Y")))
    label2=Label(f_top, font="Arial 12", width=50, height=15, bg="lightgreen")
    label2.config(text=str(b.strftime("%H:%M:%S")))
    label3=Label(f_top, text="Место для общего времени тренировки", font="Arial 12", width=50, height=15, bg="#29b514")
    label4=Label(f_middle, text="Место для таймера тренировки", font="Arial 12", width=50, height=15, bg="red")
    label5=Label(f_middle, text="Кнопка начала тренировки", font="Arial 12", width=50, height=15, bg="#800606")
    label6=Label(f_bot, text="", font="Arial 12", width=50, height=15, bg="#800606")
    f_top.pack()
    f_middle.pack()
    f_bot.pack()
    label1.pack(side=LEFT, anchor=NW)
    label2.pack(side=LEFT, anchor=N)
    label3.pack(side=LEFT, anchor=NE)
    label4.pack(side=LEFT, anchor=NW)
    label5.pack(side=LEFT, fill=X)
    root.mainloop()
