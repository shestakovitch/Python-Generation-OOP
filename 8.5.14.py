"""Декоратор @snake_case
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и
не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое
слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого.
Например, beeGeek и helloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовывать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case
и lower Camel Case на Snake Case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты
класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel
Case на Snake case, если False — остаться прежним.

Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case,
lower Camel Case или Snake Case."""


import inspect as i


def go_to_snake(atr_name: str) -> str:
    sc_method = ''
    for index, letter in enumerate(atr_name):
        if letter.isupper() and index !=0:
            letter = f'_{letter}'
            sc_method += letter
        else:
            sc_method += letter
    if sc_method[:2] == '__':
        return sc_method[1:].lower()
    return sc_method.lower()


def snake_case(attrs=False):
    def wrapper(cls):
        for old_atr, _obj in i.getmembers(cls):
            if not old_atr.startswith('__'):
                new_method = ''
                if i.isfunction(_obj):
                    new_method = go_to_snake(old_atr)
                elif attrs:
                    new_method = go_to_snake(old_atr)
                else:
                    new_method=old_atr
                if new_method not in cls.__dict__:
                    setattr(cls, new_method, getattr(cls, old_atr))
                    delattr(cls, old_atr)
        return cls
    return wrapper


# Sample Input 1:
#
#
# @snake_case()
# class MyClass:
#     def FirstMethod(self):
#         return 1
#
#     def superSecondMethod(self):
#         return 2
#
#
# obj = MyClass()
#
# print(obj.first_method())
# print(obj.super_second_method())
#
# Sample Output 1:
#
# 1
# 2
#
# Sample Input 2:
#
#
# @snake_case(attrs=True)
# class MyClass:
#     FirstAttr = 1
#     superSecondAttr = 2
#
#
# print(MyClass.first_attr)
# print(MyClass.super_second_attr)
#
# Sample Output 2:
#
# 1
# 2
#
# Sample Input 3:
#
#
# @snake_case()
# class MyClass:
#     FirstAttr = 1
#
#     def FirstMethod(self):
#         return 1
#
#
# obj = MyClass()
#
# print(MyClass.FirstAttr)
# print(obj.first_method())
# Sample Output 3:
#
# 1
# 1