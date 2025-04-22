import requests
data = requests.get('https://dummyjson.com/products')
product_data=data.json()
status_code = data.status_code
print(product_data)
print(status_code)
print(type(producet_data))
print(type(status_code))
print(len(products))