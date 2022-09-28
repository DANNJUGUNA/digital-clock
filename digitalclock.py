from datetime import datetime
from tkinter import *
import tkinter
import pyglet

pyglet.font.add_file("digital-7.ttf")

 #coulors to be used
color1="#36901E"
color2="white"

clock=Tk()
clock.resizable(False,False)
clock.geometry("360x180")
clock.configure(background=color1)

def timeAndDate():
   currenttime=datetime.now()
   time=currenttime.strftime("%H:%M:%S")
   weekday=currenttime.strftime("%A")
   date=currenttime.day
   month=currenttime.month
   month2=currenttime.strftime("%b")
   year=currenttime.strftime("%Y")
   timelabel.config(text=time)
   timelabel.after(200,timeAndDate)


   dy.config(text=weekday +""+ str(date)+ "/" +str(month)+"/"+ year)


timelabel=Label(clock,font=('digital-7',60,'bold'),bg=color1,fg=color2)
timelabel.grid(row=0,column=2,sticky=NW)

dy=Label(clock,font=('digital-7',20,'bold'),bg=color1,fg=color2)
dy.grid(row=1,column=2,sticky=NW)

timeAndDate()
clock.mainloop()
