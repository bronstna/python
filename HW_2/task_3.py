n_month = input('Введите номер месяца: ')
x, y, w, z = 'зима','весна','лето','осень'
month_dict = {'1':x, '2':x, '3':y, '4':y, '5':y, '6':w, '7':w, '8':w, '9':z, '10':z, '11':z,  '12':x}
print(month_dict[n_month])
season_list = [x, x, y, y, y, w, w, w, z, z, z, x]
print (season_list[int(n_month) - 1])
