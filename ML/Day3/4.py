from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
data=pd.read_csv("Example.csv",delimiter='\t')

X=data


print(X)

kmeans=KMeans(n_clusters=3)

kmeans.fit(X)
y_kmeans=kmeans.predict(X)
print(y_kmeans)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50,cmap='viridis')
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()
