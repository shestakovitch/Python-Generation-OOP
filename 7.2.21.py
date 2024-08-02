"""Класс FieldTracker🌶️🌶️
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов
своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:

base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо
исходное (указанное при определении) значение этого атрибута, если оно было изменено
has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута
было изменено хотя бы раз, или False в противном случае
changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а
значениями — их исходные значения
save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои
значения, а их текущие значения считаются исходными
Гарантируется, что наследники класса FieldTracker:

всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений
отслеживаемым атрибутам
Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение
отличается от текущего.

Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных
атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный
класс используется только с корректными данными."""


class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)


# Sample Input 1:
#
# class Point(FieldTracker):
#     fields = ('x', 'y', 'z')
#
#     def __init__(self, x, y, z):
#         self.x, self.y, self.z = x, y, z
#         super().__init__()
#
# point = Point(1, 2, 3)
#
# print(point.base('x'))
# print(point.has_changed('x'))
# print(point.changed())
# Sample Output 1:
#
# 1
# False
# {}
# Sample Input 2:
#
# class Point(FieldTracker):
#     fields = ('x', 'y', 'z')
#
#     def __init__(self, x, y, z):
#         self.x, self.y, self.z = x, y, z
#         super().__init__()
#
# point = Point(1, 2, 3)
# point.x = 0
# point.z = 4
# point.z = 5
#
# print(point.base('x'))
# print(point.base('z'))
# print(point.has_changed('x'))
# print(point.has_changed('z'))
# print(point.changed())
# Sample Output 2:
#
# 1
# 3
# True
# True
# {'x': 1, 'z': 3}
# Sample Input 3:
#
# class Point(FieldTracker):
#     fields = ('x', 'y', 'z')
#
#     def __init__(self, x, y, z):
#         self.x, self.y, self.z = x, y, z
#         super().__init__()
#
# point = Point(1, 2, 3)
# point.x = 0
# point.z = 4
# point.save()
#
# print(point.base('x'))
# print(point.base('z'))
# print(point.has_changed('x'))
# print(point.has_changed('z'))
# print(point.changed())
# Sample Output 3:
#
# 0
# 4
# False
# False
# {}