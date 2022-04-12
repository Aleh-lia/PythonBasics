print('Задание 1')
"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
|--settings
|--mainapp
|--adminapp
|--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
"""

# import os
# pattern_task_1 = {
#     'my_projectt_lesson_7_1': [
#         {'setting':[]},
#         {'mainapp':[]},
#         {'adminapp':[]},
#         {'authapp':[]}
#     ]
# }
# for root, folders in pattern.items():
#     if os.path.exists(root):
#         print(root, 'exists')
#     else:
#         for folder in folders:
#             cur_dir = os.path.join(root, folder)
#             os.makedirs(cur_dir)

print(f"{'':-^90}")
print('Задание 2')
"""
2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
    |--settings
    |   |--__init__.py 
    |   |--dev.py
    |   |--prod.py
    |--mainapp
    |   |--__init__.py
    |   |--models.py
    |   |--views.py
    |   |--templates
    |       |--mainapp
    |           |--base.html
    |           |--index.html
    |--authapp
    |   |--__init__.py
    |   |--models.py
    |   |--views.py
    |   |--templates
    |       |--authapp
    |           |--base.html
    |           |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
"""

# import yaml
# import os
#
#
# pattern_task_2 = {
#     'my_project_lesson_7_2': [
#         {'setting': [
#             '__init__.py',
#             'dev.py',
#             'prod.py'
#         ]
#         },
#
#         {'mainapp': [
#             '__init__.py',
#             'models.py',
#             'views.py',
#             {'templates': [
#                 {'mainapp': [
#                     'base.html',
#                     'index.html'
#                 ]
#                 }
#             ]
#             }
#         ]
#         },
#
#         {'authapp': [
#             '__init__.py',
#             'models.py',
#             'views.py',
#             {'templates':[
#                 {'authapp':[
#                     'base.html',
#                     'index.html'
#                 ]
#                 }
#             ]
#             }
#         ]
#         }
#     ]
# }
#
# f = open('config.yaml', 'w')
# f.write(yaml.dump(pattern_task_2))
# f.close()
#
# with open("config.yaml") as config_file:
#     pattern_task_2 = yaml.safe_load(config_file)
#
#
# def create_structure (data):
#     for folder, data_tmps in data.items():
#         if not os.path.exists(folder):
#             os.mkdir(folder)
#         os.chdir(folder)
#         for data_tmp in data_tmps:
#             if isinstance(data_tmp, dict):
#                 create_structure(data_tmp)
#             else:
#                 if not os.path.exists(data_tmp):
#                     if '.' in data_tmp:
#                         with open(data_tmp, 'w') as f:
#                             f.write('')
#     else:
#         os.chdir('../')
#
#
# create_structure(pattern_task_2)

print(f"{'':-^90}")
print('Задание 3')
"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
    ...
    |--templates
    |   |--mainapp
    |   |   |--base.html
    |   |   |--index.html
    |   |--authapp
    |       |--base.html
    |       |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
"""

# import os
# import  shutil
# my_dir = 'task_7_3'
# if not os.path.exists(my_dir):
#     os.mkdir(my_dir)
#
# folder  = r'my_project_lesson_7_2'
# files = []
#
# for r, d, f in os.walk(folder):
# #    for file in f:
# #        if '.py' in file:
# #            files.append(os.path.join(r, file))
#     for file in f:
#         if '.html' in file:
#             files.append(os.path.join(r, file))
# for path in files:
#     folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
#     if not os.path.exists(folder):
#         os.mkdir(folder)
#     save_path =os.path.join(folder, os.path.basename(path))
#     shutil.copy(path, save_path)

print(f"{'':-^90}")
print('Задание 4')
"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
} Ту
т 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    number = len(str(file))
    out_dict[10 ** number] += 1

print(out_dict)

print(f"{'':-^90}")
print('Задание 5')
"""
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]),
например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
} С
охраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.


Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""