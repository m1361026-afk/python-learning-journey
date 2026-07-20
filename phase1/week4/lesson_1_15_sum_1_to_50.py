# Start the accumulator at zero because no numbers have been added yet
count = 1
total = 0
while count <= 50:
    total += count
    count += 1
print(f"Total: {total}")