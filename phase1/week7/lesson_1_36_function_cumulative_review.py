cart = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 25, "quantity": 4},
    {"name": "Backpack", "price": 1200, "quantity": 1},
    {"name": "Calculator", "price": 650, "quantity": 2}
]

def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal

def get_high_subtotal_products(cart, threshold):
    high_subtotal_products = []

    for order in cart:
        subtotal = calculate_subtotal(order["price"], order["quantity"])
        if subtotal >= threshold:
            high_subtotal_products.append(order["name"])

    return high_subtotal_products

def check_shipping(total):
    if total >= 2500:
        return "Free shipping"
    return "Shipping fee required"

total = 0
total_quantity = 0
for order in cart:
    subtotal = calculate_subtotal(order["price"], order["quantity"])
    total += subtotal
    total_quantity += order["quantity"]

high_subtotal_products = get_high_subtotal_products(cart, 1000)
shipping = check_shipping(total)

print(f"Total: {total}")
print(f"Total quantity: {total_quantity}")
print(f"Products with subtotal at least 1000: {high_subtotal_products}")
print(f"Shipping: {shipping}")
    