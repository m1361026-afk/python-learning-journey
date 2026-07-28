# Build a score list
scores = [78, 92, 85, 100, 67]

if len(scores) > 0:
    print(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
else:
    print("No scores available.")