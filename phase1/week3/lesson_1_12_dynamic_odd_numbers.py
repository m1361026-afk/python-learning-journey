# Read the maximum number from the user
max_number = int(input("Please enter a maximum number: "))

if 1 <= max_number <= 100:
    # Make sure the max_number can be included
    stop = max_number + 1
    # Print all odd numbers from 1 to the maximum number
    for i in range(1, stop, 2):
        print(i)
else:
    print("Invalid input.")