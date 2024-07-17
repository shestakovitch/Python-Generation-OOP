"""Класс Formatter
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о
переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу, должно
быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной."""

from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @staticmethod
    @format.register(int)
    def _int_format(obj):
        print(f'Целое число: {obj}')

    @staticmethod
    @format.register(float)
    def _float_format(obj):
        print(f'Вещественное число: {obj}')

    @staticmethod
    @format.register(tuple)
    def _tuple_format(obj):
        print(f'Элементы кортежа: {str(obj)[1:-1]}')

    @staticmethod
    @format.register(list)
    def _list_format(obj):
        print(f'Элементы списка: {str(obj)[1:-1]}')

    @staticmethod
    @format.register(dict)
    def _dict_format(obj):
        print(f'Пары словаря: {str(obj.items())[12:-2]}')


# Sample Input 1:
#
# Formatter.format(1337)
# Formatter.format(20.77)
# Sample Output 1:
#
# Целое число: 1337
# Вещественное число: 20.77
# Sample Input 2:
#
# Formatter.format([10, 20, 30, 40, 50])
# Formatter.format(([1, 3], [2, 4, 6]))
# Sample Output 2:
#
# Элементы списка: 10, 20, 30, 40, 50
# Элементы кортежа: [1, 3], [2, 4, 6]
# Sample Input 3:
#
# Formatter.format({'Cuphead': 1, 'Mugman': 3})
# Formatter.format({1: 'one', 2: 'two'})
# Formatter.format({1: True, 0: False})
# Sample Output 3:
#
# Пары словаря: ('Cuphead', 1), ('Mugman', 3)
# Пары словаря: (1, 'one'), (2, 'two')
# Пары словаря: (1, True), (0, False)
# Sample Input 4:
#
# try:
#     Formatter.format('All them years, Dutch, for this snake?')
# except TypeError as e:
#     print(e)
# Sample Output 4:
#
# Аргумент переданного типа не поддерживается