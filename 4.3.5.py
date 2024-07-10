"""Класс Circle
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:

radius — радиус круга
diameter — диаметр круга
area — площадь круга
Примечание 1. Площадь круга вычисляется по формуле πr**2, где r — радиус круга, π — константа, которая выражает
отношение длины окружности к ее диаметру.

Примечание 2. Импортировать константу π можно из модуля math:

from math import pi
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""

from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius ** 2


# Sample Input 1:
# circle = Circle(1)
# print(circle.radius)
#
# Sample Output 1:#
# 1
#
# Sample Input 2:
# circle = Circle(5)
# print(circle.radius)
# print(circle.diameter)
# print(circle.area)
#
# Sample Output 2:
# 5
# 10
# 78.53981633974483