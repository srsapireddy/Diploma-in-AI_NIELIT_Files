import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

Xtrain=pd.read_csv('BTCtrain.csv')
print(Xtrain.head())

Xtrain=Xtrain.as_matrix()
Xtrain=Xtrain[:,[1]]

sc=MinMaxScaler()
Xtrain=sc.fit_transform(Xtrain)

xtrain=Xtrain[0:2694]
ytrain=Xtrain[1:2695]

xtrain=np.reshape(xtrain,(2694,1,1))
regressor=Sequential()
regressor.add(LSTM(units=400,activation='sigmoid',input_shape=(None,1)))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam',loss='mean_squared_error')
regressor.fit(xtrain,ytrain,batch_size=32,epochs=20)

testdata=pd.read_csv('BTCtest.csv')
testdata=testdata.as_matrix()
realprice=testdata[:,[1]]


inputs=sc.transform(realprice)
inputs=np.reshape(inputs,(8,1,1))
p=regressor.predict(inputs)
p=sc.inverse_transform(p)

plt.plot(realprice,color='green',label='Current BTC Value')
plt.plot(p,color='red',label='Predicted BTC Values')
plt.title('BTC Value Prediction')
plt.xlabel("days")
plt.ylabel('BTC Value')
plt.legend()
plt.show()



