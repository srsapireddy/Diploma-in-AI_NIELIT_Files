from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split,cross_val_score
import pandas as pd
train1=pd.read_csv('train.csv',delimiter='\t')
test1=pd.read_csv('test.csv',delimiter='\t')

train=train1.as_matrix()
test=test1.as_matrix()


X_train,X_test,y_train,y_test=train[:,[0,1]],test[:,[0,1]],train[:,2],test[:,2]

knn=KNeighborsClassifier(n_neighbors=3)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
knn.fit(X_train,y_train)
p=knn.predict(X_test)
print(confusion_matrix(y_test,p))

print(accuracy_score(y_test,p))

print(knn)
