students = [
    {"name": "Amy", "score": 85},
    {"name": "Ben", "score": 59},
    {"name": "Cara", "score": 100},
    {"name": "David", "score": 60}
]

def check_pass(score):
    if score >= 60:
        return "Pass"
    return "Fail"

def calculate_average(students):
    total_score = 0
    for student in students:
        total_score += student["score"]
    return total_score / len(students)

def get_failing_students(students):
    failing_students = []
    for student in students:
        if check_pass(student["score"]) == "Fail":
            failing_students.append(student["name"])
    return failing_students

average_score = calculate_average(students)
failing_students = get_failing_students(students)

for student in students:
    print(f"{student["name"]}: {check_pass(student["score"])}")

print(f"Average score: {average_score:.2f}")
print(f"Failing students: {failing_students}")

print(check_pass(59))
print(check_pass(60))
print(check_pass(100))