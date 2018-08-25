'''
Aというフォルダの画像全体をベクトル化するプログラム
'''

import os
import pathlib
import numpy as np
from PIL import Image

def create_vec():

    picdir = pathlib.Path.cwd().parent / 'pictures/ver1/'

    firstpic = np.reshape(np.array(Image.open(str(picdir)+'/000.jpg')),(1,-1))
    picmat = firstpic


    for dirs in picdir.iterdir():
        if dirs.is_dir():
            for p in dirs.iterdir():
                pic_tmp = np.reshape(np.array(Image.open(p)),(1,-1))
                picmat = np.append(picmat,pic_tmp,axis=0)
    return(picmat)


