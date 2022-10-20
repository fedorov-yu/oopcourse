class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            self.validator(i)
        super().__init__(lst)

    @staticmethod
    def validator(value):
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.validator(key)
        self.validator(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.validator(value)
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5  # TypeError
