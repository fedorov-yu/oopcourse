from random import randint


class GamePole:
    """ игровое поле"""
    __instance = None

    def __init__(self, N, M, total_mines):
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        GamePole.__instance = None

    @property
    def pole(self):
        return self.__pole_cells

    @pole.setter
    def pole(self, value):
        self.__pole_cells = value

    def init_pole(self):
        """ раставляет мины по полю"""
        for row in self.pole:
            for x in row:
                x.is_open = True
                x.is_mine = False
        i = 0
        while i < self._total_mines:
            x = randint(0, self._n - 1)
            y = randint(0, self._m - 1)
            if self.pole[x][y].is_mine:
                continue
            self.pole[x][y].is_mine = True
            i += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine:
                    count_of_mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx if
                                          0 <= x + i < self._n and 0 <= y + j < self._m))
                    self.pole[x][y].number = count_of_mines

    def open_cell(self, i, j):
        """открывает ячейку поля именяя параметр __is_open для cell"""
        if i < 0 or i > self._n - 1 or j < 0 or j > self._m - 1:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        """ вывод поля в консоль"""
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))


class Cell:
    """клетка поля"""

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = True

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open

    def __repr__(self):
        return f"клетка "


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole = GamePole(5, 5, 5)
# print(pole.pole[1])
pole.init_pole()
pole.show_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
