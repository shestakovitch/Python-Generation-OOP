"""Класс Vector
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в
следующем порядке:

x — координата вектора по оси x
y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:

Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов == и!=. Два вектора считаются
равными, если их координаты по обеим осям совпадают. Методы, реализующие операции сравнения, должны уметь сравнивать как
два вектора между собой, так и вектор с кортежем из двух чисел, представляющих координаты x и y.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.

Примечание 3. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной."""


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented


# Sample Input 1:
#
# a = Vector(1, 2)
# b = Vector(1, 2)
#
# print(a == b)
# print(a != b)
# Sample Output 1:
#
# True
# False
# Sample Input 2:
#
# a = Vector(1, 2)
# pair1 = (1, 2)
# pair2 = (3, 4)
# pair3 = (5, 6, 7)
# pair4 = (1, 2, 3, 4)
# pair5 = (1, 4, 3, 2)
#
# print(a == pair1)
# print(a == pair2)
# print(a == pair3)
# print(a == pair4)
# print(a == pair5)
# Sample Output 2:
#
# True
# False
# False
# False
# False