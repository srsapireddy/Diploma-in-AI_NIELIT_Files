#!/usr/bin/env python3
from tkinter import *
def bhan():
 t2.set(t1.get())
mwin=Tk()
mwin.geometry('400x200+50+50')
mwin.title('SampleGUI')
t1=StringVar()
t2=StringVar()
e1=Entry(mwin,width=20,textvariable=t1)
e2=Entry(mwin,width=20,textvariable=t2)
t1.set('sample')
b1=Button(mwin,text='click',command=bhan)
e1.focus()
e1.pack()
b1.pack()
e2.pack()
mwin.mainloop()
