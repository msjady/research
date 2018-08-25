pic_num=156
pic_1folder=31

plt.scatter(X[0], Y[0],c='lime',label='center')
plt.scatter(X[1:pic_1folder], Y[1:pic_1folder],c='red',label='Anger')
plt.scatter(X[pic_1folder+1:pic_1folder*2], Y[pic_1folder+1:pic_1folder*2],c='blue',label='Disgust')
plt.scatter(X[pic_1folder*2+1:pic_1folder*3], Y[pic_1folder*2+1:pic_1folder*3],c='green',label='Fear')
plt.scatter(X[pic_1folder*3+1:pic_1folder*4], Y[pic_1folder*3+1:pic_1folder*4],c='purple',label='Happy')
plt.scatter(X[pic_1folder*4+1:pic_1folder*5], Y[pic_1folder*4+1:pic_1folder*5],c='cyan',label='Sadness')
plt.show()