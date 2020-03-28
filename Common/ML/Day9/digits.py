from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

digits=load_digits()
X=digits.data
y=digits.target
print(X.shape)
print(y.shape)
print(digits.images.shape)
#print(y[0])
#print(digits.images[0])
svm=SVC()
svm.fit(X,y)
p=svm.predict(X)
print(confusion_matrix(y,p))
print(y)
print(p)
import matplotlib.pyplot as plt

i_g=list(zip(digits.images,digits.target))
for index,(image,label) in enumerate(i_g[:8]):
	plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r)
	plt.title(label)
plt.show()



