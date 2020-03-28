from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering 
X,y_true=make_moons(n_samples=300,noise=0.05,random_state=0)
print(X)

model=SpectralClustering(n_clusters=2, affinity='nearest_neighbors')

#model.fit(X)
y_kmeans=model.fit_predict(X)
print(y_kmeans)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50,cmap='viridis')
#centers=kmeans.cluster_centers_
#plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()

