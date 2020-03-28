from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pickle
iris=load_iris()
X=iris.data
y=iris.target
knn= KNeighborsClassifier()
knn2= KNeighborsClassifier()
knn.fit(X,y) 
file1 ="knnmodel"
pickle.dump(knn,open(file1,'wb'))


knn2=pickle.load(open(file1,'rb'))
print(knn2.predict([[3,3,2,2]]))


