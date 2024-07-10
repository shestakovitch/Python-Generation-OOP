"""Класс Knight ♞
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в
следующем порядке:

horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:

horizontal — координата коня на шахматной доске по горизонтальной оси
vertical — координата коня на шахматной доске по вертикальной оси
color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с
указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться
конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, —
символом *
Примечание 1. Шахматное поле имеет вид:



Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, x, y):
        return True if ('abcdefgh'.index(self.horizontal) - 'abcdefgh'.index(x)) ** 2 + (self.vertical - y) ** 2 == 5 else False

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        board = [['.*'[abs(('abcdefgh'.index(self.horizontal) - j) * (8 - self.vertical - i)) == 2] for j in range(8)] for i in range(8)]
        board[8 - self.vertical]['abcdefgh'.index(self.horizontal)] = 'N'
        [print(*row, sep='') for row in board]


# Sample Input 1:
#
# knight = Knight('c', 3, 'white')
#
# print(knight.color, knight.get_char())
# print(knight.horizontal, knight.vertical)
# Sample Output 1:
#
# white N
# c 3
# Sample Input 2:
#
# knight = Knight('c', 3, 'white')
#
# print(knight.horizontal, knight.vertical)
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))
#
# knight.move_to('e', 4)
# print(knight.horizontal, knight.vertical)
# Sample Output 2:
#
# c 3
# False
# True
# e 4
# Sample Input 3:
#
# knight = Knight('c', 3, 'white')
#
# knight.draw_board()
# Sample Output 3:
#
# ........
# ........
# ........
# .*.*....
# *...*...
# ..N.....
# *...*...
# .*.*....