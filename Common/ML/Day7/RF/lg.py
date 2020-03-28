from sklearn.datasets import load_diabetes

data=load_diabetes()
X=data.data
y=data.target
print(X)
print(y)
