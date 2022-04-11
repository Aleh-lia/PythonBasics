print('Задание 1')
"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>,
<requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
"""
# with open('nginx_logs.txt') as f:
#     data = []
#     for line in f:
#         splitted = line.split()
#         data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
# print(data)






print(f"{'':-^90}")
print('Задание 2')
"""
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""






print(f"{'':-^90}")
print('Задание 3')
"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

# my_file_users = open('users.csv', 'w+', encoding='utf-8')
# my_file_users.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович\n')
# my_file_users.close()
# my_file_hobby = open('hobby.csv', 'w+', encoding='utf-8')
# my_file_hobby.write('скалолазание, охота\nгорные лыжи')
# my_file_hobby.close()
# # print(my_file_users)
# print(my_file_hobby)
# file = open('hobby.csv', 'r', encoding='utf-8')
# print(file.read())
# print(file.writable())


from itertools import zip_longest
import json

users_hobby = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        users_lines = users.readlines()
        hobby_lines = hobby.readlines()
        print(len(users_lines) < len(hobby_lines))
        if len(users_lines) < len(hobby_lines):
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_hobby in zip_longest(users, hobby):
            print((line_user, line_hobby))
            users_hobby[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby

    with open('task3.json', 'w', encoding='utf-8') as f:
        json.dump(users_hobby, f, ensure_ascii=False)
    print(users_hobby)



print(f"{'':-^90}")
print('Задание 4')
"""
4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
двоеточие и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""





print(f"{'':-^90}")
print('Задание 5')
"""
5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
"""






print(f"{'':-^90}")
print('Задание 6')
"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
записанных данных. При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
● просто запуск скрипта — выводить все записи;
● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
этому числу, до конца;
● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
первому числу, по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
177879,1
"""

# my_file = open('bakery.csv', 'a', encoding='utf-8')
# my_file.write('5978,5\n8914,3\n7879,1\n1573,7')

# add_sale.py
import sys

price = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

# show_sales.py
import sys

nums = sys.argv[1:]
print(nums)
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())

print(f"{'':-^90}")
print('Задание 7')
"""
7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
которой не существует.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""