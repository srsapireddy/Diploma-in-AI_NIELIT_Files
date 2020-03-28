
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv('train.csv')

X = df.drop(['datetime','count'], axis=1)
y = df['count']

#Without normalising----------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf =LinearRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(mean_squared_error(p, y_test))

plt.scatter(y_test,p)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

#With normalising------------------------------------------------------------------------------

normalized_X = preprocessing.normalize(X)

X_train, X_test, y_train, y_test = train_test_split(normalized_X, y, test_size=0.3)

rf =LinearRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(mean_squared_error(p, y_test))

plt.scatter(y_test,p)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

#With scaling-------------------------------------------------------------------------------------

X_scaled = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

rf =LinearRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(mean_squared_error(p, y_test))

plt.scatter(y_test,p)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

#With minmaxscaling--------------------------------------------------------------

min_max_scaler = preprocessing.MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_minmax, y, test_size=0.3)

rf =LinearRegression()
rf.fit(X_train ,y_train)
p = rf.predict(X_test)

print(mean_squared_error(p, y_test))

plt.scatter(y_test,p)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()


