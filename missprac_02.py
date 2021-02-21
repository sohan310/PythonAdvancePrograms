import pandas as pd
import numpy as np
df=pd.read_csv("Teams.csv")

####    PROBLEM NO 1    ####

a=df.groupby("Team")
div=a.get_group("Riders")
print(div)
b=a.get_group("Devils")
print(b)
c=a.get_group(" Kings")
print(c)
d=a.get_group("Royals")
print(d)
####    PROBLEM NO 2    ####

a=df.groupby("Team")
div=a.get_group("Riders")
print(div)
    

####    PROBLEM NO 3    ####

mp=df.groupby("Year")
m1=mp.get_group(2014)
print(m1.max())
####    PROBLEM NO 4    ####

x=df.groupby("Rank")
rank=x.get_group(1)
print(rank)


####    PROBLEM NO 5    ####

hp=df.groupby("Team")
rider=hp.get_group("Riders")
print(rider.max())

devils=hp.get_group("Devils")
print(devils.max())

kings=hp.get_group(" Kings")
print(kings.max())

royals=hp.get_group("Royals")
print(royals.max())

####    PROBLEM NO 6    ####

print(rider.mean())
print(devils.mean())
print(kings.mean())
print(royals.mean())


teams=df.groupby("Team")
print(teams["Points"].agg(np.mean))
