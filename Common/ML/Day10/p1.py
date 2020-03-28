from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
iris=load_iris()
X=iris.data
y=iris.target

print(X)
print(X.shape)
pca=PCA(2)

X_transformed=pca.fit_transform(X)

print(X_transformed)
print(X_transformed.shape)
tree1=LinearDiscriminantAnalysis()
tree2=DecisionTreeClassifier()

p=tree1.fit(X,y).predict(X)
pt=tree2.fit(X_transformed,y).predict(X_transformed)

print(confusion_matrix(p,y))
print(confusion_matrix(pt,y))
