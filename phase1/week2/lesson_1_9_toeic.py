# 任務 C
# Ask the user to enter their TOEIC score and convert it to an integer
user_score = int(input("Please enter your TOEIC score: "))
# Determine the TOEIC level based on the entered score
if user_score >= 905:
    print("Level A")
elif user_score >= 785:
    print("Level B")
elif user_score >= 550:
    print("Level C")
elif user_score >= 225:
    print("Level D")
else:
    print("Level E")