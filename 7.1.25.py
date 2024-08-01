"""Иерархия классов 🐍
С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных:

                                    Animal
                                  /        \
                               Fish        Bird
                                            |
                                        FlyingBird

"""


class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass


# Sample Input:
#
# print(issubclass(Fish, Animal))
# print(issubclass(Bird, Animal))
# print(issubclass(FlyingBird, Animal))
# print(issubclass(FlyingBird, Bird))
# Sample Output:
#
# True
# True
# True
# True