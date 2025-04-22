import json,requests

products=requests.get('https://dummyjson.com/products')
#print(type(product))# <class 'list'>

fp=none
try:
    fp =open('products.json','w')
    json.dump(products,fp)
    print("new json file created successfully")
except Exception as err:
    print(err)
finally:
    fp.close()
    

