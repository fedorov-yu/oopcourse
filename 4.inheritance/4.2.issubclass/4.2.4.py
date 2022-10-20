class Tuple(tuple):
    def __init__(self, obj):
        super().__init__(obj)

    def __add__(self, other):
        return self.__class__(super().__add__(tuple(other)))

t = Tuple([1, 2, 3])
print(t)
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
