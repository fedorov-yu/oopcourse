class Thing:
    id = 0

    def __init__(self, name=None, price=None, weight=None, dims=None, memory=None, frm=None):
        Thing.id += 1
        self.id = Thing.id
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return '({}, {}, {}, {}, {}, {}, {})'.format(*self.__dict__.values())


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm



table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())