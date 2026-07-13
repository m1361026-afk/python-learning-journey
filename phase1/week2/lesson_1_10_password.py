# 任務 D：密碼格式檢查
# Ask the user to enter a password
user_password = input("please enter a password: ")
# Check whether the password conform to the rules
if len(user_password) >= 8 and "@" in user_password:
    print("密碼符合規定")
else:
    print("密碼不合規定")