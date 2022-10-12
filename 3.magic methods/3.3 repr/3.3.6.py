import math
from functools import reduce


class RadiusVector:
    def __init__(self, *args):
        self.__coords = [0] * args[0] if len(args) == 1 else [*args]

    def set_coords(self, *args):
        self.__coords = list(args[:len(self.__coords)]) + self.__coords[len(args):]

    def get_coords(self, ):
        return self.__coords

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        # return math.sqrt(reduce(lambda x, y: x+y*y, *self.__coords))
        return math.sqrt(sum(map(lambda x: x ** 2, self.__coords)))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)