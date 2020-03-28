#!/usr/bin/env python3
from tkinter import *
def ehan1():
 print('Clicked')
mwin=Tk()
mwin.title('SampleGUI')
mwin.geometry('400x200+50+50')
b1=Button(mwin,text='Click',command=ehan1)
b1.pack()
mwin.mainloop()
