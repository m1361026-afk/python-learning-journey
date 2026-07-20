# Keep asking until the user enters a valid number
while True:
    user_number = int(input("Please enter a number from 1 to 100: "))
    if 1 <= user_number <= 100:
        print(f"Valid number: {user_number}")
        break
    print("Invalid input.")