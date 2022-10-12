class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.volume = self.__a * self.__b * self.__c

    @staticmethod
    def calc_volume(self):
        self.volume = self.__a * self.__b * self.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value in (self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value in (self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value in (self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__c = value

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            self.calc_volume(self)
            return self.volume < other.volume

    def __le__(self, other):
        if isinstance(other, self.__class__):
            self.calc_volume(self)
            return self.volume <= other.volume

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            self.calc_volume(self)
            return self.volume > other.volume

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            self.calc_volume(self)
            return self.volume >= other.volume


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

    def __repr__(self):
        return f"{self.name} -- {self.dim.volume}"


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
print(trainers.dim.volume)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume)
print(lst_shop_sorted)
