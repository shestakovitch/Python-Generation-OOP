""" Класс QuadraticPolynomial
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать
три аргумента в следующем порядке:

a — коэффициент a квадратного трехчлена
b — коэффициент b квадратного трехчлена
c — коэффициент c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса QuadraticPolynomial должен возвращать значение выражения
ax**2+bx+c, где a,b и c — коэффициенты квадратного трехчлена.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной."""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


# Sample Input 1:
#
# func = QuadraticPolynomial(1, 2, 1)
#
# print(func(1))
# print(func(2))
# Sample Output 1:
#
# 4
# 9
# Sample Input 2:
#
# func = QuadraticPolynomial(1, 3, 4)
#
# print(func(1))
# print(func(2))
# Sample Output 2:
#
# 8
# 14