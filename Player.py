class Player:
    def __init__(self, name, cards):
        self.name = f'Gracz nr {name}'
        self.cards = cards

    def __str__(self):
        return self.name

    def place_card(self):
        return self.cards.pop(0)
