"""Класс SuppressAll
Требовалось реализовать класс SuppressAll. При создании экземпляра класс не должен был принимать никаких аргументов.

Предполагалось, что экземпляр класса SuppressAll будет являться контекстным менеджером, подавляющим любое исключение,
которое возбуждается во время выполнения кода внутри блока with.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте класс SuppressAll
правильно.

Примечание 1. Наглядные примеры использования класса SuppressAll продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Класс SuppressAll должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной."""


class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return True


# Sample Input 1:
#
# print('start')
#
# with SuppressAll():
#     print('Python generation!')
#     raise ValueError
#
# print('end')
# Sample Output 1:
#
# start
# Python generation!
# end
# Sample Input 2:
#
# print('start')
#
# with SuppressAll():
#     print('Python generation!')
#
# print('end')
# Sample Output 2:
#
# start
# Python generation!
# end