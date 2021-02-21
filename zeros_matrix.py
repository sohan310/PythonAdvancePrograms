import numpy as np

#---MATRIX FILLED WTH ZEROS ---

a=np.zeros((3,4))
print(a)

#---MATRIX FILLED WITH ONES ---

b=np.ones((3,4))
print(b)

#---MATRIX FILLED WITH USER NUMBER ---

c=np.full((3,3),3)
print(c)

#---MATRIX WITH RANDOM DECIMAL NUMBER ---

d=np.random.random((3,4))
print(d)

#---MATRIX WITH RANDOM NUMBERS ---

e=np.random.randint(0,20,(3,4))
print(e)

#---MATRIX RESHAPING ---

f=np.array([[2,1],[3,5],[6,7],[8,9]])
print(f.reshape(4,2))

g=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
print(g.reshape(3,4))

#---Matrix reshaping with multiple columns ---

print(g.reshape(1,-1))

#--- martix Flattening converts(2d into 1d) ---

print(g.flatten())

#--- Matrix Min And Max And Sum ---

h=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(h.min())
print(h.max())
print(h.sum())
print("min from col",h.min(axis=0))
print("max from col",h.max(axis=0))
print("sum from col",h.sum(axis=0))
print("min from row",h.min(axis=1))
print("max from row",h.max(axis=1))
print("sum from row",h.sum(axis=1))

#--- Sorting Matrix if numbers are not in order --- 
print(np.sort(h,axis=0))
