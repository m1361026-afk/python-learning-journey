# Print a 3-by-5 rectangle of stars
for row in range(3):
    for column in range(5):
        # Print five stars on the same line
        print("*", end="")

    # Move to the next line after completing one row
    print()