print('Задание 1')
"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

# from time import sleep
# from itertools import cycle
# from colorama import init, Fore
# from colorama import Back
# init(autoreset=True)
#
# class TrafficLight:
#
#
#     def __init__(self):
#         self.__color = ((Fore.BLACK + Back.LIGHTRED_EX + ' Red    ', 7), (Fore.BLACK + Back.LIGHTYELLOW_EX + ' Yellow ', 2), (Fore.BLACK + Back.LIGHTGREEN_EX + ' Green  ', 5))
#
#     def running(self):
#         for color, sec in cycle(self.__color):
#             print(color, '{}'.format(sec))
#             sleep(sec)
#
# traffic_light = TrafficLight()
# traffic_light.running()



print(f"{'':-^90}")
print('Задание 2')
"""
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def calc_mass(self):
        mass = self._length * self._width * 25 * 5
        return mass



my_road = Road(21, 4000)
print(my_road.calc_mass(), 'т')



print(f"{'':-^90}")
print('Задание 3')
"""
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:


    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return round(self._income_wage +self._income_bonus, 2)


worker_1 = Position('Petr', 'Petrov', 'senior', {"wage": 17000.37, "bonus": 48000.21})
print(worker_1.get_full_name())
print(worker_1.get_total_income())


print(f"{'':-^90}")
print('Задание 4')
"""
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} останавливается!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))

    def show_speed(self):
        print('текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Внимание. Превышена максимальная скорость!')
        super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Внимание. Превышена максимальная скорость!')
        super().show_speed()

class PoliceCar(Car):
    pass



sport_car = SportCar(240, 'Синий', 'Спортивная машина', False)
town_car = TownCar(140, 'Красный', 'Городская машина', False)
work_car = WorkCar(90, 'Черный', 'Раабочая машина', False)
police_car = PoliceCar(210, 'Синий', 'Поличейский автомабиль', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')


print(f"{'':-^90}")
print('Задание 5')
"""
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка происходит ручкой')


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        print('Отрисовка происходит карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка происходит маркером')



pen = Pen('')
pencil = Pencil('')
handle = Handle('')

pen.draw()
pencil.draw()
handle.draw()
