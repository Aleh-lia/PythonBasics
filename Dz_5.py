
print('Задание 1')
"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1>
>> next(odd_to_15)
3.
..
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""


def odd_gen(n):
    for i in range(1, n + 1, 2):
        yield i


print(*odd_gen(11))
n = int(input('Введите любое число : '))
print(type(odd_gen(n)))
print(*odd_gen(n))


print(f"{'':-^90}")
print('Задание 2')

"""
2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
"""

nums = int(input('Введите любое число : '))
odd_num_no_yield = (i for i in range(1, nums + 1, 2))

print(type(odd_num_no_yield))
print(*odd_num_no_yield)


print(f"{'':-^90}")
print('Задание 3')

"""
3. Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:

('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:

('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""



tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Елена', 'Елена', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():

    len_klasses = len(klasses)


    return \
        ((tutors, klasses[i]) if i < len_klasses else (tutors, None)
        for i, tutors in enumerate(tutors))


print(type(my_gen()))
print(*my_gen())

print(f"{'':-^90}")
print('Задание 4')
"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
сделать оптимизацию кода по памяти, по скорости.
"""
import time
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for x,y in enumerate(src):
    if y > src[x - 1] and x != 0:
        new_list.append(y)

t = time.perf_counter()
print(new_list)
print('память :', sys.getsizeof(new_list))
print('время :', time.perf_counter() - t)

print(f"{'':*^50}")

def my_filter():
    return (y for (x,y) in zip(src[:-2], src[1:]) if  x < y)


t = time.perf_counter()
print(list(my_filter()))
print('память :', sys.getsizeof(my_filter()))
print('время :', time.perf_counter() - t)

print(f"{'':-^90}")
print('Задание 5')
"""
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""



import time
import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_list_1 = []
for i in src:
    if src.count(i) != 1:
        continue
    my_list_1.append(i)


print(my_list_1)
t = time.perf_counter()
print('память :', sys.getsizeof(my_list_1))
print('время :', time.perf_counter() -t)

print(f"{'':*^50}")


my_list_2 = [ i for i in src if src.count(i) == 1 ]
print(my_list_2)
t = time.perf_counter()
print('память :', sys.getsizeof(my_list_2))
print('время :', time.perf_counter() -t)
