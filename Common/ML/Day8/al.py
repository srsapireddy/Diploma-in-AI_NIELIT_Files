from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score,KFold
from matplotlib import pyplot as plt
data=load_iris()
X=data.data
y=data.target

models=[]
models.append(("KNN",KNeighborsClassifier()))
models.append(("GNB",GaussianNB()))
models.append(("CART",DecisionTreeClassifier()))
models.append(("RF",RandomForestClassifier()))
models.append(("LG",LogisticRegression()))
results=[]
names=[]
for name,model in models:
	kfold=KFold(n_splits=10,random_state=7)
	v=cross_val_score(model,X,y,cv=kfold,scoring='accuracy')
	results.append(v)
	names.append(name)
	print(name)
	print(v)
fig=plt.figure()
fig.suptitle('Algorithm Comparison')
ax=fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


