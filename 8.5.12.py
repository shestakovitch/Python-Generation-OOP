"""Декоратор @jsonattr
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение
JSON объекта, содержащегося в этом файле."""


import json


def jsonattr(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        def wrapper(cls):
            for key, value in data.items():
                setattr(cls, key, value)
            return cls
    return wrapper


# SampleInput:
#
# with open('test.json', 'w') as file:
#     file.write('{"x": 1, "y": 2}')
#
#
# @jsonattr('test.json')
# class MyClass:
#     pass
#
#
# print(MyClass.x)
# print(MyClass.y)
#
# Sample Output:
#
# 1
# 2