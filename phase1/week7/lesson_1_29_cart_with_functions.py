cart = [
    {"name": "Keyboard", "price": 1200, "quantity": 1},
    {"name": "Mouse", "price": 650, "quantity": 2},
    {"name": "Monitor", "price": 5200, "quantity": 1},
    {"name": "USB Cable", "price": 180, "quantity": 3}
]

def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal

def check_shipping(total):
    if total >= 7000:
        return "Free shipping"
    else:
        return "Shipping fee required"
# Track the order total, total quantity, and products that meet the subtotal threshold
total = 0
total_quantity = 0
products_at_least_1000 = []

for order in cart:
    subtotal = calculate_subtotal(order["price"], order["quantity"])
    print(f"{order["name"]}: {subtotal}")
    total += subtotal
    total_quantity += order["quantity"]
    if subtotal >= 1000:
        products_at_least_1000.append(order["name"])

print(f"Total: {total}")
print(f"Total quantity: {total_quantity}")
print(f"Products with subtotal at least 1000: {products_at_least_1000}")

shipping_result = check_shipping(total)
print(f"Shipping: {shipping_result}")