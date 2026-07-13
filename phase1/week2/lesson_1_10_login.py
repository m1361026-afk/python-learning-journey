# 任務 B：系統登入判斷
# Set the correct username and password
correct_username = "liao@1115"
correct_password = "901115"
# Ask the user to enter their username and password
user_name = input("Please enter your name: ")
user_password = input("Please enter your password: ")
# Set the account's blocked status
is_blocked = False
# Check whether the credentials are correct and the account is not blocked
if (
    user_name == correct_username 
    and user_password == correct_password
    and not is_blocked
):
    print("登入成功")
else:
    print("登入失敗")