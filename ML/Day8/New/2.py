#!/usr/bin/env python
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
df=pd.read_csv('/home/ai2/banking.csv',delimiter=',')
en= LabelEncoder()
print(df.head())
for i in df.columns:
 if(df[i].dtype=='object'):
  df[i]=en.fit_transform(df[i])
 
X=df.drop('y',axis=1)
y=df['y']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
rf=GaussianNB()
rf.fit(X_train,y_train)
p=rf.predict(X_test)

print (accuracy_score(p,y_test))
print(confusion_matrix(p,y_test))


