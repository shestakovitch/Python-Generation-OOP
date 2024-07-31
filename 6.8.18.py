"""Класс TypeChecked
Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение
атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное количество
позиционных аргументов, каждый из которых является типом данных.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов,
указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено исключение
TypeError с текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса TypeChecked нет, она может быть произвольной."""


class TypeChecked:
    def __init__(self, *args):
        self.types = args

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if not isinstance(value, self.types):
            raise TypeError('Некорректное значение')
        obj.__dict__[self._attr] = value


# Sample Input 1:
#
# class Student:
#     name = TypeChecked(str)
#
# student = Student()
# student.name = 'Mary'
#
# print(student.name)
# Sample Output 1:
#
# Mary
# Sample Input 2:
#
# class Student:
#     name = TypeChecked(str)
#
# student = Student()
#
# try:
#     print(student.name)
# except AttributeError as e:
#     print(e)
# Sample Output 2:
#
# Атрибут не найден
# Sample Input 3:
#
# class Student:
#     name = TypeChecked(str)
#
# student = Student()
# student.name = 'Mary'
#
# try:
#     student.name = 99
# except TypeError as e:
#     print(e)
#
# print(student.name)
# Sample Output 3:
#
# Некорректное значение
# Mary
# Sample Input 4:
#
# class Student:
#     age = TypeChecked(int, float)
#
# student = Student()
#
# student.age = 18
# print(student.age)
#
# student.age = 18.5
# print(student.age)
# Sample Output 4:
#
# 18
# 18.5