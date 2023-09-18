import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("car.csv")

print(df.head(0))
data1=[]
data2=[]
data=df.groupby("Price")
for name,group in data:
    print(name)
    print(sum(group["Ferrari"]))
    data1.append(name)
    #data2.append(sum(group["Quantity"]))
    #data2.append(max(group["Quantity"]))
    #data2.append(min(group["Quantity"]))


#plt.bar("data1,data2")
#plt.hist([300,350,370])
#plt.scatter([2,3,4],[3,2,6])
#plt.show()