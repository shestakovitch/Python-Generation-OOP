"""Класс AdvancedTuple
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения
(+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания
экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый
экземпляр класса AdvancedTuple.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной."""


class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        return AdvancedTuple(tuple(other) + tuple(self))


# Sample Input 1:
#
# advancedtuple = AdvancedTuple([1, 2, 3])
#
# print(advancedtuple + (4, 5))
# print(advancedtuple + [4, 5])
# print({'a': 1, 'b': 2} + advancedtuple)
# Sample Output 1:
#
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# ('a', 'b', 1, 2, 3)
# Sample Input 2:
#
# advancedtuple = AdvancedTuple([1, 2, 3])
#
# advancedtuple += [4, 5]
# advancedtuple += iter([6, 7, 8])
# print(advancedtuple)
# print(type(advancedtuple))
# Sample Output 2:
#
# (1, 2, 3, 4, 5, 6, 7, 8)
# <class '__main__.AdvancedTuple'>