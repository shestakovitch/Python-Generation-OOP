"""Декоратор @returns
Реализуйте класс декоратор @returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое
значение принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError.

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен
уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @returns, но не код,
вызывающий его."""


import functools


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, self.datatype):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper


# Sample Input 1:
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# print(add(1, 2))
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('1', '2'))
# except Exception as error:
#     print(type(error))
# Sample Output 2:
#
# <class 'TypeError'>