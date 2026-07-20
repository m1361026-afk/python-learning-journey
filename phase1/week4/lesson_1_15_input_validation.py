# Get the user's input number
user_number = int(input("Please enter a number from 1 to 10: "))
# Check whether the input is a valid number
while (user_number < 1) or (user_number > 10):
    print("Invalid input.")
    user_number = int(input("Please enter a number from 1 to 10: "))
    
print(f"Valid number: {user_number}")
  
        

