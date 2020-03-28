from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Binarizer
import numpy
iris=load_iris()
X=iris.data
y=iris.target

print(iris.feature_names)
print(X.shape)
print(y.shape)
print(X[1,])
scaler=StandardScaler()
m=MinMaxScaler(feature_range=(0,100))
#X=scaler.fit_transform(X)
X=m.fit_transform(X)
#numpy.set_printoptions(precision=2,threshold=10000)
print(X)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)

print(knn.predict([[3,5,4,2]]))
print(knn.predict(X))
print(y)
