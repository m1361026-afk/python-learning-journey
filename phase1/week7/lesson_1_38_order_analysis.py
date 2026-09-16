orders = [
    {"product": "Keyboard", "price": 1200, "quantity": 2},
    {"product": "Mouse", "price": 650, "quantity": 1},
    {"product": "Monitor", "price": 5200, "quantity": 1},
    {"product": "USB Cable", "price": 180, "quantity": 4}
]

def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_order_total(orders):
    total = 0
    for order in orders:
        total += calculate_subtotal(order["price"], order["quantity"])
    return total

def get_high_value_products(orders, threshold):
    high_value_products = []
    for order in orders:
        if calculate_subtotal(order["price"], order["quantity"]) >= threshold:
            high_value_products.append(order["product"])
    return high_value_products

def check_discount(total):
    if total >= 8000:
        return "Discount eligible"
    return "No discount"

for order in orders:
    print(f"{order["product"]}: {calculate_subtotal(order["price"], order["quantity"])}")

order_total = calculate_order_total(orders)
print(f"Total: {order_total}")
print(f"High-value products: {get_high_value_products(orders, 2000)}")
print(f"Discount: {check_discount(order_total)}")

print(check_discount(7999))
print(check_discount(8000))
print(check_discount(8001))