from sklearn.datasets import load_boston
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
import numpy as np
#alphas=np.array([1,0.1,0.001,.0001])
alphas=range(0.0,1.0,0.1)
print(alphas)
model=Ridge()
grid=GridSearchCV(estimator=model,param_grid=dict(alpha=alphas))
boston=load_boston()
X=boston.data
y=boston.target
grid.fit(X,y)
#print(grid)
print(grid.best_score_)
print(grid.best_estimator_.alpha)
