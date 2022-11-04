class Card:
    def __init__(self, color, value):
        self.color = color
        self.name = str(value)
        match value:
            case 'As':
                self.value = 14
            case 'Król':
                self.value = 13
            case 'Dama':
                self.value = 12
            case 'Walet':
                self.value = 11
            case other:
                self.value = value

    def __str__(self):
        return f'Karta {self.name} - {self.color}'
