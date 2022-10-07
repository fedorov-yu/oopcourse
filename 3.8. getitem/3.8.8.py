class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.lst = []

    def __checker(self, other):
        if not isinstance(other, int) or other > len(self.lst):
            raise IndexError('неверный индекс')

    def __calc_sum(self, other, old=0):
        if sum([i.weight for i in self.lst]) + other.weight - old > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self.__calc_sum(thing)
        self.lst.append(thing)

    def __getitem__(self, item):
        self.__checker(item)
        return self.lst[item]

    def __setitem__(self, key, value):
        self.__checker(key)
        self.__calc_sum(value, self.lst[key].weight)
        self.lst[key] = value

    def __delitem__(self, key):
        self.__checker(key)
        self.lst.pop(key)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"{self.name} -- {self.weight}"


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag.lst)
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
