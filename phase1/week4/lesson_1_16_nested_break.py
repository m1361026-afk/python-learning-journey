# Process each row with the outer loop
for row in range(1, 4):
    # Process each column in the current row
    for column in range(1, 5):
        if column == 3:
            break
        print(f"Row {row}, Column {column}")