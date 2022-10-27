class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2:
            self.__points.append(tuple(args))
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self._checker(x)
        self._checker(y)
        self.x = x
        self.y = y

    @staticmethod
    def _checker(value):
        if not type(value) in (float, int):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"

    def __repr__(self):
        return f"PointTrack: {self.x}, {self.y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))

tr.add_back(PointTrack(1.4, 0))
print(tr.points)
tr.pop_front()
print(tr.points)
tr.add_front(PointTrack(0, 0))
for pt in tr.points:
    print(pt)
