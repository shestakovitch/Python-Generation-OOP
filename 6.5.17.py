"""Класс HtmlTag 🌶️
HTML — это язык разметки, используемый для определения структуры веб-страниц, посещаемых пользователями. HTML
предоставляет средства для создания заголовков, абзацев, ссылок, цитат и других элементов. Каждый HTML-элемент
обозначается открывающим и закрывающим тегами:

<p>Если в ходе теста нет угрозы жизни, разве это вообще наука?</p>
Теги заключаются в угловые скобки. Они определяют, где элемент начинается и где он заканчивается. Единственным различием
между открывающим и закрывающим тегами является косая черта, которая предшествует имени тега.

Открывающий и закрывающий теги, а также заключенное в них содержимое, могут располагаться как на одной строке
(пример выше), так и на разных. Если теги и содержимое располагаются на разных строках, то сперва указывается
открывающий тег, затем на следующий строке с отступом в два пробела указывается содержимое, а после на следующей строке
указывается закрывающий тег, который располагается на том же уровне отступов, что и открывающий тег:

<p>
  Наука не решает вопрос Почему?, она решает вопрос А почему бы и нет?
</p>
Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

tag — HTML тег
inline — булево значение, по умолчанию равняется False
Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать HTML-код
с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их
содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных
строках.

Класс HtmlTag должен иметь один метод экземпляра:

print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.

Примечание 2. В качестве отступов для каждого уровня используйте два пробела.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и
__exit__(). Реализация же протокола может быть произвольной."""


class HtmlTag:
    level = -1

    def __init__(self, tag, inline=False):
        self.tag, self.inline = tag, inline

    def __enter__(self):
        self.__class__.level += 1
        if not self.inline:
            print(f'{"  " * self.__class__.level}<{self.tag}>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.inline:
            print(f'{"  " * self.__class__.level}</{self.tag}>')
        self.__class__.level -= 1

    def print(self, text):
        if self.inline:
            print(f'{"  " * self.__class__.level}<{self.tag}>{text}</{self.tag}>')
        else:
            print(f'{"  " * self.__class__.level}  {text}')


# Sample Input 1:
#
# with HtmlTag('body') as _:
#     with HtmlTag('h1') as header:
#         header.print('Поколение Python')
#     with HtmlTag('p') as section:
#         section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
# Sample Output 1:
#
# <body>
#   <h1>
#     Поколение Python
#   </h1>
#   <p>
#     Cерия курсов по языку программирования Python от команды BEEGEEK
#   </p>
# </body>
# Sample Input 2:
#
# with HtmlTag('body') as _:
#     with HtmlTag('h1', True) as header:
#         header.print('Поколение Python')
#     with HtmlTag('p', True) as section:
#         section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
# Sample Output 2:
#
# <body>
#   <h1>Поколение Python</h1>
#   <p>Cерия курсов по языку программирования Python от команды BEEGEEK</p>
# </body>
# Sample Input 3:
#
# with HtmlTag('body') as _:
#     with HtmlTag('h1', True) as header:
#         header.print('Здесь есть что-то интересное')
#     with HtmlTag('a', True) as section:
#         section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')
# Sample Output 3:
#
# <body>
#   <h1>Здесь есть что-то интересное</h1>
#   <a>https://stepik.org/media/attachments/course/98974/watch_me.mp4</a>
# </body>