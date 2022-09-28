import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __repr__(self):
        return f"{self.name} -- {self.weight} -- {self.price}"


lst_in = list(map(str.strip, sys.stdin.readlines()))
print(lst_in)
shop_items = {}
lst_in2 = []
for item in lst_in:
    name, weight, price = item.rsplit(maxsplit=2)
    obj = ShopItem(name[:-1], weight, price)
    shop_items.setdefault(obj, [obj, 0])[-1] += 1
print(shop_items)
