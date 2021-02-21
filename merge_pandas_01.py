import pandas as pd

d1={"id":[1,2,3,4,5],"name":["a","b","c","d","e"]}
d2={"id":[1,2,3,4,5],"marks":[11,22,33,44,55]}

##print(d1)
##print(d2)
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
##d3=pd.merge(df1,df2,on="id")
##print(d3)
##d4=pd.concat([df1,df2],keys=["1st","2nd"],sort=False)
##print(d4)

print(df1[(df1.name=="c") | (df1.id==4)])
print(df2[(df2.marks==33) | (df2.id==1)])
