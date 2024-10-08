"""Класс HTTPStatusCodes
Коды состояния HTTP представляют собой трехзначные целые числа и используются для указания успешности конкретного HTTP
запроса. Выделяют пять групп кодов состояния:

информация (100-199)
успех (200-299)
перенаправление (300-399)
ошибка клиента (400-499)
ошибка сервера (500-599)
Реализуйте класс HTTPStatusCodes, описывающий перечисление с  кодами состояния HTTP. Перечисление должно иметь пять
элементов:

CONTINUE — элемент со значением 100
OK — элемент со значением 200
USE_PROXY — элемент со значением 305
NOT_FOUND — элемент со значением 404
BAD_GATEWAY — элемент со значением 502
Элемент перечисления должен иметь два метода:

info() — метод, возвращающий двухэлементный кортеж, содержащий имя элемента и его значение
code_class() — метод, возвращающий название группы на русском, к которой относится элемент
Примечание 1. Подробнее про коды состояния HTTP можно почитать по ссылке.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса HTTPStatusCodes нет, она может быть произвольной."""


from enum import Enum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        d = {'CONTINUE': 'информация', 'OK': 'успех', 'USE_PROXY': 'перенаправление', 'NOT_FOUND': 'ошибка клиента',
             'BAD_GATEWAY': 'ошибка сервера'}
        return d[self.name]


# Sample Input:
#
# print(HTTPStatusCodes.OK.info())
# print(HTTPStatusCodes.OK.code_class())
# Sample Output:
#
# ('OK', 200)
# успех