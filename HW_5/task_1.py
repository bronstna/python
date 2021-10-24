with open('test.txt', 'w') as file:
    input_line = input('Текст :\n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Текст :\n')