"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
some_list = [9, 17, 'Dog', False, -2, 0.9, {2, 4, 5}, (1, 2, 3), ({1, 2, 3}), {'first':'HelloWorld', 'second': 123}]
def  some_type(n):
    for n in range(len(some_list)):
        print(type(some_list[n]))
    return
some_type(some_list)

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
some_list = []
n = int(input('Введите колличество элементов списка\n>>>'))
print('Введите числа')
for i in range(0, n):
    user_list = int(input())
    some_list.append(user_list)
    print(some_list)

a = -1

for i in range(len(some_list)//2):
    print("Было - ", i, some_list)
    some_list[a],some_list[i] = some_list[i], some_list[a]
    print("Стало - ", some_list)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
 (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
some_month = int(input('Пожалуйтса, введите номер месяца'))
if some_month == 1 or some_month == 2 or some_month == 12:
    print(season_list[0])
    print(season_dict.get(1))
elif some_month == 3 or some_month == 4 or some_month == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif some_month == 6 or some_month == 7 or some_month == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif some_month == 9 or some_month == 10 or some_month == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print('Нет такого месяца')

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

some_string = input(str('Введите слова через пробел\n>>>'))
some_word = []
word_number = 1
for n in range(some_string.count(' ') + 1):
    some_word = some_string.split()
    if len(some_word) > 10:
        print(f'{word_number} {some_word [n]}')
        word_number += 1
    else:
        print(f'{word_number} {some_word [n] [0:10]}')
        word_number += 1

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя 
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг равен - {my_list}')
some_number = int(input('Введите число или 0 для выхода\n>>>'))
while some_number != 0:
    for a in range(len(my_list)):
        if my_list[a] == some_number:
            my_list.insert(a + 1, some_number)
            break
        elif my_list[0] < some_number:
            my_list.insert(0, some_number)
        elif my_list[-1] > some_number:
            my_list.append(some_number)
        elif my_list[a] > some_number and my_list[a + 1] < some_number:
            my_list.insert(a +1, some_number)
    print(f'Текущий список - {my_list}')
    some_number = int(input('Введите число\n>>> '))

"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с 
параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать 
программно, т.е. запрашивать все данные у пользователя.
"""

goods = []
features = {'Название продукта': '', 'Цена продукта': '', 'Колличество': '', 'Номер': ''}
analytics = {'Название продукта': [], 'Цена продукта': [], 'Колличество': [], 'Номер': []}
num = 0
some_feature = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения ввода 'Enter', для вывода аналитики 'A'\n>>>").upper()
    if control == 'Q': #Никак не могу понять почему на Q не работает break..
        break
    num += 1
    if control == 'A':
        print(f'\n Аналитика \n{"-" * 100}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 100)
    for f in features.keys():
        some_feature = input(f'Введите "{f}"')
        features[f] = int(some_feature) if (f == 'Цена продукта' or f == 'Колличество') else some_feature
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'Название продукта': input("Название продукта"), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'Номер': input("Номер")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'Название продукта': my_dict.get('Название продукта'), 'цена': my_dict.get('цена'), 'Количество': my_dict.get('Количество'),
         'Номер': my_dict.get('Номер')})
print(my_list)
print(my_analys)

