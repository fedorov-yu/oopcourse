class ObjList:
    def __init__(self, data='', prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, ObjList) or obj is None:
            self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if isinstance(obj, ObjList) or obj is None:
            self.__prev = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data


class LinkedList:

    def __init__(self, ):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """Добавление объекта в список"""
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if self.head is None:
            self.head = obj

    def __get_obj_by_index(self, indx):
        """ Нахождение элемента по индексу"""
        head = self.head
        counter = 0
        while head and counter < indx:
            head = head.next
            counter += 1
        return head

    def remove_obj(self, indx):
        """ Удаление элемента"""
        obj = self.__get_obj_by_index(indx)
        if not obj:
            return
        if obj.prev:
            obj.prev.next = obj.next
        if obj.next:
            obj.next.prev = obj.prev
        if self.head == obj:
            self.head = obj.next
        if self.tail == obj:
            self.tail = obj.prev
        tmp = self.head
        counter = 0
        return obj.data

    def __len__(self):
        counter = 0
        if self.head is None:
            return counter
        tmp = self.head
        counter += 1
        while tmp.next:
            counter += 1
            tmp = tmp.next
        return counter

    def __call__(self, indx):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
print(linked_lst.remove_obj(2))
print(linked_lst(2))
linked_lst.add_obj(ObjList("Python ООП"))
print(linked_lst(2))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev
print(n, s)
