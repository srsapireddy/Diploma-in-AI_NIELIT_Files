from sklearn.datasets.samples_generator import make_moons
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering 
from sklearn.cluster import KMeans

X,y_true=make_moons(300,noise=0.05,random_state=0)

plt.scatter(X[:,0],X[:,1],s=50,cmap='viridis')
print(X)

sc=SpectralClustering(n_clusters=2,affinity='nearest_neighbors')

#sc.fit(X)
y_sc=sc.fit_predict(X)
print(y_sc)
plt.scatter(X[:,0],X[:,1],c=y_sc,s=50,cmap='viridis')
'''
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
'''
plt.show()


