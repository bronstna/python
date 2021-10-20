import sys

if len(sys.argv) < 4:
    print(f'Введите данные(выработка в часах, ставка в час, премия)!')
else:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    total = x * y + z
    print(total)
