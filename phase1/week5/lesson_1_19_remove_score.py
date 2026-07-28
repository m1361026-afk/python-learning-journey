# Build and display a score list
scores = [80, 90, 75, 90]
print(f"Before: {scores}")

# Check whether the score the user wants to delete exists in the list
user_input = int(input("Please enter the score you want to delete: "))
if user_input in scores:
    scores.remove(user_input)
    print(f"After: {scores}")
else:
    print("Score not found.")