"""Класс Versioned🌶️
Реализуйте класс Versioned, описывающий дескриптор, предоставляющий доступ как к текущему значению атрибута, так и ко
всем предыдущим, если значение атрибута когда-либо изменялось. При создании экземпляра класс не должен принимать никаких
аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо
дополнительных проверок.

Класс Versioned должен иметь два метода экземпляра:

get_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n.
Метод должен возвращать n-ое по счету значение атрибута этого экземпляра класса. Например, если значение атрибута было
установлено, а затем изменено, то метод get_version() должен уметь вернуть как установленное значение (первое по счету),
так и измененное (второе по счету)
set_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n.
Метод должен устанавливать n-ое по счету значение атрибута в качестве текущего
Примечание 1. Вызов метода set_version() не должен приравниваться к изменению значения атрибута. Будем считать, что
атрибут изменяет свое значение только в том случае, если эта операция выполняется через точечную нотацию или функцию
setattr().

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Versioned нет, она может быть произвольной."""


class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr][-1]

    def __set__(self, obj, value):
        obj.__dict__.setdefault(self._attr, []).append(value)

    def get_version(self, obj, n):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        temp = obj.__dict__ [self._attr][n - 1]
        obj.__dict__.setdefault(self._attr, []).append(temp)


# Sample
# Input
# 1:
#
#
# class Student:
#     age = Versioned()
#
#
# student = Student()
#
# student.age = 18
# student.age = 19
#
# print(student.age)
# Sample
# Output
# 1:
#
# 19
# Sample
# Input
# 2:
#
#
# class Student:
#     age = Versioned()
#
#
# student = Student()
#
# student.age = 18
# student.age = 19
# student.age = 20
#
# print(student.age)
# print(Student.age.get_version(student, 1))
# print(Student.age.get_version(student, 2))
# print(Student.age.get_version(student, 3))
# Sample
# Output
# 2:
#
# 20
# 18
# 19
# 20
# Sample
# Input
# 3:
#
#
# class Student:
#     age = Versioned()
#
#
# student = Student()
#
# student.age = 18
# student.age = 19
# student.age = 20
#
# print(student.age)
# Student.age.set_version(student, 1)
# print(student.age)
# Sample
# Output
# 3:
#
# 20
# 18