# Print the numbers from 1 before meeting 4 
print("Break result: ")
for num in range(1, 8):
    if num == 4:
        break
    print(num)
# Skip 4 while printing the numbers from 1 to 7
print("Continue result: ")
for num in range(1, 8):
    if num == 4:
        continue
    print(num)