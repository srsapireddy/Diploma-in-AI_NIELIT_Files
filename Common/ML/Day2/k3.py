from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split,cross_val_score
iris=load_iris()
X=iris.data
y=iris.target
knn=KNeighborsClassifier(n_neighbors=3)
scores=cross_val_score(knn,X,y,cv=20,scoring='accuracy')
print(scores)


