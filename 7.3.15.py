"""Класс FuzzyString
Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=,
<=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString
должен совпадать с процессом создания экземпляра класса str.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.

Примечание 2. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной."""


class FuzzyString(str):
    def __new__(cls, obj):
        instance = super().__new__(cls, obj)
        instance.obj = obj.lower()
        return instance

    def __eq__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj != other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj < other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj > other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj <= other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return self.obj >= other.lower()
        return NotImplemented

    def __contains__(self, other):
        if isinstance(other, (FuzzyString, str)):
            return other.lower() in self.obj
        return NotImplemented


# Sample Input:
#
# s1 = FuzzyString('BeeGeek')
# s2 = FuzzyString('beegeek')
#
# print(s1 == s2)
# print(s1 in s2)
# print(s2 in s1)
# print(s2 not in s1)
# Sample Output:
#
# True
# True
# True
# False