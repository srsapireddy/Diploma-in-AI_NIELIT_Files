from sklearn.datasets import load_iris
iris =load_iris()
print(iris.feature_names)
print(iris.data)
X=iris.data
y=iris.target

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=1)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2)

knn.fit(X_train,y_train)
predictions=knn.predict(X_test)

from sklearn.linear_model import LogisticRegression

lg=LogisticRegression()
lg.fit(X_train,y_train)

predictions2=lg.predict(X_test)







print(predictions)
print(y_test)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report




print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print(classification_report(y_test,predictions2))
