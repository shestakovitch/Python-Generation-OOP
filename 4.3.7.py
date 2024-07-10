"""Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь один метод экземпляра:

shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом —
paf, и так далее"""


class Gun:
    def __init__(self):
        self.shoot_cnt = 0

    def shoot(self):
        print('paf' if self.shoot_cnt % 2 else 'pif')
        self.shoot_cnt += 1


# Sample Input 1:
#
# gun = Gun()
#
# gun.shoot()
# Sample Output 1:
#
# pif
# Sample Input 2:
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# gun.shoot()
# gun.shoot()
# Sample Output 2:
#
# pif
# paf
# pif
# paf