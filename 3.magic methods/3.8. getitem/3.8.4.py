class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, instance.data_type):
            raise ValueError(instance.message)
        setattr(instance, self.name, value)


class Abstract:
    data_type = None
    message = ''
    default_value = None
    value = IntegerValue()

    def __init__(self, start_value=None):
        self.value = start_value or self.default_value


class CellInteger(Abstract):
    data_type = int
    message = 'возможны только целочисленные значения'
    default_value = 0


class CellString(Abstract):
    data_type = str
    message = 'возможны только строки'
    default_value = ''


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        return self.cells[item[0]][item[-1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[-1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
print(table[1, 1])
table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
