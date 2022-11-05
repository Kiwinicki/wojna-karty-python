class Card:
    def __init__(self, value: int, figure: str, color: str):
        self.value = value
        self.figure = figure
        self.color = color

    def __str__(self):
        return f'Karta figura: {self.figure}, kolor: {self.color}'
