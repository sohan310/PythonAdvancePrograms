import pandas as pd
df=pd.read_csv("Teams.csv")
#print(df)

#---
a=df.groupby("Team")
print(a.groups)
div=a.get_group("Riders")
print(div)

##year=df.groupby("Year")
##print(year.groups)
