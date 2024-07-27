"""Класс ReversedSequence
Реализуйте класс ReversedSequence, описывающий объект, который реализует доступ к элементам некоторой последовательности
в обратном порядке. При создании экземпляра класс должен принимать один аргумент:

sequence — последовательность
При передаче экземпляра класса ReversedSequence в функцию len() должна возвращаться его длина, представленная
количеством элементов в исходной последовательности.

Также экземпляр класса ReversedSequence должен быть итерируемым объектом, элементами которого являются элементы исходной
последовательности в обратном порядке.

Наконец, экземпляр класса ReversedSequence должен позволять получать значения элементов исходной последовательности с
помощью индексов, при этом индексация должна производиться в обратном порядке, то есть по индексу 0 должен быть доступен
последний элемент исходной последовательности, по индексу 1 — предпоследний элемент, по индексу 2 — предпредпоследний
элемент, и так далее.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса ReversedSequence должен зависеть от последовательности, на основе которой он был создан.
Другими словами, если исходная последовательность изменится, то должен измениться и экземпляр класса ReversedSequence.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса ReversedSequence нет, она может быть произвольной."""


class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        return self.sequence[~item]


# Sample Input 1:
#
# reversed_list = ReversedSequence([1, 2, 3, 4, 5])
#
# print(reversed_list[0])
# print(reversed_list[1])
# print(reversed_list[2])
# Sample Output 1:
#
# 5
# 4
# 3
# Sample Input 2:
#
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = ReversedSequence(numbers)
#
# print(reversed_numbers[0])
# numbers.append(6)
# print(reversed_numbers[0])
# Sample Output 2:
#
# 5
# 6
# Sample Input 3:
#
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = ReversedSequence(numbers)
# print(len(reversed_numbers))
#
# numbers.append(6)
# numbers.append(7)
# print(len(reversed_numbers))
# Sample Output 3:
#
# 5
# 7