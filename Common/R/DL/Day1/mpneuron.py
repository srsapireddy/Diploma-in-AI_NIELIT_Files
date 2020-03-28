import sklearn.datasets
import numpy as np
import pandas as pd
from sklearn.preprocessing import Binarizer
from sklearn.metrics import accuracy_score
breast_cancer = sklearn.datasets.load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify = y)

np.set_printoptions(suppress=True)

print(X_train)

b=Binarizer(100)

X_binarised_train = b.transform(X_train)
X_binarised_test = b.transform(X_test)
print(X_binarised_train)



class MPNeuron:
  
  def __init__(self):
    self.b = None
    
  def model(self, x):
    return(sum(x) >= self.b)
  
  def predict(self, X):
    Y = []
    for x in X:
      result = self.model(x)
      Y.append(result)
    return np.array(Y)
  
  def fit(self, X, Y):
    accuracy = {}
    
    for b in range(X.shape[1] + 1):
      self.b = b
      Y_pred = self.predict(X)
      accuracy[b] = accuracy_score(Y_pred, Y)
      print(b," ",accuracy[b])  
    best_b = max(accuracy, key = accuracy.get)
    self.b = best_b
    
    print('Optimal value of b is', best_b)
    print('Highest accuracy is', accuracy[best_b])

#Calling the class MPNeuron
mp_neuron = MPNeuron()
print(X_binarised_train,y_train)


#Calling the fit method inside the class on the training data
mp_neuron.fit(X_binarised_train, y_train)

#testing the model on the test data.
Y_test_pred = mp_neuron.predict(X_binarised_test)
accuracy_test = accuracy_score(Y_test_pred, y_test)

#print the accuracy of the test data
print(accuracy_test)

