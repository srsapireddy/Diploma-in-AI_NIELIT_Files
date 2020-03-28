from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
# load data
iris = load_iris()

# initiate PCA and classifier
pca = PCA(3)
classifier = DecisionTreeClassifier()

# transform / fit

X_transformed = pca.fit_transform(iris.data)
print(X_transformed)

classifier.fit(X_transformed, iris.target)
# predict "new" data
# (I'm faking it here by using the original data)

newdata = iris.data

# transform new data using already fitted pca
# (don't re-fit the pca)
newdata_transformed = pca.transform(newdata)

# predict labels using the trained classifier

pred_labels = classifier.predict(newdata_transformed)

print(confusion_matrix(iris.target,pred_labels))
