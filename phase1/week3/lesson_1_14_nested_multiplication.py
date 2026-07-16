# The outer loop selects the first number
for first_number in range(1, 4):
    # The inner loop multiplies it by each number from 1 to 3
    for second_number in range(1, 4):
        multiplier = first_number * second_number
        print(f"{first_number} * {second_number} = {multiplier}")