class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value

s = """Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3"""

animals = [Animal(*line.split('; ')) for line in s.splitlines()]