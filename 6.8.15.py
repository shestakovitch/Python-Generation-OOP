"""Класс NonKeyword
Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение
атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:

name — имя атрибута, за которым будет закреплен дескриптор
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым
ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError
с текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной."""


from keyword import kwlist


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


# Sample Input 1:
#
# class Student:
#     name = NonKeyword('name')
#
# student = Student()
# student.name = 'Peter'
#
# print(student.name)
# Sample Output 1:
#
# Peter
# Sample Input 2:
#
# class Student:
#     name = NonKeyword('name')
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
#     name = NonKeyword('name')
#
# student = Student()
# student.name = 'Peter'
#
# try:
#     student.name = 'class'
# except ValueError as e:
#     print(e)
# Sample Output 3:
#
# Некорректное значение