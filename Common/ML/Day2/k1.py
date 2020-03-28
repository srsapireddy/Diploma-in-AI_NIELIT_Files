from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
iris=load_iris()
X=iris.data
y=iris.target
print(y)
print(iris.feature_names)
knn=KNeighborsClassifier()
knn.fit(X,y)
print(knn.predict(X[[2]]))
print(knn.predict([[3,5,4,2]]))


p=knn.predict(X)
print(confusion_matrix(y,p))
print(accuracy_score(y,p))
