class ShopInterface:

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        ShopItem.ID += 1
        self.__id = self.ID

    def get_id(self):
        return self.__id


i1 = ShopItem('name', 10, 10)
i2 = ShopItem('name2', 10, 10)
print(i1.get_id(), i2.get_id())
