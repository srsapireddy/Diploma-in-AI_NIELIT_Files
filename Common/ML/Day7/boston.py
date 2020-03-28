from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
iris=load_boston()
X=iris.data
y=iris.target
rf=RandomForestRegressor()
rf.fit(X,y)
p=rf.predict(X)
print(mean_squared_error(p,y))

