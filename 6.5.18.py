"""Класс TreeBuilder 🌶️🌶️
Дерево — одна из наиболее широко распространённых структур данных в информатике, эмулирующая древовидную структуру в
виде набора связанных узлов.



Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13. Узлы без
потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13.

Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово строить
древовидную структуру данных (дерево).

Класс TreeBuilder должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
structure() — метод, возвращающий структуру дерева в виде вложенных списков
Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего блока
with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева, возвращаемой
методом structure().

Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел, тот, в свою очередь,
другой, и так далее.

Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева выводится
лишь после ее построения.

Примечание 3. Наглядные примеры использования класса TreeBuilder продемонстрированы в тестовых данных.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 5. Класс TreeBuilder должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной."""


class TreeBuilder:
    def __init__(self):
        self.tree = {0: []}
        self.level = 0

    def __enter__(self):
        self.level += 1
        self.tree.setdefault(self.level, [])

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tree[self.level]:
            self.tree[self.level - 1].append(self.tree[self.level][:])
        self.tree[self.level].clear()
        self.level -= 1

    def add(self, obj):
        self.tree[self.level].append(obj)

    def structure(self):
        return self.tree[0]


# Sample
# Input
# 1:
#
# tree = TreeBuilder()
# print(tree.structure())
#
# tree.add('1st')
# print(tree.structure())
#
# with tree:
#     tree.add('2nd')
#     with tree:
#         tree.add('3rd')
#     tree.add('4th')
#     with tree:
#         pass
#
# print(tree.structure())
# Sample
# Output
# 1:
#
# []
# ['1st']
# ['1st', ['2nd', ['3rd'], '4th']]
# Sample
# Input
# 2:
#
# tree = TreeBuilder()
#
# tree.add('1st')
#
# with tree:
#     tree.add('2nd')
#     with tree:
#         tree.add('3rd')
#         with tree:
#             tree.add('4th')
#             with tree:
#                 tree.add('5th')
#     with tree:
#         pass
#
# tree.add('6th')
# print(tree.structure())
# Sample
# Output
# 2:
#
# ['1st', ['2nd', ['3rd', ['4th', ['5th']]]], '6th']
# Sample
# Input
# 3:
#
# tree = TreeBuilder()
#
# with tree:
#     tree.add(1)
#     tree.add(2)
#     with tree:
#         tree.add(3)
#         with tree:
#             tree.add(4)
#     with tree:
#         tree.add(5)
#
# print(tree.structure())
# Sample
# Output
# 3:
#
# [[1, 2, [3, [4]], [5]]]