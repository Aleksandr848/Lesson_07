from abc import ABC
from abc import abstractmethod


class Clothes(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def amount_of_fabric(self):
        pass


class Cout(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    def amount_of_fabric(self):
        return round(self.v / 6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def amount_of_fabric(self):
        return round(self.h * 2 + 0.3, 2)


a = Cout(78)
b = Suit(187)

print(a.amount_of_fabric())
print(b.amount_of_fabric)
