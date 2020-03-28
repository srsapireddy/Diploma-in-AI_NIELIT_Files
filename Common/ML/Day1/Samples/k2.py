from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,confusion_matrix
iris=load_iris()
print(iris.feature_names)
X=iris.data
y=iris.target

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

print(X_train.shape)
print(y_train.shape)
knn.fit(X_train,y_train)

p=knn.predict(X_test)
print(p.shape)
print(confusion_matrix(y_test,p))
print(knn)
 
