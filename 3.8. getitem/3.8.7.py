class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = True
                j.value = 0

    def __getitem__(self, item):
        x, y = item
        if isinstance(item, slice):
            return tuple(self.pole[item].value)
        if isinstance(y, slice):
            res = self.pole[x][y]
            return tuple([i.value for i in res])
        if isinstance(x, slice):
            res = tuple([i[y] for i in self.pole])
            return tuple([i.value for i in res])
        return self.pole[x][y].value

    def __setitem__(self, key, value):
        if not all(0 <= i < 3 for i in key):
            raise IndexError('неверный индекс клетки')
        if not self.pole[key[0]][key[-1]].is_free:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[-1]].value = value
        self.pole[key[0]][key[-1]].is_free = False


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

    def __repr__(self):
        return f"{self.value}"


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
print(game.pole)
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]
print(v1)  # 1, 0, 0
v2 = game[:, 0]
print(v2)  # 1, 2, 0
