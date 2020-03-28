from sklearn.datasets import load_digits
from sklearn.metrics  import confusion_matrix
digits=load_digits()
X=digits.data
y=digits.target

print(digits.images.shape)
print(X[1,])
print(y)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()

p=dt.fit(X,y).predict(X)
print(confusion_matrix(p,y))



i_g=list(zip(digits.images,digits.target))
import matplotlib.pyplot as plt
for index,(image,label) in enumerate(i_g[10:17]):
	plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r)
	plt.title(label)
plt.show()
	
