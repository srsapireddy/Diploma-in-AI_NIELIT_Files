from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error 
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
iris=load_boston()
X=iris.data
y=iris.target
tree= KNeighborsRegressor()
tree.fit(X,y)
p=tree.predict(X)
print(X)
print(y)
print(p)
print(mean_squared_error(y,p))
plt.scatter(y,p)
plt.show()