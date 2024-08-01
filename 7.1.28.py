"""Класс Counter и подклассы
1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен принимать один
аргумент:

start — начальное значение счетчика, по умолчанию равняется 0
Экземпляр класса Counter должен иметь один атрибут:

value — текущее значение счетчика
Класс Counter должен иметь два метода экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число
не передано, метод должен увеличить значение счетчика на единицу
dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число не
передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении
оно становится отрицательным
2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого можно
увеличивать, но нельзя уменьшать. Процесс создания экземпляра класса NonDecCounter должен совпадать с процессом создания
экземпляра класса Counter.

Экземпляр класса NonDecCounter должен иметь один атрибут:

value — текущее значение счетчика
Класс NonDecCounter должен иметь один метод экземпляра:

dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counter
3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение которого можно
увеличивать лишь до определенного числа. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

start — начальное значение счетчика, по умолчанию равняется 0
limit — максимально возможное значение счетчика, по умолчанию равняется 10
Экземпляр класса LimitedCounter должен иметь один атрибут:

value — текущее значение счетчика
Класс LimitedCounter должен иметь один метод экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число
не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения счетчика метод не должен
превышать установленный лимит
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной."""


class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(0, self.value - n)


class NonDecCounter(Counter):
    def dec(self, n=0):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, n=1):
        self.value = min(self.value + n, self.limit)


# Sample Input 1:
#
# print(issubclass(NonDecCounter, Counter))
# print(issubclass(LimitedCounter, Counter))
# Sample Output 1:
#
# True
# True
# Sample Input 2:
#
# counter = Counter()
#
# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(3)
# print(counter.value)
# counter.dec(10)
# print(counter.value)
# Sample Output 2:
#
# 0
# 6
# 2
# 0
# Sample Input 3:
#
# counter = NonDecCounter(10)
#
# print(counter.value)
# counter.inc()
# counter.inc(10)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(50)
# print(counter.value)
# Sample Output 3:
#
# 10
# 21
# 21
# 21
# Sample Input 4:
#
# counter = LimitedCounter()
#
# print(counter.value)
# counter.inc()
# counter.inc(4)
# print(counter.value)
# counter.dec()
# counter.dec(2)
# print(counter.value)
# counter.inc(20)
# print(counter.value)
# Sample Output 4:
#
# 0
# 5
# 2
# 10