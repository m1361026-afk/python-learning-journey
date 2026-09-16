cart = [
    {"name": "Keyboard", "price": 1200, "quantity": 1},
    {"name": "Mouse", "price": 650, "quantity": 2},
    {"name": "Monitor", "price": 5200, "quantity": 1},
]

def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal

def calculate_cart_total(cart):
    total = 0
    for order in cart:
        subtotal = calculate_subtotal(order["price"], order["quantity"])
        total += subtotal
    return total

cart_total = calculate_cart_total(cart)
print(f"The total price of the cart: {cart_total}")