
import numpy as np
import math

# 楕円フィッティング
"""（参考）最小二乗法による円フィッティングをする関数
    input: x,y 円フィッティングする点群

    output  cxe 中心x座標
            cye 中心y座標
            re  半径

    参考
    一般式による最小二乗法（円の最小二乗法）　画像処理ソリューション
    http://imagingsolution.blog107.fc2.com/blog-entry-16.html
"""
"""(参考)勉強しよう数学3C
https://schoolhmath3c.blogspot.com/
"""


def EllipseFitting(x,y):
    
    sumx2 = sum([ix ** 2 for ix in x])
    sumx4 = sum([ix ** 4 for ix in x])
    sumy2 = sum([iy ** 2 for iy in y])
    sumy4 = sum([iy ** 4 for iy in y])

    sumxy = sum([ix * iy for (ix,iy) in zip(x,y)])
    sumx3y = sum([(ix ** 3) * iy for (ix,iy) in zip(x,y)])
    sumx2y2 = sum([(ix ** 2) * (iy ** 2) for (ix,iy) in zip(x,y)])
    sumxy3 = sum([ix * (iy ** 3) for (ix,iy) in zip(x,y)])



    F = np.array([[sumx4,sumx3y,sumx2y2],
                  [sumx3y,sumx2y2,sumxy3],
                  [sumx2y2,sumxy3,sumy4]])

    H = np.array([[sumx2],
                  [sumxy],
                  [sumy2]])

    T=np.linalg.inv(F).dot(H)


    #楕円の式をPrint
    #print(str(T[0])+"x^2+"+str(T[1])+"xy+"+str(T[2])+"y^2=1")

    t02 = T[0]-T[2]
    if t02 == 0:
        theta = math.pi/4.0
    else:   
        theta = math.atan(T[1]/(T[0]-T[2]))/2.0

    

    cos = math.cos(theta)
    sin = math.sin(theta)

    a2 = 1.0/(T[0]*cos*cos + T[1]*cos*sin + T[2]*sin*sin)
    a = math.sqrt(abs(a2)) #長軸

    cos = math.cos(theta+(math.pi/2.0))
    sin = math.sin(theta+(math.pi/2.0))

    b2 = 1.0/(T[0]*cos*cos + T[1]*cos*sin + T[2]*sin*sin)
    b = math.sqrt(abs(b2)) #短軸

    #print(str(a)+","+str(b))
    #print(theta)

    g = np.c_[np.r_[T[0],T[1]/2.0] , np.r_[T[1]/2.0,T[2]]]

    return (a,b,theta,g)