#!/usr/bin/env python3

from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np


dataset = open('x15.txt')
print(dataset)
X=dataset[:,3]
print(X)
y=dataset[5].astype(int)  

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

tree1=DecisionTreeRegressor()
tree1.fit(X_train,y_train)
p=tree1.predict(X_test)
print(p)
print(mean_squared_error(y,p))
plt.scatter(y,p)
plt.show()
print(accuracy_score(y,p))
print(confusion_matrix(y,p))