# Calculate the sum from 1 to the number entered by the user
user_number = int(input("Please enter a number: "))

# Validate the number before starting the calculation
if 1 <= user_number <= 1000:
    total = 0
    stop = user_number + 1
    for i in range(1, stop):
        total += i

    print(total)
else:
    print("Invalid input.")