"""Класс StrExtension
Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен
принимать никаких аргументов.

Класс StrExtension должен иметь три статических метода:

remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без
учета регистра и возвращает полученный результат
leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся
латинскими буквами, и возвращает полученный результат
replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все
символы из chars на char с учетом регистра и возвращает полученный результат.
Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными."""


import re


class StrExtension:

    @staticmethod
    def remove_vowels(string):
        return re.sub(r'[aeiouy]', r'', string, flags=re.I)

    @staticmethod
    def leave_alpha(string):
        return re.sub(r'[^a-zA-Z]', r'', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', fr'{char}', string)


# Sample Input 1:
#
# print(StrExtension.remove_vowels('Python'))
# print(StrExtension.remove_vowels('Stepik'))
# Sample Output 1:
#
# Pthn
# Stpk
# Sample Input 2:
#
# print(StrExtension.leave_alpha('Python111'))
# print(StrExtension.leave_alpha('__Stepik__()'))
# Sample Output 2:
#
# Python
# Stepik
# Sample Input 3:
#
# print(StrExtension.replace_all('Python', 'Ptn', '-'))
# print(StrExtension.replace_all('Stepik', 'stk', '#'))
# Sample Output 3:
#
# -y-ho-
# S#epi#