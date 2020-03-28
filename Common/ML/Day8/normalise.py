import pandas as pd
# Normalize the data attributes for the Iris dataset.
from sklearn.datasets import load_iris
from sklearn import preprocessing
# load the iris dataset
iris = load_iris()
print(iris.data.shape)
# separate the data from the target attributes
X = iris.data
y = iris.target
# normalize the data attributes
#pd.set_option('display.float_format', lambda x: '%.3f' % x)
normalized_X = preprocessing.normalize(X)

print(normalized_X)
