class StringDigit(str):
    def __init__(self, string):
        if any(x.isalpha() for x in string):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        # res = str(other) + str(self)
        # print(other)
        # print(self)
        return self.__class__(str(other) + str(self))


sd = StringDigit("123")
print(sd)  # 123
sd = sd + "456"  # StringDigit: 123456
sd = "789" + sd  # StringDigit: 789123456
print(sd)
# sd = sd + "12f"  # ValueError
