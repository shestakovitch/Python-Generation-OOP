"""Класс ValueDict
Реализуйте класс ValueDict, наследника класса dict, описывающий словарь c дополнительным функционалом. Процесс создания
экземпляра класса ValueDict должен совпадать с процессом создания экземпляра класса dict.

Класс ValueDict должен иметь два метода экземпляра:

key_of() — метод, принимающий в качестве аргумента объект value и возвращающий первый ключ экземпляра класса ValueDict,
имеющий значение value. Если такого ключа нет, метод должен вернуть None.
keys_of() — метод, принимающий в качестве аргумента объект value и возвращающий итерируемый объект, элементами которого
являются все ключи экземпляра класса ValueDict, имеющие значение value
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ValueDict нет, она может быть произвольной."""


class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k

    def keys_of(self, value):
        return (k for k, v in self.items() if v == value)


# Sample Input 1:
#
# valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})
#
# print(valuedict.key_of(2))
# print(*valuedict.keys_of(2))
# Sample Output 1:
#
# banana
# banana orange
# Sample Input 2:
#
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
#
# valuedict = ValueDict(countries)
#
# print(valuedict.key_of('Moscow'))
# print(*valuedict.keys_of('Washington'))
# Sample Output 2:
#
# None
# Sample Input 3:
#
# valuedict = ValueDict({})
#
# print(valuedict.key_of(12))
# print(*valuedict.keys_of(33))
# Sample Output 3:
#
# None