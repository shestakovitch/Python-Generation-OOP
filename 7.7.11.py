"""Классы USADate и ItalianDate
1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три
аргумента в следующем порядке:

year — год
month — месяц
day — день
Класс USADate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три
аргумента:

year — год
month — месяц
day — день
Класс ItalianDate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from datetime import date


class USADate:
    def __init__(self, year, month, day):
        self.dt = date(year, month, day)

    def format(self):
        return self.dt.strftime('%m-%d-%Y')

    def iso_format(self):
        return self.dt


class ItalianDate(USADate):
    def format(self):
        return self.dt.strftime('%d/%m/%Y')


# Sample Input 1:
#
# usadate = USADate(2023, 4, 6)
#
# print(usadate.format())
# print(usadate.iso_format())
# Sample Output 1:
#
# 04-06-2023
# 2023-04-06
# Sample Input 2:
#
# italiandate = ItalianDate(2023, 4, 6)
#
# print(italiandate.format())
# print(italiandate.iso_format())
# Sample Output 2:
#
# 06/04/2023
# 2023-04-06