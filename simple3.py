import pandas as pd

df= pd.read_csv('project/IPL_Matches_2008_2022.csv')

print(df)
print(df.iloc[780:])
#print(df.loc[10:30])
print(df.loc[10:20,["Team1","Team2"]])
df1 =df.query("City in ('Hyderabad')")
print(df1)
print(df1.groupby(['Team2']))




'''city=[]
for index,data in df.loc[df["City"]=="Ahmedabad"].iterrows():
    city.append(data)
print(city)'''









