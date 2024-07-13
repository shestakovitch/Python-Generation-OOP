"""Класс QuadraticPolynomial
Квадратный трехчлен – это многочлен вида ax**2+bx+c, где a≠0. Например:

x**2+1
x**2−5x+6

Значение переменной x, при котором квадратный трехчлен обращается в ноль, называют его корнем. Квадратный трехчлен может
иметь один корень, два корня или вовсе не иметь корней. Корни квадратного трехчлена, если они существуют, находятся по
формуле:

x1,2=(−b±(b**2−4ac)**0.5)/2a

Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать
три аргумента в следующем порядке:

a — коэффициент a квадратного трехчлена
b — коэффициент b квадратного трехчлена
c — коэффициент c квадратного трехчлена

Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

a — коэффициент a квадратного трехчлена
b — коэффициент b квадратного трехчлена
c — коэффициент c квадратного трехчлена

Класс QuadraticPolynomial должен иметь четыре свойства:

x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:

x1=(−b-(b**2-4ac)**0.5)/2a

Если квадратный трехчлен не имеет корней (b**2−4ac<0), значением свойства должно быть значение None
x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:

x2=(−b+(b**2-4ac)**0.5)/2a

Если квадратный трехчлен не имеет корней (b**2−4ac<0), значением свойства должно быть значение None
view — свойство, доступное только для чтения, возвращающее строку вида:
ax^2 + bx + c
где a, b и с представляют коэффициенты квадратного трехчлена

coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида:
(a, b, c)
где a, b и с представляют коэффициенты квадратного трехчлена
Примечание 1. Если квадратный трехчлен имеет лишь один корень, значения свойств x1 и x2 должны совпадать.

Примечание 2. При изменении коэффициентов квадратного трехчлена через соответствующие атрибуты или свойство coefficients
значения свойств x1, x2, view и coefficients также должны изменяться.

Примечание 3. Если какие-либо коэффициенты квадратного трехчлена равны нулю, они по-прежнему должны присутствовать в
строке, возвращаемой свойством view, дополнительно их убирать не нужно.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной."""

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def x1(self):
        return None if self.b ** 2 - 4 * self.a * self.c < 0 else (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5)\
                                                                  / (2 * self.a)

    @property
    def x2(self):
        return None if self.b ** 2 - 4 * self.a * self.c < 0 else (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5)\
                                                                  / (2 * self.a)

    @property
    def view(self):
        b, sign_b = abs(self.b), '-' if self.b < 0 else '+'
        c, sign_c = abs(self.c), '-' if self.c < 0 else '+'
        return f'{self.a}x^2 {sign_b} {b}x {sign_c} {c}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, numbers):
        self.a, self.b, self.c = numbers


# Sample Input 1:
#
# polynom = QuadraticPolynomial(1, 2, -3)
#
# print(polynom.a)
# print(polynom.b)
# print(polynom.c)
# Sample Output 1:
#
# 1
# 2
# -3
# Sample Input 2:
#
# polynom = QuadraticPolynomial(1, 2, -3)
#
# print(polynom.x1)
# print(polynom.x2)
# Sample Output 2:
#
# -3.0
# 1.0
# Sample Input 3:
#
# polynom = QuadraticPolynomial(1, 2, -3)
#
# print(polynom.view)
# print(polynom.coefficients)
# Sample Output 3:
#
# 1x^2 + 2x - 3
# (1, 2, -3)