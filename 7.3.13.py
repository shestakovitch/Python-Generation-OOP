"""Класс UpperPrintString
Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра класса
UpperPrintString должен совпадать с процессом создания экземпляра класса str.

Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:

<значение строки в верхнем регистре>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса UpperPrintString нет, она может быть произвольной."""


class UpperPrintString(str):
    def __str__(self):
        return self.upper()


# Sample Input 1:
#
# s1 = UpperPrintString('beegeek')
# s2 = UpperPrintString('BeeGeek')
#
# print(s1)
# print(s2)
# Sample Output 1:
#
# BEEGEEK
# BEEGEEK
# Sample Input 2:
#
# s = UpperPrintString('beegeek')
# print(list(s))
# Sample Output 2:
#
# ['b', 'e', 'e', 'g', 'e', 'e', 'k']