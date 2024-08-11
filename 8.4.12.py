"""Декоратор @takes_numbers
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено
исключение TypeError с текстом:

Аргументы должны принадлежать типам int или float
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен
уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код,
вызывающий его."""


import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for item in (*args, *kwargs.values()):
            if not isinstance(item, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)


# Sample
# Input
# 1:
#
#
# @takes_numbers
# def mul(a, b):
#     return a * b
#
#
# print(mul(1, 2))
# print(mul(1, 2.5))
# print(mul(1.5, 2))
# print(mul(1.5, 2.5))
# Sample
# Output
# 1:
#
# 2
# 2.5
# 3.0
# 3.75
# Sample
# Input
# 2:
#
#
# @takes_numbers
# def mul(a, b):
#     return a * b
#
#
# try:
#     print(mul(1, '2'))
# except TypeError as error:
#     print(error)
# Sample
# Output
# 2:
#
# Аргументы должны принадлежать типам int или float