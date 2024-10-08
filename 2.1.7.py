"""Покемоны
Артур владеет небольшой коллекцией карточек с покемонами, среди которых встречаются дубликаты. Он хочет оставить по
одной карточке каждого типа, а остальные продать.

Напишите программу, которая определяет, сколько дубликатов из своей коллекции Артур может продать.

Формат входных данных
На вход программе подается произвольное количество строк, которые представляют коллекцию карточек с покемонами. В каждой
строке указывается имя покемона с карточки.

Формат выходных данных
Программа должна вывести единственное число — количество карточек, которые из данной коллекции можно продать, чтобы
оставить по одной карточке каждого типа.

Примечание 1. Рассмотрим первый тест. Чтобы оставить по одной карточке каждого типа, достаточно продать две карточки
Pichu и одну карточку Tyrogue."""

print(len(pokemons := [item.strip() for item in open(0)]) - len(set(pokemons)))

"""Sample Input 1:
Pichu
Pichu
Tyrogue
Pichu
Combee
Marill
Tyrogue

Sample Output 1:
3

Sample Input 2:
Tyrogue
Pichu
Combee

Sample Output 2:
0
"""