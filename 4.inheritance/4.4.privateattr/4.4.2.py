class Furniture:
    def __init__(self, name: str, weight: int | float):
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        keys = {'_name': self.__verify_name, '_weight': self.__verify_weight}
        if key in keys:
            keys[key](value)
        super().__setattr__(key, value)

    @staticmethod
    def __verify_name(name):
        if not type(name) == str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        if not type(weight) in (int, float):
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
fr = Furniture(10, 10)
