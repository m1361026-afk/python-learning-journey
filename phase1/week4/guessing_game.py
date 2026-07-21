# Import the random module to generate a random number
import random

# Get a random number from 1 to 100
secret_number = random.randint(1, 100)

# Count the user's valid guesses
guess_count = 0

# Keep asking until the user guesses the secret number
while True:
    user_guess = int(input("Please guess a number from 1 to 100: "))
    # Reject guesses outside the valid range
    if (user_guess < 1) or (user_guess > 100):
        print("Invalid input.")
        continue

    guess_count += 1
    if (user_guess < secret_number):
        print("Too low.")
    elif (user_guess > secret_number):
        print("Too high.")
    else:
        print("Correct!")
        break

print(f"You guessed {guess_count} times.")



