class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.param])

    def __add__(self, other):
        result_matrix = ''
        if len(self.param) == len(other.param):
            for line1, line2 in zip(self.param, other.param):
                if len(line1) != len(line2):
                    return 'Разная длина строк'
                sum_lines = [i + j for i, j in zip(line1, line2)]
                result_matrix += ' '.join(map(str, sum_lines)) + '\n'
        else:
            return 'Разный размер матриц'
        return result_matrix


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[6, 5, 4], [3, 2, 1], [0, -1, -2]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)
