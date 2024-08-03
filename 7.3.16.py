"""Класс TitledText
Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании экземпляра
класс должен принимать два аргумента в следующем порядке:

content — текст
text_title — заголовок текста
Класс TitledText должен иметь один метод экземпляра:

title() — метод, возвращающий заголовок текста
Примечание 1. Значением экземпляра класса TitledText должен быть именно текст, а не заголовок текста или текст вместе с
заголовком.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса TitledText нет, она может быть произвольной."""


class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance

    def title(self):
        return self.text_title


# Sample Input 1:
#
# titled = TitledText('Сreate a class Soda', 'Homework')
#
# print(titled)
# print(titled.title())
# print(issubclass(TitledText, str))
# Sample Output 1:
#
# Сreate a class Soda
# Homework
# True
# Sample Input 2:
#
# titled1 = TitledText('Сreate a class Soda', 'Homework')
# titled2 = TitledText('Сreate a class Soda', 'Exam')
#
# print(titled1 == titled2)
# Sample Output 2:
#
# True