class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.__lst = [cell(0) for _ in range(max_length)]

    def __checker(self, key):
        if not isinstance(key, int) or not (0 <= key <= self.max_length - 1):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__checker(item)
        return self.__lst[item].val

    def __setitem__(self, key, value):
        self.__checker(key)
        self.__lst[key].val = value

    def __str__(self):
        return " ".join([str(i) for i in self.__lst])


class Num:
    message = ''
    data_type = None
    default_value = None

    def __init__(self, start_value=None):
        self._val = start_value or self.default_value

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, item):
        if not isinstance(item, self.data_type):
            raise ValueError(self.message)
        self._val = item

    def __repr__(self):
        return f"{self._val}"


class Integer(Num):
    data_type = int
    message = 'Must be int'
    default_value = 0


class Float(Num):
    data_type = float
    message = 'Must be float'
    default_value = 0.0


# ar_int = Array(10, cell=Integer)
ar_int = Array(10, cell=Float)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10.0
print(ar_int[1])
# ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1  # должно генерироваться исключение IndexError
