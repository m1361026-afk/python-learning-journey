# The outer loop selects the first number in each multiplication group
for first_number in range(1, 10):
    # The inner loop multiplies the first number by each number from 1 to 9
    for second_number in range(1, 10):
        product = first_number * second_number
        print(f"{first_number} * {second_number} = {product}")

    # Separate each multiplication group with a blank line
    print()