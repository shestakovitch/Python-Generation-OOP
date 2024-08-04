"""Класс DefaultList
Реализуйте класс DefaultList, наследника класса UserList, описывающий список, который при попытке получить элемент по
несуществующему индексу возвращает значение по умолчанию. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса DefaultList. Если не передан,
начальный набор элементов считается пустым
default — значение, возвращаемое при попытке получить элемент по несуществующему индексу. По умолчанию равняется None
Примечание 1. Экземпляр класса DefaultList не должен зависеть от итерируемого объекта, на основе которого он был создан.
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса DefaultList измениться не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DefaultList нет, она может быть произвольной."""


from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, item):
        try:
            return self.data[item]
        except IndexError:
            return self.default


# Sample Input 1:
#
# defaultlist = DefaultList([1, 2, 3])
#
# print(defaultlist[0])
# print(defaultlist[-1])
# print(defaultlist[100])
# print(defaultlist[-100])
# Sample Output 1:
#
# 1
# 3
# None
# None
# Sample Input 2:
#
# defaultlist = DefaultList([1, 2, 3], 0)
#
# print(defaultlist[0])
# print(defaultlist[-1])
# print(defaultlist[100])
# print(defaultlist[-100])
# Sample Output 2:
#
# 1
# 3
# 0
# 0