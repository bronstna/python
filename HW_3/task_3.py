def new_f (num_1, num_2, num_3):
    sum_nums = num_1 + num_2 + num_3
    return sum_nums - min((num_1, num_2, num_3))

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
a = new_f(x, y, z)

print(a)