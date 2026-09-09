# Store the correct student's profile information
correct_student = {
    "name": "Kevin",
    "score": 88
}

correct_student["score"] = 95
print("Correct student:")
for key, value in correct_student.items():
    print(f"{key}: {value}")
print(f"Number of fields: {len(correct_student)}")

# Store the wrong student's profile information
wrong_student = {
    "name": "Kevin",
    "score": 88
}

wrong_student["Score"] = 95
print("Wrong student:")

if "score" in wrong_student:
    print(f"score: {wrong_student["score"]}")
else:
    print("score information is not available.")

if "Score" in wrong_student:
    print(f"Score: {wrong_student["Score"]}")
else:
    print("Score information is not available.")

print(f"Number of fields: {len(wrong_student)}")

