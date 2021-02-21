import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
#---Matrix Sliced By Row---

#print(a[row,column])
#print(a[startrow:stoprow:Step_of_row,startcol:stopcol:stepcol])
print("Slicing by row with one jump\n=",a[::2,:],"\n")
print("Slicing by column with one jump\n=",a[:,0::2],"\n")
print("slicing by 1st and last row with one jump \n=",a[::2,::2],"\n")
print("Slicing to Central ele\n=",a[1:2:1,1:2:1])
