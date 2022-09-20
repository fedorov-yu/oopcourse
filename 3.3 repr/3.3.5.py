import math


class Complex:

    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @staticmethod
    def __check_instance(value):
        if type(value) in (int, float):
            return True
        raise ValueError("Неверный тип данных")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if self.__check_instance(value):
            self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if self.__check_instance(value):
            self.__img = value

    def __abs__(self):
        return math.sqrt(self.__real**2 + self.__img**2)


cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
print(abs(cmp))