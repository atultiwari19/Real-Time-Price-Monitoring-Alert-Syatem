# pip install requests
# pip install pandas
# pip install numpy
# pip install matplotlib
#  pip install seaborn

import requests
import json
data = requests.get("https://fakestoreapi.com/products")
product_data = json.loads(data.content)
column_name1 = product_data[0].keys()
column_name1 = list(column_name1)[0:5]
print(list(column_name1))

for i in product_data: 
    for j,k in i.items():
        print(j,k)
