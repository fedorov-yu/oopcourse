class Desc:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner, ):
        return instance.__dict__[self.name]

    def __set__(self, instance, value, ):
        instance.__dict__[self.name] = value


class Money:
    cb = Desc()
    volume = Desc()

    def __init__(self, volume=0, cb=None):
        self.cb = cb
        self.volume = volume

    @staticmethod
    def checker(money):
        if money.cb is None:
            raise ValueError("Неизвестен курс валют")

    @staticmethod
    def convert_money(other):
        if isinstance(other, MoneyD):
            return round(other.cb.rates['rub'] * other.volume)
        if isinstance(other, MoneyE):
            return round(other.cb.rates['euro'] * other.cb.rates['rub'] * other.volume)
        if isinstance(other, MoneyR):
            return round(other.volume)

    def __eq__(self, other):
        self.checker(other)
        return self.convert_money(self) == self.convert_money(other)

    def __lt__(self, other):
        self.checker(other)
        return self.convert_money(self) < self.convert_money(other)

    def __le__(self, other):
        self.checker(other)
        return self.convert_money(self) <= self.convert_money(other)


class MoneyR(Money):
    currency = 'rub'


class MoneyD(Money):
    currency = 'dollar'


class MoneyE(Money):
    currency = 'euro'


class CentralBank:
    rates = {}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
e = MoneyE(100)
d1 = MoneyD(800)
d2 = MoneyD(800.0005)

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(e)
CentralBank.register(d1)
CentralBank.register(d2)

print(d1 == d2)

if e < d:
    print('e<d')
else:
    print('pupa')

if d > r:
    print('d>r vse norm')
else:
    print('pupalupa')

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
