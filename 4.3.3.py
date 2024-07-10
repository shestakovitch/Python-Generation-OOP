"""Класс User
Вам доступен класс User, описывающий интернет-пользователя. При создании экземпляра класс принимает один аргумент:

name — имя пользователя
Экземпляр класса User имеет два атрибута:

name — имя пользователя
friends — количество друзей пользователя, начальным значением является 0
Класс User имеет один метод экземпляра:

add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество друзей пользователя на
n
Найдите и исправьте ошибки, допущенные при реализации метода add_friends().

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


"""
Sample Input 1:
user = User('Arthur')
print(user.friends)

Sample Output 1:
0

Sample Input 2:
user = User('Timur')
user.add_friends(2)
user.add_friends(2)
user.add_friends(3)
print(user.friends)

Sample Output 2:
7
"""