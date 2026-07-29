# Build a score list
scores = [40, 55, 60, 70, 85, 100]

# Check if the list is empty
if len(scores) > 0:
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score:.2f}")
    above_average_count = 0

    # Check each score against independent criteria
    for score in scores:
        if score < 60:
            print(f"Failing score: {score}")

        if score > average_score:
            print(f"Above-average score: {score}")
            above_average_count += 1

    print(f"Above-average count: {above_average_count}")

else:
    print("No scores available.")