pic_num=156
pic_num_1f=31

plt.scatter(X[0], Y[0],c='lime',label='center')
plt.scatter(X[1:pic_num_1f], Y[1:pic_num_1f],c='red',label='Anger')
plt.scatter(X[pic_num_1f+1:pic_num_1f*2], Y[pic_num_1f+1:pic_num_1f*2],c='blue',label='Disgust')
plt.scatter(X[pic_num_1f*2+1:pic_num_1f*3], Y[pic_num_1f*2+1:pic_num_1f*3],c='green',label='Fear')
plt.scatter(X[pic_num_1f*3+1:pic_num_1f*4], Y[pic_num_1f*3+1:pic_num_1f*4],c='purple',label='Happy')
plt.scatter(X[pic_num_1f*4+1:pic_num_1f*5], Y[pic_num_1f*4+1:pic_num_1f*5],c='cyan',label='Sadness')
plt.show()