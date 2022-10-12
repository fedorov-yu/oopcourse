class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.__db = dict()

    def __calc(self):
        self.rows = max(i[0] for i in self.__db.keys()) + 1
        self.cols = max(i[-1] for i in self.__db.keys()) + 1

    def add_data(self, row, col, data):
        if not (row, col) in self.__db:
            self.__db[(row, col)] = data
            self.__calc()

    def remove_data(self, row, col):
        try:
            del self.__db[(row, col)]
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')
        self.__calc()

    def __getitem__(self, item):
        row, col = item
        if not (row, col) in self.__db:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.__db[row, col]

    def __setitem__(self, key, value):
        row, col = key
        self.__db[row, col] = value
        self.__calc()


class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки

print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5]  # ValueError
st.remove_data(12, 3)  # IndexError
