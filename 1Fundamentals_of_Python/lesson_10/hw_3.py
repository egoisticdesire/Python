class Cell:
    def __init__(self, num):
        self.num = int(num)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) \
               + '\n' + '*' * (self.num % rows)

    def __add__(self, other):
        return 'Sum: ' + str(self.num + other.num)

    def __sub__(self, other):
        return f'Sub: {self.num - other.num}' if self.num > other.num \
            else 'Кол-во ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Multiply: ' + str(self.num * other.num)

    def __truediv__(self, other):
        return 'Truediv: ' + str(self.num / other.num)

    def __floordiv__(self, other):
        return 'Floordiv: ' + str(self.num // other.num)


cell_1 = Cell(55)
cell_2 = Cell(89)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(10))
