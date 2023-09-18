import json
import requests

print(requests)
#r= requests.get('https://jsonplaceholder.typicode.com/todos')
r= requests.get('http://ankursingh.xyz/api/productshow.php')
'''print(type(r))
print(r)
l =[]'''

df2= r.json().values()
data1=[]
for i in df2:
    data1.append(i)
data2=data1[0][0]
print(data2['product_id'])




