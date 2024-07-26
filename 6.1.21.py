""" Класс LoopTracker🌶️
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в
исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на
данный момент
empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент
опустевшего итератора
first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор
не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение
AttributeError с текстом:
Исходный итерируемый объект пуст
last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный
момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с
текстом:
Последнего элемента нет
Класс LoopTracker должен иметь один метод экземпляра:

is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
Реализация же протокола может быть произвольной."""


class LoopTracker:
    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._empty_accesses = self._accesses = 0
        self._is_empty = False
        try:
            self._nextvalue = self._first = next(self._iterable)
        except StopIteration:
            self._is_empty = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty:
            self._empty_accesses += 1
            raise StopIteration
        self._curvalue = self._nextvalue
        self._accesses += 1
        try:
            self._nextvalue = next(self._iterable)
        except StopIteration:
            self._is_empty = True
        return self._curvalue

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if hasattr(self, '_first'):
            return self._first
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if hasattr(self, '_curvalue'):
            return self._curvalue
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return self._is_empty


# Sample Input 1:
#
# loop_tracker = LoopTracker([1, 2, 3])
#
# print(next(loop_tracker))
# print(list(loop_tracker))
# Sample Output 1:
#
# 1
# [2, 3]
# Sample Input 2:
#
# loop_tracker = LoopTracker([1, 2, 3])
#
# print(loop_tracker.accesses)
# next(loop_tracker)
# next(loop_tracker)
# print(loop_tracker.accesses)
# Sample Output 2:
#
# 0
# 2
# Sample Input 3:
#
# loop_tracker = LoopTracker([1, 2, 3])
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)
#
# print(next(loop_tracker))
# print(loop_tracker.first)
# Sample Output 3:
#
# 1
# 1
# 1
# 2
# 1
# 3
# 1
# Sample Input 4:
#
# loop_tracker = LoopTracker([1, 2, 3])
#
# print(next(loop_tracker))
# print(loop_tracker.last)
#
# print(next(loop_tracker))
# print(loop_tracker.last)
#
# print(next(loop_tracker))
# print(loop_tracker.last)
# Sample Output 4:
#
# 1
# 1
# 2
# 2
# 3
# 3