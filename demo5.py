import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("car.csv")
print(df.head(0))
df1=df.head(10)
name= input("enter cols1")
name1= input("enter cols2")
print(df1[name])
col1 =df1[name]
col2 =df1[name1]
plt.plot(col1,col2)
plt.show()

