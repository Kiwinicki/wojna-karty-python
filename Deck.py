import random
from Card import Card

colors = ('Pik', 'Kier', 'Trefl', 'Karo')
figures = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'As', 'Król', 'Dama', 'Walet')


class Deck:
    def __init__(self):
        self.cards = []
        for color in colors:
            for fig in figures:
                value = None
                match fig:
                    case 'As':
                        value = 14
                    case 'Król':
                        value = 13
                    case 'Dama':
                        value = 12
                    case 'Walet':
                        value = 11
                    case other:
                        value = int(fig)
                self.cards.append(Card(value=value, figure=fig, color=color))

    def shuffle(self):
        for i, val in enumerate(self.cards):
            randPos = random.randrange(len(self.cards))
            self.cards[i], self.cards[randPos] = self.cards[randPos], self.cards[i]
