"""Функция limited_hash() 🌶️
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:

left — целое число
right — целое число
hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()
Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его
хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right], и
возвращает полученный результат.

Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без
преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его в
left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования, но в другую
сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться циклично при
очередном выходе из диапазона.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию limited_hash(), но не код,
вызывающий ее."""


def limited_hash(left, right, hash_function=hash):
    def func(x):
        return left + (hash_function(x) - left) % (right - left + 1)
    return func


# Sample Input 1:
#
# hash_function = limited_hash(10, 15)
#
# print(hash_function(10))
# print(hash_function(11))
# print(hash_function(15))
# Sample Output 1:
#
# 10
# 11
# 15
# Sample Input 2:
#
# hash_function = limited_hash(10, 15)
#
# print(hash_function(16))
# print(hash_function(17))
# print(hash_function(21))
# print(hash_function(22))
# print(hash_function(23))
# Sample Output 2:
#
# 10
# 11
# 15
# 10
# 11
# Sample Input 3:
#
# hash_function = limited_hash(10, 15)
#
# print(hash_function(9))
# print(hash_function(8))
# print(hash_function(4))
# print(hash_function(3))
# print(hash_function(2))
# Sample Output 3:
#
# 15
# 14
# 10
# 15
# 14