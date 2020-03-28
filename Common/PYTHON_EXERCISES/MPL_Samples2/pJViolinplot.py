#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
item_sales=[9,30,60,50,25,8,70,75,73,7,75,30,8,76,10]
spobj.violinplot(item_sales)
plt.show()
