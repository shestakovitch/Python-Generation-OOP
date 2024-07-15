"""Класс Pet
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:

name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:

name — имя домашнего животного
Класс Pet должен иметь три метода класса:

first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было
создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было
создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
Примечание 1. Никаких ограничений касательно реализации класса Pet нет, она может быть произвольной.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""


class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


# Sample Input 1:
#
# print(Pet.first_pet())
# print(Pet.last_pet())
# print(Pet.num_of_pets())
# Sample Output 1:
#
# None
# None
# 0
# Sample Input 2:
#
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())
# Sample Output 2:
#
# Ratchet
# Rivet
# 3