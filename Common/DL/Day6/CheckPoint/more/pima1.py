from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import numpy


numpy.random.seed(10)


dataset = numpy.loadtxt("pimaindians.csv", delimiter=",")


X= dataset[:,0:8]
y= dataset[:,8]


model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


filepath="weights.best.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

model.fit(X, y, epochs=50, batch_size=10,callbacks=callbacks_list)


predictions = model.predict(X)

rounded = [round(x[0]) for x in predictions]
print(rounded)


scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))





# Fit the model
#model.fit(X, y, validation_split=0.33, epochs=150, batch_size=10, callbacks=callbacks_list, verbose=0)
