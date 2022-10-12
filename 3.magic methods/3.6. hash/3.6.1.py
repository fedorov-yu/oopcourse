class Rect:
    def __init__(self, x, y, width, height):
        self.x = x if type(x) in (float, int) else None
        self.y = y if type(y) in (float, int) else None
        self.width = width if type(width) in (float, int) else None
        self.height = height if type(height) in (float, int) else None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash((self.width, self.height))



r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
print( h1 == h2)