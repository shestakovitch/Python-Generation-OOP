"""Декоратор @ignore_exception
Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов
исключений, и выводит текст:

Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если
возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @ignore_exception, но не
код, вызывающий его."""


from functools import wraps


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exceptions as err:
                print(f'Исключение {type(err).__name__} обработано')
        return wrapper


# Sample Input 1:
#
#
# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def func(x):
#     return 1 / x
#
#
# func(0)
#
# Sample Output 1:
#
# Исключение ZeroDivisionError обработано
#
# Sample Input 2:
#
# min = ignore_exception(ZeroDivisionError)(min)
#
# try:
#     print(min(1, '2', 3, [4, 5]))
# except Exception as error:
#     print(type(error))
#
# Sample Output 2:
#
# <class 'TypeError'>