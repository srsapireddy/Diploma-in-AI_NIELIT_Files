import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
(X_train,y_train),(X_test,y_test)=mnist.load_data()
print(X_train.shape)


from keras.utils import to_categorical
classes=np.unique(y_train)

nClasses=len(classes)
print(nClasses)
print(classes)

plt.figure(figsize=[10,5])

plt.subplot(121)
plt.imshow(X_train[0,:,:],cmap='gray')
plt.title(y_train[0])
#plt.show()


dimData=np.prod(X_train.shape[1:])
print(dimData)
print(X_train[0])
X_train=X_train.reshape(X_train.shape[0],1,28,28)
X_test=X_test.reshape(X_test.shape[0],1,28,28)

X_train=X_train.astype('float32')
y_train=y_train.astype('float32')


X_train/=255
X_test=X_test/255
print(X_test)
y_train1=to_categorical(y_train)
y_test1=to_categorical(y_test)

print(y_train)
print(y_train1[1:10])


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras import backend as K
K.set_image_dim_ordering('th')


def base_model():

	# create model
	model = Sequential()
	model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(15, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(10, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

model=base_model()

print(model.summary())

#model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200)
history=model.fit(X_train,y_train1,batch_size=256,epochs=2,verbose=1,validation_data=(X_test,y_test1))
[test_loss,test_acc]=model.evaluate(X_test,y_test1)
print(test_loss,test_acc)


