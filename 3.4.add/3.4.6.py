class Box3D:
    def __init__(self, width: int | float, height: int | float, depth: int | float):
        self.width = width
        self.height = height
        self.depth = depth

    def get_attrs(self):
        return self.width, self.height, self.depth

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*map(sum, zip(self.get_attrs(), other.get_attrs())))

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(*[i * other for i in self.get_attrs()])

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + other * (-1)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return self.__class__(*[i // other for i in self.get_attrs()])

    def __mod__(self, other):
        if isinstance(other, int):
            return self.__class__(*[i % other for i in self.get_attrs()])
