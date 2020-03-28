from sklearn import datasets
from sklearn.decomposition import PCA

wine = datasets.load_wine()

print("Features: ", wine.feature_names)

print("Labels: ", wine.target_names)

wine.data.shape

print(wine.data[0:5])

print(wine.target)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test

from sklearn import svm

# initiate PCA and classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
pca = PCA(2)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# transform / fit

X_transformed = pca.fit_transform(wine.data)
print(X_transformed)

clf.fit(X_transformed, wine.target)
# predict "new" data

newdata = wine.data

# transform new data using already fitted pca
newdata_transformed = pca.transform(newdata)

# predict labels using the trained classifier

pred_labels = clf.predict(newdata_transformed)

print("Accuracy:",metrics.accuracy_score(wine.target,pred_labels))
print(confusion_matrix(wine.target,pred_labels))