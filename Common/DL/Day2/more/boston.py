import numpy as np

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

iris_data = load_boston() # load the iris dataset
x = iris_data.data
y_ = iris_data.target.reshape(-1, 1) # Convert data to a single column
# One Hot encode the class labels
y=y_
'''
encoder = OneHotEncoder()
#encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y_)
#print(y)
'''
# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)

# Build the model

model = Sequential()

model.add(Dense(10, input_shape=(13,), activation='relu', name='fc1'))
model.add(Dense(10, activation='relu', name='fc2'))
model.add(Dense(1, activation='linear', name='output'))

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='mean_squared_error', metrics=['mse'])

print('Neural Network Model Summary: ')
print(model.summary())



# Train the model
model.fit(train_x, train_y, verbose=1, batch_size=50, epochs=150)

# Test on unseen data

results = model.evaluate(test_x, test_y)

print('Final test set loss: {:4f}'.format(results[0]))
print('Final test set accuracy: {:4f}'.format(results[1]))

