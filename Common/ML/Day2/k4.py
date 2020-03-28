from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
k_range=list(range(1,25))
scores=[]
for k in k_range:
	knn=KNeighborsClassifier(n_neighbors=k)
	knn.fit(X_train,y_train)
	p=knn.predict(X_test)
	t=accuracy_score(y_test,p)
	scores.append(t)
plt.plot(k_range,scores)
plt.xlabel("Value of K")
plt.ylabel('Testing Accuracy')
plt.show()

