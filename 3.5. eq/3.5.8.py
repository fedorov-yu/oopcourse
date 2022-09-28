class Box:

    def __init__(self):
        self.__lst = []

    def add_thing(self, obj, ):
        if isinstance(obj, Thing):
            self.__lst.append(obj)

    def get_things(self):
        return self.__lst

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # counter = 0
            # length = len(self.__lst)
            # for i in self.__lst:
            #     for j in other.__lst:
            #         if i == j:
            #             counter += 1
            # return counter == length
            return sorted(self.__lst) == sorted(other.__lst)


class Thing:
    def __init__(self, name, mass):
        self.name = name.lower() if type(name) == str else str
        self.mass = mass if type(mass) in (int, float) else None

    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.name == other.name and self.mass == other.mass

    def __lt__(self, other):
        if isinstance(other, Thing):
            return self.mass < other.mass

    def __repr__(self):
        return f'{self.name} -- {self.mass}'


b1 = Box()
b2 = Box()
t1 = Thing('pisya', 100)
t2 = Thing('Psya', 500)
b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True

print(res)
print(t1 != t2)