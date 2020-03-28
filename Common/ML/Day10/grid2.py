from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
k=range(1,26)
model=KNeighborsClassifier()
grid=GridSearchCV(estimator=model,param_grid=dict(n_neighbors=k))
iris=load_iris()
X=iris.data
y=iris.target
grid.fit(X,y)
#print(grid)
print(grid.best_score_)
print(grid.best_estimator_.n_neighbors)
