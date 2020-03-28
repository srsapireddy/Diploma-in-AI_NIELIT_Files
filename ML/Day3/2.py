from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris=load_iris()
X=iris.data

print(X)
plt.scatter(X[:,0],X[:,1])
plt.show()

kmeans=KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
print(y_kmeans)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,cmap='viridis')
plt.show()