"""Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь три метода экземпляра:

shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом —
paf, и так далее
shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля"""


class Gun:
    def __init__(self):
        self.counter = 0

    def shots_count(self):
        return self.counter

    def shoot(self):
        print('paf' if self.counter % 2 else 'pif')
        self.counter += 1

    def shots_reset(self):
        self.counter = 0


# Sample Input 1:
#
# gun = Gun()
#
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# Sample Output 1:
#
# 0
# pif
# 1
# paf
# 2
# Sample Input 2:
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# print(gun.shots_count())
# gun.shots_reset()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# Sample Output 2:
#
# pif
# paf
# 2
# 0
# pif
# 1