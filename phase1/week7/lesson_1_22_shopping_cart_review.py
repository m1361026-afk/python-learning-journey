# Store the cart information
cart = [
    {"name": "Keyboard", "price": 1200, "quantity": 1},
    {"name": "Mouse", "price": 650, "quantity": 2},
    {"name": "Monitor", "price": 5200, "quantity": 1},
    {"name": "USB Cable", "price": 180, "quantity": 3}
]
# Set variables to calculate the total price of the cart and count the amount of goods in cart
total = 0
total_quantity = 0
# Store the names of products whose subtotal is at least 1000
products_at_least_1000 = []
# Get the information from the cart
for info in cart:
    subtotal = info["price"] * info["quantity"]
    print(f"{info["name"]}: {subtotal}")
    total += subtotal
    # Store products whose subtotal meets the threshold
    if subtotal >= 1000:
        products_at_least_1000.append(info["name"])
    total_quantity += info["quantity"]

print(f"Total: {total}")
print(f"Products with subtotal at least 1000: {products_at_least_1000}")
print(f"Total quantity: {total_quantity}")
# Determine shipping eligibility based on the total price
if total >= 7000:
    print(f"Free shipping")
else:
    print("Shipping fee required")