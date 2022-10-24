class ItemAttrs:
    def __getitem__(self, item):
        return self.__dict__[list(self.__dict__.keys())[item]]

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value


class Point(ItemAttrs):
    def __init__(self, y, x):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
