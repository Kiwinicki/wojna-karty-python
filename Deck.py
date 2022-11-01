# klasa talii kart

import random
from Card import Card

colors = ('Pik', 'Kier', 'Trefl', 'Karo')
values_per_color = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    'As', 'Król', 'Dama', 'Walet')
jokers = [{'value': 'Joker', 'color': 'czarny'},
          {'value': 'Joker', 'color': 'czerwony'}]

card = Card(color='Pik', value=1)
print(card)


class Deck:
    def __init__(self):
        self.cards = []
        for val in values_per_color:
            for clr in colors:
                self.cards.append({'value': val, 'color': clr})
        self.cards.extend(jokers)

    def shuffle(self):
        for i in range(len(self.cards)):
            randPos = random.randrange(len(self.cards))
            self.cards[i], self.cards[randPos] = self.cards[randPos], self.cards[i]

    def compare(self, card1, card2):
        print('porównuje karty...')
