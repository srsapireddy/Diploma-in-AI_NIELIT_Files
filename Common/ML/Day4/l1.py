from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error 
from sklearn.model_selection import train_test_split
import numpy as np

data=load_boston()
X=data.data
y=data.target
print(X)
print(y)
lr=LinearRegression()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


lr.fit(X_train,y_train)
p=lr.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,p)))
print(mean_absolute_error(y_test,p))

print(lr.coef_)
print(lr.intercept_)
