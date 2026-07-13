# 任務 A：駕照資格判斷
# Ask the user to enter their age and convert it to an integer
user_age = int(input("Please enter your age: "))
# Ask the user to enter whether they pass the physical examination
user_phy = input("Please enter whether you pass the physical examination (Yes/No): ")
# Check whther the user conform to the rule
if user_age >= 18 and user_phy == "Yes":
    print("可以報考駕照")
else:
    print("不能報考駕照")