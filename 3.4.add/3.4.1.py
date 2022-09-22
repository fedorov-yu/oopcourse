class NewList:
    """Вычитание списков"""
    def __init__(self, lst: list = None):
        self._lst = lst[:] if lst and type(lst) == list else []

    @staticmethod
    def __checker(other):
        if isinstance(other, (list, NewList)):
            return True
        else:
            raise ArithmeticError("Операнды должны быть типа list или NewList")

    @staticmethod
    def __diff_list(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1
        copied = lst_2[:]
        return [x for x in lst_1 if not NewList.__is_elem(x, copied)]

    @staticmethod
    def __is_elem(elem, lst):
        result = any(map(lambda x: (type(elem), elem) == (type(x), x), lst))
        if result:
            lst.remove(elem)
        return result

    def __sub__(self, other):
        if self.__checker(other):
            other_list = other if type(other) == list else other.get_list()
            return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if self.__checker(other):
            return NewList(self.__diff_list(other, self._lst))

    def get_list(self):
        return self._lst


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_1.get_list())
print(lst1.get_list())
print(lst2.get_list())
print(res_2.get_list())
print(res_3.get_list())
print(res_4.get_list())
