from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
X=iris.data
y=iris.target

print(iris.feature_names)
print(X.shape)
print(y.shape)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)

print(knn.predict(X))
print(y)
