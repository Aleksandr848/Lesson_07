from abc import ABC
from abc import abstractmethod


class Clothes(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class Amount(Clothes):
    def __init__(self, v, h):
        super().__init__()
        self.v = v
        self.h = h

    def coat(self):
        return round(self.v / 6.5 + 0.5, 2)

    @property
    def suit(self):
        return round(self.h * 2 + 0.3, 2)


b = Amount(87, 99)

print(b.coat())
print(b.suit)
