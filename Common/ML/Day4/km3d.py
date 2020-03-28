import pandas as pd;
import numpy as np
import matplotlib.pyplot as plt
data =pd.read_csv('sample.csv', delimiter =',')
print(data.head())
data=data.as_matrix()
f1=data[:,0]
f2=data[:,1]
f3=data[:,2]

X=data
#f1=data['x'].values
#f2=data['y'].values
#f3=data['z'].values

#X=np.array(list(zip(f1,f2,f3)))

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(f1, f2, f3, c=y_kmeans,cmap='viridis');

centers = kmeans.cluster_centers_

plt.show()
