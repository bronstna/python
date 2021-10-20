def gen_factorial(number):
    cur = 1
    for i in range(1, number + 1):
        cur *= i
        yield cur

n = 8
for ind, el in enumerate(gen_factorial(n)):
    print(f'#{ind + 1} {el}')