class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push_back(self, obj):
        if self.tail:
            self.tail.next = obj

        self.tail = obj
        if not self.top:
            self.top = obj

    def pop_back(self):
        if not self.top:
            return
        tmp = self.top
        while tmp.next and tmp.next != self.tail:
            tmp = tmp.next
        if self.top == self.tail:
            self.top = self.tail = None
        else:
            tmp.next = None
            self.tail = tmp

    @staticmethod
    def __checker(other):
        if not isinstance(other, StackObj):
            raise ValueError("other must be StackObj")

    def __add__(self, other):
        self.__checker(other)
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) == list:
            for i in other:
                self.push_back(StackObj(i))
        return self

    def __iadd__(self, other):
        self.__checker(other)
        return self.__add__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def get_datas(self):
        tmp = self.top
        lst = []
        while tmp:
            lst.append(tmp.data)
            tmp = tmp.next
        return lst


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"
print(st.get_datas())

st = st + StackObj("2")
print(st.get_datas())
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
