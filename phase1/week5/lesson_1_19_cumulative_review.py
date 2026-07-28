# Set the correct password and attempt counter
correct_password = "python123"
remaining_attempts = 3

# Allow up to three password attempts
while remaining_attempts > 0:
    user_input = input("Please enter your password: ")
    if user_input == correct_password:
        print("Login successful.")
        break

    remaining_attempts -= 1
    if remaining_attempts > 1:
        print(f"Incorrect password. {remaining_attempts} attempts remaining.")
    elif remaining_attempts == 1:
        print(f"Incorrect password. {remaining_attempts} attempt remaining.")
    else:
        print("Login failed.")

