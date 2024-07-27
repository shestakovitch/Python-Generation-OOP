"""Класс OrderedSet
Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один
аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан,
начальный набор элементов считается пустым
Класс OrderedSet должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного множества
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества,
если он в нем присутствует
При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.

Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
например, с помощью цикла for.

Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы,
реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и
экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным
множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных
позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют
равную длину и содержат равные элементы без учета их расположения.

Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан.
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться не должен.

Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен
вернуть константу NotImplemented.

Примечание 3. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной."""


class OrderedSet:
    def __init__(self, iterable=None):
        self._iterable = dict.fromkeys(iterable, None) if iterable else dict()

    def __len__(self):
        return len(self._iterable)

    def __iter__(self):
        yield from self._iterable

    def __contains__(self, item):
        return item in self._iterable

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self._iterable) == len(other._iterable) and all(x == y for x, y in zip(self._iterable, other._iterable))
        if isinstance(other, set):
            return set(self._iterable) == other
        return NotImplemented

    def add(self, obj):
        self._iterable.setdefault(obj, None)

    def discard(self, obj):
        self._iterable.pop(obj, None)


# Sample Input 1:
#
# orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
#
# print(*orderedset)
# print(len(orderedset))
# Sample Output 1:
#
# bee python stepik geek
# 4
# Sample Input 2:
#
# orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
#
# print('python' in orderedset)
# print('C++' in orderedset)
# Sample Output 2:
#
# True
# False
# Sample Input 3:
#
# orderedset = OrderedSet()
#
# orderedset.add('green')
# orderedset.add('green')
# orderedset.add('blue')
# orderedset.add('red')
# print(*orderedset)
# orderedset.discard('blue')
# orderedset.discard('white')
# print(*orderedset)
# Sample Output 3:
#
# green blue red
# green red