"""Класс NonNegativeObject
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных
аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если
значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной."""


class NonNegativeObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)


# Sample Input 1:
#
# point = NonNegativeObject(x=1, y=-2, z=0, color='black')
#
# print(point.x)
# print(point.y)
# print(point.z)
# print(point.color)
# Sample Output 1:
#
# 1
# 2
# 0
# black
# Sample Input 2:
#
# point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')
#
# print(point.x)
# print(point.y)
# print(point.z)
# print(point.color)
# Sample Output 2:
#
# 1.5
# 2.3
# 0.0
# yellow