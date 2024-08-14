"""Декоратор @track_instances
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут
instances, содержащий список всех созданных экземпляров этого класса.

Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в
котором они были созданы."""


from functools import wraps


def track_instances(cls):
    old__init__ = cls.__init__
    cls.instances = []

    @wraps(old__init__)
    def new_init(self, *args, **kwargs):
        old__init__(self, *args, **kwargs)
        cls.instances.append(self)
    cls.__init__ = new_init
    return cls


# Sample Input:
#
# @track_instances
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person({self.name!r})'
#
#
# obj1 = Person('object 1')
# obj2 = Person('object 2')
#
# print(Person.instances)
# Sample Output:
#
# [Person('object 1'), Person('object 2')]