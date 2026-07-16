# Calculate the sum of all multiples of 3 up to the entered limit
user_input = int(input("Please enter a number between 1 and 100: "))

if 1 <= user_input <= 100:
    total = 0
    stop = user_input + 1

    for i in range(3, stop, 3):
        total += i

    print(f"Sum: {total}")
else:
    print("Invalid input.")