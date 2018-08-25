import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pylab as plt
from create_vec import create_vec

picmat = create_vec()

X_reduced = PCA(n_components=4).fit_transform(picmat)
xi = 1 #X軸は第何主成分
yi = 3 #Y軸は第何主成分
X = X_reduced[0:160,xi] / 1000
Y = X_reduced[0:160,yi] / 1000

plt.scatter(X[0:31], Y[0:31],c='red',label='Anger')
plt.scatter(X[32:63], Y[32:63],c='blue',label='Disgust')
plt.scatter(X[64:95], Y[64:95],c='green',label='Fear')
plt.scatter(X[96:127], Y[96:127],c='purple',label='Happy')
plt.scatter(X[128:159], Y[128:159],c='cyan',label='Sadness')
plt.show()