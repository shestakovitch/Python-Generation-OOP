"""Класс Logger
Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать никаких аргументов.

Предполагалось, что при установке или изменении значения атрибута экземпляра класса Logger будет выводиться текст:

Изменение значения атрибута <имя атрибута> на <новое значение атрибута>
Также планировалось, что при удалении атрибута будет выводиться текст:

Удаление атрибута <имя атрибута>
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Logger.

Примечание. Никаких ограничений касательно реализации класса Logger нет, она может быть произвольной."""


class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]


# Sample Input 1:
#
# obj = Logger()
#
# obj.attr = 1
# del obj.attr
# Sample Output 1:
#
# Изменение значения атрибута attr на 1
# Удаление атрибута attr
# Sample Input 2:
#
# obj = Logger()
#
# obj.name = 'pygen'
# obj.rating = '5*'
# obj.ceo = 'Timur'
# del obj.rating
# obj.rating = '6*'
# Sample Output 2:
#
# Изменение значения атрибута name на pygen
# Изменение значения атрибута rating на 5*
# Изменение значения атрибута ceo на Timur
# Удаление атрибута rating
# Изменение значения атрибута rating на 6*