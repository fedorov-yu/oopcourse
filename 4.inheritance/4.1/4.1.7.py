class Vector:
    def __init__(self, *args: list[int] | list[float]):
        self.lst = tuple(args)

    def checker(self, other):
        if len(self.lst) != len(other.lst):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.lst)

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.checker(other)
        if isinstance(other, Vector):
            new_lst = [self.lst[i] + other.lst[i] for i in range(len(self.lst))]
            return self.__make_vector(new_lst)

    def __sub__(self, other):
        self.checker(other)
        if isinstance(other, Vector):
            new_lst = [self.lst[i] - other.lst[i] for i in range(len(self.lst))]
            return self.__make_vector(new_lst)


class VectorInt(Vector):
    def __init__(self, *args):
        if all([type(i) == int for i in args]):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2
print(v.get_coords())

assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
