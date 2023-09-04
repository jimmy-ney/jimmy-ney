# Task_1

user_msg = input("Введите строку: ")
letters = list(user_msg)
what_replace = ":"
for_what_replace = ";"
index = 0
replace_count = 0
for letter in letters:
    if letter == what_replace:
        letters[index] = for_what_replace
        replace_count += 1
    index += 1

print("Исправленная строка:", end=' ')
for letter in letters:
    print(letter, end='')

print("Кол-во замен:", replace_count)

# Task_2

msg = input("Введите строку: ")
index_of_letter = int(input("Номер символа: ")) - 1  # сразу отнимаем 1, чтобы превратить номер в индекс
letters = list(msg)
count = 0
if index_of_letter > 0:
    print("Символ слева:", letters[index_of_letter - 1])
    if letters[index_of_letter - 1] == letters[index_of_letter]:
        count += 1
if index_of_letter < len(letters) - 1:
    print("Символ справа:", letters[index_of_letter + 1])
    if letters[index_of_letter + 1] == letters[index_of_letter]:
        count += 1

if count == 0:
    print("Таких же символов нет.")
elif count == 1:
    print("Есть ровно один такой же символ.")
elif count == 2:
    print("Таких символов два.")

# Task_3

words_list = []
counts = [0, 0, 0]

for i in range(3):
    print("Введите", i + 1, "слово", end=' ')
    word = input()
    words_list.append(word)

text = input("Слово из текста: ")
while text != "end":
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input("Слово из текста: ")

print("Подсчёт слов в тексте")
for i in range(3):
    print(words_list[i], ':', counts[i])