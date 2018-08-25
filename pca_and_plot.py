import numpy as np
from sklearn.decomposition import PCA
from create_vec import create_vec

def pca_pic():
    [picmat,pic_num,pic_num_1f] = create_vec()

    PCA(n_components=4).fit(picmat)
    X_reduced = PCA(n_components=4).fit_transform(picmat)

    return(X_reduced,pic_num,int(pic_num_1f))

