from distributed.tests.test_client import MyException


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Количество клеток - {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            raise MyException ('Нельзя вычесть из меньшего большее!')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(int(self.quantity / other.quantity))

    def make_order(self, row):
        self.row = row
        # self.quantity = quantity
        div = int(self.quantity / self.row)
        remain = self.quantity % self.row
        return str('*' * row + '\n') * div + '*' * remain


a = Cell(45)
b = Cell(36)

c = a + b
# n = b - a
d = a - b
e = a * b
f = a / b

print(f'Сложение. {c}')
print(f'Вычитание. {d}')
print(f'Умножение. {e}')
print(f'Деление. {f}')
# print(n)
print(b.make_order(5))
