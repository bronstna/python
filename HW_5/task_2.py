with open('test.txt') as file:
    file_lines = file.readlines()
    str_am = 0
    for num, line in enumerate(file_lines):
        str_am += 1
        words_am = len(line.split())
        print(f'#{num + 1} - {words_am} words')
    print(f'{str_am} strokes')