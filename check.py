import pandas as pd

df= pd.read_csv('project/IPL_Matches_2008_2022.csv')


#print(df.loc[1:2])


#print(df.loc[1:5,"City":"Team2"])


#print(df.loc[1:5,:"Team2"])

"""print(df.loc[df["City"]=="Ahmedabad"])
print(df.loc[df["City"]=="Mumbai"])"""


"""City=[]
City.append(df.loc[df["City"]=="Ahmedabad"])
for index,data in df.loc[df["City"]=="Ahmedabad"].iterrows():
    City.append(data)
print(City)"""



#print(df.loc[1:5].loc[:,["Venue","Team2"]])
#print(df.loc[1:5].loc[:,"City":"Team1"])
#print(df.loc[1:5].loc[:,"City"])
#print(df.loc[1:5].loc[:,:"Season"])
#print(df.loc[df["City"]=="Ahmedabad"])


#print(df.iloc[1:8])
#print(df.iloc[1:8,2])
#print(df.iloc[1:8,2:])
#print(df.iloc[1:8,:-6])

#print(df.iloc[1:8:,-4:-1])

"""print(df.where(df.City=="Mumbai","NA",))
"""


#print(df.filter(items=["City","Umpire1"]))

"""print(df.filter(items=[1,4],axis=0))
print(df.filter(like='23',axis=0))"""

df1 =df.query("City in ('Delhi','Hyderabad')")
print(df1)
print(df1.groupby(['City']))
for data,group in df1.groupby(['City',"Team1"]):
    print(data)
    print(group)



















