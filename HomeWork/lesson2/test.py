user_n = int(input('Введите пожалуйста число которое хотите сложить в формате n+nn+nnn\n>>>')) # Привел к типу "число"
string_n = str(user_n) # Привел к типу "строка"
nn = string_n + string_n
nnn = string_n + string_n + string_n
summ_n = user_n + int(nn) + int(nnn)
print(summ_n)