#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#ffffff')
spobj=fobj.add_subplot(1,1,1)
item_sales=[90,30,60,50,25,80,70,75,73,77,75,30,80,76,10]
spobj.boxplot(item_sales)
plt.show()
