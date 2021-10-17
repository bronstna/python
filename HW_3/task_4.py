def new_f (x, y):
    if x < 0:
        return "x должен быть больше 0"
    if y > 0:
        return "y должен быть больше 0"
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z

x = float(input("Пожалуйста, введите положительное число X: "))
y = int(input("Пожалуйста, введите отрицательное число Y: "))
print(new_f(x, y))