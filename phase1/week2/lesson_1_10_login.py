# 任務 B：系統登入判斷
# Set the correct user's name and password
correct_name = "liao@1115"
correct_password = "901115"
# Ask the user to enter the name and password
user_name = input("Please enter your name: ")
user_password = input("Please enter your password: ")
# Set is_blocked = False
is_blocked = False
# Check whether the user can login
if (
    user_name == correct_name 
    and user_password == correct_password
    and not is_blocked
):
    print("登入成功")
else:
    print("登入失敗")