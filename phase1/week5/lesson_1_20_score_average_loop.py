# Build a score list
scores = [80, 90, 75, 60, 45]
total_score = 0

# Accumulate the total score
for score in scores:
    print(f"Score: {score}")
    total_score += score

# Calculate the average score
average_score = total_score / len(scores)
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
