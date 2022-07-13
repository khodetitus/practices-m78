class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)
        self.n = n
        self.m = m

    def get_matrix(self, n, m):
        num = 1
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    # @property
    # def matrix(self):
    #     return self._matrix
    #
    # @matrix.setter
    # def matrix(self, value: "Matrix.matrix"):
    #     if self.n == len(value) and self.m == len(value[0]):
    #         self._matrix = value
    #     else:
    #         raise ValueError("doesnt match")

    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def getElement(self, i, j):
        return self.matrix[i - 1][j - 1]

    def setElement(self, i, j, element):
        self.matrix[i - 1][j - 1] = element

    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def getTranspose(self):
        return self.get_readable_matrix_string(self.transpose(self.matrix))

    def doTranspose(self):
        self.matrix = self.transpose(self.matrix)

    def multiply(self, matrix):
        result = [[0 for j in range(len(matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += self.matrix[i][k] * matrix[k][j]
        return result

    def getMultiply(self, matrix):
        return self.get_readable_matrix_string(self.multiply(matrix))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num * other for num in row] for row in self.matrix])


class SquareMatrix(Matrix):
    def __init__(self, n, m):
        super().__init__(n, m)

    def det(self):
        if self.n == self.m and self.m == 2:
            m = self.matrix
            result = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            return result
        else:
            raise ValueError("len matrix is not 2")


m1 = Matrix(2, 3)
print(m1)
print("1")
print(m1.getElement(2, 2))
print("2")
m1.setElement(2, 2, -10)
print(m1.getTranspose())
print("3")
print(m1)
print("4")
m1.doTranspose()
print(m1)
print("5")
m2 = Matrix(2, 3)
print(m2)
print(m2.getMultiply(m1))
print(m2 * m1)
print(m1)
print(m1 * 3)
matrix2dar2 = SquareMatrix(2, 2)
matrix2dar2.matrix = [[1, 2], [3, 4]]
print(matrix2dar2.det())
