##default
""" 
def Graph():
    print("graph")
def Data():
    print("data")


while True:
    num =int(input("enter 1 for graph\n2 for data\n3 form break"))
   
    if num==1:
        Graph()
    elif num==2:
        Data()
    elif num==3:
        break
    else:
        print("enter right input")
 """        
""" 
def Graph():
     return "graph"
def Data():
    return "data"

##default loop
while True:
    num =int(input("enter 1 for graph\n2 for data\n3 form break"))
   
    if num==1:
        print(Graph())
    elif num==2:
        d=Data()
        print(d)
    elif num==3:
        break
    else:
        print("enter right input")
 """
""" 
def Graph(name):
    print(name)
def Data(name):
    print(name)


while True:
    num =int(input("enter 1 for graph\n2 for data\n3 form break"))
   
    if num==1:
        Graph("graph")
    elif num==2:
        Data("data")
    elif num==3:
        break
    else:
        print("enter right input") """

import pandas as pd
import matplotlib.pyplot as plt
def Graph(name):
    plt.plot(name)
    plt.show()
    
def Data(name):

    print(name)

while True:
    num =int(input("enter 1 for graph\n2 for data\n3 form break"))
    df =pd.DataFrame([3,2,5,4,6,7,7])
    if num==1:
        Graph(df)
    elif num==2:
        Data(df)
    elif num==3:
        break
    else:
        print("enter right input")