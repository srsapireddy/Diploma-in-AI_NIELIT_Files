# you can make this a lot easier using Pipeline

from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris,load_wine
iris=load_iris()
X=iris.data
y=iris.target
# fits PCA, transforms data and fits the decision tree classifier
# on the transformed data
pipe = Pipeline([('pca', PCA()),
                 ('tree', DecisionTreeClassifier())])

pipe.fit(iris.data, iris.target)

p=pipe.predict(iris.data)
print(confusion_matrix(iris.target,p))
