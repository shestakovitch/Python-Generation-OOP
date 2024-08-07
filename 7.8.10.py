"""Классы Item и ShoppingCart
1. Реализуйте класс Item, описывающий товар. При создании экземпляра класс должен принимать два аргумента в следующем
порядке:

name — название товара
price — цена товара в долларах
Экземпляр класса Item должен иметь следующее неформальное строковое представление:

<название товара>, <цена товара>$
2. Также реализуйте класс ShoppingCart, описывающий корзину для покупок. При создании экземпляра класс должен принимать
один аргумент:

items — итерируемый объект, определяющий начальный набор товаров в корзине. Если не передан, корзина считается пустой
Класс ShoppingCart должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента товар и добавляющий его в корзину
total() — метод, возвращающий суммарную стоимость всех товаров в корзине
remove() — метод, принимающий в качестве аргумента название товара и удаляющий его из корзины. Если в корзине несколько
товаров с указанным именем, они должны быть удалены все
Экземпляр класса ShoppingCart должен иметь следующее неформальное строковое представление:

<название первого товара в корзине>, <цена первого товара в корзине>$
<название второго товара в корзине>, <цена второго товара в корзине>$
...
Примечание 1. Если корзина для покупок пуста, то ее неформальным строковым представлением должна быть пустая строка.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


class Item:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def __repr__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def __repr__(self):
        return '\n'.join(str(i) for i in self.items)


# Sample Input 1:
#
# item1 = Item('Yoga Mat', 130)
# item2 = Item('Flannel Shirt', 22)
#
# print(item1)
# print(item2)
# Sample Output 1:
#
# Yoga Mat, 130$
# Flannel Shirt, 22$
# Sample Input 2:
#
# shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])
#
# shopping_cart.add(Item('Flannel Shirt', 22))
# print(shopping_cart)
# print(shopping_cart.total())
# Sample Output 2:
#
# Yoga Mat, 130$
# Flannel Shirt, 22$
# 152
# Sample Input 3:
#
# shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])
#
# shopping_cart.remove('Yoga Mat')
# print(shopping_cart)
# print(shopping_cart.total())
# Sample Output 3:
#
# Flannel Shirt, 22$
# 22