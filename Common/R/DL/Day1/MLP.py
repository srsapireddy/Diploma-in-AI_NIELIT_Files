from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
iris = load_iris()
type(iris)
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target



knn=MLPClassifier()
print(knn)

knn.fit(X,y)
print(knn.predict([[3,5,4,2]]))
p=knn.predict(X)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y,p))

