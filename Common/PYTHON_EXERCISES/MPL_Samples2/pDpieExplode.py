#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(2,1,1)
spobj1=fobj.add_subplot(2,1,2)
fruits='Apple Orange Grapes Mango Pineapple'.split()
sales=[30,40,25,10,35]
colrs='r y c g b'.split()
expl=[0.1,0,0,0,0]
#patches,texts=spobj.pie(sales,explode=expl,colors=colrs,shadow=True,startangle=120)
#spobj.pie(sales,explode=expl,colors=colrs,autopct='%.1f',shadow=True,startangle=120)
#spobj.pie(sales,explode=expl,colors=colrs,autopct='%.1f%%',shadow=True,startangle=120)
spobj.pie(sales,explode=expl,colors=colrs,autopct='%.1f%%',labels=fruits,shadow=True,startangle=120)
spobj1.pie(sales,explode=expl,colors=colrs,autopct='%.2f',labels=fruits,shadow=True,startangle=120)
#print patches
#print texts
#plt.legend(patches,fruits,loc='best')
plt.show()
