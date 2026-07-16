# Calculate the sum of all odd numbers from 1 to 99
odd_total = 0
# Track the total number of loop iterations
count = 0

for i in range(1, 100, 2):
    odd_total += i
    count += 1

print(f"The total is {odd_total}. The loop ran {count} iterations.")