#!/usr/bin/env python3
from tkinter import *
exp=''
def bh1():
 global exp
 exp+='1'
 tv1.set(exp)
def bh2():
 global exp
 exp+='2'
 tv1.set(exp)
def bhp():
 global exp
 exp+='+'
 tv1.set(exp)
def bhe():
 global exp
 exp=str(eval(exp))
 tv1.set(exp)
def bh3():
 pass
def bh4():
 pass
def bhm():
 pass
mwin=Tk()
mwin.title('Calculator')
#mwin.geometry('400x200+50+50')
tv1=StringVar()
e1=Entry(mwin,textvariable=tv1)
b1=Button(mwin,text='1',command=bh1)
b2=Button(mwin,text='2',command=bh2)
b3=Button(mwin,text='3',command=bh3)
b4=Button(mwin,text='4',command=bh4)
bp=Button(mwin,text='+',command=bhp)
bm=Button(mwin,text='-',command=bhm)
be=Button(mwin,text='=',command=bhe)
e1.grid(row=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=2,column=0)
b4.grid(row=2,column=1)
bp.grid(row=1,column=2)
bm.grid(row=1,column=3)
be.grid(row=2,column=2,columnspan=2)
mwin.mainloop()
