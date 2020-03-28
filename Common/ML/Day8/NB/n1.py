from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
iris=load_iris()
X=iris.data
y=iris.target
nb=GaussianNB()
nb.fit(X,y)
p=nb.predict(X)
print(confusion_matrix(y,p))
