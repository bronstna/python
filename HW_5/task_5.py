import random

with open('test_n.txt', 'w') as file:
    for _ in range(10):
        file.write(f'{random.randint(0, 10)} ')

with open('test_n.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)
print(sum)