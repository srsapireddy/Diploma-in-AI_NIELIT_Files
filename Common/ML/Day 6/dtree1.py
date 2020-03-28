from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,classification_report

iris=load_iris()
X=iris.data
y=iris.target

tree1=DecisionTreeClassifier()
tree1.fit(X,y)
p=tree1.predict(X)
print(confusion_matrix(y,p))

print(classification_report(y,p))

