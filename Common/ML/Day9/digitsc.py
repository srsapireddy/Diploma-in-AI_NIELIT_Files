from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
data=load_digits()
X=data.data
y=data.target
print(data.images.shape)
print(X.shape)
print(y.shape)

import matplotlib.pyplot as plt
print(y)
print(X[1,:])
i_g=list(zip(data.images,y))
for index,(image,label) in enumerate(i_g[:8]):
	plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r)
	plt.title(label)
plt.show()

tree=DecisionTreeClassifier()
p=tree.fit(X,y).predict(X)

print(p)
print(y)
print(confusion_matrix(p,y))

