import pathlib
import numpy as np
from pca_and_plot import pca_pic
from get_threshold import get_threshold
from ellipsefitting import EllipseFitting

path = pathlib.Path.cwd().parent / 'data/Thresholds/'

[X_reduced,pic_num,pic_num_1f] = pca_pic()

xi = 1 #X軸は第何主成分
yi = 3 #Y軸は第何主成分

X = (X_reduced[0:pic_num,xi] - X_reduced[0,xi])/1000.0
Y = (X_reduced[0:pic_num,yi] - X_reduced[0,yi])/1000.0

[Thresholdx_alice,Thresholdy_alice] = get_threshold(X,Y,pic_num_1f,str(path)+"/Alice.txt")
[Thresholdx_bob,Thresholdy_bob] = get_threshold(X,Y,pic_num_1f,str(path)+"/Bob.txt")

print(Thresholdx_alice)

EllipseFitting(Thresholdx_alice,Thresholdy_alice)


