from sklearn import datasets
from sklearn.decomposition import PCA

cancer = datasets.load_breast_cancer()

print("Features: ", cancer.feature_names)

print("Labels: ", cancer.target_names)

cancer.data.shape

print(cancer.data[0:5])

print(cancer.target)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test

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

X_transformed = pca.fit_transform(cancer.data)
print(X_transformed)

clf.fit(X_transformed, cancer.target)
# predict "new" data

newdata = cancer.data

# transform new data using already fitted pca
newdata_transformed = pca.transform(newdata)

# predict labels using the trained classifier

pred_labels = clf.predict(newdata_transformed)

print("Accuracy:",metrics.accuracy_score(cancer.target,pred_labels))
print(confusion_matrix(cancer.target,pred_labels))