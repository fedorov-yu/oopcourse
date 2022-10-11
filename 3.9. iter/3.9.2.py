# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             for j in range(i+1):
#                 yield self.lst[i][j]


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return iter(l[j] for i, l in enumerate(self.lst, 1) for j in range(i))


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
