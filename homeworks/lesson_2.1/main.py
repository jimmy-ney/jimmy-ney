#Task_1

numbers = [3, 7, 5]

while True:

    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)

    for _ in numbers:
        print(_ ** 2, _ ** 3, _ ** 4)
print()

#Task_2

numbers = []
for _ in range(0, 100):
    numbers.append(_)
print(numbers)

#Task_3

id_list = []
list_range = int(input('Кол-во сотрудников в офисе: '))
id_check = 0
id_answ = 0

for _ in range(1, list_range + 1):
    id_list.append(int(input('ID сотрудника: ')))

id_check = int(input('Какой ID ищем? '))

for id in id_list:
    if id == id_check:
        id_answ = 1

if id_answ == 1:
    print('Сотрудник работает!')
else:
    print('Сотрудник не работает!')