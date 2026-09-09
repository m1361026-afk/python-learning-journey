# Store the student's profile information
student = {
    "name": "Kevin",
    "age": 24,
    "score": 88
}

# Update the score and add the student's city
student["score"] = 95
student["city"] = "Taipei"

print(f"Name: {student["name"]}")
print(f"Age: {student["age"]}")
print(f"Score: {student["score"]}")
print(f"City: {student["city"]}")
print(f"Number of fields: {len(student)}")