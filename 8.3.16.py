"""Классы MovieGenres и Movie
1. Реализуйте класс MovieGenres, описывающий флаг с жанрами кино. Флаг должен иметь пять элементов:

ACTION
COMEDY
DRAMA
FANTASY
HORROR
2. Также реализуйте класс Movie, описывающий фильм. При создании экземпляра класс должен принимать два аргумента в
следующем порядке:

name — название фильма
genres — жанр фильма (элемент флага MovieGenres)
Класс Movie должен иметь один метод экземпляра:

in_genre() — метод, принимающий в качестве аргумента жанр и возвращающий True, если фильм принадлежит данному жанру, или
False в противном случае
Экземпляр класса Movie должен иметь следующее неформальное строковое представление:

<название фильма>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from enum import Flag


class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16


class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre):
        return genre in self.genres

    def __str__(self):
        return self.name


# Sample Input 1:
#
# movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
#
# print(movie)
# Sample Output 1:
#
# The Lord of the Rings
# Sample Input 2:
#
# movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
#
# print(movie.in_genre(MovieGenres.FANTASY))
# print(movie.in_genre(MovieGenres.COMEDY))
# print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))
# Sample Output 2:
#
# True
# False
# True