"""Классы MinStat, MaxStat и AverageStat
1. Реализуйте класс MinStat, описывающий объект, который находит минимальное значение среди определенного набора чисел.
При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MinStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий минимальное число из набора. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
2. Также реализуйте класс MaxStat, описывающий объект, который находит максимальное значение среди определенного набора
чисел. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MaxStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий максимальное число из набора. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
3. Наконец, реализуйте класс AverageStat, описывающий объект, который находит среднее арифметическое определенного
набора чисел. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс AverageStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий среднее арифметическое набора чисел. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=[]):
        self.iterable = iterable if iterable else []

    def add(self, num):
        self.iterable.append(num)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self.iterable.clear()


class MinStat(Stat):
    def result(self):
        return min(self.iterable, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.iterable, default=None)


class AverageStat(Stat):
    def result(self):
        if self.iterable:
            return sum(self.iterable) / len(self.iterable)
        return None


# Sample Input 1:
#
# minstat = MinStat([1, 2, 4])
# maxstat = MaxStat([1, 2, 4])
# averagestat = AverageStat([1, 2, 4])
#
# minstat.add(5)
# maxstat.add(5)
# averagestat.add(5)
#
# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())
# Sample Output 1:
#
# 1
# 5
# 3.0
# Sample Input 2:
#
# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()
#
# for i in range(1, 6):
#     minstat.add(i)
#     maxstat.add(i)
#     averagestat.add(i)
#
# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())
# Sample Output 2:
#
# 1
# 5
# 3.0
# Sample Input 3:
#
# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()
#
# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())
# Sample Output 3:
#
# None
# None
# None