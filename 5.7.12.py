"""Класс RomanNumeral🌶️🌶️
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен
принимать один аргумент:

number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его
значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=,
>, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью
операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.

Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих
арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

Примечание 4. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной."""


from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return self.number

    def __int__(self):
        return RomanNumeral.roman_to_arabic(self.number)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.__int__() == other.__int__()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.roman_to_arabic(self.number) > RomanNumeral.roman_to_arabic(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(RomanNumeral.arabic_to_roman(int(self) + int(other)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(RomanNumeral.arabic_to_roman(int(self) - int(other)))
        return NotImplemented

    @staticmethod
    def roman_to_arabic(number):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        for i in range(len(number) - 1, -1, -1):
            num = roman[number[i]]
            if 3 * num < summ:
                summ -= num
            else:
                summ += num
        return summ

    @staticmethod
    def arabic_to_roman(number):
        arabic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                  500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= number:
                result += arabic[n]
                number -= n
        return result


# Sample Input 1:
#
# number = RomanNumeral('IV') + RomanNumeral('VIII')
#
# print(number)
# print(int(number))
# Sample Output 1:
#
# XII
# 12
# Sample Input 2:
#
# number = RomanNumeral('X') - RomanNumeral('VI')
#
# print(number)
# print(int(number))
# Sample Output 2:
#
# IV
# 4
# Sample Input 3:
#
# a = RomanNumeral('X')
# b = RomanNumeral('XII')
#
# print(a == b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# Sample Output 3:
#
# False
# False
# True
# False
# True