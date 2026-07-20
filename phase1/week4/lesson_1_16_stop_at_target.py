# Get the user's input to set the target number
target_number = int(input("Please enter a number from 1 to 10: "))

# Run the loop only when the target is within the valid range
if 1 <= target_number <= 10:
    current_num = 1
    while True:
        print(current_num)
        if current_num == target_number:
            break

        current_num += 1
    print("Target reached.")
else:
    print("Invalid input.")

    