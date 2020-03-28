from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

from mpl_toolkits import mplot3d
data=pd.read_csv("sample.csv")

X=data.as_matrix()


print(X)

kmeans=KMeans(n_clusters=5)

kmeans.fit(X)
y_kmeans=kmeans.predict(X)
print(y_kmeans)
fig=plt.figure()
ax=plt.axes(projection='3d')


ax.scatter3D(X[:,0],X[:,1],X[:,2],c=y_kmeans,s=50,cmap='viridis')
centers=kmeans.cluster_centers_
ax.scatter3D(centers[:,0],centers[:,1],centers[:,2],s=200,c='red')
plt.show()
