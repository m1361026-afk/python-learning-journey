# Build a score list
scores = [0, 40, 59, 60, 70, 70, 85, 100]

# Check if the list is empty
if len(scores) > 0:
    print(f"Scores: {scores}")
    print(f"Number of scores: {len(scores)}")
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")

    # Classify scores using the passing threshold
    passing_count = 0
    failing_count = 0
    failing_scores = []
    for score in scores:
        if score < 60:
            failing_count += 1
            failing_scores.append(score)
        else:
            passing_count += 1

    print(f"Failing score: {failing_scores}")
    print(f"Passing count: {passing_count}")
    print(f"Failing count: {failing_count}")
else:
    print("No scores available.")
