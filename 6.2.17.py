"""
Класс MutableString 🌶️
Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:

string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
Класс MutableString должен иметь два метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:

<текущее значение изменяемой строки>
Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:

MutableString('<текущее значение изменяемой строки>')
При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои
символы, например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью
индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные
срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +,
результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.

Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных
атрибутов нет.

Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный
класс используется только с корректными данными."""


class MutableString:
    def __init__(self, string: str=''):
        self.string = string

    def __repr__(self):
        return f"MutableString('{self.string}')"

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        yield from self.string

    def __getitem__(self, index):
        return MutableString(self.string[index])

    def __setitem__(self, key, value):
        temp = list(self.string)
        temp[key] = value
        self.string = ''.join(temp)

    def __delitem__(self, key):
        temp = list(self.string)
        del temp[key]
        self.string = ''.join(temp)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()


# Sample Input 1:
#
# mutablestring = MutableString('beegeek')
#
# print(*mutablestring)
# print(str(mutablestring))
# print(repr(mutablestring))
# Sample Output 1:
#
# b e e g e e k
# beegeek
# MutableString('beegeek')
# Sample Input 2:
#
# mutablestring = MutableString('Beegeek')
#
# mutablestring.lower()
# print(mutablestring)
# mutablestring.upper()
# print(mutablestring)
# Sample Output 2:
#
# beegeek
# BEEGEEK
# Sample Input 3:
#
# mutablestring1 = MutableString('bee')
# mutablestring2 = MutableString('geek')
#
# print(mutablestring1 + mutablestring2)
# print(mutablestring2 + mutablestring1)
# Sample Output 3:
#
# beegeek
# geekbee
# Sample Input 4:
#
# mutablestring = MutableString('beegeek')
#
# print(mutablestring)
# mutablestring[0] = 'B'
# mutablestring[-4] = 'G'
# print(mutablestring)
# Sample Output 4:
#
# beegeek
# BeeGeek