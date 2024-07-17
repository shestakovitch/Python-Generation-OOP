"""Класс Matrix 🌶️🌶️
Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать три аргумента в
следующем порядке:

rows — количество строк в матрице
cols — количество столбцов в матрице
value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
Экземпляр класса Matrix должен иметь два атрибута:

rows — количество строк в матрице
cols — количество столбцов в матрице
Класс Matrix должен иметь два метода экземпляра:

get_value() — метод, принимающий в качестве аргументов строку row и столбец col и возвращающий элемент матрицы со
строкой row и столбцом col
set_value() — метод, принимающий в качестве аргументов строку row, столбец col и значение value и устанавливающий в
качестве значения элемента матрицы со строкой row и столбцом col значение value
Экземпляр класса Matrix должен иметь следующее формальное строковое представление:

Matrix(<количество строк в матрице>, <количество столбцов в матрице>)
Неформальным строковым представлением должна быть строка, в которой перечислены все элементы матрицы. Элементы строки
матрицы должны быть разделены пробелом, строки матрицы должны быть разделены символом переноса строки \n. Например, для
объекта Matrix(2, 3) неформальным строковым представлением должна быть строка 0 0 0\n0 0 0, которая при выводе будет
отображаться следующим образом:

0 0 0
0 0 0
Также экземпляр класса Matrix должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с
исходными элементами
результатом унарного - должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с
элементами, взятыми с противоположным знаком
результатом унарного ~ должен являться новый экземпляр класса Matrix, представляющий транспонированную матрицу
Наконец, при передаче экземпляра класса Matrix в функцию round() должен возвращаться новый экземпляр класса Matrix c
исходным количеством строк и столбцов и с элементами, округленными с помощью функции round(). Во время передачи в
функцию round() должна быть возможность в качестве второго необязательного аргумента указать целое число, определяющее
количество знаков после запятой при округлении.

Примечание 1. Индексация строк и столбцов в матрице начинается с нуля.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Matrix нет, она может быть произвольной."""


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows, self.cols, self.value = rows, cols, value
        self.matrix = [[value]*cols for i in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __str__(self):
        return '\n'.join([' '.join(str(c) for c in row) for row in self.matrix])

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols, self.value)
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, -self.matrix[i][j])
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows, self.value)
        for i in range(self.cols):
            for j in range(self.rows):
                new_matrix.set_value(i, j, self.get_value(j, i))
        return new_matrix

    def __round__(self, n=None):
        new_matrix = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, round(self.matrix[i][j], n))
        return new_matrix


# Sample Input 1:
#
# print(Matrix(2, 3))
# Sample Output 1:
#
# 0 0 0
# 0 0 0
# Sample Input 2:
#
# matrix = Matrix(2, 3, 1)
#
# print(+matrix)
# print()
# print(-matrix)
# Sample Output 2:
#
# 1 1 1
# 1 1 1
#
# -1 -1 -1
# -1 -1 -1
# Sample Input 3:
#
# matrix = Matrix(2, 3, 1)
#
# print(matrix)
# print()
# print(~matrix)
# Sample Output 3:
#
# 1 1 1
# 1 1 1
#
# 1 1
# 1 1
# 1 1