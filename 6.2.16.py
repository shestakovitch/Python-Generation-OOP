"""Класс HistoryDict 🌶️
Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании
экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор
элементов считается пустым
Класс HistoryDict должен иметь пять методов экземпляра:

keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса
HistoryDict
items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в
виде кортежей (<ключ>, <значение>)
history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все
значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не
содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а
значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например,
с помощью цикла for.

Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам,
добавлять новые пары (ключ, значение) и удалять уже имеющиеся.

Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими
словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.

Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов
нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный
класс используется только с корректными данными."""


class HistoryDict:
    def __init__(self, data={}):
        self._data = {key: [value] for key, value in data.items()}

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data.keys()

    def __getitem__(self, key):
        return self._data[key][-1]

    def __setitem__(self, key, value):
        self._data.setdefault(key, []).append(value)

    def __delitem__(self, key):
        del self._data[key]

    def keys(self):
        return self._data.keys()

    def values(self):
        return [v[-1] for v in self._data.values()]

    def items(self):
        return [(k, v[-1]) for k, v in self._data.items()]

    def history(self, key):
        return self._data.get(key, [])

    def all_history(self):
        return {key: value for key, value in self._data.items()}


# Sample Input 1:
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(historydict['ducks'])
# print(historydict['cats'])
# print(len(historydict))
# Sample Output 1:
#
# 99
# 1
# 2
# Sample Input 2:
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(*historydict)
# print(*historydict.keys())
# print(*historydict.values())
# print(*historydict.items())
# Sample Output 2:
#
# ducks cats
# ducks cats
# 99 1
# ('ducks', 99) ('cats', 1)
# Sample Input 3:
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# historydict['ducks'] = 100
# print(historydict.history('ducks'))
# print(historydict.history('cats'))
# print(historydict.history('dogs'))
# Sample Output 3:
#
# [99, 100]
# [1]
# []
# Sample Input 4:
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(historydict.all_history())
# historydict['ducks'] = 100
# historydict['ducks'] = 101
# historydict['cats'] = 2
# print(historydict.all_history())
# Sample Output 4:
#
# {'ducks': [99], 'cats': [1]}
# {'ducks': [99, 100, 101], 'cats': [1, 2]}
# Sample Input 5:
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# historydict['dogs'] = 1
# print(len(historydict))
# del historydict['ducks']
# del historydict['cats']
# print(len(historydict))
# Sample Output 5:
#
# 3
# 1