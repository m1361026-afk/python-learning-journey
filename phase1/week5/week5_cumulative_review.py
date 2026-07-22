# Get the number of scores and initialize the accumulators
user_input = int(input("How many scores will you input: "))
total_score = 0
valid_score_count = 0

for score_number in range(1, user_input + 1):
    # Get the user's score
    user_score = int(input(f"Please enter number {score_number} score: "))

    # Reject scores outside the valid range
    if (user_score < 0) or (user_score > 100):
        print("Invalid score.")
        continue
    
    # Add the valid score to the total and update the count
    total_score += user_score
    valid_score_count += 1

if valid_score_count > 0:
    print(f"The number of valid scores: {valid_score_count}")
    print(f"The average score: {(total_score/valid_score_count):.2f}")
else:
    print("No valid scores.")