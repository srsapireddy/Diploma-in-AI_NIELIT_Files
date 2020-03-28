import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
(X_train,y_train),(X_test,y_test)=mnist.load_data()
print(X_train.shape)

from keras.utils import to_categorical
classes=np.unique(y_train)
nClasses=len(classes)
print(classes)
print(nClasses)

plt.figure(figsize=[10,5])
plt.subplot(121)
plt.imshow(X_train[0,:,:],cmap='gray')
plt.title(y_train[0])
#plt.show()

dimData=np.prod(X_train.shape[1:])
print(dimData)

X_train=X_train.reshape(X_train.shape[0],dimData)
X_test=X_test.reshape(X_test.shape[0],dimData)
X_train=X_train/255
X_test=X_test/255


y_train1=to_categorical(y_train)
y_test1=to_categorical(y_test)

from keras.models import Sequential
from keras.layers import Dense

model=Sequential()

model.add(Dense(512,activation='relu',input_shape=(dimData,)))
model.add(Dense(512,activation='relu'))
model.add(Dense(nClasses,activation='softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train1,batch_size=256,epochs=3,verbose=1,validation_data=(X_test,y_test1))

[test_loss,test_acc]=model.evaluate(X_test,y_test1)


x=model.predict(X_test[0].reshape(-1,784))
print(x)
print(np.argmax(x))
print(y_test[0])

print(y_test1[0])
