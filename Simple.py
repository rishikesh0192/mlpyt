import pandas as pd

df =pd.read_csv("retail_sales_dataset.csv")
print(df)
""" print("*********************************")
print(df.head())
 """
print("*********************************")
#print(df.head(0))
df1=df.head(10)
print(df1["Product Category"])
print(df1[["Product Category","Date"]])


data =["user1","user2"]
col=["name"]
row=["r1","r2"]
df = pd.DataFrame(data,columns=col,index=row)
print(df)
print(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%)
print(df.head())

