"""Функция is_decimal()
Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с необязательного
символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка стоит перед
символом дефиса.

Реализуйте функцию is_decimal(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в
противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_decimal(), но не код,
вызывающий ее."""


def is_decimal(string):
    try:
        return bool(float(string))
    except:
        return False

"""
Sample Input 1:
print(is_decimal('100'))

Sample Output 1:
True

Sample Input 2:
print(is_decimal('199.1'))

Sample Output 2:
True

Sample Input 3:
print(is_decimal('-0.2'))

Sample Output 3:
True

Sample Input 4:
print(is_decimal('.-95'))

Sample Output 4:
False

Sample Input 5:
print(is_decimal('-.95'))

Sample Output 5:
True

Sample Input 6:
print(is_decimal('.10'))

Sample Output 6:
True
"""