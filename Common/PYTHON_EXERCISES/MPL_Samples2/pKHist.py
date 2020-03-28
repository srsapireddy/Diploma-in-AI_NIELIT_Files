#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales=[30,1,2,2,60,50,25,80,70,80,81,2,3,4,75,73,77,75,75,7,30,80,76,10]
item_sales1=[30,1,2,2,60,50,25,80,70,80,81,2,3,4,75,73,77,75,75,7,30,80,76,10]
item_sales1.sort()
ba=np.array(item_sales1)
num_bins=5
#rval=spobj.hist(item_sales,num_bins)
rval=spobj.hist(item_sales,ba.max())

for i in rval:
 print("---------------")
 print("i=",i)
for i in rval[2]:
 print("---------------")
 print("i=",i)
 print("i=",i.get_height())

print(item_sales1)
pind=0
for ind in [i.get_height() for i in rval[2]]:
 print(item_sales1[pind:pind+int(ind)])
 pind=pind+int(ind)

print(item_sales)
plt.show()
