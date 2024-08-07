"""Класс Queue
Реализуйте класс Queue, описывающий очередь, элементами которой являются пары ключ: значение. При создании экземпляра
класс должен принимать один аргумент:

pairs — список или словарь, определяющий начальный набор элементов очереди. Порядок элементов в очереди должен совпадать
с их порядком в переданном итерируемом объекте. Если не передан, очередь считается пустой
Класс Queue должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента элемент и добавляющий его в конец очереди. Элементом в данном случае
является двухэлементный кортеж, содержащий ключ и значение. Если в очереди уже содержится элемент с указанным ключом, он
должен быть перенесен в конец очереди, а его значение должно быть обновлено
pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Элементом в данном случае является двухэлементный
кортеж, содержащий ключ и значение. Если очередь пуста, должно быть возбуждено исключение KeyError с текстом:
Очередь пуста
Экземпляр класса Queue должен иметь следующее формальное строковое представление:

Queue([(<ключ 1-го элемента>, <значение 1-го элемента>), (<ключ 2-го элемента>, <значение 2-го элемента>), ...])
При передаче экземпляра класса Queue в функцию len() должно возвращаться количество элементов в нем.

Примечание 1. Вероятно, при решении задачи будет удобно воспользоваться одним из классов из модуля collections.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной."""


class Queue:
    def __init__(self, pairs={}):
        self.pairs = dict(pairs)

    def add(self, pair):
        if pair[0] in self.pairs:
            del self.pairs[pair[0]]
        self.pairs.update(dict([pair]))

    def pop(self):
        if not len(self.pairs):
            raise KeyError('Очередь пуста')
        first_k = next(iter(self.pairs))
        return first_k, self.pairs.pop(first_k)

    def __len__(self):
        return len(self.pairs)

    def __str__(self):
        return f'Queue({[(k, v) for k, v in self.pairs.items()]})'


# Sample Input 1:
#
# queue = Queue()
#
# queue.add(('one', 1))
# queue.add(('two', 2))
# print(queue)
# Sample Output 1:
#
# Queue([('one', 1), ('two', 2)])
# Sample Input 2:
#
# queue = Queue([('one', 1)])
#
# queue.add(('two', 2))
# print(queue.pop())
# print(queue.pop())
# print(queue)
# Sample Output 2:
#
# ('one', 1)
# ('two', 2)
# Queue([])
# Sample Input 3:
#
# queue = Queue({'one': 1, 'two': 2})
#
# print(len(queue))
# queue.add(('three', 1))
# print(len(queue))
# Sample Output 3:
#
# 2
# 3
# Sample Input 4:
#
# queue = Queue()
#
# queue.add(('one', 1))
# queue.add(('two', 2))
# print(queue)
# queue.add(('one', 10))
# print(queue)
# Sample Output 4:
#
# Queue([('one', 1), ('two', 2)])
# Queue([('two', 2), ('one', 10)])
# Sample Input 5:
#
# queue = Queue()
#
# try:
#     queue.pop()
# except KeyError as error:
#     print(error)
# Sample Output 5:
#
# 'Очередь пуста'