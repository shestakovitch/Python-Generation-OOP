"""Классы LeftParagraph и RightParagraph
Будем называть словом любую последовательность из одной или более латинских букв.

1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен
принимать один аргумент:

length — длина строки абзаца
Класс LeftParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в
текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен
автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым,
то есть начинается формирование нового
2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс
должен принимать один аргумент:

length — длина строки абзаца
Класс RightParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в
текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен
автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий
абзац считается пустым, то есть начинается формирование нового
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from abc import ABC, abstractmethod
import textwrap


class Paragraph(ABC):

    def __init__(self, length):
        self.length = length
        self.data = []

    def add(self, text):
        self.data.extend(text.split())

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        print(textwrap.fill(' '.join(self.data), width=self.length))
        self.data.clear()


class RightParagraph(Paragraph):
    def end(self):
        print('\n'.join(map(lambda x: x.rjust(self.length), textwrap.wrap(' '.join(self.data), self.length))))
        self.data.clear()


# Sample Input 1:
#
# leftparagraph = LeftParagraph(10)
#
# leftparagraph.add('death')
# leftparagraph.add('can have me')
# leftparagraph.add('when it earns me')
# leftparagraph.end()
# Sample Output 1:
#
# death can
# have me
# when it
# earns me
# Sample Input 2:
#
# rightparagraph = RightParagraph(10)
#
# rightparagraph.add('death')
# rightparagraph.add('can have me')
# rightparagraph.add('when it earns me')
# rightparagraph.end()
# Sample Output 2:
#
#  death can
#    have me
#    when it
#   earns me