#Task_1

nums_list = []
N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)

#Task_2

nums_list = []
summ = 0

N = int(input('Кол-во чисел в списке: '))

# Заполнение списка
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

K = int(input('Введите кратное: '))

for i in nums_list:
    if i % K == 0:
        summ += i

print('Сумма индексов кратных', K, ':', summ)

#Task_3

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')