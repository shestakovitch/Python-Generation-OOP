"""Класс ReadableTextFile
Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:

filename — имя текстового файла
Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на
чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце. Также контекстный
менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера, то есть иметь методы
__enter__() и __exit__(). Реализация же протокола может быть произвольной."""


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return open(self.filename, mode='r', encoding='utf-8', newline='\r\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# Sample Input 1:
#
# with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
#     print('Только посмотрите!', file=file)
#     print('Как величаво она парит в воздухе', file=file)
#     print('Как орел', file=file)
#     print('На воздушном шаре', file=file)
#
# with ReadableTextFile('glados_quotes.txt') as file:
#     for line in file:
#         print(line)
# Sample Output 1:
#
# Только посмотрите!
# Как величаво она парит в воздухе
# Как орел
# На воздушном шаре
# Sample Input 2:
#
# with open('poem.txt', 'w', encoding='utf-8') as file:
#     print('Я кашлянул в звенящей тишине,', file=file)
#     print('И от шального эха стало жутко…', file=file)
#     print('Расскажет ли утятам обо мне', file=file)
#     print('под утро мной испуганная утка?', file=file)
#
# with ReadableTextFile('poem.txt') as file:
#     for line in file:
#         print(line)
# Sample Output 2:
#
# Я кашлянул в звенящей тишине,
# И от шального эха стало жутко…
# Расскажет ли утятам обо мне
# под утро мной испуганная утка?