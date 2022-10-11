class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


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

    def push_front(self, obj):
        if self.top:
            obj.next = self.top
            self.top = obj
        else:
            self.top = self.tail = obj

    def __len__(self):
        return sum(1 for _ in self)

    def __checker(self, item):
        if not isinstance(item, int) or item > len(self) - 1 or item < 0:
            raise IndexError('неверный индекс')

    def __get_obj_by_index(self, item):
        self.__checker(item)
        for i, obj in enumerate(self):
            if i == item:
                return obj

    def __getitem__(self, item):
        return self.__get_obj_by_index(item).data

    def __setitem__(self, key, value):
        self.__get_obj_by_index(key).data = value

    def __iter__(self):
        tmp = self.top
        while tmp:
            yield tmp
            tmp = tmp.next
