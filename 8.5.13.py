"""Декоратор @singleton
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то
есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.

Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке."""


def singleton(cls):
    old_new = cls.__new__
    cls._instance = None

    def new(self, *args, **kwargs):

        if cls._instance is None:
            cls._instance = old_new(cls)

        return cls._instance
    cls.__new__ = new
    return cls


# Sample Input:
#
#
# @singleton
# class MyClass:
#     pass
#
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(obj1 is obj2)
#
# Sample Output:
#
# True