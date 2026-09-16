products = [
    {"name": "Laptop Stand", "price": 1500, "quantity": 2},
    {"name": "Webcam", "price": 2200, "quantity": 1},
    {"name": "USB Hub", "price": 800, "quantity": 3},
    {"name": "Desk Lamp", "price": 950, "quantity": 1}
]

def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_order_total(products):
    total = 0
    for product in products:
        total += calculate_subtotal(product["price"], product["quantity"])
    return total

def get_high_subtotal_products(products, threshold):
    high_subtotal_products = []
    for product in products:
        if calculate_subtotal(product["price"], product["quantity"]) >= threshold:
            high_subtotal_products.append(product["name"])
    return high_subtotal_products

def get_membership_level(total):
    if total >= 8000:
        return "Gold"
    elif total >= 5000:
        return "Silver"
    else:
        return "Standard"

total_quantity = 0
for product in products:
    total_quantity += product["quantity"]
    print(f"{product["name"]}: {calculate_subtotal(product["price"], product["quantity"])}")

products_total = calculate_order_total(products)
print(f"Order total: {products_total}")
print(f"Total quantity: {total_quantity}")
print(f"High-value products: {get_high_subtotal_products(products, 2000)}")
print(f"Membership level: {get_membership_level(products_total)}")

print(get_membership_level(4999))
print(get_membership_level(5000))
print(get_membership_level(7999))
print(get_membership_level(8000))