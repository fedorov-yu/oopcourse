class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        if isinstance(indx, int):
            self.items.pop(indx)

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name: str, money: int | float):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            res = self.money + other.money
        if isinstance(other, (int, float)):
            res = self.money + other
        return res

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f"{self.name} -- {self.money}"


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.get_items())

it1 = Item("name", 1000)
it2 = Item("name2", 2000)
print(it1+it2)

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
    print(s)