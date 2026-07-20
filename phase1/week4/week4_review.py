# Get the number of rows and columns
rows = int(input("Please enter the amount of rows: "))
columns = int(input("Please enter the amount of columns: "))

# Check whether both inputs are within the valid range
if (1 <= rows <= 5) and (1 <= columns <= 5):
    total_positions = 0
    # The outer loop processes each row
    for row in range(1, rows + 1):
        # The inner loop processes each column in the current row
        for column in range(1, columns + 1):
            print(f"Row {row}, Column {column}")
            total_positions += 1
    print(f"Total positions: {total_positions}")
else:
    print("Invalid input.")