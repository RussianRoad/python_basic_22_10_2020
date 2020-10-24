"""
first_result = int(input('Введите результат 1 дня\n>>>'))
wish_result = int(input('Введите желаемый результат\n>>>'))
exp = 0.1
day_count = int((first_result * exp) + first_result)
while day_count < wish_result:
     exp += 0.1
     continue
if day_count >= wish_result:
    print('Вы достигли результата!')
"""
"""
x = int(input('Введите результат 1 дня\n>>>'))
y = int(input('Введите желаемый результат\n>>>'))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(day)
"""

x = int(input('Введите результат 1 дня\n>>>'))
y = int(input('Введите желаемый результат\n>>>'))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)