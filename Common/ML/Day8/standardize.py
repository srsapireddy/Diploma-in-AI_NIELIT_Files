import pandas as pd
# Standardize the data attributes for the Iris dataset.
from sklearn.datasets import load_iris
from sklearn import preprocessing
# load the Iris dataset
iris = load_iris()
print(iris.data.shape)
# separate the data and target attributes
X = iris.data
y = iris.target
# standardize the data attributes
pd.set_option('display.float_format', lambda X: '%.3f' % X)
standardized_X = preprocessing.scale(X)

print(standardized_X)

