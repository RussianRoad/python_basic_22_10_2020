first_result = int(input('Введите результат 1 дня\n>>>'))
wish_result = int(input('Введите желаемый результат\n>>>'))
exp = 0.1
day_count = int((first_result * exp) + first_result)
while day_count < wish_result:
     exp += 0.1
     continue
if day_count >= wish_result:
    print('Вы достигли результата!')

