def int_new (txt):
    word = txt[0].upper() + txt[1:].lower()
    return word

string = input("Введите слова, разделяя их пробелами: ")
for word in string.split(' '):
    print(f'{int_new(word)}', end=' ')