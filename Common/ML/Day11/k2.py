
from sklearn.neighbors import KNeighborsClassifier
import pickle


knn1=KNeighborsClassifier()


file='k1'


knn1=pickle.load(open(file,'rb'))

p=knn1.predict([[5,5,5,5]])


print(p)
