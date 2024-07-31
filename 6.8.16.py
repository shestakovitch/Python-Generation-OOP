"""Класс NonNegativeInteger
Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое
значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента в
следующем порядке:

name — имя атрибута, за которым будет закреплен дескриптор
default — значение по умолчанию. Если не передан, имеет значение None
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не
установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию
равняется None, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным
целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с
текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной."""


class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr, self._default = name, default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__ and self._default is None:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__.get(self._attr, self._default)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


# Sample Input 1:
#
# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
# student.score = 90
#
# print(student.score)
# Sample Output 1:
#
# 90
# Sample Input 2:
#
# class Student:
#     score = NonNegativeInteger('score', 0)
#
# student = Student()
#
# print(student.score)
# student.score = 0
# print(student.score)
# Sample Output 2:
#
# 0
# 0
# Sample Input 3:
#
# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
#
# try:
#     print(student.score)
# except AttributeError as e:
#     print(e)
# Sample Output 3:
#
# Атрибут не найден
# Sample Input 4:
#
# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
#
# try:
#     student.score = -90
# except ValueError as e:
#     print(e)
# Sample Output 4:
#
# Некорректное значение