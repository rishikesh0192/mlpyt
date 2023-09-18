import pandas as pd
import matplotlib.pyplot as plt

def Line(type):

    plt.plot(type)
    plt.show()
    
def Bar(df1,df2):
    
    plt.bar(df1,df2)
    plt.show()

def Graph(df1,df2):
    num = int(input("Enter 1 for line\nenter 2 for bar"))
    if num==1:
        Line(df1)
    elif num==2:
        Bar(df1,df2)

def Data(df1,df2):

    print(df1)
    print(df2)

while True:
    num =int(input("enter 1 for graph\n2 for data\n3 form break\n"))
    df=pd.read_csv("retail_sales_dataset.csv")
    df1=df.head(10)
    print(df.head(0))
    data1 = input("enter col1")
    data2 = input("enter col2")
    datadf1=df1[data1]
    datadf2=df1[data2]

    




