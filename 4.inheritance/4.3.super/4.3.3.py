class SellItem:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price


class House(SellItem):

    def __init__(self, name: str, price: int | float, material: str, square: str):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):

    def __init__(self, name: str, price: int | float, size: int, rooms: int):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):

    def __init__(self, name: str, price: int | float, square: str):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.lst = list()

    def add_object(self, obj):
        if isinstance(obj, (Land, House, Flat)):
            self.lst.append(obj)

    def remove_obj(self, obj):
        if obj in self.lst:
            self.lst.remove(obj)

    def get_objects(self):
        return self.lst
