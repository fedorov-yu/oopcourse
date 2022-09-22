class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __checker(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")

    def __add__(self, other):
        self.__checker(other)
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        self.__checker(other)
        return self + other

    def __iadd__(self, other):
        self.__checker(other)
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __sub__(self, other):
        self.__checker(other)
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        self.__checker(other)
        return self - other

    def __isub__(self, other):
        self.__checker(other)
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        self.__checker(other)
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        self.__checker(other)
        return self * other

    def __imul__(self, other):
        self.__checker(other)
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __truediv__(self, other):
        self.__checker(other)
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        self.__checker(other)
        return self / other

    def __itruediv__(self, other):
        self.__checker(other)
        self.lst_math = [i / other for i in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])  # ListMath: [1, -5, 7.68]
lst = lst + 76  # сложение каждого числа списка с определенным числом
print(lst)
lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
print(lst)
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst)
lst = lst - 76  # вычитание из каждого числа списка определенного числа
print(lst)
lst = 7.0 - lst  # вычитание из числа каждого числа списка
print(lst)
lst -= 76.3
print(lst)
lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst)
lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst)
lst *= 5.54
print(lst)
lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst)
lst = 3 / lst  # деление числа на каждый элемент списка
print(lst)
lst /= 13.0
print(lst)
