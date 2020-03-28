#accuracy score 
#confusion matrix
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("pimaindians.csv",delimiter=",")

X=data.iloc[:, 0:7].values  
y=data.iloc[:, 8].values
rf=LogisticRegression()
print(rf)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
rf.fit(X_train,y_train)
predictions=rf.predict(X_test)

print (accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))