"""
Задание №1
"""
print('Вас приветствует анонимный автомобильбный опросник!')
own_car = input('Марка вашего авто?\n>>>')
age_car = input('Год выпуска вашего авто?\n>>>')
cash_counter = input('Самая большая сумма потрачена вами на ТО автомобиля в рублях\n>>>')
age_car = int(age_car)
print('Ваш автомобиль: {0}, год выпуска {1}, самое крупное ТО {2} рублей.'.format(own_car, age_car, cash_counter))
print('Приезжайте в "Павел сервис" сделаем дешевле!')

"""
Задание №2
"""

print('Вас приветствует конвертатор секунд!')
user_seconds_request = input('Сколько секунд вы хотите перевести в формат чч:мм:сс?\n>>>')
user_seconds_request = int(user_seconds_request)
hours = user_seconds_request // 3600
minutes = (user_seconds_request // 60)%60
seconds = user_seconds_request % 60
answer = f"Конвертация {user_seconds_request} секунд, равна: {hours}:{minutes}:{seconds}"
print(answer)

"""
Задание №3
"""
user_n = int(input('Введите пожалуйста число\n>>>')) # Привел к типу "число"
string_n = str(user_n) # Привел к типу "строка"
nn = string_n + string_n
nnn = string_n + string_n + string_n
summ_n = user_n + int(nn) + int(nnn)
print(summ_n)

"""
Задание №4
"""
user_number = int(input('Введите пожалуйста целое положительно число и я найду самую большую цифру в нем\n>>>'))
max_number = 0
while user_number > 0:
    calculating = user_number % 10
    if calculating >= max_number: max_number = calculating
    user_number //= 10
print(max_number)

"""
Задание №5
"""

user_income = int(input('Введите выручку вашей фирмы за год\n>>>'))
user_cost = int(input('Введите издержки вашей фирмы за год\n>>>'))
user_profit = int(user_income - user_cost)  #Прибыль
user_margin = int(user_profit / user_income * 100)  #Рентабельность

if user_income > user_cost:
    print('Ваша фирма прибыльна, ура!')
    print('Рентабельность работы вашей фирмы: {0} процентов.'.format(user_margin))
    user_workers = int(input('Введите колличество сотрудников вашей фирмы\n>>>'))
    personel_profit = user_profit / user_workers
    print(f"Прибыль на каждого сотрудника составляет: {personel_profit} рублей.")
else:
    print('Ваша фирма убыточна, увы.')

"""
Задание № 6
"""

first_result = int(input('Введите результат 1 дня в км.\n>>>'))
wish_result = int(input('Введите желаемый результат в км.\n>>>'))
day_count = 1
while first_result < wish_result:
    first_result *= 1.1
    day_count += 1
print(f'При ежедневном увеличении нагрузки на 10%, вы достигните желаемого результа через {day_count} дней')

