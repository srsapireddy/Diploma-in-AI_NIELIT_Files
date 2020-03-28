
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
# load data
iris = load_iris()

pca = PCA()
classifier = LinearDiscriminantAnalysis()


X_transformed = pca.fit_transform(iris.data)

classifier.fit(X_transformed, iris.target)

newdata = iris.data

newdata_transformed = pca.transform(newdata)


pred_labels = classifier.predict(X_transformed)

print(confusion_matrix(iris.target,pred_labels))
