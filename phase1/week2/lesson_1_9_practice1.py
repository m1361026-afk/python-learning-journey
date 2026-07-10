# 任務 A
# Ask the user to enter their score and convert it to an integer
score = int(input("Please enter your score: "))
# Determine the grade based on the score range
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

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