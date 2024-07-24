"""Класс DefaultObject
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default,
имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы, передаваемые
после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.

При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса DefaultObject нет, она может быть произвольной."""


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return self.default


# Sample Input 1:
#
# god = DefaultObject(name='Ares', mythology='greek')
#
# print(god.name)
# print(god.mythology)
# print(god.age)
# Sample Output 1:
#
# Ares
# greek
# None
# Sample Input 2:
#
# god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')
#
# print(god.name)
# print(god.mythology)
# print(god.age)
# Sample Output 2:
#
# Tyr
# scandinavian
# 0