import math
from matplotlib import pylab as plt
import matplotlib.patches as patches

def show(X,Y,Thresholdx_alice,Thresholdy_alice,Thresholdx_bob,Thresholdy_bob,pic_num_1f,a1,b1,theta1,a2,b2,theta2):

    plt.scatter(X[0], Y[0],c='lime',label='center')
    plt.scatter(X[1:pic_num_1f], Y[1:pic_num_1f],c='red',label='Anger')
    plt.scatter(X[pic_num_1f+1:pic_num_1f*2], Y[pic_num_1f+1:pic_num_1f*2],c='blue',label='Disgust')
    plt.scatter(X[pic_num_1f*2+1:pic_num_1f*3], Y[pic_num_1f*2+1:pic_num_1f*3],c='green',label='Fear')
    plt.scatter(X[pic_num_1f*3+1:pic_num_1f*4], Y[pic_num_1f*3+1:pic_num_1f*4],c='purple',label='Happy')
    plt.scatter(X[pic_num_1f*4+1:pic_num_1f*5], Y[pic_num_1f*4+1:pic_num_1f*5],c='cyan',label='Sadness')

    plt.plot(Thresholdx_alice,Thresholdy_alice,"ob",color = "pink",label="threshold1") 
    plt.plot(Thresholdx_bob,Thresholdy_bob,"ob",color = "black",label="threshold2") 

    e1 = patches.Ellipse(xy=(0, 0), width=2*a1, height=2*b1,angle = math.degrees(theta1),fc='white', ec='r',alpha=0.3,label = "Alice_ellipse")
    e2 = patches.Ellipse(xy=(0, 0), width=2*a2, height=2*b2,angle = math.degrees(theta2),fc='white', ec='b',alpha=0.3,label = "Bob_ellipse")

    ax = plt.axes()

    ax.add_patch(e1)
    ax.add_patch(e2)

    plt.axis('scaled')

    plt.legend()
    plt.show()