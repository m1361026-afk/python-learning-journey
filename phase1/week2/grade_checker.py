# Ask the user to enter their score and convert it to an integer
user_score = int(input("Please enter your score: "))
# Validate the score and determine the corresponding grade
if user_score < 0 or user_score > 100:
    print("分數輸入錯誤")
elif user_score >= 90:
    print("A")
elif user_score >= 80:
    print("B")
elif user_score >= 70:
    print("C")
elif user_score >= 60:
    print("D")
else:
    print("F")