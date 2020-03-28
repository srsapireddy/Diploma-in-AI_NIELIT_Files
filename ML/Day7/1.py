#!usr/bin/env python3
# Random Forest Classifier

# Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score


# Importing the dataset
dataset = pd.read_csv('pimaindians.csv')
X = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train,y_train)
p=classifier.predict(X_test)
print(p)
print(accuracy_score(y_test,p))
print(confusion_matrix(y_test,p))