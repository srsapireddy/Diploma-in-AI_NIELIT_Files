from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("xclara.txt",delimiter='\t')
X=data.as_matrix()
plt.scatter(X[:,0],X[:,1])
plt.show()

kmeans=KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
print(y_kmeans)
centers=kmeans.cluster_centers_
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50,cmap='viridis')
plt.scatter(centers[:,0],centers[:,1],s=200,c='red')
plt.show()

