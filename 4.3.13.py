"""Класс Todo
Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Todo должен иметь один атрибут:

things — изначально пустой список дел, которые нужно выполнить
Класс Todo должен иметь четыре метода экземпляра:

add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде
кортежа:
(<название дела>, <приоритет>)
get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих
приоритет n
get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(),
должны располагаться в том порядке, в котором они были добавлены в список.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""


class Todo:
    def __init__(self):
        self.things = []

    def add(self, task, priority):
        self.things.append((task, priority))

    def get_by_priority(self, n):
        return [task for task, priority in self.things if priority == n]

    def get_low_priority(self):
        return [task for task, priority in self.things if priority == min([priority for task, priority in self.things])]

    def get_high_priority(self):
        return [task for task, priority in self.things if priority == max([priority for task, priority in self.things])]


# Sample Input 1:
#
# todo = Todo()
#
# print(todo.things)
# print(todo.get_by_priority(1))
# print(todo.get_low_priority())
# print(todo.get_high_priority())
# Sample Output 1:
#
# []
# []
# []
# []
# Sample Input 2:
#
# todo = Todo()
#
# todo.add('Проснуться', 3)
# todo.add('Помыться', 2)
# todo.add('Поесть', 2)
#
# print(todo.get_by_priority(2))
# Sample Output 2:
#
# ['Помыться', 'Поесть']
# Sample Input 3:
#
# todo = Todo()
#
# todo.add('Ответить на вопросы', 5)
# todo.add('Сделать картинки', 1)
# todo.add('Доделать задачи', 4)
# todo.add('Дописать конспект', 5)
#
# print(todo.get_low_priority())
# print(todo.get_high_priority())
# print(todo.get_by_priority(3))
# Sample Output 3:
#
# ['Сделать картинки']
# ['Ответить на вопросы', 'Дописать конспект']
# []