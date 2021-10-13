user_input = input ('list: ')
input_list = user_input.split()
len_list = len(input_list)
x = 0

if len_list > 1:
    while x < len_list - 1:
        input_list[x], input_list[x+1] =input_list [x+1], input_list[x]
        x +=2


print(input_list)