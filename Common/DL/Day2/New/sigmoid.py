
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
b=1
y=1/(1+(np.exp(-x*.8+b)))
print(x)
print(y)
plt.plot(x,y)
plt.show()

