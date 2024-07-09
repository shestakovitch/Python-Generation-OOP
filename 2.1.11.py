"""Pycon
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.

Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.

Формат входных данных
На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.

Формат выходных данных
Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате
DD.MM.YYYY.

Примечание 1. Гарантируется, что подаваемые год и месяц всегда корректны."""

from datetime import date

year, month = int(input()), int(input())
for i in range(1, 8):
    if date(year, month, i).isoweekday() == 4:
        day = i + 21
print(date(year, month, day).strftime('%d.%m.%Y'))

"""
Sample Input 1:
2012
3

Sample Output 1:
22.03.2012

Sample Input 2:
2015
2

Sample Output 2:
26.02.2015

Sample Input 3:
2018
6

Sample Output 3:
28.06.2018
"""