# Store the product's information
product = {
    "name": "Keyboard",
    "price": 1200,
    "stock": 15
}

print("Fields:")
for key in product.keys():
    print(key)

print("Values:")
for value in product.values():
    print(value)

print("Product information:")
for key, value in product.items():
    print(f"{key}: {value}")