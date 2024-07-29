"""Класс AdvancedTimer
Реализуйте класс AdvancedTimer. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса AdvancedTimer должен являться многоразовым контекстным менеджером, который замеряет время выполнения
кода внутри каждого блока with.

Также экземпляр класса AdvancedTimer должен иметь четыре атрибута:

last_run — число, представляющее время выполнения кода внутри последнего блока with
runs — список чисел, каждое из которых представляет время выполнения какого-либо кода внутри блока with. Первый элемент
списка должен представлять собой время выполнения кода внутри первого блока with, второй элемент — внутри второго блока
with, и так далее
min — число, представляющее минимальное время выполнения кода внутри блока with среди всех замеров
max — число, представляющее максимальное время выполнения кода внутри блока with среди всех замеров
Если экземпляр класса AdvancedTimer ни разу не использовался для замера скорости выполнения какого-либо блока кода,
значения атрибутов last_run, min и max должны равняться None.

Примечание 1. Наглядные примеры использования класса AdvancedTimer продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Класс AdvancedTimer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы
__enter__() и __exit__(). Реализация же протокола может быть произвольной."""


from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = self.min = self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = perf_counter() - self.start
        self.runs.append(self.elapsed)
        self.last_run = self.runs[-1]
        self.min = min(self.runs)
        self.max = max(self.runs)


# Sample Input 1:
#
# timer = AdvancedTimer()
#
# print(timer.runs)
# print(timer.last_run)
# print(timer.min)
# print(timer.max)
# Sample Output 1:
#
# []
# None
# None
# None
# Sample Input 2:
#
# from time import sleep
#
# timer = AdvancedTimer()
#
# with timer:
#     sleep(1.5)
# print(round(timer.last_run, 1))
#
# with timer:
#     sleep(0.7)
# print(round(timer.last_run, 1))
#
# with timer:
#     sleep(1)
# print(round(timer.last_run, 1))
# Sample Output 2:
#
# 1.5
# 0.7
# 1.0
# Sample Input 3:
#
# from time import sleep
#
# timer = AdvancedTimer()
#
# with timer:
#     sleep(1.5)
#
# with timer:
#     sleep(0.7)
#
# with timer:
#     sleep(1)
#
# print([round(runtime, 1) for runtime in timer.runs])
# print(round(timer.min, 1))
# print(round(timer.max, 1))
# Sample Output 3:
#
# [1.5, 0.7, 1.0]
# 0.7
# 1.5