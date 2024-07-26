"""Класс SkipIterator
Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект
n — целое неотрицательное число
Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable,
пропуская по n элементов, а затем возбуждает исключение StopIteration.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной."""


from itertools import islice


class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = islice(iterable, 0, None, n + 1)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


# Sample Input 1:
#
# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу
#
# print(*skipiterator)
# Sample Output 1:
#
# 1 3 5 7 9
# Sample Input 2:
#
# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента
#
# print(*skipiterator)
# Sample Output 2:
#
# 1 4 7 10
# Sample Input 3:
#
# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы
#
# print(*skipiterator)
# Sample Output 3:
#
# 1 2 3 4 5 6 7 8 9 10