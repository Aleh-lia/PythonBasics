print('Задание 1')
# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для
# проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен
# список?

duration = int(input('Введите любое число: '))
if duration < 60 :
    print(duration, 'сек')
elif 60 <= duration < 3600:
    number_minutes = duration // 60
    number_seconds = duration - number_minutes * 60
    print(number_minutes, 'мин', number_seconds , 'сек')
elif 3600 <= duration < 86400:
    number_hour = duration // 3600
    number_hour_minutes = duration - number_hour * 3600
    number_minutes = number_hour_minutes // 60
    number_seconds = duration - (number_hour * 3600 + number_minutes * 60)
    print(number_hour, 'час', number_minutes, 'мин', number_seconds , 'сек')
elif 86400 <= duration:
    number_day = duration // 86400
    number_day_hour = duration - number_day * 86400
    number_hour = number_day_hour // 3600
    number_day_minutes = duration - (number_day * 86400 + number_hour * 3600)
    number_minutes = number_day_minutes // 60
    number_seconds = duration - (number_day * 86400 + number_hour * 3600 + number_minutes * 60)
    print(number_day , 'дн', number_hour, 'час', number_minutes, 'мин', number_seconds , 'сек')

print('///////////////////////////////////////////////////////////////////////////////////////////')

print('Задание 2')
# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.



my_list = []
for i in range(1, 1001, 2):
    if i % 2 != 0:
        number = i ** 3
        check_sum = 0
        while(number != 0):
            check_sum = check_sum + number % 10
            number = number // 10
        if (check_sum % 7 == 0):
            my_list.append(i)
    i += 1
print(' a)', sum(my_list))

my_list_17 = []
for i in my_list:
    number = i + 17
    check_sum = 0
    while number != 0:
        check_sum = check_sum + number % 10
        number = number // 10
    if check_sum % 7 == 0:
        my_list_17.append(i)
    i += 1

print(' b)', sum(my_list_17))


print('///////////////////////////////////////////////////////////////////////////////////////////')

print('Задание 3')

# 3. Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

# //////////////////////////////////////

# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
# Пробуйте их решать, если уверены в своих силах.


for percent in range(1, 101):
    if 4 < percent % 100 <= 20:
        word = 'процентов'
    elif 1 < percent % 10 < 5:
        word = 'процента'
    elif percent % 10 == 1:
        word = 'процент'
    else:
        word = 'процентов'
    print(percent, word)
