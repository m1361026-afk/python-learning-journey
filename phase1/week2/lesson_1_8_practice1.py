# 任務 A
# Ask the user to enter an integer
num = int(input("Please enter an integer: "))
# Check whether the number can be divided by 2
if num % 2 == 0:
    print("偶數")
else:
    print("奇數")

# 任務 B
# Set the correct password
correct_password = "abc@123"
# Ask the user to enter the password
user_password = input("Please enter the password: ")
# Check whether the user's password is equal to the correct password
if user_password == correct_password:
    print("登入成功")
else:
    print("登入失敗")

# 任務 C
# Ask the user to enter the amount
amount = int(input("Please enter your amount: "))
# Check whether the amount is greater than or equal to the threshold 1000
if amount >= 1000:
    print("符合免運資格")
else:
    print("需要支付運費")