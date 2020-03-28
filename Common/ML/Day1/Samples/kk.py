from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
X,y_true =make_blobs(n_samples=300,centers=4,cluster_std=0.6)
print(X)
plt.scatter(X[:,0],X[:,1],s=50)
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=100,cmap='viridis')
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='black',s=200)
plt.show()
