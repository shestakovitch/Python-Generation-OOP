"""Класс Peekable 🌶️
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в
исходном порядке, а затем возбуждает исключение StopIteration.

Класс Peekable должен иметь один метод экземпляра:

peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор.
Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один
необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если
итератор пуст
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной."""


from copy import copy


class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def peek(self, default='wtf'):
        copy_iterable = copy(self.iterable)
        if default == 'wtf':
            return next(copy_iterable)
        return next(copy_iterable, default)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


# Sample Input 1:
#
# iterator = Peekable('beegeek')
#
# print(next(iterator))
# print(next(iterator))
# print(*iterator)
# Sample Output 1:
#
# b
# e
# e g e e k
# Sample Input 2:
#
# iterator = Peekable('Python')
#
# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())
# print(next(iterator))
# print(iterator.peek())
# print(iterator.peek())
# Sample Output 2:
#
# P
# y
# y
# y
# t
# t
# Sample Input 3:
#
# iterator = Peekable('Python')
#
# print(*iterator)
# print(iterator.peek(None))
# Sample Output 3:
#
# P y t h o n
# None