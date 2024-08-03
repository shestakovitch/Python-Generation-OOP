"""Класс LowerString
Реализуйте класс LowerString, наследника класса str, описывающий строку, которая во время создания автоматически
переводится в нижний регистр. При создании экземпляра класс должен принимать один аргумент:

obj — объект, определяющий начальное значение строки. Может быть не передан, в таком случае начальное значение считается
пустой строкой
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса LowerString нет, она может быть произвольной."""


class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())


# Sample Input 1:
#
# s1 = LowerString('BEEGEEK')
# s2 = LowerString('BeeGeek')
#
# print(s1)
# print(s2)
# print(s1 == s2)
# print(issubclass(LowerString, str))
# Sample Output 1:
#
# beegeek
# beegeek
# True
# True
# Sample Input 2:
#
# print(LowerString(['Bee', 'Geek']))
# print(LowerString({'A': 1, 'B': 2, 'C': 3}))
# Sample Output 2:
#
# ['bee', 'geek']
# {'a': 1, 'b': 2, 'c': 3}
# Sample Input 3:
#
# s = LowerString('BeeGeek')
#
# print(s[0], s[3])
# Sample Output 3:
#
# b g