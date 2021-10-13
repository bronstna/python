user_input = input('Предложение: ')
words = user_input.split()
for num, word in enumerate (words):
    print(f'#{num} - {word[:10]}')

