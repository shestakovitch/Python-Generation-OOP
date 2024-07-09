"""Функция is_fraction()
Будем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /,
а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична от нуля (знаменатель не может
равняться нулю). Последовательность, представляющая собой обыкновенную дробь, может начинаться с необязательного символа
дефиса -.

Реализуйте функцию is_fraction(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_fraction(), но не код,
вызывающий ее."""

from re import fullmatch


def is_fraction(string: str):
    return bool(fullmatch(r'\-?\d+/0*[1-9]\d*', string))

"""
Sample Input 1:
print(is_fraction('1000/1'))

Sample Output 1:
True

Sample Input 2:
print(is_fraction('-54/9'))

Sample Output 2:
True

Sample Input 3:
print(is_fraction('71'))

Sample Output 3:
False

Sample Input 4:
print(is_fraction('1 / 82'))

Sample Output 4:
False

Sample Input 5:
print(is_fraction('1/0'))

Sample Output 5:
False
"""