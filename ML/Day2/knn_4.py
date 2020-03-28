

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd

dataset1=open('ecoli.data')
dataset=dataset1.read()
print dataset



X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
predictions=knn.predict(X_test)
print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))