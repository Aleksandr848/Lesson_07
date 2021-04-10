class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['  '.join(['%d' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.matrix)


a = Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
print(a)
print(' +')
b = Matrix([[2, 4, 6, 8], [4, 6, 8, 10], [6, 8, 10, 12]])
print(b)
print(' =')
m = a + b
print(m)
