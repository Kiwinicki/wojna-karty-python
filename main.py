# 1. określona ilość kart jest dzielona równo na graczy
# 2. każdy z graczy wykłada kartę
# 3. wszystkie wyłożone karty są porównywane i ten gracz który położył najlepszą kartę zbiera resztę i daje ją na spód swojej talii
# 4. jeśli zostały wyłożone 2 karty tego samego typu (nie liczy się kolor np. dzwonki, serca) to zaczyna się "wojna" i każdy z tych graczy daje jedną kartę spodem i na nią jedną kartę wierzchem, ten gracz, który ma lepszą kartę na wierzchu zabiera wszystkie karty biorące udział w wojnie

from Deck import Deck
from Player import Player

# tworzę talię
deck = Deck()
print(len(deck.cards))

# pobieram liczbę graczy
num_of_players = 0
while type(num_of_players) != 'int':
    print('Podaj liczbę graczy:')
    try:
        num_of_players = int(input())
        if type(num_of_players) == int:
            break
    except:
        print('Liczba graczy powinna być liczbą całkowitą')

print(num_of_players)

# tasuję talię
deck.shuffle()

# tworzę i rozdaję karty
players = []
for i in range(num_of_players):
    cards_per_player = len(deck.cards) // num_of_players
    player_cards = deck.cards[i*cards_per_player:(i+1)*cards_per_player]
    players.append(Player(name=i+1, cards=player_cards))

print(players[0].name, len(players[0].cards))
