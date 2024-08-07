"""Классы Point и Circle
1. Реализуйте класс Point, описывающий точку на плоскости. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:

x — координата точки по оси x
y — координата точки по оси y
Экземпляр класса Point должен иметь следующее неформальное строковое представление:

(<координата x>, <координата y>)

2. Также реализуйте класс Circle, описывающий окружность на плоскости. При создании экземпляра класс должен принимать
два аргумента в следующем порядке:

radius — радиус окружности
center — точка с координатами центра окружности, представленная экземпляром класса Point
Экземпляр класса Circle должен иметь следующее неформальное строковое представление:

(<координата центра по оси x>, <координата центра по оси y>), r = <радиус>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{self.center}, r = {self.radius}'


# Sample Input:
#
# point = Point(1, 1)
# circle = Circle(5, point)
#
# print(point)
# print(circle)
# Sample Output:
#
# (1, 1)
# (1, 1), r = 5