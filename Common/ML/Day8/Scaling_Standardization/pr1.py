import pandas 
import scipy 
import numpy 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,MinMaxScaler 
from sklearn.metrics import confusion_matrix
dataframe = pandas.read_csv("pimaindians.csv") 
array = dataframe.as_matrix()
  
# separate array into input and output components 
X = array[:,0:8] 
y = array[:,8] 

knn=KNeighborsClassifier(3)
knn.fit(X,y)
p=knn.predict(X)
print(confusion_matrix(y,p))
scaler=MinMaxScaler(feature_range=(0,10))
X1=X
X=scaler.fit_transform(X)

knn.fit(X,y)
p=knn.predict(X)
print(confusion_matrix(y,p))



  
# summarize transformed data 
import numpy
numpy.set_printoptions(precision=3) 

print(X[0:5,:]) 
numpy.set_printoptions(precision=3) 
print(X1[0:5,:]) 
