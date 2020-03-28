from sklearn.datasets import load_iris 
from sklearn.metrics import confusion_matrix
iris = load_iris() 
type(iris) 
print(iris.feature_names) 
print(iris.data) 
X=iris.data 
y=iris.target 


from sklearn import svm
model =svm.SVC(kernel='rbf',C=0.1,gamma=0.2)

model.fit(X,y) 

p=model.predict(X)
print(confusion_matrix(p,y))

print(model.predict([[3,5,4,2]])) 

