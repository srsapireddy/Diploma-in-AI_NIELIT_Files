from sklearn.datasets import load_iris
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
iris=load_iris()
X=iris.data
y=iris.target
y=to_categorical(y)

print(y)
model=Sequential()
model.add(Dense(10,input_shape=(4,),activation='relu',name='fc1'))
model.add(Dense(10,activation='relu',name='fc2'))
model.add(Dense(3,activation='softmax',name='output'))
optimizer=Adam(lr=0.001)

model.compile(optimizer,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X,y,verbose=0,batch_size=8,epochs=50)
results=model.evaluate(X,y)
print(results)




