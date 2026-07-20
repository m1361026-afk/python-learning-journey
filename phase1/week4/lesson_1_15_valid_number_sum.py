# Get a number from the user
user_number = int(input("Please enter a number from 1 to 20: "))

# Keep asking until the user enters a number from 1 to 20
while (user_number < 1) or (user_number > 20):
    print("Invalid input.")
    user_number = int(input("Please enter a number from 1 to 20: "))

# Calculate the sum of the numbers from 1 to the user's number
count = 1
total = 0
while count <= user_number:
    total += count
    count += 1

print(f"Total from 1 to {user_number}: {total}")
