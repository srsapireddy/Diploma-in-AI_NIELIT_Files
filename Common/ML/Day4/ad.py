

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
data = pd.read_csv("Advertising.csv")
#print(data.head())
data = data.as_matrix()
X = data[:,1:4]
y = data[:,-1] 

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

model = LinearRegression()
model.fit(X_train,y_train)

p = model.predict(X_test)
print(mean_squared_error(y_test,p))
plt.scatter(y_test,p)
plt.show()

