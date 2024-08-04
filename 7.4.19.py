"""Класс AdvancedList
Реализуйте класс AdvancedList, наследника класса list, описывающий список с дополнительным функционалом. Процесс
создания экземпляра класса AdvancedList должен совпадать с процессом создания экземпляра класса list.

Класс AdvancedList должен иметь три метода экземпляра:

join() — метод, объединяющий все элементы экземпляра класса AdvancedList в строку и возвращающий полученный результат.
Метод должен принимать один строковый аргумент, по умолчанию равный пробелу, который является разделителем элементов
списка в результирующей строке
map() — метод, принимающий в качестве аргумента функцию func и применяющий ее к каждому элементу экземпляра класса
AdvancedList. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый
filter() — метод, принимающий в качестве аргумента функцию func и удаляющий из экземпляра класса AdvancedList те
элементы, для которых функция func вернула значение False. Метод должен изменять исходный экземпляр класса AdvancedList,
а не возвращать новый
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AdvancedList нет, она может быть произвольной."""


class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(map(str, self))

    def map(self, func):
        self[:] = list(map(func, self))

    def filter(self, func):
        self[:] = list(filter(func, self))


# Sample Input 1:
#
# advancedlist = AdvancedList([1, 2, 3, 4, 5])
#
# print(advancedlist.join())
# print(advancedlist.join('-'))
# Sample Output 1:
#
# 1 2 3 4 5
# 1-2-3-4-5
# Sample Input 2:
#
# advancedlist = AdvancedList([1, 2, 3, 4, 5])
#
# advancedlist.map(lambda x: -x)
#
# print(advancedlist)
# Sample Output 2:
#
# [-1, -2, -3, -4, -5]
# Sample Input 3:
#
# advancedlist = AdvancedList([1, 2, 3, 4, 5])
#
# advancedlist.filter(lambda x: x % 2 == 0)
#
# print(advancedlist)
# Sample Output 3:
#
# [2, 4]
# Sample Input 4:
#
# advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
# id1 = id(advancedlist)
#
# advancedlist.filter(bool)
# id2 = id(advancedlist)
#
# print(advancedlist)
# print(id1 == id2)
# Sample Output 4:
#
# [1, 2, 3, 4, 5]
# True