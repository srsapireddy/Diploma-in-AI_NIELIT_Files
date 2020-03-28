#!/usr/bin/env python
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import svm,datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
cancer= datasets.load_breast_cancer()
X=cancer.data
y=cancer.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X)
print(X.shape)
pca=PCA(2)
X_transformed=pca.fit_transform(X)
print(X_transformed)
print(X_transformed.shape)
svm1=LinearDiscriminantAnalysis()
p=svm1.fit(X,y).predict(X)
svm2=SVC()

pt=svm2.fit(X,y).predict(X)
print(confusion_matrix(p,y))
print(confusion_matrix(pt,y))
print(accuracy_score(p,y))
print(accuracy_score(pt,y))
