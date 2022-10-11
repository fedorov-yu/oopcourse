class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __repr__(self):
        return f"{self.__data}"


class TableValues:
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.tbl = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    @staticmethod
    def __checker(item):
        if any(type(i) != int for i in item):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__checker(item)
        x, y = item[0], item[-1]
        if x <= self.rows and y <= self.cols:
            return self.tbl[x][y].data

    def __setitem__(self, key, value):
        self.__checker(key)
        if type(value.data) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        x, y = key[0], key[-1]
        if x <= self.rows and y <= self.cols:
            self.tbl[x][y].data = value

    def __iter__(self):
        for row in self.tbl:
            yield (x.data for x in row)


table = TableValues(3, 3)
table[1, 1] = Cell(1)  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[1, 1]  # считывание значения из ячейки с индексами row, col
# print(value)

for j, row in enumerate(table):
    print('строка ', j)  # перебор по строкам
    for i, value in enumerate(row):  # перебор по столбцам
        print(f"строка {i}", value, end=' ')  # вывод значений ячеек в консоль
    print()
