"""Класс Const
Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения, но не разрешать изменять
значения этих атрибутов, а также удалять их. При попытке изменить значение атрибута должно возбуждаться исключение
AttributeError с текстом:

Изменение значения атрибута невозможно
При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:

Удаление атрибута невозможно
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Const нет, она может быть произвольной."""


class Const:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')


# Sample Input 1:
#
# videogame = Const(name='Cuphead')
#
# videogame.developer = 'Studio MDHR'
# print(videogame.name)
# print(videogame.developer)
# Sample Output 1:
#
# Cuphead
# Studio MDHR
# Sample Input 2:
#
# videogame = Const(name='Disco Elysium')
#
# try:
#     videogame.name = 'Half-Life: Alyx'
# except AttributeError as e:
#     print(e)
# Sample Output 2:
#
# Изменение значения атрибута невозможно
# Sample Input 3:
#
# videogame = Const(name='The Last of Us')
#
# try:
#     del videogame.name
# except AttributeError as e:
#     print(e)
# Sample Output 3:
#
# Удаление атрибута невозможно