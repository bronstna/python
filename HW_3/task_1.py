def div_n(x, y):
    if y == 0:
        return "Нельзя поделить на 0"
    else:
        return x / y

x = float(input("x: "))
y = float(input("y: "))
print(div_n(x, y))

