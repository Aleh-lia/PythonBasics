print('Задание 1')
"""
Task 1
Написать функцию email_parse(<email_address>), которая при помощи
регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и
возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""


import re

EMAIL_MASK = re.compile(r'^([a-z0-9_/.-]+)@([0-9a-z_/.)]+\.[a-z/.]{2,6})')


def email_parse(email):
    found_info = EMAIL_MASK.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    return name, addr

# print(email_parse('someone@geekbrainsru'))
print(email_parse('someone@geekbrains.ru'))
# email = input('Для проверки введите любой email: ')
# print(email_parse(email))

print(f"{'':-^90}")
print('Задание 2')
"""
Task2
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера 
из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
для получения информации вида: 
(<remote_addr>, 
<request_datetime>, 
<request_type>, 
<requested_resource>, 
<response_code>, 
<response_size>), 
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


"""

print(f"{'':-^90}")
print('Задание 3')
"""
Task3
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
5: <class 'int'>


Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных 
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции,
например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):

    @wraps(func)

    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


a = calc_cube(3, 5)
print(a)
print(calc_cube.__name__)


print(f"{'':-^90}")
print('Задание 4')


"""
# Task4
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные 
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?

"""

from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube.__name__)
a = calc_cube(5)
print(a)
print('-/'*30)
b = calc_cube(-5)
print(b)


