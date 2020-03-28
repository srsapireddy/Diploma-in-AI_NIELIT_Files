#!/usr/bin/env python
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
df=pd.read_csv('/home/ai37/banking.csv',delimiter=',')
en=LabelEncoder()
for i in df.columns:
 if(df[i].dtype=='object'):
  df[i]=en.fit_transform(df[i])
X= df.select_dtypes(include=['int64','float64']).drop('y',axis=1)
y=df['y']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
p=knn.predict(X_test)
print(accuracy_score(p,y_test))
print(confusion_matrix(p,y_test))

