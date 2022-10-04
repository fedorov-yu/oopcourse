class Track:
    def __init__(self, start_x, start_y):
        self.__start = (start_x, start_y)
        self.__point = []

    def get_track(self):
        return self.__point

    def __checker(self, item):
        if not isinstance(item, int) or item < 0 or item > len(self.__point) - 1:
            raise IndexError('некорректный индекс')

    def add_point(self, x, y, speed):
        self.__point.append([(x, y), speed])

    def __getitem__(self, item):
        self.__checker(item)
        return self.__point[item][0], self.__point[item][-1]

    def __setitem__(self, key, value):
        self.__checker(key)
        if isinstance(value, (int, float)):
            self.__point[key][-1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

# print(tr.get_track())
# print(tr[0])

tr[2] = 60
c, s = tr[2]
print(c, s)

# res = tr[3]  # IndexError
