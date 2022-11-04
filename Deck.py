import random
from Card import Card

colors = ('Pik', 'Kier', 'Trefl', 'Karo')
values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          'As', 'Król', 'Dama', 'Walet')


class Deck:
    def __init__(self):
        self.deck = []
        for color in colors:
            for value in values:
                self.deck.append(Card(color, value))

    def shuffle(self):
        for i, val in enumerate(self.deck):
            randPos = random.randrange(len(self.deck))
            self.deck[i], self.deck[randPos] = self.deck[randPos], self.deck[i]
