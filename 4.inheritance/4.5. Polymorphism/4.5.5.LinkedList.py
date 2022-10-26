from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = self._tail = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj

        if self._tail:
            self._tail._next = obj
        self._tail = obj
        return self._tail

    def pop_back(self):
        if not self._top:
            return
        tmp = self._top
        while tmp._next and tmp._next != self._tail:
            tmp = tmp._next
        popped = self._tail
        if self._top == self._tail:
            self._top = self._tail = None
        else:
            tmp._next = None
            self._tail = tmp
        return popped

    def get_all_objects(self):
        lst = []
        tmp = self._top
        while tmp:
            lst.append(tmp)
            tmp = tmp._next
        return lst


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __repr__(self):
        return f"{self._data}"


"""-------------------------------------------------TESTS------------------------------------------------"""
assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"

st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
