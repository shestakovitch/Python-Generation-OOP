"""Контекстный менеджер reversed_print
Реализуйте контекстный менеджер reversed_print с помощью декоратора @contextmanager, который не принимает никаких
аргументов.

Контекстный менеджер reversed_print должен позволять выполнять все операции записи в стандартный поток вывода sys.stdout
внутри блока with в обратном порядке.

Примечание 1. Наглядные примеры использования класса reversed_print продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный
менеджер используется только с корректными данными."""


from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    standart_output = sys.stdout.write
    sys.stdout.write = lambda x: standart_output(x[::-1])
    yield
    sys.stdout.write = standart_output


# Sample Input 1:
#
# print('Вывод вне блока with')
#
# with reversed_print():
#     print('Вывод внутри блока with')
#
# print('Вывод вне блока with')
# Sample Output 1:
#
# Вывод вне блока with
# htiw аколб иртунв довыВ
# Вывод вне блока with
# Sample Input 2:
#
# with reversed_print():
#     print('python')
#     print('beegeek')
#
# print('Вывод вне блока with')
# Sample Output 2:
#
# nohtyp
# keegeeb
# Вывод вне блока with
# Sample Input 3:
#
# print('Если жизнь одаривает вас лимонами — не делайте лимонад')
# print('Заставьте жизнь забрать их обратно!')
#
# with reversed_print():
#     print('Мне не нужны твои проклятые лимоны!')
#     print('Что мне с ними делать?')
#
# print('Требуйте встречи с менеджером, отвечающим за жизнь!')
# Sample Output 3:
#
# Если жизнь одаривает вас лимонами — не делайте лимонад
# Заставьте жизнь забрать их обратно!
# !ыномил еытялкорп иовт ынжун ен енМ
# ?ьталед имин с енм отЧ
# Требуйте встречи с менеджером, отвечающим за жизнь!