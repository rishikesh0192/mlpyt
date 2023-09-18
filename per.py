import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('csv files/pokemon_data.csv')
#print top 10......
print(df.head(10))
#groupby single col.......
'''data=df.groupby("Model")
for name,group in data:
    print(name)'''
################################
name= input("enter cols1")
name1= input("enter cols2")
col1 =df[name]
col2 =df[name1]
plt.plot(col1,col2)
plt.show()
