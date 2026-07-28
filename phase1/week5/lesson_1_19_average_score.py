# Build a score list
scores = [80, 90, 75, 85]

# Calculate and display the average score
if len(scores) > 0:
    average_score = sum(scores) / len(scores)
    print(f"Scores: {scores}")
    print(f"Average score: {average_score:.2f}")
else:
    print("No scores available.")