class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    @staticmethod
    def __matrix_checker(matrix):
        for i in matrix:
            if not all(type(j) in (int, float) for j in i) or len(i) != len(matrix[0]):
                raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix):
        self.__matrix_checker(matrix)
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]

        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1
        
        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)

        return res