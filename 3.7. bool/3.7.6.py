class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __checker(self, value, ):
        if isinstance(value, self.__class__):
            if len(self.coords) != len(value.coords):
                raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__checker(other)
        return self.__class__(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other):
        self.__checker(other)
        return self.__class__(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __mul__(self, other):
        self.__checker(other)
        return self.__class__(*[self.coords[i] * other.coords[i] for i in range(len(self.coords))])

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            for i in range(len(self.coords)):
                self.coords[i] += other.coords[i]
        if isinstance(other, int):
            for i in range(len(self.coords)):
                self.coords[i] += other
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            for i in range(len(self.coords)):
                self.coords[i] -= other
        if isinstance(other, self.__class__):
            for i in range(len(self.coords)):
                self.coords[i] -= other.coords[i]
        return self

    def __eq__(self, other):
        self.__checker(other)
        return all(self.coords[i] == other.coords[i] for i in range(len(self.coords)))



v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True