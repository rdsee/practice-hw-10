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

