"""Класс ColoredPoint
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать
три аргумента в следующем порядке:

x — координата точки по оси x
y — координата точки по оси y
color — цвет точки
Класс ColoredPoint должен иметь три свойства:

x — свойство, доступное только для чтения, возвращающее координату точки по оси x
y — свойство, доступное только для чтения, возвращающее координату точки по оси y
color — свойство, доступное только для чтения, возвращающее цвет точки
Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и !=.
Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.

Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение, вычисленное
с помощью функции hash() на основе кортежа, первым элементом которого является координата точки по оси x, вторым —
координата точки по оси y, третьим — цвет точки.

Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен
вернуть константу NotImplemented.

Примечание 2. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной."""


class ColoredPoint:
    def __init__(self, x, y, color):
        self._x, self._y, self._color = x, y, color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


# Sample Input 1:
#
# point1 = ColoredPoint(1, 2, 'white')
# point2 = ColoredPoint(1, 2, 'white')
# point3 = ColoredPoint(3, 4, 'black')
#
# print(point1 == point2)
# print(hash(point1) == hash(point2))
# print(point1 == point3)
# print(hash(point1) == hash(point3))
# Sample Output 1:
#
# True
# True
# False
# False
# Sample Input 2:
#
# points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
#
# print(points)
# Sample Output 2:
#
# {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
# Sample Input 3:
#
# point = ColoredPoint(1, 2, 'white')
#
# try:
#     point.color = 'black'
# except AttributeError as e:
#     print('Error')
# Sample Output 3:
#
# Error