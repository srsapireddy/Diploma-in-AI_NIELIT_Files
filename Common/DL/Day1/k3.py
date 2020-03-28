import numpy as np

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

iris =load_boston()
X=iris.data
y_=iris.target.reshape(-1,1)

y=y_
'''
encoder=OneHotEncoder()
y=encoder.fit_transform(y_)
'''
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
model =Sequential()
model.add(Dense(10,input_shape=(13,),activation='relu',name='fc1'))
model.add(Dense(10,activation='relu',name='fc2'))
model.add(Dense(1,input_shape=(1,),activation='linear',name='output'))

optimizer=Adam(lr=0.001)

model.compile(optimizer,loss='mean_squared_error',metrics=['mse'])

model.fit(Xtrain,ytrain,verbose=2,batch_size=3,epochs=150)

results=model.evaluate(Xtrain,ytrain)
print(results[0])






