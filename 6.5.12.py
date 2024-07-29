"""
Класс WriteSpy🌶️
Реализуйте класс WriteSpy. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

file1 — файловый объект
file2 — файловый объект
to_close — булево значение, по умолчанию равняется False
Экземпляр класса WriteSpy должен являться контекстным менеджером, который выполняет операцию записи сразу в оба файловых
объекта file1 и file2. Параметр to_close должен определять состояние файловых объектов file1 и file2 после завершения
блока with. Если он имеет значение True, после завершения блока with контекстный менеджер должен закрыть оба файловых
объекта, если False — оставить открытыми.

Класс WriteSpy должен иметь четыре метода экземпляра:

write() — метод, принимающий в качестве аргумента текст и записывающий его в оба файловых объекта. Если хотя бы один из
файловых объектов закрыт или недоступен для записи, должно быть возбуждено исключение ValueError с текстом:
Файл закрыт или недоступен для записи
close() — метод, немедленно закрывающий оба файловых объекта
writable() — метод, возвращающий True, если оба файловых объекта доступны для записи, или False в противном случае
closed() — метод, возвращающий True, если оба файловых объекта закрыты, или False в противном случае
Примечание 1. Наглядные примеры использования класса WriteSpy продемонстрированы в тестовых данных.

Примечание 2. Для проверки того, является ли файловый объект доступным для записи, используйте метод writable(). Данный
метод возвращает True, если файловый объект доступен для записи, или False в противном случае. При попытке применить
метод на закрытом файловом объекте будет возбуждено исключение.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Класс WriteSpy должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и
__exit__(). Реализация же протокола может быть произвольной."""


class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1, self.file2, self.to_close = file1, file2, to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()

    def write(self, text):
        if not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        return self.file1.writable() and self.file2.writable()

    def closed(self):
        return self.file1.closed and self.file2.closed


# Sample
# Input
# 1:
#
# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')
#
# with WriteSpy(f1, f2, to_close=True) as combined:
#     combined.write('You shall seal the blinding light that plagues their dreams\n')
#     combined.write('You are the Vessel\n')
#     combined.write('You are the Hollow Knight')
#
# print(f1.closed, f2.closed)
#
# with open('file1.txt') as file1, open('file2.txt') as file2:
#     print(file1.read())
#     print(file2.read())
# Sample
# Output
# 1:
#
# True True
# You shall seal the blinding light that plagues their dreams
# You are the Vessel
# You are the Hollow Knight
# You shall seal the blinding light that plagues their dreams
# You are the Vessel
# You are the Hollow Knight
# Sample
# Input
# 2:
#
# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')
#
# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.writable())
#
# f1 = open('file1.txt')
# f2 = open('file2.txt')
#
# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.writable())
# Sample
# Output
# 2:
#
# True
# False
# Sample
# Input
# 3:
#
# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')
#
# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.closed())
#     f1.close()
#     print(combined.closed())
#     f2.close()
#     print(combined.closed())
# Sample
# Output
# 3:
#
# False
# False
# True