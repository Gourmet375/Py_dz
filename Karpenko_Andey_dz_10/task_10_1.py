class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])


rows = int(input('Введите количество строк и столбцов матрицы: '))
cols = rows

matrix_1 = Matrix([[i * j for j in range(rows)] for i in range(cols)])
matrix_2 = Matrix([[i + j for j in range(rows)] for i in range(cols)])

print('Первая матрица:\n', matrix_1, end='\n\n')
print('Вторая матрица:\n', matrix_2, end='\n\n')
print('Сумма первой и второй матрицы:\n', matrix_1 + matrix_2)
