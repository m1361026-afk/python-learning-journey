def calculate_with_print(price, quantity):
    total = price * quantity
    print(total)

def calculate_with_return(price, quantity):
    return price * quantity

result_1 = calculate_with_print(650, 2)
result_2 = calculate_with_return(650, 2)

print(f"result_1: {result_1}")
print(f"result_2: {result_2}")