#!/usr/bin/env python
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.svm import SVR
from sklearn import svm,datasets
data=load_boston()
X=data.data
y=data.target
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

pca=PCA(3)
model=svm.SVC(kernel='rbf')
X_transformed=pca.fit_transform(X)
print(X_transformed)
print(X_transformed.shape)
p=SVR(kernel='rbf')
p1=p.fit(X_transformed,y).predict(X_transformed)
print(mean_squared_error(y,p1))
print( "increasing the principal components")
pca1=PCA(4)
X_transformed1=pca1.fit_transform(X)
print(X_transformed1)
print(X_transformed1.shape)
p2=SVR(kernel='rbf')
p3=p2.fit(X_transformed1,y).predict(X_transformed1)

print(mean_squared_error(y,p3))

print( "decreasing the principal components")
pca2=PCA(2)
X_transformed2=pca2.fit_transform(X)
print(X_transformed1.shape)
print(X_transformed2)
p4=SVR(kernel='rbf')
p5=p4.fit(X_transformed2,y).predict(X_transformed2)
print(mean_squared_error(y,p5))



