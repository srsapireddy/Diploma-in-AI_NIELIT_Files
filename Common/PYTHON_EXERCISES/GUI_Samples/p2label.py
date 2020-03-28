#!/usr/bin/env python3
from tkinter import *
mwin=Tk()
mwin.title('SampleGUI')
mwin.geometry('200x100+10+20')
lbl=Label(mwin)
fo=('Times',20,'bold')
lbl.config(text='sample label',bg='red',fg='#00FF00',height=3,width=15)
lbl.config(font=fo)
lbl.pack(side=LEFT,anchor=N)
mwin.mainloop()
