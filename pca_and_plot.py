import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pylab as plt
from create_vec import create_vec

picmat = create_vec()
print(picmat.shape)

PCA(n_components=4).fit(picmat)
X_reduced = PCA(n_components=4).fit_transform(picmat)

xi = 1 #X軸は第何主成分
yi = 3 #Y軸は第何主成分

X = (X_reduced[0:155,xi] - X_reduced[0,xi])/1000.0
Y = (X_reduced[0:155,yi] - X_reduced[0,yi])/1000.0

plt.scatter(X[0], Y[0],c='lime',label='center')
plt.scatter(X[1:31], Y[1:31],c='red',label='Anger')
plt.scatter(X[32:62], Y[32:62],c='blue',label='Disgust')
plt.scatter(X[63:93], Y[63:93],c='green',label='Fear')
plt.scatter(X[94:124], Y[94:124],c='purple',label='Happy')
plt.scatter(X[125:155], Y[125:155],c='cyan',label='Sadness')
plt.show()