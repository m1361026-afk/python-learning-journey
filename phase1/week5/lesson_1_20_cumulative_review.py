# Create a list
scores = []

# Collect up to five valid scores
while len(scores) < 5:
    user_input = int(input("Please enter a score: "))
    if user_input == -1:
        break
    elif (user_input < 0) or (user_input > 100):
        print("Invalid score.")
        continue
    else:
        scores.append(user_input)

# Check if the scores list is empty
if len(scores) == 0:
    print("No scores available.")
else:
    print(f"Scores: {scores}")
    print(f"Number of scores: {len(scores)}")
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    scores.sort(reverse=True)
    print(f"Sorted scores: {scores}")
