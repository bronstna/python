rating_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

rating = int(input("Введите рейтинг: "))
inserted = False
for index, elem in enumerate(rating_list):
    if rating > elem:
        rating_list.insert(index, rating)
        insert = True
        break

if not inserted:
    rating_list.append(rating)

print(rating_list)
