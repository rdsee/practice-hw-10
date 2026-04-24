# #Modules
# import random
# # from random import *
# # from random import randint, choice
#
# print(random.randint(1,100)) #random numbers
#
# print(random.choice("qwerty")) # random symbols
#
# print(random.randrange(10)) #random nums in range
# print(random.randrange(1, 30))
# print(random.randrange(1, 30, 2))
#
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)# random position in list
# print(nums)

# import math
#
# print(-math.inf) # -infinity
# print(math.inf) # +infinity
# print(math.ceil(10.2)) #огругление в большую сторону
# print(math.floor(10.999)) #огругление в меньшую сторону
# print(math.factorial(10)) #функция факториала
# print(math.pow(2 , 4)) #перевод в степень
# print(math.sqrt(9)) #квадратный корень

# from decimal import *
# number = 0.1 + 0.1 + 0.1
# print(number)
#
# number = Decimal('0.1') #Необходимо для вычисления округленного дробного числа.
# number = number + number + number
# print(number)
#
# number = Decimal('0.333')
# print(number)
# number = number.quantize(Decimal('1.00')) #Приводит число к нужному дробному окончанию после запятой.
# print(number)
#
# number = Decimal('0.32345234234')
# print(number)
# number = number.quantize(Decimal('1.0000'))
# print(number)

# import datetime as dt
#
# print(dt.date.today())
# print(dt.date(2022, 11, 12))
# print(dt.time())
# print(dt.time(10, 12, 10))
# print(dt.time(11, 12))
#
# print(dt.datetime.now()) #date + hours
# dt_now = dt.datetime.now()
# print(dt.datetime) #prints class
#
# my_date = dt.datetime.strptime('12/02/2000', '%d/%m/%Y') #Возмонжность вывода даты в подобном формате
# print(my_date)

# from datetime import datetime, timezone, timedelta
#
# #naive
# naive = datetime.now()
# print("Naive time: ", naive)
#
# #UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC time: ", UTC)
#
# #Creating a datetime with JST (Japan) Timezone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("JST time: ", jst_dateTime)

#Генераторы коллекций
# v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
#
# # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)

#Dictionary comprehensive
# my_dict_formated = {i: i * 2 for i in range(10) if i > 2}
# print(my_dict_formated)

#Generator function
# generator = (i for i in range(5))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

#for i in generator:
    #print(i)

# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
# my_gen = create_generator()
# print(my_gen)
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             my_gen.close()
# except Exception as e:
#     print(e)

############
#Регулярные выражения
# \d - соответствует любой одной цифре и заменяет собой выражение от 0 до 9
# \D - исключает все цифры и заменяет [^0-9];
# \w - заменяет любую цифру, букву, а также знак нижнего
# \W - любой символ кроме латиницы, цифр или нижнего под
# \s - соответствует любому пробельному символу;
# \S - описывает любой непробельный символ.
#
#
# . Один символ, кроме новой строки \n.
# ? 0 или 1 вхождение шаблона слева
# + 1 и более вхождений шаблона слева
# * 0 и более вхождений шаблона слева
# \w Любая цифра или буква (\W - всё, кроме цифр или букв)
# \d Любая цифра [0-9] (\D - всё, кроме цифр)
# \s Любой символ пробела (\S - любой непробельный символ)
# \b Граница слова
# [..] Один из символов в скобках ([^..] - любой символ, кроме)
# \ Экранирование специальных символов (\. означает точку или \)
# ^ и $ Начало и конец строки соответственно
# {n,m} От n до m вхождений ({,m} до m вхождений)


import re

string = "It is a long established fact that a reader"
string_mixed = "Hello123 World456 test789"
string_email = "Contact us at hello@gmail.com or support@yahoo.com"
string_phone = "Call us: +1(234)567-89-00 or 8-800-555-35-35"
string_multiline = "First line\nSecond line\nThird line"

# ============ ОСНОВНЫЕ ПРИМЕРЫ ============

# \w* — 0 и более букв/цифр (включает пустые строки)
result = re.findall(r'\w*', string)
print(result)

# \w+ — 1 и более букв/цифр (только слова, без пустых строк)
result = re.findall(r'\w+', string)
print(result)

# \w+$ — 1 и более букв/цифр в конце строки
result = re.findall(r'\w+$', string)
print(result)

# ^\w+ — 1 и более букв/цифр в начале строки
result = re.findall(r'^\w+', string)
print(result)

# \w\w — ровно 2 буквы/цифры подряд
result = re.findall(r'\w\w', string)
print(result)

# \w{4} — ровно 4 буквы/цифры подряд
result = re.findall(r'\w{4}', string)
print(result)

# \w{3,5} — от 3 до 5 букв/цифр подряд
result = re.findall(r'\w{3,5}', string)
print(result)

# \s — любой пробельный символ
result = re.findall(r'\s', string)
print(result)

# \S — любой непробельный символ
result = re.findall(r'\S', string)
print(result)

# \b\w{4}\b — слова ровно из 4 букв (граница слова)
result = re.findall(r'\b\w{4}\b', string)
print(result)

# [aeiou] — любая гласная буква
result = re.findall(r'[aeiou]', string)
print(result)

# [^aeiou\s] — любой символ кроме гласных и пробелов
result = re.findall(r'[^aeiou\s]', string)
print(result)

# \w+\s\w+ — два слова подряд через пробел
result = re.findall(r'\w+\s\w+', string)
print(result)

# [A-Z]\w* — слова начинающиеся с заглавной буквы
result = re.findall(r'[A-Z]\w*', string)
print(result)

# \w+ed — слова заканчивающиеся на "ed"
result = re.findall(r'\w+ed', string)
print(result)

# t\w* — слова начинающиеся на букву "t"
result = re.findall(r't\w*', string)
print(result)

# . — любой символ кроме новой строки
result = re.findall(r'.', string)
print(result)

# .{3} — любые 3 символа подряд кроме новой строки
result = re.findall(r'.{3}', string)
print(result)


# ============ ЦИФРЫ ============

# \d — любая цифра
result = re.findall(r'\d', string_mixed)
print(result)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# \d+ — последовательность цифр подряд
result = re.findall(r'\d+', string_mixed)
print(result)  # ['123', '456', '789']

# \D — любой символ кроме цифры
result = re.findall(r'\D+', string_mixed)
print(result)  # ['Hello', ' World', ' test']

# [0-9]{3} — ровно 3 цифры подряд
result = re.findall(r'[0-9]{3}', string_mixed)
print(result)  # ['123', '456', '789']

# \w+\d+ — слово содержащее цифры в конце
result = re.findall(r'[A-Za-z]+\d+', string_mixed)
print(result)  # ['Hello123', 'World456', 'test789']


# ============ ТЕЛЕФОН ============

# \d+ — все группы цифр из номера телефона
result = re.findall(r'\d+', string_phone)
print(result)  # ['1', '234', '567', '89', '00', '8', '800', '555', '35', '35']

# \+\d\(\d{3}\)\d{3}-\d{2}-\d{2} — номер формата +1(234)567-89-00
result = re.findall(r'\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}', string_phone)
print(result)  # ['+1(234)567-89-00']

# \d-\d{3}-\d{3}-\d{2}-\d{2} — номер формата 8-800-555-35-35
result = re.findall(r'\d-\d{3}-\d{3}-\d{2}-\d{2}', string_phone)
print(result)  # ['8-800-555-35-35']


# ============ EMAIL ============

# \S+@\S+ — любой email (всё что есть до и после @)
result = re.findall(r'\S+@\S+', string_email)
print(result)  # ['hello@gmail.com', 'support@yahoo.com']

# \w+@\w+\.\w+ — email в формате имя@домен.зона
result = re.findall(r'\w+@\w+\.\w+', string_email)
print(result)  # ['hello@gmail.com', 'support@yahoo.com']

# \w+ — только имена до @ (логины)
result = re.findall(r'\w+(?=@)', string_email)
print(result)  # ['hello', 'support']

# (?<=@)\w+ — только домены после @
result = re.findall(r'(?<=@)\w+', string_email)
print(result)  # ['gmail', 'yahoo']


# ============ МНОГОСТРОЧНЫЙ ТЕКСТ ============

# ^ и $ с флагом re.MULTILINE — начало и конец каждой строки
result = re.findall(r'^\w+', string_multiline, re.MULTILINE)
print(result)  # ['First', 'Second', 'Third']

result = re.findall(r'\w+$', string_multiline, re.MULTILINE)
print(result)  # ['line', 'line', 'line']

