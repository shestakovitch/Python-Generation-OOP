"""Семья
С помощью множественного наследования постройте иерархию из приведенных ниже четырех классов. При решении старайтесь
свести дублирование кода к минимуму.

1. Реализуйте класс Father, описывающий отца. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Father должен иметь один атрибут:

mood — настроение
Класс Father должен иметь два метода экземпляра:

greet() — метод, возвращающий строку Hello!
be_strict() — метод, изменяющий значение атрибута mood на строку strict
2. Также реализуйте класс Mother, описывающий мать. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Mother должен иметь один атрибут:

mood — настроение
Класс Mother должен иметь два метода экземпляра:

greet() — метод, возвращающий строку Hi, honey!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
3. Помимо этого, реализуйте класс Daughter, описывающий дочь. При создании экземпляра класс должен принимать один
аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Daughter должен иметь один атрибут:

mood — настроение
Класс Daughter должен иметь три метода экземпляра:

greet() — метод, возвращающий строку Hi, honey!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
be_strict() — метод, изменяющий значение атрибута mood на строку strict
4. Наконец, реализуйте класс Son, описывающий сына. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Son должен иметь один атрибут:

mood — настроение
Класс Son должен иметь три метода экземпляра:

greet() — метод, возвращающий строку Hello!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
be_strict() — метод, изменяющий значение атрибута mood на строку strict
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from abc import ABC, abstractmethod


class Relative(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood

    @abstractmethod
    def greet(self):
        pass


class Father(Relative):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Relative):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


# Sample Input 1:
#
# father = Father()
# mother = Mother()
#
# print(father.mood)
# print(mother.mood)
# print(father.greet())
# print(mother.greet())
# Sample Output 1:
#
# neutral
# neutral
# Hello!
# Hi, honey!
# Sample Input 2:
#
# father = Father('happy')
# mother = Mother('unhappy')
#
# print(father.mood)
# print(mother.mood)
# father.be_strict()
# mother.be_kind()
# print(father.mood)
# print(mother.mood)
# Sample Output 2:
#
# happy
# unhappy
# strict
# kind