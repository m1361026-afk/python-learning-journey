# Read the starting number for the countdown
user_number = int(input("Please enter a number: "))

# Validate the number before starting the countdown
if 3 <= user_number <= 20:
    # Count down from the user's number to 1
    for i in range(user_number, 0, -1):
        print(i)
        
    print("Go!")
else:
    print("Invalid input.")