"""Класс DevelopmentTeam
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший).
При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:

add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем
разработчика, и добавляющий их в число junior-разработчиков
add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем
разработчика, и добавляющий их в число senior-разработчиков
Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его
junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:

(<имя разработчика>, 'junior')
в то время как senior-разработчики — в виде кортежей:

(<имя разработчика>, 'senior')
Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной."""


class DevelopmentTeam:
    def __init__(self):
        self.junior, self.senior = [], []

    def add_junior(self, *args):
        for name in args:
            self.junior.append((name, 'junior'))

    def add_senior(self, *args):
        for name in args:
            self.senior.append((name, 'senior'))

    def __iter__(self):
        yield from self.junior + self.senior


# Sample Input 1:
#
# beegeek = DevelopmentTeam()
#
# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# beegeek.add_senior('Gvido')
# print(*beegeek, sep='\n')
# Sample Output 1:
#
# ('Timur', 'junior')
# ('Arthur', 'junior')
# ('Valery', 'junior')
# ('Gvido', 'senior')
# Sample Input 2:
#
# beegeek = DevelopmentTeam()
#
# print(len(list(beegeek)))
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# beegeek = DevelopmentTeam()
#
# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# print(*beegeek, sep='\n')
# Sample Output 3:
#
# ('Timur', 'junior')
# ('Arthur', 'junior')
# ('Valery', 'junior')