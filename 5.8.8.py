"""Класс Item
Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три
аргумента в следующем порядке:

name — название предмета
price — цена предмета в рублях
quantity — количество предметов
Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной
буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной."""


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)


# Sample Input 1:
#
# fruit = Item('banana', 15, 5)
#
# print(fruit.price)
# print(fruit.quantity)
# Sample Output 1:
#
# 15
# 5
# Sample Input 2:
#
# fruit = Item('banana', 15, 5)
#
# print(fruit.name)
# print(fruit.total)
# Sample Output 2:
#
# Banana
# 75
# Sample Input 3:
#
# course = Item('pygen', 3900, 2)
#
# print(course.name)
# print(course.price)
# print(course.quantity)
# print(course.total)
# Sample Output 3:
#
# Pygen
# 3900
# 2
# 7800