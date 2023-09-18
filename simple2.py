import pandas as pd
df2=pd.read_csv("graduation_dataset.csv")
""" print(df2)
print(df2.head())
print(df2.head(10))
print(df2["GDP"])
print(df2["Course"])

print(df2[["Application mode","Target"]])
 """
print("**********************************************")
data=["name1","name2"]
col=["Name"]
row=["t1","t2"]
df = pd.DataFrame(data,columns=col)
print(df)
data={"id":[1,2,3,4],
      "number":["user1","user2","user3","user4"],
      "salary":[200,300,400,500]
      }
'''
col=["name"]
row=["e1","e2"]
'''
df= pd.DataFrame(data)
print(df)
print(df["number"])
print(df["Attendence"])



