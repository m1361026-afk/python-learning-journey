# 任務 B
# Ask the user to enter their BMI and convert it to a floating-point number
bmi = float(input("Please enter your BMI: "))
# Determine the BMI category based on the entered value
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("正常範圍")
elif bmi < 27:
    print("體重過重")
else:
    print("肥胖")