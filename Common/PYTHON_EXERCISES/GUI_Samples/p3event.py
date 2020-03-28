#!/usr/bin/env python3
from tkinter import *
def ehan1(e):
 print('Clicked at %d,%d'%(e.x,e.y))
mwin=Tk()
mwin.title('SampleGUI')
mwin.geometry('400x200+50+50')
lbl=Label(mwin)
fo=('Times',20,'bold')
lbl.config(text='sample label',bg='red',fg='#00FF00',height=3,width=15)
lbl.config(font=fo)
lbl.bind('<Button-1>',ehan1)
lbl.pack(side=LEFT,anchor=N)
mwin.mainloop()
