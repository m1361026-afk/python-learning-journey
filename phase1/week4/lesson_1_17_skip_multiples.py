# Skip multiples of 3 while processing the numbers from 1 to 20
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num)