from sklearn import preprocessing
enc = preprocessing.OneHotEncoder()
X=[[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
enc.fit(X)  
print(X)
X=enc.transform(X)
print(X.toarray())
print(X)

