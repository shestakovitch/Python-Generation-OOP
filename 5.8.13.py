"""Класс AttrsNumberObject
Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных
аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:

attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам
атрибут attrs_num
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной."""


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        return len(self.__dict__) + 1


# Sample Input 1:
#
# music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')
#
# print(music_group.attrs_num)
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# music_group = AttrsNumberObject()
#
# print(music_group.attrs_num)
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# music_group = AttrsNumberObject(name='Woodkid', genre='pop')
#
# print(music_group.attrs_num)
# music_group.country = 'France'
# print(music_group.attrs_num)
# Sample Output 3:
#
# 3
# 4
# Sample Input 4:
#
# music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')
#
# print(music_group.attrs_num)
# del music_group.genre
# print(music_group.attrs_num)
# Sample Output 4:
#
# 3
# 2