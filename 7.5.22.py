"""Функции is_iterator() и is_iterable()
1. Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимые функции, но не код, вызывающий их."""


def is_iterable(obj):
    return '__iter__' in dir(obj)


def is_iterator(obj):
    return '__next__' in dir(obj)


# Sample Input 1:
#
# print(is_iterable(123))
# print(is_iterable([1, 2, 3]))
# print(is_iterable((1, 2, 3)))
# print(is_iterable('123'))
# print(is_iterable(iter('123')))
# print(is_iterable(map(int, '123')))
# Sample Output 1:
#
# False
# True
# True
# True
# True
# True
# Sample Input 2:
#
# print(is_iterator(123))
# print(is_iterator([1, 2, 3]))
# print(is_iterator((1, 2, 3)))
# print(is_iterator('123'))
# print(is_iterator(iter('123')))
# print(is_iterator(map(int, '123')))
# Sample Output 2:
#
# False
# False
# False
# False
# True
# True