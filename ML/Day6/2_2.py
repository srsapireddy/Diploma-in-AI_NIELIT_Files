from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
iris=load_boston()

print(iris.feature_names)
X=iris.data
y=iris.target
print(y)
tree1=DecisionTreeRegressor()
tree1.fit(X,y)
p=tree1.predict(X)
print(p)
print(mean_squared_error(y,p))
plt.scatter(y,p)
plt.show()