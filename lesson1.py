"""
!PEP-8!
переменная snake_case
CamelCase
Kebab-case

!Pep-272!
"""


#first_variable_string = "HELLO GB"  # строки str неизменяемые
#first_variable_string2 = 'Hello \'GB'

#print(first_variable_string)
#print(first_variable_string2)

"""
Арифметические операторы
+
-
*
/
// - целочисленное деление(деление на целое число без остатка)
% остаток целочисленного деления(с остатком)
** - оператор возведения в степень

+=
-=

"""

# числа и числовые типы

#variable_int = 12  # int целое число
#variable_float = 12.122  # float дробное число
"""
a = '222'
type(a)
<class 'str'>
int(a)
222
type(a)
<class 'str'>
b = int(a)
type(b)

"""

#user_name = input('ваше имя\n>>>')
#age = input('Ваш возраст\n>>>')
#age = int(age)
print('Привет {0} твой возраст {1}'.format(user_name, age))  # метод формат МАССИВ
#user_hello_string = f"Привет {user_name} твой возраст {age}"
#print(user_hello_string)

#variable_bool = False  # bool булевый - только 2 значения
#variable_bool2 = True

"""
Операторы сравнения и логические операторы
>
<
>=
<=
!=
==

and
or
not
"""

if age > 18:  #оператор если который вернет правду или ложь
   print('Доступ разрешен к разделу ХХХ');
elif age > 16:  # сокращение от else if
    print('Доступ к боевикам');
#elif age > 8:
   # print('Доступ к мультикам');
#else:
   # print('Доступ запрещен');


"""
Циклы
"""
idx = 0
while idx < 10:  # while пока это утверждение истина будет выполняться следующий блок кода
    if idx % 2:
        idx += 3
        continue
    print(idx)
    idx += 1
    #if idx == 6:
       #break
    #idx = idx +1;
else:
    print('Else Cycle')

"""
nan - not a number
inf - infinity

1234 - вернуть последнее число - 1234 % 10 = 4 , 100 1000 и т.д.

оператор "not" True = False
'e' in 'hello'
not 'e' in 'hello'
"""

