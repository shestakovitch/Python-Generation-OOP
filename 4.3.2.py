"""Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь один метод экземпляра:

shoot() — метод, при вызове которого выводится строка pif"""


class Gun:
    def shoot(self):
        print('pif')


"""
Sample Input 1:
gun = Gun()
gun.shoot()

Sample Output 1:
pif

Sample Input 2:
gun = Gun()
gun.shoot()
gun.shoot()
gun.shoot()

Sample Output 2:
pif
pif
pif
"""