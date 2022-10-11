class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            # print(*args)
            self.__check_types(args)
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.lst = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            # print(*args)
            self.__check2d(*args)
            self.lst = list(*args)
            self.rows = len(self.lst)
            self.cols = len(self.lst[0])

    @staticmethod
    def __length_matrix(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or not all([len(matrix1[i]) == len(matrix2[i]) for i in range(len(matrix1))]):
            raise ValueError('операции возможны только с матрицами равных размеров')

    @staticmethod
    def __check2d(lst):
        for i in lst:
            for j in i:
                if type(j) != int or len(i) != len(lst[0]):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    @staticmethod
    def __check_types(lst):
        if not all([type(i) == int for i in (lst[0], lst[1])]) or type(lst[-1]) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __check_item(self, item):
        if not all([type(i) == int for i in item]):
            raise IndexError('недопустимые значения индексов')
        if item[0] < 0 or item[0] > len(self.lst) or item[-1] < 0 or item[-1] > len(self.lst[0]):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__check_item(item)
        return self.lst[item[0]][item[-1]]

    def __setitem__(self, key, value):
        self.__check_item(key)
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        self.lst[key[0]][key[-1]] = value

    def __add__(self, other):
        if isinstance(other, int):
            new_lst = [[i + other for i in j] for j in self.lst]
            return self.__class__(new_lst)
        self.__length_matrix(self.lst, other.lst)
        new_lst = [[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)]
        return self.__class__(new_lst)

    def __sub__(self, other):
        if isinstance(other, int):
            new_lst = [[i - other for i in j] for j in self.lst]
            return self.__class__(new_lst)
        self.__length_matrix(self.lst, other.lst)
        new_lst = [[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)]
        return self.__class__(new_lst)


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"

mt = Matrix([[1, 2], [3, 4]])
mt1 = Matrix([[1, 2], [3, 4]])
mt2 = Matrix([[1, 2], [3, 4]])
res = mt1 + mt2
print(res.lst)
res = mt[0, 0]  # 1
print(res)
res = mt[0, 1]  # 2
print(res)
res = mt[1, 0]  # 3
print(res)
res = mt[1, 1]  # 4
print(res)
mt[0, 0] = 0.1
