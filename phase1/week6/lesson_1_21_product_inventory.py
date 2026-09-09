# Store product information
product = {
    "name": "Keyboard",
    "price": 1200,
    "stock": 5
}

print("Original product:")
for key, value in product.items():
    print(f"{key}: {value}")

product["price"] = 1350
product["category"] = "Accessories"

if "stock" in product:
    print(f"Stock: {product["stock"]}")
else:
    print("Stock information is not available.")

if "discount" in product:
    print(f"Discount: {product["discount"]}")
else:
    print("Discount information is not available.")

print("Updated product:")
for key, value in product.items():
    print(f"{key}: {value}")

print(f"Number of fields: {len(product)}")