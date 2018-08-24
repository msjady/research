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

import numpy as np


def EllipseFitting(x,y):

    sumx2 = sum([ix ** 2 for ix in x])
    sumy2 = sum([iy ** 2 for iy in y])
    sumy4 = sum([iy ** 4 for iy in y])

    sumxy = sum([ix * iy for (ix,iy) in zip(x,y)])
    sumx3y = sum([(ix ** 3) * iy for (ix,iy) in zip(x,y)])
    sumx2y2 = sum([(ix ** 2) * (iy ** 2) for (ix,iy) in zip(x,y)])
    sumxy3 = sum([ix * (iy ** 3) for (ix,iy) in zip(x,y)])



    F = np.array([[sumx2y2,sumxy3,sumxy],
                  [sumxy3,sumy4,sumy2],
                  [sumxy,sumy2,len(x)]])

    H = np.array([[-sumx3y],
                  [-sumx2y2],
                  [-sumx2]])

    T=np.linalg.inv(F).dot(H)

    #楕円の式をPrint
    print("x^2+"+T(1)+"xy+"+T(2)+"y^2+"+T(3)+"=0")



    '''
    #cxe=float((T[0]*T[3]-2*T[1]*T[2])/(4*T[1]-T[0]*T[0]))
    #cye=float((T[0]*T[2]-2*T[3])/(4*T[1]-T[0]*T[0]))
    theta = math.atan(T[0]/(1-T[1]))/2

    cos1 = math.cos(theta)
    cos2 = math.cos(theta) ** 2
    sin1 = math.sin(theta)
    sin2 = math.sin(theta) ** 2
    

    #tmpa = (cxe * cos1 + cye * sin1) ** 2 - T[4] * cos2 - (((cxe * sin1 - cye * cos1) ** 2 - T[4] * sin2) * ((sin2-T[1]*cos2)/(cos2 - T[1]*sin2)))
    #tmpb = (cxe * sin1 - cye * cos1) ** 2 - T[4] * sin2 - (((cxe * cos1 + cye * sin1) ** 2 - T[4] * cos2) * ((cos2-T[1]*sin2)/(sin2 - T[1]*cos2)))

    
    tmpa = - T[2] * cos2 + (T[2] * sin2) * ((sin2-T[1]*cos2)/(cos2 - T[1]*sin2))
    tmpb = - T[2] * sin2 + (T[2] * cos2) * ((cos2-T[1]*sin2)/(sin2 - T[1]*cos2))

    print(tmpa)

    a = math.sqrt(abs(tmpa))
    b = math.sqrt(abs(tmpb))

    g11 = (a ** 2 * sin2 + b ** 2 * cos2)/(a ** 2 * b ** 2)
    g12 = (2 * sin1 * cos1 * (b ** 2 - a ** 2))/(a ** 2 * b ** 2)
    g22 = (a ** 2 * cos2 + b ** 2 * sin2)/(a ** 2 * b ** 2)

    G = [[g11, g12],
         [g12, g22]]

    '''

    return (1)

