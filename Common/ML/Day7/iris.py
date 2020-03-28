from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
iris=load_iris()
X=iris.data
y=iris.target
rf=RandomForestClassifier()
rf.fit(X,y)
p=rf.predict(X)
print(confusion_matrix(p,y))

