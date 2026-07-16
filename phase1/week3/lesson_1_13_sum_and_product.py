# Calculate the sum and product from 0 to the number user entered
user_input = int(input("Please enter a number: "))

# # Validate the number before starting the calculation
if 1 <= user_input <= 10:
    total = 0
    product = 1
    stop = user_input + 1

    for i in range(1, stop):
        total += i
        product *= i
    
    print(f"Sum: {total}")
    print(f"Product: {product}")
else:
    print("Invalid input.")
    

