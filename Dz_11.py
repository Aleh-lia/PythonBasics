print('Задание 1')
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в 
виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен 
проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    __date: str

    def __init__(self, date: str) -> None:
        self.__date = date

    @staticmethod
    def is_valid(date: str):

        day: int
        month: int
        year: int

        try:
            day, month, year = Date.split_to_numb(date)
        except:
            return False

        if not 1 <= month <= 12:
            return False

        if not 0 <= year:
            return False

        if not 1 <= day <= 31:
            return False


        if month in [4, 6, 9, 11] and day == 31:
            return False


        if (
                month == 2 and
                day == 29 and
                year % 4 != 0 and
                year % 100 != 0 and
                year % 400 != 0
        ):
            return False

        return True

    @classmethod
    def split_to_numb(cls, date: str):
        try:
            return(list(map(int, date.split("-"))))
        except:
            raise ValueError("can't split by integer")



print(f"{'':-^90}")
print('Задание 2')
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

# class DivideZero(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)
#
#
# if __name__ == "__main__":
#     from sys import exit
#
#     a = 0
#     b = 0
#     try:
#         a = float(input("введите a: "))
#         b = float(input("введите b: "))
#     except:
#         print("неверный ввод")
#         exit(1)
#
#     try:
#         if b == 0:
#             raise DivideZero("Вы делите на ноль")
#         print(f"All is ok {a}/{b} = {a/b}")
#     except DivideZero as ex:
#         print(ex)

print(f"{'':-^90}")
print('Задание 3')
"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка 
на наличие только чисел. Проверить работу исключения на реальном примере. 
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и 
строки. Во время ввода пользователем очередного элемента необходимо реализовать 
проверку типа элемента. Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и 
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
# class NumbersOnly(Exception):
#
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)
#
#
# if __name__ == "__main__":
#
#     lst = []
#     while True:
#         try:
#             inp = input()
#             if inp == "stop":
#                 break
#             elif not inp.isdigit():
#                 raise NumbersOnly()
#             else:
#                 lst.append(int(inp))
#         except NumbersOnly:
#             print("Вы вводите данные, а не число")
#
#     print(*lst)



print(f"{'':-^90}")
print('Задание 4-6')
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом 
классе определите параметры, общие для приведённых типов. В классах-наследниках 
реализуйте параметры, уникальные для каждого типа оргтехники.
"""

"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за 
приём оргтехники на склад и передачу в определённое подразделение компании. Для 
хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру (например, словарь).
"""

"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум 
возможностей, изученных на уроках по ООП.
"""
from abc import ABC

class StoreExcept(Exception):
    pass

class EmptyStore(StoreExcept):
    pass

class WrongReq(StoreExcept):
    pass

class StrongFilter(StoreExcept):
    pass

class Store:
    __ID: int = 0
    __single = None
    __store_lst: list['Equip'] = []

    def __new__(cls):

        if not cls.__single:
            cls.__single = super(Store, cls).__new__(cls)

        return cls.__single

    @classmethod
    def add_equip(cls, *equips: 'Equip'):
        for equip in equips:
            equip.equip_id = cls.__ID
            cls.__ID += 1
            cls.__store_lst.append(equip)
            print(f"add {type(equip)} to store")

    @classmethod
    def filter_equip(cls, flt: 'EquipFilter') -> list['Equip']:

        if len(cls.__store_lst) == 0:
            raise EmptyStore()

        res = filter(lambda x: (type (x) is flt.equip_type), cls.__store_lst)


        res = filter(lambda x: x.user == "", res)

        for attr_flt in flt.attr_flts:
            res = filter(attr_flt, res)

        res = list(res)
        length = len(res)

        if length == 0 or length < flt.count:
            raise StrongFilter()

        if flt.count == 0:
            return list(res)

        return res[:flt.count]

    @classmethod
    def applue_req(cls, user_name: str, *equips: 'Equip'):

        for equip in cls.__store_lst:
            if equip in equips:
                equip.user = user_name


class EquipFilter:
    equip_type: 'type'
    count: int = 0
    attr_flts: list = []

    def __init__(self, equip_type, *filts, **kwargs) -> None:
        self.equip_type = equip_type
        self.count = kwargs.get("count", 0)
        self.attr_flts = list(filts)


class Equip(ABC):
    __equip_id: int = -1
    create_by: str = ""
    user: str = ""

    @property
    def equip_id(self):
        return self.__equip_id

    @equip_id.setter
    def equip_id(self, id_):
        if self.__equip_id == -1:
            self.__equip_id = id_


class Printer(Equip):
    ink: bool = False
    print_size: list[str] = []


class Shrader(Equip):
    page_size: list[str] = []


class Scanner(Equip):
    scan_size: list[str] = []


class Copper(Printer, Scanner):
    page_in_try: int = 0


def main():
    store = Store()



    p = [Printer() for _ in range(3)]

    p[0].create_by = "Sony"
    p[0].ink = True
    p[0].print_size.append("A4")
    p[0].print_size.append("A3")

    p[1].create_by = "Epson"
    p[1].ink = True
    p[1].print_size.append("A4")

    p[2].create_by = "Cannon"
    p[2].ink = False
    p[2].print_size.append("A3")



    s = Scanner()

    s.create_by = "Epson"
    s.scan_size.append("A4")



    c = [Copper() for _ in range(2)]

    c[0].create_by = "Xerox"
    c[0].ink = True
    c[0].print_size.append("A4")
    c[0].scan_size.append("A3")
    c[0].page_in_try = 300

    c[1].create_by = "Xerox"
    c[1].ink = True
    c[1].print_size.append("A3")
    c[1].scan_size.append("A4")
    c[1].page_in_try = 300

    try:
        store.filter_equip(EquipFilter(Printer))
    except EmptyStore:
        print("Store is empty")

    store.add_equip(*c)
    store.add_equip(*p, s)

    try:
        print(store.filter_equip(EquipFilter(Printer, count=10)))
    except StrongFilter:
        print("Filter is strong")

    try:
        req = store.filter_equip(EquipFilter(Printer, lambda x: x.ink == True, count=1))
        print(*req)
        store.applue_req("company", *req)
        print(store.filter_equip(EquipFilter(Copper, lambda x: "A3" in x.scan_size)))
    except StrongFilter:
        print("Filter is strong")


if __name__ == "__main__":
    main()


print(f"{'':-^90}")
print('Задание 7')
"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных 
чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса 
(комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""

from math import e, sqrt

class Complex:
    __real: float
    __img: float


    @property
    def real(self):
        return self.__real

    @property
    def img(self):
        return self.__img

    @real.setter
    def real(self, new_real):
        if new_real.__class__ is int or new_real.__class__ is float:
            self.__real = new_real
        else:
            raise ValueError(f"{new_real.__class__} can't be real")

    @img.setter
    def img(self, new_img):
        if new_img.__class__ is int or new_img.__class__ is float:
            self.__img = new_img
        else:
            raise ValueError(f"{new_img.__class__} can't be img")

    def __init__(self, __real: float = 0, __img: float = 0) -> None:
        self.__real = __real
        self.__img = __img

    def __str__(self) -> str:
        return f"{self.__real}{' + ' if self.__img >= 0 else ' - ' }{'{'}{abs(self.__img)}{'}'}"

    def __add__(self, other):
        return self.__add__sub__(other, func=lambda x, y: x + y)

    def __sub__(self, other):
        return self.__add__sub__(other, func=lambda x, y: x - y)

    def __iadd__(self, other):
        result = self.__add__sub__(other, func=lambda x, y: x + y)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __isub__(self, other):
        result = self.__add__sub__(other, func=lambda x, y: x - y)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __imul__(self, other):
        result = self.__mul__(other)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __itruediv__(self, other):
        result = self.__mul__(other)
        self.__real = result.__real
        self.__img = result.__img
        return self

    def __bool__(self):
        return self.__img != 0 and self.__real != 0

    def __mul__(self, other):
        if other.__class__ is int or other.__class__ is float:
            return Complex(__real=self.__real * other, __img=self.__img * other)
        elif other.__class__ is Complex:
            return Complex(
                __real=self.__real * other.__real - self.__img * other.__img,
                __img=self.__real * other.__real + self.__img * other.__img
            )
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")

    def __truediv__(self, other):
        if other.__class__ is int or other.__class__ is float:
            return self / Complex(other)
        elif other.__class__ is Complex:
            div = other.__real ** 2 + other.__img ** 2
            return Complex(
                __real=(self.__real * other.__real + self.__img * other.__img) / div,
                __img=(self.__img * other.__real - self.__real * other.__img) / div
            )
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")

    def __abs__(self):
        return sqrt(self.__real ** 2 + self.__img ** 2)

    def __add__sub__(self, other, func):
        if other.__class__ is int or other.__class__ is float:
            return Complex(__real=func(self.__real, other), __img=self.__img)
        elif other.__class__ is Complex:
            return Complex(__real=func(self.__real, other.__real), __img=func(self.__img, other.__img))
        else:
            raise ValueError(f"No implement __add__ with {other.__class__}")