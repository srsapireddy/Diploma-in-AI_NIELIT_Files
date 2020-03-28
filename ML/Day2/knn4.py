

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
data=pd.read_csv("ecoli.csv")
train1=pd.read_csv('ecoli.csv',delimiter='\s')
test1=pd.read_csv('ecoli.csv',delimiter='\s')
train=train1.as_matrix()
test=test1.as_matrix()
X_train,X_test,y_train,y_test=train[:,[2,8]],test[:,[2,8]],train[:,[9]],test[:,[9]]
Knn=kNeighborsclassifier(n,neighbors=3)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
knn.fit(x_train,y_train)
p=knn.predict(x_test)
print(Confusion_matrix(y_test,p))
print(accuracy_matrix(y_test.p))





