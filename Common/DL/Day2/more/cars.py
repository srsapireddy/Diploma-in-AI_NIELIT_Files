import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense


#from tensorflow.python.keras.wrappers.scikit_learn import 

import os;

#os.chdir(path)
#os.getcwd()


#Variables
dataset=pd.read_csv("cars.csv", delimiter="\s+", )
dataset=dataset.as_matrix()
x=dataset[:,0:5]
y=dataset[:,5]
y=np.reshape(y, (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(x))
xscale=scaler_x.transform(x)
print(scaler_y.fit(y))
yscale=scaler_y.transform(y)



X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)


model = Sequential()
model.add(Dense(12, input_dim=5, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.summary()



model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])




history = model.fit(X_train, y_train, epochs=50, batch_size=50,  verbose=1, validation_split=0.2)



print(history.history.keys())
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()


