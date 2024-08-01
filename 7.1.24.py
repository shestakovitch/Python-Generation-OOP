"""Иерархия классов 🔶
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры:
                                        Shape
                                    /           \
                                Polygon         Circle
                              /        \
                    Quadrilateral      Triangle
                        |               |        \
            Parallelogram   IsoscelesTriangle   EquilateralTriangle
                    |
                Rectangle
                   |
                Square

"""


class Shape:
    pass


class Circle(Shape):
    pass


class Polygon(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass


class Triangle(Polygon):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


# Sample Input 1:
# 
# print(issubclass(Circle, Shape))
# print(issubclass(Polygon, Shape))
# Sample Output 1:
#
# True
# True
# Sample Input 2:
#
# print(issubclass(Triangle, Polygon))
# print(issubclass(IsoscelesTriangle, Triangle))
# print(issubclass(EquilateralTriangle, Triangle))
# Sample Output 2:
#
# True
# True
# True