# 任務 D
# Ask the user to enter their age and convert it to an integer
user_age = int(input("Please enter your age: "))
# Determine the ticket price based on the user's age
if user_age < 6:
    print("未滿 6 歲：免費")
elif user_age < 12:
    print("6～11 歲：兒童票 200 元")
elif user_age < 65:
    print("12～64 歲：一般票 300 元")
else:
    print("65 歲以上：敬老票 250 元")