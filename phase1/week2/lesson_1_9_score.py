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