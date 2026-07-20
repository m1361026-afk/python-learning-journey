# Skip 5 while printing the numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)