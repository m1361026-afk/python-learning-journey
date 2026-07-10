# Set the correct password
correct_password = "123@abc"
# Ask the user to enter the password
user_password = str(input("Please enter your password: "))
# Check whether the entered password matches the correct password
if user_password == correct_password:
    print("密碼正確")

print("密碼檢查完成")