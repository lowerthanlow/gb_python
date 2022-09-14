class Clothes:

    def __init__(self, name):
        self.name = name


    def __add__(self, other):
        result = self.length() + other.length()
      
        return f'Итого: {result:.2f}'

    @property
    def full(self):
      return f'{self.name}: {self.length():.2f}'



class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V


    def length(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H


    def length(self):
        return 2 * self.H + 0.3


coat = Coat('Пальто', 63)
suit = Suit('Костюм', 1.37)
print(coat.full)
print(suit.full)
print(coat + suit)
