"""Класс Vector
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:

x — координата вектора по оси x
y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:

Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с помощью операторов + и -
соответственно:

результатом сложения должен являться новый экземпляр класса Vector, координата по оси x которого равна сумме координат
по оси x исходных векторов, координата по оси y — сумме координат по оси y исходных векторов

результатом вычитания должен являться новый экземпляр класса Vector координата по оси x которого равна разности
координат по оси x исходных векторов с учетом порядка, координата по оси y — разности координат по оси y исходных
векторов с учетом порядка

Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с помощью операторов * и /
соответственно:

результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены на n
результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены на n
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как
вектор на число, так и число на вектор.

Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса
Vector всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.

Примечание 3. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной."""


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Vector(self.x / other, self.y / other)
        return NotImplemented


# Sample Input 1:
#
# a = Vector(1, 2)
# b = Vector(3, 4)
#
# print(a + b)
# print(a - b)
# print(b + a)
# print(b - a)
# Sample Output 1:
#
# Vector(4, 6)
# Vector(-2, -2)
# Vector(4, 6)
# Vector(2, 2)
# Sample Input 2:
#
# a = Vector(3, 4)
#
# print(a * 2)
# print(2 * a)
# print(a / 2)
# Sample Output 2:
#
# Vector(6, 8)
# Vector(6, 8)
# Vector(1.5, 2.0)