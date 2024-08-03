"""
Класс SuperInt
Реализуйте класс SuperInt, наследника класса int, описывающий целое число с дополнительным функционалом. Процесс
создания экземпляра класса SuperInt должен совпадать с процессом создания экземпляра класса int.

Класс SuperInt должен иметь четыре метода экземпляра:

repeat() — метод, принимающий в качестве аргумента целое число n, по умолчанию равное 2, и возвращающий экземпляр класса
SuperInt, продублированный n раз
to_bin() — метод, возвращающий двоичное представление экземпляра класса SuperInt. Двоичное представление может быть как
в виде экземпляра класса str, так и int
next() — метод, возвращающий новый экземпляр класса SuperInt, который больше текущего на единицу
prev() — метод, возвращающий новый экземпляр класса SuperInt, который меньше текущего на единицу
Также экземпляр класса SuperInt должен быть итерируемым объектом, элементами которого являются его цифры слева направо.
Сами цифры так же должны быть представлены в виде экземпляров класса SuperInt.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса SuperInt нет, она может быть произвольной."""


class SuperInt(int):
    def repeat(self, n=2):
        if self > 0:
            return SuperInt(str(self) * n)
        return f'-{str(abs(self)) * n}'

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        return (SuperInt(i) for i in str(abs(self)))


# Sample Input 1:
#
# superint1 = SuperInt(17)
# superint2 = SuperInt(-17)
#
# print(superint1.repeat())
# print(superint2.repeat(3))
# Sample Output 1:
#
# 1717
# -171717
# Sample Input 2:
#
# superint1 = SuperInt(17)
# superint2 = SuperInt(-17)
#
# print(superint1.to_bin())
# print(superint2.to_bin())
# Sample Output 2:
#
# 10001
# -10001
# Sample Input 3:
#
# superint = SuperInt(17)
#
# print(superint.prev())
# print(superint.next())
# Sample Output 3:
#
# 16
# 18
# Sample Input 4:
#
# superint1 = SuperInt(1337)
# superint2 = SuperInt(-2077)
#
# print(*superint1)
# print(*superint2)
# Sample Output 4:
#
# 1 3 3 7
# 2 0 7 7