# 任務 A：駕照資格判斷
# Ask the user to enter their age and convert it to an integer
user_age = int(input("Please enter your age: "))
# Ask whether the user passed the physical examination
physical_exam_result = input("Please enter whether you pass the physical examination (Yes/No): ")
# Check whether the user meets all requirements
if user_age >= 18 and physical_exam_result == "Yes":
    print("可以報考駕照")
else:
    print("不能報考駕照")