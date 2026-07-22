# Create a score list
scores = [70, 85, 90]
print(f"Before: {scores}")

# Get the score position and its new value
score_position = int(input("Please enter the score you want to correct (1-3): "))
new_score = int(input("Please enter the new score (0-100): "))
if (score_position < 1) or (score_position > 3) or (new_score < 0) or (new_score > 100):
    print("Invalid input.")
else:
    scores[score_position - 1] = new_score
    print(f"After: {scores}")