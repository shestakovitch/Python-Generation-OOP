"""Класс NumberList
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа.
При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один
элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа
Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и
insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно
возбуждаться исключение TypeError с текстом:

Элементами экземпляра класса NumberList должны быть числа
Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан.
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной."""


from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=[]):
        super().__init__(self.is_num(i) for i in iterable)

    @staticmethod
    def is_num(num):
        if isinstance(num, (int, float)):
            return num
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def append(self, other):
        self.data.append(self.is_num(other))

    def extend(self, other):
        self.data.extend(self.is_num(i) for i in other)

    def insert(self, index, item):
        self.data.insert(index, self.is_num(item))

    def __setitem__(self, key, value):
        self.data.__setitem__(key, self.is_num(value))

    def __iadd__(self, other):
        return self.data + [self.is_num(i) for i in other]


# Sample Input 1:
#
# numberlist = NumberList([1, 2])
#
# numberlist.append(3)
# numberlist.extend([4, 5])
# numberlist.insert(0, 0)
# print(numberlist)
# Sample Output 1:
#
# [0, 1, 2, 3, 4, 5]
# Sample Input 2:
#
# numberlist = NumberList([0, 1.0])
#
# numberlist[1] = 1
# numberlist = numberlist + NumberList([2, 3])
# numberlist += NumberList([4, 5])
# print(numberlist)
# Sample Output 2:
#
# [0, 1, 2, 3, 4, 5]
# Sample Input 3:
#
# try:
#     numberlist = NumberList(['a', 'b', 'c'])
# except TypeError as error:
#     print(error)
# Sample Output 3:
#
# Элементами экземпляра класса NumberList должны быть числа
# Sample Input 4:
#
# numberlist = NumberList([1, 2, 3])
#
# try:
#     numberlist.append('4')
# except TypeError as error:
#     print(error)
# Sample Output 4:
#
# Элементами экземпляра класса NumberList должны быть числа