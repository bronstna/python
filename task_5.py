print ("Ведите выручку")
x = int (input())
print ("Введите издержки")
y = int (input())
if x>y:
    print ("Ваша прибыль", x-y)
else:
    print ("Ваш убыток", y-x)

print ('Введите количество сотрудников')
z = int (input())
print ("прибыль фирмы в расчете на одного сотрудника", int((x-y)/z))
