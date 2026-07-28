# Build and display a score list
scores = [80, 90, 75]
print(f"Before: {scores}")

# Validate the score before adding it to the list
user_input = int(input("Please enter your score: "))
if 0 <= user_input <= 100:
    scores.append(user_input)
    print(f"After: {scores}")
else:
    print("Invalid score.")