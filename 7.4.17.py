"""Класс EasyDict
Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как
по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать с
процессом создания экземпляра класса dict.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной."""


class EasyDict(dict):
    def __getattr__(self, item):
        return self[item]


# Sample Input 1:
#
# easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})
#
# print(easydict['name'])
# print(easydict.city)
# Sample Output 1:
#
# Timur
# Moscow
# Sample Input 2:
#
# easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})
#
# easydict['city'] = 'Dubai'
# easydict['age'] = 30
# print(easydict.city)
# print(easydict.age)
# Sample Output 2:
#
# Dubai
# 30
# Sample Input 3:
#
# easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})
#
# easydict.age = 21
# print(easydict)
# Sample Output 3:
#
# {'name': 'Artur', 'city': 'Almetevsk'}