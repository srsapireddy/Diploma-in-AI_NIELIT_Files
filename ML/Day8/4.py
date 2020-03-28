#!/usr/bin/env python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('Immunotherapy.csv')

X = df.drop('Result_of_Treatment', axis=1)
y = df['Result_of_Treatment']

#Without normalising----------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf =LogisticRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(accuracy_score(p, y_test))
print(confusion_matrix(p, y_test))


#With normalising------------------------------------------------------------------------------

normalized_X = preprocessing.normalize(X)

X_train, X_test, y_train, y_test = train_test_split(normalized_X, y, test_size=0.3)

rf =LogisticRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(accuracy_score(p, y_test))
print(confusion_matrix(p, y_test))



#With scaling-------------------------------------------------------------------------------------

X_scaled = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

rf =LogisticRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(accuracy_score(p, y_test))
print(confusion_matrix(p, y_test))



#With minmaxscaling--------------------------------------------------------------

min_max_scaler = preprocessing.MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_minmax, y, test_size=0.3)

rf =LogisticRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(accuracy_score(p, y_test))
print(confusion_matrix(p, y_test))



