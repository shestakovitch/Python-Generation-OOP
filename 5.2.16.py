"""Класс IPAddress
IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети. IP-адреса представляют
собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38. Каждое число в наборе принадлежит
интервалу от 0 до 255. Таким образом, полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:

ipaddress — IP-адрес, представленный в одном из следующих вариантов:
строка из четырех целых чисел, разделенных точками
список или кортеж из четырех целых чисел
Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:

IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:

<IP-адрес в виде четырех целых чисел, разделенных точками>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса IPAddress нет, она может быть произвольной."""


from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return self.ipaddress


# Sample Input 1:
#
# ip = IPAddress('8.8.1.1')
#
# print(str(ip))
# print(repr(ip))
# Sample Output 1:
#
# 8.8.1.1
# IPAddress('8.8.1.1')
# Sample Input 2:
#
# ip = IPAddress([1, 1, 10, 10])
#
# print(str(ip))
# print(repr(ip))
# Sample Output 2:
#
# 1.1.10.10
# IPAddress('1.1.10.10')
# Sample Input 3:
#
# ip = IPAddress((1, 1, 11, 11))
#
# print(str(ip))
# print(repr(ip))
# Sample Output 3:
#
# 1.1.11.11
# IPAddress('1.1.11.11')