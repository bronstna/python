def total (nums_str, stop):
    numbers_list = nums_str.split (' ')
    total_list = 0
    for i in numbers_list:
        if i == stop:
            break
        total_list += int(i)
    return total_list

stop = '!'
finished = False
s = 0
while not finished:
    nums_str_user = input("Введите числа, разделяя их пробелом: ")
    s += total(nums_str_user, stop)
    finished = stop in nums_str_user
    print(f'Сумма = {s}')

