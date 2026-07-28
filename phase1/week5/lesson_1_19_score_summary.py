# Build a score list
scores = [88, 60, 75, 100, 59]
print(f"Before: {scores}")

user_input = int(input("Please enter a score between 0 and 100: "))
if 0 <= user_input <= 100:
    scores.append(user_input)
    print(f"Number of scores: {len(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    scores.sort(reverse=True)
    print(f"After: {scores}")
else:
    print("Invalid score.")
    print(f"After: {scores}")