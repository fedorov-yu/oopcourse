class Shop:

    def __init__(self, name):
        self.goods = []
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    current_id = 0
    # attrs = {'name': [str,], 'weight': [int, float], 'price': [int,]}

    def __new__(cls, *args, **kwargs):
        cls.current_id += 1
        return super().__new__(cls, )

    def __init__(self, name, weight, price):
        self.id = self.current_id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'id' and isinstance(value, int) and 0 <= value:
            object.__setattr__(self, key, value)
        elif (key == 'price' or key == 'weight') and isinstance(value, (float, int)) and 0 <= value:
            object.__setattr__(self, key, value)
        elif key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
shop.add_product(Product("Pythwqeon", 15.0, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price} {p.id}")