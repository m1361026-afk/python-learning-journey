# Build a score list
scores = [80, 59, 60, 45, 100, 0, 75]
passing_count = 0
failing_count = 0

# Classify each score as passing or failing
for score in scores:
    if score < 60:
        print(f"Failing score: {score}")
        failing_count += 1
    else:
        passing_count += 1

print(f"Passing count: {passing_count}")
print(f"Failing count: {failing_count}")
