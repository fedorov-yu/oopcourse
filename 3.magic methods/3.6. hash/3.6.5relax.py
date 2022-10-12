class Dimensions:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __new__(cls, a, b, c):
        if not all(float(i) > 0 for i in (a, b, c)):
            raise ValueError("габаритные размеры должны быть положительными числами")
        return super().__new__(cls,)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return f"{self.a}, {self.b}, {self.c}"

s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
s_inp = s_inp.split(";")
lst_dims = sorted([Dimensions(i.split()[0], i.split()[1], i.split()[2]) for i in s_inp])
print(lst_dims)