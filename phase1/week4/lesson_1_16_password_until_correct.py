# Set the correct password
correct_password = "python123"

while True:
    # Get the user's password and check whether it's correct
    user_password = input("Please enter your password: ")
    if user_password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")
