import numpy as np
import sympy as sym

def solveM(H,G):
    
    #H = M.T * G * M 
    H = np.around(np.array(H),decimals=0)
    G = np.around(np.array(G),decimals=0)

    print(G)
    print(H)
    
    X,Y,Z,W = sym.symbols('X Y Z W')
    sym.init_printing()

    E1 = G[0,0] * (X ** 2) + 2 * G[0,1] * X * Z + G[1,1] * (Z ** 2) - H[0,0]
    E2 = G[0,0] * X * Y + G[0,1] * (X * W + Y * Z) + G[1,1] * Z * W - H[0,1]
    E3 = G[0,0] * (Y ** 2) + 2 * G[0,1] * Y * W + G[1,1] * (W ** 2) - H[1,1]  
    E4 = X * Y + Z * W

    print("Sとく")
    #print(E1,E2,E3,E4)
    S = sym.solve([E1,E2,E3,E4],[X,Y,Z,W],dict = True,warn = True,manual = True)
    print("S終わる")

    i = 0
    #h = np.array(H)
    #g = np.array(G)

    #print(S)
    for i in range(8):
        M = [[S[i][X],S[i][Y]],
            [S[i][Z],S[i][W]]]
        m = np.array(M)

    print("dif解く")
    mcheck(m,H,G)
    print("dif終わる")

    return m