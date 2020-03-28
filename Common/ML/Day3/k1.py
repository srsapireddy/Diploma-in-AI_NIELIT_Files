from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
X,y_true=make_blobs(n_samples=300,centers=4,cluster_std=0.6)
print(X)
plt.scatter(X[:,0],X[:,1])
plt.show()

kmeans=KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
print(y_kmeans)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,cmap='viridis')
plt.show()
print(confusion_matrix(y_true,y_kmeans))

