# Store the student's profile information
student = {
    "name": "Kevin",
    "score": 95,
    "city": "Taipei"
}

if "score" in student:
    print(f"Score: {student["score"]}")
if "city" in student:
    print(f"City: {student["city"]}")
else:
    print("City information is not available.")