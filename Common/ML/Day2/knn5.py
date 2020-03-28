from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
iris=load_iris()
X=iris.data
y=iris.target

print(iris.feature_names)
print(X.shape)
print(y.shape)

knn=KNeighborsClassifier(n_neighbors=3)

scores=cross_val_score(knn,X,y,cv=20,scoring='accuracy')

print(scores)
