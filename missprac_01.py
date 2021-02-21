import pandas as pd
df=pd.read_csv("titanic.csv")
print(df)

####    PROBLEM NO 1    ####

print(df.isna().sum())


####    PROBLEM NO 2    ####

df=df.fillna(0)
print(df.isna().sum())
print(df)


####    PROBLEM NO 3    ####

df["Name"]=df["Name"].fillna("Unknown")
print(df["Name"])


####    PROBLEM NO 4    ####

avg=df["Age"].mean()
df["Age"]=df["Age"].fillna(avg)
print(df.isna().sum())
print(df["Age"])

####    PROBLEM NO 5    ####

df["Cabin"]=df["Cabin"].fillna("NA")
print(df["Cabin"])

####    PROBLEM NO 6    ####

df["Survived"]=df["Survived"].replace({0:"Dead",1:"Alive"})
print(df["Survived"])
print(df)
