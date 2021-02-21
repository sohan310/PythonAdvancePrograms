import pandas as pd
ab=pd.read_csv("Teams.csv")
print(ab)

print(ab.info())

print(ab.head())

print(ab.tail())
print(ab.iloc[[2,4,6],[1,3]])

print(ab.loc[:3,["Rank","Year"]])

first_point=ab.iloc[0][0]
print(first_point)
print(ab.iloc[[0],:])

print(ab.loc[:10,["Year"]])
print(ab.iloc[:10,[3]])

sample_records=ab.iloc[[1,2,3,5,8],:]
print(sample_records)


print(ab.loc[[0,5,10],["Rank","Points","Team"]])

ab1=ab.tail(5).iloc[:,[1,2]]
print(ab1)
'''

print(ab.iloc[::2,:])
print(ab.iloc[1::2,:])
'''
