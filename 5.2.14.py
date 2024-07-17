"""Класс Rectangle
Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в
следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:

Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Rectangle нет, она может быть произвольной."""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


# Sample Input 1:
#
# rectangle = Rectangle(1, 2)
#
# print(str(rectangle))
# print(repr(rectangle))
# Sample Output 1:
#
# Rectangle(1, 2)
# Rectangle(1, 2)
# Sample Input 2:
#
# rectangle1 = Rectangle(1, 2)
# rectangle2 = Rectangle(3, 4)
#
# print(rectangle1)
# print(repr(rectangle2))
# Sample Output 2:
#
# Rectangle(1, 2)
# Rectangle(3, 4)