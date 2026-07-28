# Build and display a score list
scores = [80, 90, 75]
print(f"Before: {scores}")

user_input = int(input("Please enter a score: "))
if 0 <= user_input <= 100:
    scores.append(user_input)
    print(f"After: {scores}")
else:
    print("Invalid score.")

print(f"Number of scores: {len(scores)}")