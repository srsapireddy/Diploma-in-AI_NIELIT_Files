#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name_xticks='Ram Tom Raj Ravi Roy Anil'.split()
x_val=np.arange(len(stud_name_xticks))
stud_scores=[90,30,60,50,25,80]
#spobj.bar(x_val,stud_scores,align='center',width=.5,alpha=.5,color='r')
spobj.bar(x_val,stud_scores,align='center',width=.5,alpha=.5,color='r',tick_label=stud_name_xticks)
#plt.xticks(x_val,stud_name_xticks)
#spobj.set_xticks(x_val)
spobj.set_yticks(np.linspace(0,100,6))
#spobj.set_xticklabels(stud_name_xticks,rotation=45)
spobj.set_xlabel('Candidates')
spobj.set_title('Assessment chart')
plt.show()
