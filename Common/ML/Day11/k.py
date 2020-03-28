from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
import pickle

X=iris.data
y=iris.target

knn=KNeighborsClassifier()
knn1=KNeighborsClassifier()

knn.fit(X,y)

file='k1'

pickle.dump(knn,open(file,'wb'))

knn1=pickle.load(open(file,'rb'))

p=knn1.predict([[3,2,2,1]])


print(p)
