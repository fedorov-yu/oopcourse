class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.tail:
            self.tail.next = obj

        self.tail = obj
        if not self.top:
            self.top = obj

    def pop(self):
        if not self.top:
            return
        tmp = self.top
        while tmp.next and tmp.next != self.tail:
            tmp = tmp.next
        popped = tmp.next
        if self.top == self.tail:
            self.top = self.tail = None
        else:
            tmp.next = None
            self.tail = tmp
        return popped

    def __len__(self):
        tmp = self.top
        i = 0
        while tmp:
            i += 1
            tmp = tmp.next
        return i

    def __checker(self, item):
        if not isinstance(item, int) or item > len(self) - 1 or item < 0:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__checker(item)
        i = 0
        tmp = self.top
        while i < item:
            tmp = tmp.next
            i += 1
        return tmp

    def __setitem__(self, key, value):
        tmp = self.__getitem__(key)
        n = tmp.next
        value.next = n
        self[key - 1].next = value

    def __call__(self):
        lst = []
        tmp = self.top
        while tmp:
            lst.append(tmp.data)
            tmp = tmp.next
        return lst


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st())
print(len(st))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
print(st[0].data)
print(st.pop().data, 'popped')
print(len(st), st())
# res = st[3]  # исключение IndexError
